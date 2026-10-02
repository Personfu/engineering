#!/usr/bin/env python3
"""Build detailed, source-bound ATLAS engineering profiles as static SVG.

This standard-library generator reads controlled registry records. It writes
117 original mission profiles and a portfolio dashboard, not measurements,
readiness scores, acquired project observations or completed experiment claims.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import math
import textwrap
import xml.etree.ElementTree as ET
from pathlib import Path

PALETTE = {'navy':'#07172d', 'panel':'#0c2540', 'panel_dark':'#0a1d34',
           'teal':'#65dfc4', 'copper':'#efb281', 'magenta':'#ee8fe1',
           'electric_blue':'#73b7ff', 'white':'#eff6ff', 'muted':'#b5c9dc',
           'line':'#34546e', 'ink':'#112d45'}
N, P, D = PALETTE['navy'], PALETTE['panel'], PALETTE['panel_dark']
T, C, M, B = (PALETTE[k] for k in ['teal','copper','magenta','electric_blue'])
W, MUTED, RULE = PALETTE['white'], PALETTE['muted'], PALETTE['line']
EXPECTED = {'A':12, 'B':28, 'C':30, 'D':7, 'E':8, 'F':2, 'G':8, 'H':9, 'I':13}
NS = '{http://www.w3.org/2000/svg}'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def esc(value):
    return html.escape(str(value), quote=True)


def txt(x,y,value,size=18,color=W,weight=400,mono=False,anchor='start',spacing=None):
    family = 'Consolas, Menlo, monospace' if mono else 'Arial, Helvetica, sans-serif'
    extra = f' letter-spacing="{spacing}"' if spacing is not None else ''
    return (f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}" '
            f'font-family="{family}" text-anchor="{anchor}"{extra}>{esc(value)}</text>')


def wrap(value,width):
    return textwrap.wrap(str(value), width=width, break_long_words=True,
                         break_on_hyphens=False, replace_whitespace=True) or ['—']


def text_lines(x,y,values,size=18,gap=25,color=W,weight=400,mono=False):
    return ''.join(txt(x,y+i*gap,v,size,color,weight,mono) for i,v in enumerate(values))


def rect(x,y,w,h,fill=P,r=14,stroke=None,extra=''):
    border=f' stroke="{stroke}"' if stroke else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"{border}{extra}/>'


def line(x1,y1,x2,y2,color=RULE,width=1,extra=''):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"{extra}/>'


def document(width,height,title,description,body):
    defs=('<pattern id="engineering-grid" width="32" height="32" patternUnits="userSpaceOnUse">'
          '<path d="M32 0H0V32" fill="none" stroke="#42647f" stroke-width=".65" opacity=".2"/>'
          '</pattern><pattern id="scan-lines" width="8" height="8" patternUnits="userSpaceOnUse">'
          '<path d="M0 7H8" stroke="#88bfe8" stroke-width=".5" opacity=".07"/></pattern>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="profile-title profile-description">'
            f'<title id="profile-title">{esc(title)}</title><desc id="profile-description">{esc(description)}</desc>'
            '<defs>'+defs+'</defs>'+rect(0,0,width,height,N,20)+rect(0,0,width,height,'url(#engineering-grid)',20)
            +body+'</svg>\n')


def corners(x,y,w,h,color):
    return ''.join(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2"/>' for d in
                   [f'M{x} {y+14}V{y}H{x+14}',f'M{x+w-14} {y}H{x+w}V{y+14}',
                    f'M{x} {y+h-14}V{y+h}H{x+14}',f'M{x+w-14} {y+h}H{x+w}V{y+h-14}'])


def orbital(cx,cy,radius,seed=0,accent=T):
    out=[]
    for i in range(3):
        angle=-34+i*43+seed%13
        out.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{radius-i*radius*.19:.2f}" '
                   f'ry="{radius*.47-i*radius*.08:.2f}" fill="none" stroke="{accent}" '
                   f'stroke-width="1.3" opacity=".5" transform="rotate({angle} {cx} {cy})"/>')
    for i in range(7):
        angle=math.radians(i*51+seed*7)
        px,py=cx+radius*.86*math.cos(angle),cy+radius*.6*math.sin(angle)
        out.append(f'<circle cx="{px:.2f}" cy="{py:.2f}" r="{3+i%3}" fill="{C if i%2 else accent}"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{radius*.17:.2f}" fill="{D}" stroke="{M}" stroke-width="2"/>')
    return ''.join(out)


def unique_sources(project,annex):
    by_url={}
    for source in project['sources']+annex.get('additional_sources',[]):
        by_url.setdefault(source['url'],source)
    return list(by_url.values())


def counts(project,annex):
    return {'fields':len(annex['data_dictionary']), 'requirements':len(annex['requirements']),
            'planned_verification_cases':len(annex['verification_cases']),
            'derivation_steps':len(annex['derivation']), 'trade_options':len(annex['trade_study']),
            'failure_modes':len(annex['failure_modes']), 'implementation_work_packages':len(annex['implementation']),
            'cited_resources':len(unique_sources(project,annex)), 'data_resource_pointers':len(project['data']),
            'original_investigation_steps':len(project['plan']), 'validation_gates':len(project['validation']),
            'retained_work_packages':len(project.get('subprojects',[])) or 1}


def science_panel(x,y,width,label,paragraphs,accent=T,size=18,chars=77):
    blocks=[wrap(p,chars) for p in paragraphs]
    height=75+sum(len(b)*25+17 for b in blocks)
    out=[rect(x,y,width,height,P,14,RULE),corners(x,y,width,height,accent),
         txt(x+24,y+34,label,13,accent,700,mono=True,spacing=1.1)]
    cursor=y+69
    for block in blocks:
        out.append(text_lines(x+24,cursor,block,size,25,W))
        cursor += len(block)*25+17
    return ''.join(out),height


def metadata_panel(x,y,width,data):
    items=[('FIELDS','fields'),('REQUIREMENTS','requirements'),('PLANNED CASES','planned_verification_cases'),
           ('DERIVATION STEPS','derivation_steps'),('TRADE OPTIONS','trade_options'),('FAILURE MODES','failure_modes'),
           ('IMPLEMENTATION PACKAGES','implementation_work_packages'),('CITED RESOURCES','cited_resources'),
           ('DATA RESOURCE POINTERS','data_resource_pointers'),('ORIGINAL STUDY STEPS','original_investigation_steps'),
           ('VALIDATION GATES','validation_gates'),('RETAINED WORK PACKAGES','retained_work_packages')]
    height=652
    out=[rect(x,y,width,height,D,14,RULE),corners(x,y,width,height,M),
         txt(x+24,y+34,'CONTROLLED ARTIFACT INVENTORY',13,M,700,mono=True)]
    for i,(label,key) in enumerate(items):
        cx=x+22+(i%2)*218
        cy=y+60+(i//2)*90
        out += [rect(cx,cy,205,77,P,9),txt(cx+13,cy+34,str(data[key]),29,W,700),
                text_lines(cx+13,cy+56,wrap(label,25),10,12,C if key=='planned_verification_cases' else MUTED,700)]
    out.append(txt(x+24,y+630,'COUNTS OF RECORDS · NO COMPLETION SCORES',11,MUTED,mono=True))
    return ''.join(out),height


def field_panel(x,y,width,fields):
    height=96+sum(49+max(0,len(wrap(r['field'],35))-1)*20 for r in fields)
    out=[rect(x,y,width,height,P,14,RULE),corners(x,y,width,height,B),
         txt(x+24,y+34,'DATA SIGNATURE / DEFINED FIELDS',13,B,700,mono=True)]
    cursor=y+69
    for index,row in enumerate(fields):
        field_lines=wrap(row['field'],35)
        out += [txt(x+23,cursor,f'{index+1:02d}',11,T,700,mono=True),
                text_lines(x+57,cursor,field_lines,15,20,W,700,mono=True)]
        cursor+=len(field_lines)*20+4
        unit_lines=wrap(str(row['unit']),47)
        # Unit details are complete in the field atlas. Here only names are the visual signature.
        out.append(txt(x+57,cursor,'dictionary → schema → acquisition template',11,MUTED))
        cursor+=25
    out.append(txt(x+24,y+height-20,'Proposed acquisition shape · observations pending',12,C))
    return ''.join(out),height


def trace_panel(x,y,width,annex):
    requirements=' · '.join(r['id'] for r in annex['requirements'])
    cases=' · '.join(r['id'] for r in annex['verification_cases'])
    req_lines,case_lines=wrap(requirements,48),wrap(cases,48)
    height=159+len(req_lines)*22+len(case_lines)*22
    out=[rect(x,y,width,height,D,14,RULE),corners(x,y,width,height,C),
         txt(x+24,y+34,'TRACEABILITY / IDs THAT STAY WITH THE WORK',11,C,700,mono=True),
         txt(x+24,y+68,'REQUIREMENT REGISTER',11,T,700,mono=True),
         text_lines(x+24,y+93,req_lines,14,22,W,mono=True)]
    cursor=y+93+len(req_lines)*22+13
    out += [txt(x+24,cursor,'SPECIFIED VERIFICATION CASES',11,C,700,mono=True),
            text_lines(x+24,cursor+25,case_lines,14,22,W,mono=True),
            txt(x+24,y+height-19,'Execution evidence is required before case closure.',12,MUTED)]
    return ''.join(out),height


def references_panel(x,y,width,sources):
    blocks=[wrap(s['title'],47) for s in sources]
    height=103+sum(len(block)*19+17 for block in blocks)
    out=[rect(x,y,width,height,P,14,RULE),corners(x,y,width,height,T),
         txt(x+24,y+34,'REFERENCE CONSTELLATION',13,T,700,mono=True)]
    cursor=y+68
    for index,block in enumerate(blocks):
        out.append(txt(x+23,cursor,f'{index+1:02d}',11,C,700,mono=True))
        out.append(text_lines(x+55,cursor,block,14,19,W))
        cursor+=len(block)*19+17
    out.append(txt(x+24,y+height-20,'References are pointers; archive acquisition is separate.',11,MUTED))
    return ''.join(out),height


def mission_profile(project,annex,sessions):
    pid=project['id']; stats=counts(project,annex); width=1400
    name_lines=wrap(project['name'],55)
    original_lines=wrap(project['original_title'],118)
    session_lines=wrap(f'SESSION {project["session"]} / {sessions[project["session"]]}',112)
    top=88+len(name_lines)*48+24+len(original_lines)*27+len(session_lines)*25+97
    seed=int(hashlib.sha256(pid.encode()).hexdigest()[:8],16)
    out=[line(48,44,94,44,T,3),txt(108,50,'ATLAS / ENGINEERING PROFILE',14,T,700,mono=True,spacing=1.2),
         txt(1352,50,pid+' · SOURCE-BOUND RESEARCH',13,C,700,mono=True,anchor='end'),
         text_lines(48,113,name_lines,38,48,W,700)]
    cursor=113+len(name_lines)*48+7
    out.append(txt(48,cursor,'ORIGINAL PROJECT / EXACT SUPPLIED TITLE',11,M,700,mono=True,spacing=.8))
    cursor+=26
    out.append(text_lines(48,cursor,original_lines,19,27,MUTED))
    cursor+=len(original_lines)*27+10
    out.append(text_lines(48,cursor,session_lines,15,25,T,700))
    cursor+=len(session_lines)*25+9
    out += [rect(48,cursor,1304,52,D,8,RULE),
            txt(66,cursor+21,'PROJECT EMPIRICAL EVIDENCE PENDING',12,C,700,mono=True),
            txt(66,cursor+41,'No project observations acquired · specified cases await execution · shared demonstrations are separately labeled',13,MUTED)]
    y0=cursor+76
    left_x,left_width,right_x,right_width=48,808,884,468
    left_y,right_y=y0,y0
    about=[project['summary']]
    for label,paras,accent in [
            ('ABOUT THIS INVESTIGATION',about,T),
            ('THE SCIENTIFIC QUESTION',[project['question']],B),
            ('TESTABLE HYPOTHESIS / NOT AN OBSERVED RESULT',[project['hypothesis']],M),
            ('MODEL BOUNDARY / ASSUMPTIONS',project['model']['assumptions'],C),
            ('VALIDITY LIMITS / THE CLAIM STOPS HERE',[project['model']['limitations']],T)]:
        body,height=science_panel(left_x,left_y,left_width,label,paras,accent,18,76)
        out.append(body);left_y+=height+24
    body,height=metadata_panel(right_x,right_y,right_width,stats)
    out.append(body);right_y+=height+24
    for panel,args in [(field_panel,(annex['data_dictionary'],)),(trace_panel,(annex,)),
                       (references_panel,(unique_sources(project,annex),))]:
        body,height=panel(right_x,right_y,right_width,*args)
        out.append(body);right_y+=height+24
    # The decorative constellation fills available space without encoding measurements.
    if right_y-left_y>200:
        blank=right_y-left_y-24
        out += [rect(left_x,left_y,left_width,blank,D,14,RULE),
                txt(left_x+24,left_y+35,'ENGINEERING CONSTELLATION / DECORATIVE',11,MUTED,mono=True),
                orbital(left_x+left_width*.5,left_y+blank*.5,min(190,blank*.30),seed%89,T),
                txt(left_x+left_width*.5,left_y+blank-31,'A question becomes a model. A model earns evidence.',18,T,anchor='middle')]
        left_y+=blank+24
    bottom=max(left_y,right_y)+2
    out += [rect(48,bottom,1304,143,D,14,RULE),corners(48,bottom,1304,143,B),
            txt(72,bottom+34,'YOUR READING ROUTE / CONTROLLED ARTIFACTS',13,B,700,mono=True)]
    nodes=[('DESIGN BASIS','question + scope',T),('MATHEMATICAL MODEL',str(stats['derivation_steps'])+' derivation steps',B),
           ('FIELD ATLAS',str(stats['fields'])+' defined fields',M),('REQUIREMENTS',str(stats['requirements'])+' specified gates',T),
           ('VERIFICATION',str(stats['planned_verification_cases'])+' planned cases',C)]
    for index,(label,detail,accent) in enumerate(nodes):
        x=72+index*256
        out += [rect(x,bottom+52,232,65,P,8),txt(x+12,bottom+77,label,11,accent,700,mono=True),
                txt(x+12,bottom+100,detail,14,W)]
        if index<4:out.append(line(x+236,bottom+86,x+250,bottom+86,MUTED,1.4))
    footer=bottom+176; height=footer+84
    out += [txt(48,footer,'NOTES FROM THE CONTROL ROOM',11,M,700,mono=True,spacing=.8),
            txt(48,footer+25,'NASA-inspired mission names are creative identifiers. This profile describes research design; it claims no NASA approval or flight qualification.',14,MUTED),
            txt(48,footer+52,'Original titles are preserved. Data pointers and citations do not establish that the original teams’ observations have been acquired.',13,MUTED),
            txt(1352,footer+72,f'{pid} / ATLAS PROFILE / STATIC + EDITABLE',10,T,700,mono=True,anchor='end')]
    desc=(f'{pid}, {project["name"]}. Original project: {project["original_title"]}. '
          f'Session {project["session"]}: {sessions[project["session"]]}. '
          f'Scientific question: {project["question"]} Testable hypothesis: {project["hypothesis"]}. '
          f'Controlled metadata counts: {json.dumps(stats,sort_keys=True)}. '
          'Project empirical evidence pending. No project observations acquired. All verification-case counts are specified planned work, not completed experiments. '
          'Decorative orbital motifs encode no measured values. No NASA affiliation or approval claimed.')
    return document(width,height,pid+' / '+project['name']+' engineering mission profile',desc,''.join(out)),width,height,stats


def dashboard(projects,annexes,sessions):
    amap={a['id']:a for a in annexes}
    totals={'projects':len(projects),'sessions':len(sessions),'fields':sum(len(a['data_dictionary']) for a in annexes),
            'requirements':sum(len(a['requirements']) for a in annexes),
            'planned_verification_cases':sum(len(a['verification_cases']) for a in annexes)}
    all_sources={s['url'] for p in projects for s in unique_sources(p,amap[p['id']])}
    derivatives=sum(len(a['derivation']) for a in annexes)
    trades=sum(len(a['trade_study']) for a in annexes)
    failures=sum(len(a['failure_modes']) for a in annexes)
    packages=sum(len(a['implementation']) for a in annexes)
    width,height=1600,2010
    out=[line(48,46,110,46,T,3),txt(127,52,'ATLAS / RESEARCH NETWORK',15,T,700,mono=True,spacing=1.8),
         txt(1552,52,'A— I / SOURCE ORDER LOCKED',14,C,700,mono=True,anchor='end'),
         txt(48,148,'MISSION CONTROL',71,W,700),
         txt(52,190,'The engineering archive with a profile for every idea.',26,MUTED),
         txt(52,227,'Models, fields, interfaces, uncertainty, trade space, verification and cited resources — all visible.',19,MUTED),
         orbital(1400,148,115,3,M)]
    for i,(key,label,accent) in enumerate([('projects','PROJECT PROFILES',T),('fields','DEFINED FIELDS',B),
                                          ('requirements','SPECIFIED REQUIREMENTS',M),
                                          ('planned_verification_cases','PLANNED VERIFICATION CASES',C)]):
        x=48+i*386
        out += [rect(x,273,362,126,P,14,RULE),corners(x,273,362,126,accent),
                txt(x+22,332,f'{totals[key]:,}',43,W,700),txt(x+22,374,label,12,accent,700,mono=True)]
    out += [txt(48,447,'THE SESSION CONSTELLATION',19,T,700,mono=True),
            txt(48,477,'Every session stays in its supplied position. Bars compare project counts only.',16,MUTED)]
    max_projects=max(EXPECTED.values())
    for index,session in enumerate(EXPECTED):
        x,y=48+(index%3)*518,510+(index//3)*228
        selected=[p for p in projects if p['session']==session]
        field_count=sum(len(amap[p['id']]['data_dictionary']) for p in selected)
        req_count=sum(len(amap[p['id']]['requirements']) for p in selected)
        case_count=sum(len(amap[p['id']]['verification_cases']) for p in selected)
        accent=[T,B,M][index%3]
        out += [rect(x,y,492,204,P,14,RULE),corners(x,y,492,204,accent),
                rect(x+18,y+17,42,42,D,8),txt(x+39,y+48,session,25,accent,700,mono=True,anchor='middle'),
                text_lines(x+76,y+37,wrap(sessions[session],35),18,23,W,700),
                txt(x+22,y+100,str(len(selected)),34,W,700),txt(x+92,y+100,'project records',15,MUTED),
                txt(x+22,y+132,f'{field_count} fields · {req_count} requirements · {case_count} planned cases',13,MUTED),
                rect(x+22,y+154,448,8,D,4),rect(x+22,y+154,448*len(selected)/max_projects,8,accent,4),
                txt(x+22,y+188,f'{session}01 — {session}{len(selected):02d} / EXACT ORIGINAL ORDER',11,accent,mono=True)]
    out += [txt(48,1262,'ARTIFACT WALL / WHAT THE REGISTRY ACTUALLY CONTAINS',18,B,700,mono=True)]
    for i,(value,label,detail,accent) in enumerate([
            (derivatives,'DERIVATION STEPS','Mathematical reasoning',B),
            (trades,'TRADE OPTIONS','Alternatives and decision rules',M),
            (failures,'FAILURE MODES','Effects, detection and mitigation',C),
            (packages,'IMPLEMENTATION PACKAGES','Specified investigation work',T),
            (len(all_sources),'DISTINCT CITED RESOURCES','Unique resource URLs',B)]):
        x=48+i*309
        out += [rect(x,1290,285,144,D,12,RULE),txt(x+18,1345,f'{value:,}',35,W,700),
                txt(x+18,1381,label,11,accent,700,mono=True),txt(x+18,1409,detail,12,MUTED)]
    out += [rect(48,1472,1504,220,P,14,RULE),corners(48,1472,1504,220,M),
            txt(72,1508,'THE EVIDENCE STATUS / SCIENTIFIC HONESTY IS PART OF THE AESTHETIC',15,M,700,mono=True),
            txt(72,1548,'PROJECT EMPIRICAL EVIDENCE PENDING',22,C,700),
            txt(72,1584,'No project observations acquired. Proposed data contracts describe future records and keep missingness explicit.',18,MUTED),
            txt(72,1616,'Shared synthetic demonstrations and the included public catalog snapshot are separately labeled in the data gallery.',18,MUTED),
            txt(72,1648,'These bars count documentation. They do not measure science success, readiness, test completion or NASA approval.',18,MUTED)]
    out += [rect(48,1730,1504,178,D,14,RULE),corners(48,1730,1504,178,T),
            txt(72,1764,'THE COMPLETE READING ROUTE',15,T,700,mono=True)]
    stages=['MISSION PROFILE','ENGINEERING RECORD','FIELD ATLAS','MODEL + FIGURES','EVIDENCE + SOURCES']
    for i,label in enumerate(stages):
        x=72+i*300
        out += [rect(x,1788,268,73,P,10),txt(x+16,1817,f'0{i+1}',12,C,700,mono=True),
                txt(x+16,1842,label,12,T if i%2==0 else B,700,mono=True)]
        if i<4:out.append(line(x+274,1826,x+292,1826,MUTED,1.5))
    out += [txt(48,1950,'ALL 117 ORIGINAL IDEAS · BOTH D03 INVESTIGATIONS · NO PROJECT DROPPED',13,C,700,mono=True),
            txt(48,1978,'Original static document artwork. Orbital motifs are decorative. NASA-inspired independent research documentation.',14,MUTED)]
    desc=('ATLAS mission control dashboard. '+json.dumps(totals,sort_keys=True)+'. '
          f'{derivatives} derivation steps, {trades} trade options, {failures} failure modes, '
          f'{packages} implementation work packages and {len(all_sources)} distinct cited resource URLs. '
          'Every count comes from the controlled registry. Session bars compare project counts only. '
          'Project empirical evidence pending; no project observations acquired; specified verification cases await execution. '
          'Shared demonstration and public catalog evidence are separately labeled. No personnel, readiness or scientific-performance values invented.')
    return document(width,height,'ATLAS mission control / complete engineering archive',desc,''.join(out)),width,height,totals


def generate(repo):
    """Write 117 co-located profiles, one dashboard and a deterministic manifest."""
    repo=Path(repo).resolve();registry=repo/'registry'
    read=lambda name:json.loads((registry/name).read_text(encoding='utf-8'))
    projects=read('projects.json');annexes=read('engineering_annexes.json')
    sessions=read('sessions.json');paths=read('project_paths.json');originals=read('original_titles.json')
    wanted=[f'{s}{i:02}' for s,count in EXPECTED.items() for i in range(1,count+1)]
    assert [p['id'] for p in projects]==wanted and [a['id'] for a in annexes]==wanted
    assert [p['id'] for p in paths]==wanted and len(projects)==117
    assert list(sessions)==list(EXPECTED), 'Session order must remain A–I.'
    assert len(next(p for p in projects if p['id']=='D03').get('subprojects',[]))>=2
    for project in projects:
        assert project['original_title']==originals[project['session']][int(project['id'][1:])-1]
    amap={a['id']:a for a in annexes};pmap={p['id']:p for p in paths}
    def save(path,content,width,height):
        assert path.resolve().is_relative_to(repo)
        tree=ET.fromstring(content)
        assert tree.find(NS+'title').text and tree.find(NS+'desc').text
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_bytes(content.encode('utf-8'))
        return {'path':str(path.relative_to(repo)).replace('\\','/'),'sha256':digest(path),
                'bytes':path.stat().st_size,'width':width,'height':height}
    records=[]
    for project in projects:
        content,width,height,stats=mission_profile(project,amap[project['id']],sessions)
        folder=repo/pmap[project['id']]['directory']
        assert folder.resolve().is_relative_to(repo/'research')
        row=save(folder/'figures/mission-profile.svg',content,width,height)
        row.update(project_id=project['id'],counts=stats)
        records.append(row)
    content,width,height,totals=dashboard(projects,annexes,sessions)
    board=save(repo/'assets/mission-control.svg',content,width,height)
    input_files=sorted(list(registry.glob('*.json'))+list(registry.glob('*.csv')))
    manifest={'generator':'ATLAS source-bound engineering mission profiles / Python standard library',
              'purpose':'Detailed static profiles from controlled research definitions; no observations, personnel, readiness scores or empirical results generated.',
              'input_hashes':{str(p.relative_to(repo)).replace('\\','/'):digest(p) for p in input_files},
              'palette':PALETTE,'fonts':{'body':'Arial, Helvetica, sans-serif','technical':'Consolas, Menlo, monospace'},
              'counts':totals,'project_order':wanted,'profile_count':len(records),'profiles':records,'dashboard':board,
              'evidence_state':'Project empirical evidence pending; specified verification cases remain planned work; shared demonstrations and public snapshot are separately labeled.'}
    assert len({r['sha256'] for r in records})==117, 'Every profile must carry unique project content.'
    (repo/'assets/profile_manifest.json').write_bytes((json.dumps(manifest,indent=2,ensure_ascii=False)+'\n').encode('utf-8'))
    print('Generated 117 detailed engineering mission profiles and the portfolio mission-control dashboard.')
    return manifest


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[1])
    args=parser.parse_args();generate(args.repo)


if __name__=='__main__':main()
