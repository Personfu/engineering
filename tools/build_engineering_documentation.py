"""Build engineering records and A-I handbooks from reviewed structured sources.

Run from any directory: python tools/build_engineering_documentation.py
Source records live in registry/projects.json and registry/engineering_annexes.json.
This produces documentation and empty data contracts, never project measurements.
Architecture SVG rendering is a separate, optional build step.
"""
import csv
import hashlib
import json
import re
from pathlib import Path
from layout import project_directory, project_document, relative, rebase_markdown

ROOT = Path(__file__).resolve().parents[1]
SESSIONS = json.loads((ROOT/'registry/sessions.json').read_text(encoding='utf-8'))
DEMOS = {
    'A01':'01_fractal_escape_distance', 'A02':'02_ideal_binary_liquidus',
    'E06':'03_balloon_thermal', 'E03':'03_balloon_thermal', 'I05':'03_balloon_thermal',
    'D04':'04_sphere_drag', 'B14':'05_hydrologic_reservoir', 'B23':'05_hydrologic_reservoir',
    'I10':'06_one_axis_attitude', 'I08':'07_two_body_convergence', 'I12':'07_two_body_convergence',
    'C08':'08_spectral_identifiability', 'H09':'08_spectral_identifiability',
    'C05':'09_real_exoplanet_sample', 'C23':'09_real_exoplanet_sample',
}
DATA_FIGURES = {
    'A01':'17_fractal_resolution_and_escape', 'A02':'16_ideal_binary_phase_regions',
    'B23':'12_hydrologic_water_ledger', 'C05':'10_catalog_values_and_coverage',
    'C23':'10_catalog_values_and_coverage', 'C08':'15_spectral_information_and_noise',
    'H09':'15_spectral_information_and_noise', 'D04':'18_sphere_drag_reference_departure',
    'E06':'11_thermal_power_and_response', 'I10':'13_attitude_phase_and_authority',
    'I08':'14_orbit_conservation_and_refinement', 'I12':'14_orbit_conservation_and_refinement',
    'I13':'14_orbit_conservation_and_refinement',
}

def link(source, target, label):
    return f'[{label}]({relative(source,target)})'

def figure(source, target, label):
    return '!'+link(source,target,label)

def plot_caption(pid):
    ledger=ROOT/'data/figures/DATA_FIGURES.json'
    if ledger.exists():
        for item in json.loads(ledger.read_text(encoding='utf-8'))['figures']:
            if item['id']==DATA_FIGURES.get(pid):return item['caption']
    return 'Illustrative reduced-model diagnostic; see the data atlas for input provenance and limits.'

def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes((value.rstrip()+'\n').encode('utf-8'))

def dump(path, obj):
    write(path, json.dumps(obj, ensure_ascii=False, indent=2))

def seq(value):
    return value if isinstance(value,list) else [value]

def prose(value):
    return '\n\n'.join(str(x) for x in seq(value))+'\n\n'

def bullets(value):
    return '\n'.join('- '+str(x) for x in seq(value))+'\n\n'

def cell(value):
    return str(value).replace('|', '&#124;').replace('\n','<br>')

def table(rows, fields, labels=None):
    labels=labels or fields
    return '| '+' | '.join(labels)+' |\n| '+' | '.join('---' for _ in fields)+' |\n'+''.join('| '+' | '.join(cell(r.get(f,'')) for f in fields)+' |\n' for r in rows)+'\n'

def equation(value):
    value=str(value)
    return ('$$\n'+value+'\n$$\n\n') if '\\' in value else ('```text\n'+value+'\n```\n\n')

def merged_sources(project, annex):
    result=[]
    seen=set()
    for s in project['sources']+annex.get('additional_sources',[]):
        if s['url'] not in seen:
            result.append(s);seen.add(s['url'])
    return result

def mission_connections(projects,annexes):
    """Rank transparent reading connections, never inferred physical dependencies."""
    lookup={a['id']:a for a in annexes}
    sources={p['id']:{s['url']:s['title'] for s in merged_sources(p,lookup[p['id']])} for p in projects}
    frequency={url:sum(url in rows for rows in sources.values()) for url in set().union(*(set(v) for v in sources.values()))}
    generic={url for url,n in frequency.items() if n>12}
    connections=[]
    for i,p in enumerate(projects):
        candidates=[]
        for j,q in enumerate(projects):
            if p['id']==q['id']:continue
            shared=sorted((sources[p['id']].keys()&sources[q['id']].keys())-generic)
            same=p['session']==q['session']
            demo=DEMOS.get(p['id']) if DEMOS.get(p['id']) and DEMOS.get(p['id'])==DEMOS.get(q['id']) else None
            if not(shared or same or demo):continue
            bases=[]
            if shared:bases.append('Shared cited technical resources')
            if demo:bases.append('Shared included reduced-model or catalog illustration')
            if same:bases.append('Same supplied discipline/session')
            row={'project_id':q['id'],'same_session':same,
                 'shared_sources':[{'title':sources[p['id']][url],'url':url} for url in shared],
                 'shared_demo':demo,'basis':bases}
            candidates.append((-(3*bool(demo)+2*len(shared)+int(same)),abs(i-j),j,row))
        candidates.sort(key=lambda row:row[:3])
        connections.append({'project_id':p['id'],'links':[r[3] for r in candidates[:6]]})
    manifest={'purpose':'Transparent reading/resource connections, not physical dependencies, collaborations or validation evidence.',
              'ranking':'Shared included illustration (3), each non-generic shared source (2), same session (1); ties follow proximity in supplied order.',
              'excluded_generic_source_urls':sorted(generic),
              'input_hashes':{f'registry/{name}.json':hashlib.sha256((ROOT/'registry'/f'{name}.json').read_bytes()).hexdigest() for name in ['projects','engineering_annexes']},
              'projects':connections}
    dump(ROOT/'registry/mission_connections.json',manifest)
    return {row['project_id']:row['links'] for row in connections}

def profile_sections(p,a,connections,all_projects):
    doc=project_document(p);directory=project_directory(p);pid=p['id'];model=p['model']
    s='## Mission profile\n\n'+figure(doc,directory/'figures/mission-profile.svg',pid+' engineering mission profile: scientific question, hypothesis, model scope and evidence status')+'\n\n'
    s+='| Profile panel | Engineering signal | Open the evidence |\n| --- | --- | --- |\n'
    s+='| Mission identity | '+cell(p['original_title'])+' | [Scientific objective](#purpose-and-scientific-objective) |\n'
    s+='| Model cockpit | '+str(len(model['equations']))+' governing expressions; '+str(len(a['derivation']))+' derivation steps; declared assumptions and validity envelope | [Mathematical formulation](#4-mathematical-model-and-derivation) |\n'
    s+='| Data blueprint | '+str(len(a['data_dictionary']))+' proposed fields with types, units and quality rules | '+link(doc,directory/'data/README.md','Field map & downloads')+' |\n'
    s+='| Verification queue | '+str(len(a['requirements']))+' proposed requirements; '+str(len(a['verification_cases']))+' specified cases; project execution evidence pending | [Case definitions](#8-verification-and-validation-cases) |\n'
    s+='| Figure wall | Architecture, field map, planned result description'+('; included shared illustration' if pid in DEMOS or pid in DATA_FIGURES else '')+' | '+link(doc,directory/'figures/README.md','Open full gallery')+' |\n'
    s+='| Resource library | '+str(len(merged_sources(p,a)))+' cited primary resources with support statements | [Cited resources](#12-cited-technical-and-scientific-resources) |\n\n'
    s+='### Model cockpit\n\n**Analysis method:** '+model['method']+'\n\n'
    s+='**Operating envelope:** '+model['limitations']+'\n\n'
    s+='**Variables and conventions**\n\n'+bullets(model['variables'])
    s+='### Artifact wall\n\n'
    if pid in DATA_FIGURES:
        s+=figure(doc,ROOT/'data/figures'/f'{DATA_FIGURES[pid]}.svg',pid+' included scientific diagnostic')+'\n\n'+plot_caption(pid)+'\n\n'
        s+=link(doc,ROOT/'data/figures'/f'{DATA_FIGURES[pid]}.provenance.json','Exact inputs, transformations and output hashes')+'\n\n'
    elif pid in DEMOS:
        s+=figure(doc,ROOT/'models/figures'/f'{DEMOS[pid]}.svg',pid+' shared illustrative model')+'\n\n'
        s+='Shared illustration with a narrower domain than the project model. '+link(doc,ROOT/'models/README.md','Read its parameters, evidence class and checks')+'.\n\n'
    else:
        s+=figure(doc,directory/'figures/architecture.svg',pid+' proposed analysis architecture')+'\n\n'+a['figure_caption']+'\n\n'
    s+='**Scientific result to produce:** '+str(p['visual'].get('description',p['visual']))+'\n\n'
    s+='### Investigation feed · planned work\n\nThe feed records proposed work packages. A row becomes executed evidence only with versioned inputs, outputs and a reviewed result.\n\n'
    rows=[{'step':f'{i+1:02}','state':'Planned','work':v} for i,v in enumerate(a['implementation'])]
    s+=table(rows,['step','state','work'],['Sequence','Evidence state','Engineering work package'])
    s+='### Mission connections\n\nConnections are reading routes based on actual shared resources, supplied sessions or included illustrations. They do not establish physical dependencies, team collaborations or validated results.\n\n'
    rows=[]
    for connection in connections:
        q=all_projects[connection['project_id']]
        details=[]
        if connection['same_session']:details.append('Session '+q['session'])
        if connection['shared_demo']:details.append('Included illustration: '+connection['shared_demo'])
        if connection['shared_sources']:
            details.extend(f'[{r["title"]}]({r["url"]})' for r in connection['shared_sources'])
        rows.append({'mission':link(doc,project_document(q),q['id']+' · '+q['name']),
                     'topic':q['original_title'],'connection':'; '.join(details)})
    s+=table(rows,['mission','topic','connection'],['Connected mission','Original investigation','Recorded connection basis'])
    s+=link(doc,ROOT/'registry/mission_connections.json','Machine-readable connection register and ranking rule')+'\n\n'
    s+='### Reading playlist\n\n| Route | Start here | Continue to |\n| --- | --- | --- |\n'
    s+='| Understand the idea | [Scientific objective](#purpose-and-scientific-objective) | [Design boundary](#1-design-basis-and-analysis-boundary) → [Mathematics](#4-mathematical-model-and-derivation) |\n'
    s+='| Inspect the data | '+link(doc,directory/'data/README.md','Visual blueprint')+' | [Provenance](#5-data-specifications-and-provenance) → [Uncertainty](#6-uncertainty-sensitivity-and-identifiability) |\n'
    s+='| Make a design decision | [Trade study](#7-engineering-trade-study) | [Failure modes](#10-failure-modes-and-interpretation-controls) → [Required outputs](#11-required-engineering-outputs) |\n'
    s+='| Prepare execution | [Requirements](#2-requirements-and-verification-traceability) | [Verification](#8-verification-and-validation-cases) → [Implementation](#9-implementation-and-reproducible-work-packages) |\n\n'
    s+='## Complete engineering dossier\n\nThe profile above is a browsing layer. The full design basis, equations, derivations, data contract, uncertainty, trades and controlled case definitions follow.\n\n'
    return s

def mission_control(projects,lookup):
    """Detailed GitHub-native portal; the canonical register retains its order."""
    doc=ROOT/'MISSION_CONTROL.md'
    s='# ATLAS · Mission control\n\n![ATLAS engineering dashboard](assets/mission-control.svg)\n\n'
    s+='[Profile directory](research/README.md) · [Data observatory](data/README.md) · [Table inventory](data/TABLES.md) · [Figure wall](data/figures/README.md) · [Continuous handbooks](handbooks/README.md)\n\n'
    s+='## Enter a mission profile\n\nEach profile opens with its scientific identity, a model cockpit, a figure wall, a planned-work feed, related reading connections and a reading playlist. Its complete engineering dossier follows: original models, derivations, interfaces, data, uncertainty, trades, verification cases, failure analysis and cited primary resources.\n\n'
    s+='| Profile room | What is visible | Controlled detail behind it |\n| --- | --- | --- |\n'
    s+='| Mission identity | Original investigation, mission name, question and testable hypothesis | Exact title and stable project ID in the source registry |\n'
    s+='| Model cockpit | Method, variables, conventions and operating envelope | Governing expressions, derivation, assumptions and boundary conditions |\n'
    s+='| Artifact wall | Architecture, data blueprint and included or planned scientific visuals | Figure captions, model methods and input/output hashes |\n'
    s+='| Data observatory | All included numerical tables and complete proposed field maps | CSV headers, units, missingness, schemas and provenance |\n'
    s+='| Investigation feed | Proposed engineering work packages | Specified evidence, execution criteria and versioned artifacts required for closure |\n'
    s+='| Mission connections | Shared cited resources, supplied disciplines and included illustrations | Transparent connection register; no inferred physical dependency or team relationship |\n'
    s+='| Reading playlist | Routes from the concept to data, decisions or execution | Direct navigation to the full engineering sections |\n\n'
    s+='## Reading playlists across the portfolio\n\nThese are thematic reading paths. They do not assert a shared experiment or an integrated flight system.\n\n'
    routes=[('Pixels to planets',['A01','C02','C15','H02','C05']),
            ('Air to orbit',['D04','E06','E08','I04','I10','I12']),
            ('Earth in balance',['B10','B14','B23','B18','G06']),
            ('Spectra to matter',['A11','H04','C08','H09','H08','A12'])]
    plookup={p['id']:p for p in projects}
    for title,ids in routes:
        s+='### '+title+'\n\n'+' → '.join(link(doc,project_document(plookup[pid]),pid+' · '+plookup[pid]['name']) for pid in ids)+'\n\n'
    s+='## Profile wall\n\nThese four profile previews illustrate the layout. The complete ordered directory below retains every project.\n\n'
    for pid in ['A01','C05','E06','I10']:
        p=plookup[pid]
        s+='### '+pid+' · '+p['name']+'\n\n'+figure(doc,project_directory(p)/'figures/mission-profile.svg',p['name']+' complete mission profile')+'\n\n'
        s+=link(doc,project_document(p),'Enter this engineering dossier')+' · '+link(doc,project_directory(p)/'data/README.md','Data blueprint')+' · '+link(doc,project_directory(p)/'figures/README.md','Figure wall')+'\n\n'
    s+='## Every original investigation · A–I directory\n\n'
    for session,title in SESSIONS.items():
        s+='### Session '+session+' · '+title+'\n\n'
        s+='[![Session '+session+'](assets/sessions/'+session+'.svg)](research/'+session+'/README.md)\n\n'
        rows=[]
        for p in projects:
            if p['session']!=session:continue
            a=lookup[p['id']]
            rows.append({'id':p['id'],'mission':link(doc,project_document(p),p['name']),
                         'topic':p['original_title'],'fields':len(a['data_dictionary']),
                         'requirements':len(a['requirements']),'cases':len(a['verification_cases'])})
        s+=table(rows,['id','mission','topic','fields','requirements','cases'],['ID','Mission profile','Original investigation','Defined fields','Proposed requirements','Specified cases'])
    s+='## Evidence desk\n\nThe public catalog snapshot, illustrative model outputs and proposed acquisition contracts carry distinct evidence labels. Project-specific empirical validation remains pending. The [data inventory](data/TABLES.md), [figure manifest](data/figures/DATA_FIGURES.json), [profile manifest](assets/profile_manifest.json) and [connection register](registry/mission_connections.json) expose the inputs behind the browsing layers. [Engineering review and integrity records](evidence/README.md) describe executed checks and their limits.\n'
    write(doc,s)

def value_schema(original):
    """Encode scientific type notation; physical semantics remain in the ICD.

    measurement<T> and model<T> use the raw T value with sidecar provenance.
    posterior<T>/distribution<T> use an explicit distribution record.
    complex values use a real/imaginary object, not invalid JSON complex tokens.
    """
    lower=original.lower().strip()
    lower=re.sub(r'^nullable\s*','',lower).strip()
    if lower.startswith('<') and lower.endswith('>'): lower=lower[1:-1]
    lower=re.sub(r'\|\s*(null|limit)\b','',lower).strip()
    wrapped=re.fullmatch(r'(measurement|model|posterior|distribution)<(.+)>',lower)
    if wrapped:
        kind,inner=wrapped.groups()
        if kind in ['measurement','model']:
            result=value_schema(inner)
            result['x-encoding']=kind+' value encoded directly; qualifier, uncertainty, calibration and model version are in the provenance sidecar.'
            return result
        sample=value_schema(inner)
        return {'type':'object','required':['representation'],
                'properties':{'representation':{'enum':['empirical','parametric','summary','unidentified']},
                              'samples':{'type':'array','items':sample},
                              'weights':{'type':['array','null'],'items':{'type':'number','minimum':0}},
                              'parameters':{'type':'object'},'summary':{'type':'object'},
                              'model_id':{'type':['string','null']}},
                'additionalProperties':True,
                'x-encoding':kind+' record: representation is explicit; weights and sample dimensions require domain validation.'}
    if lower in ['distribution','posterior'] or lower=='distribution_record':
        return value_schema('distribution<struct>')
    if lower.startswith(('struct','record','restricted record','policy','structured','edge record','geometry','text record')) or '+' in lower:
        return {'type':'object','additionalProperties':True,
                'x-encoding':'Structured JSON record; member names, frames and mandatory subfields must be frozen in the project ICD before ingestion.'}
    sparse=re.fullmatch(r'sparse<(.+)>',lower)
    if sparse:
        index={'type':'array','items':{'type':'integer','minimum':0}}
        return {'type':'object','required':['shape','row','col','data'],
                'properties':{'shape':{'type':'array','items':{'type':'integer','minimum':0},'minItems':2,'maxItems':2},
                              'row':index,'col':index,'data':{'type':'array','items':value_schema(sparse.group(1))}},
                'additionalProperties':False,
                'x-encoding':'COO sparse matrix: parallel row/col/data arrays; shape and equal lengths require domain validation.'}
    # Bracket notation has precedence over scalar names. Enforce known dimensions.
    bracket=re.search(r'\[([^]]*)\]',lower)
    if bracket:
        before=lower[:bracket.start()].strip()
        after=lower[bracket.end():].strip()
        dims=[x.strip() for x in bracket.group(1).split(',')] if bracket.group(1) else ['']
        # [] and [2] in float[2][] are ordered nested dimensions, not flattened.
        vector_prefix=re.fullmatch(r'vector<(.+)>',before)
        if vector_prefix: before=vector_prefix.group(1)
        item=value_schema(before+after) if after.startswith('[') else value_schema(before)
        for dimension in reversed(dims):
            arr={'type':'array','items':item}
            if dimension.isdigit():arr.update(minItems=int(dimension),maxItems=int(dimension))
            else:arr['x-dimension']=dimension or 'variable length; ICD-defined'
            item=arr
        return item
    pair=re.fullmatch(r'pair<(.+)>',lower)
    if pair:return {'type':'array','items':value_schema(pair.group(1)),'minItems':2,'maxItems':2}
    generic=re.fullmatch(r'(array|vector|list|set|matrix|table)<(.+)>',lower)
    if generic:
        kind,inner=generic.groups()
        if ',' in inner: item={'type':'object','additionalProperties':True,'x-fields':inner}
        else:item=value_schema(inner)
        if kind=='matrix':item={'type':'array','items':item}
        result={'type':'array','items':item}
        if kind=='set':result['uniqueItems']=True
        return result
    # Containers above take precedence: array<record> contains objects.
    if '+' in lower or any(x in lower for x in ['record','struct','object','geometry','policy']) or lower in ['state','trace','sky']:
        return {'type':'object','additionalProperties':True,
                'x-encoding':'Structured JSON record; member names, frames and mandatory subfields must be frozen in the project ICD before ingestion.'}
    if 'complex' in lower and 'covariance' not in lower:
        return {'type':'object','properties':{'real':{'type':'number'},'imag':{'type':'number'}},
                'required':['real','imag'],'additionalProperties':False,
                'x-encoding':'real and imag share the declared physical unit; covariance ordering and any complex pseudo-covariance are recorded in the sidecar.'}
    if 'table' in lower:return {'type':'array','items':{'type':'object','additionalProperties':True}}
    if any(x in lower for x in ['matrix','covariance','raster']):
        scalar=value_schema('complex' if 'complex' in lower else ('integer' if 'integer' in lower else 'float'))
        return {'type':'array','items':{'type':'array','items':scalar},'x-dimension':'row/column ordering and dimensions frozen in ICD'}
    if any(x in lower for x in ['array','vector','list','set','polyline','field']):
        scalar=value_schema('integer' if 'integer' in lower else ('float' if 'float' in lower else 'typed scalar'))
        return {'type':'array','items':scalar,'x-dimension':'ordering/shape frozen in ICD'}
    if any(x in lower for x in ['boolean','bool']):return {'type':'boolean'}
    if 'int' in lower and 'float' in lower:
        return {'type':'number','x-encoding':'Integral or real numeric source encoding accepted; exact time unit, epoch and precision must be declared. Large integer timestamps must retain lossless integer/string transport in the ingestion ICD.'}
    if any(x in lower for x in ['integer','int32','int64','uint16','uint32','uint64','uint']):
        result={'type':'integer'}
        if 'uint' in lower:result['minimum']=0
        return result
    if any(x in lower for x in ['float','number','numeric','real','double']):return {'type':'number'}
    if 'datetime' in lower:return {'type':'string','format':'date-time'}
    if lower=='date':return {'type':'string','format':'date'}
    if 'scalar' in lower:return {'type':['number','string','boolean'],'x-encoding':'Exact scalar interpretation and unit must be frozen in the ICD.'}
    return {'type':'string'}

def contracts(project, annex):
    pid=project['id']
    properties={}
    for row in annex['data_dictionary']:
        field=row['field']
        assert field not in properties,(pid,'duplicate field',field)
        props=value_schema(row['type'])
        kind=props.get('type','object')
        props['type']=list(dict.fromkeys((kind if isinstance(kind,list) else [kind])+['null']))
        props.update({'description':row['meaning'],
               'x-unit':row['unit'],
               'x-source-type':row['type'],
               'x-quality-rule':row['quality_rule']})
        properties[field]=props
    schema={'$schema':'https://json-schema.org/draft/2020-12/schema',
            'title':pid+' '+project['name']+' engineering data contract',
            'description':'Proposed record contract. No data have been collected by this generator. Null is missing/unknown and must be qualified in the separate provenance record.',
            'type':'object','properties':properties,'required':list(properties),
            'additionalProperties':False,
            'x-project-id':pid,
            'x-unit-policy':'Use documented units; do not replace missing values with zero. Reference frames, covariance basis, calibration version and quality qualifiers reside in the provenance sidecar.',
            'x-domain-validation':'Physical range, covariance validity and declared quality rules require domain validation beyond JSON Schema.'}
    directory=project_directory(project)/'data'
    directory.mkdir(parents=True,exist_ok=True)
    dump(directory/'schema.json',schema)
    # A header-only CSV is an empty acquisition template, not a synthetic result.
    path=directory/'acquisition.csv'
    with path.open('w',encoding='utf-8',newline='') as f:
        csv.writer(f,lineterminator='\n').writerow(properties.keys())
    with (directory/'dictionary.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['field','type','unit','meaning','quality_rule'],lineterminator='\n')
        w.writeheader();w.writerows(annex['data_dictionary'])

def record(project, annex, previous=None, following=None, connections=None, all_projects=None):
    p=project;a=annex;m=p['model'];pid=p['id'];session=p['session']
    doc=project_document(p); directory=project_directory(p)
    nav=[link(doc,ROOT/'research'/session/'README.md',f'Session {session}'),
         link(doc,ROOT/'ENGINEERING_DOCUMENTATION.md','All projects'),
         link(doc,ROOT/'handbooks'/f'SESSION_{session}.md',f'Session handbook')]
    if previous:nav.append(link(doc,project_document(previous),f'← {previous["id"]}'))
    if following:nav.append(link(doc,project_document(following),f'{following["id"]} →'))
    s=f'# {pid} · {p["name"]}\n\n**Original project:** {p["original_title"]}\n\n'
    s+=f'**Session {session}:** {SESSIONS[session]}\n\n'
    s+='**Document class:** engineering research design and analysis record · **Revision:** 4 · **Date:** 2026-10-02\n\n'
    s+='**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.\n\n'
    s+=' · '.join(nav)+'\n\n'
    s+='| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |\n| ---: | ---: | ---: | ---: |\n'
    s+=f'| {len(a["requirements"])} | {len(a["verification_cases"])} | {len(a["data_dictionary"])} | {len(merged_sources(p,a))} |\n\n'
    s+=' · '.join([link(doc,directory/'data/README.md','Explore the data blueprint'),
                    link(doc,directory/'figures/README.md','Open the figure gallery'),
                    link(doc,directory/'data/acquisition.csv','Download acquisition template'),
                    link(doc,ROOT/'data/README.md','Browse the data atlas')])+'\n\n---\n\n'
    s+=profile_sections(p,a,connections or [],all_projects or {pid:p})
    s+='## Purpose and scientific objective\n\n'+p['summary']+'\n\n**Question:** '+p['question']+'\n\n**Testable hypothesis:** '+p['hypothesis']+'\n\n'
    s+='## 1. Design basis and analysis boundary\n\n'+prose(a['design_basis'])
    s+='## 2. Requirements and verification traceability\n\n'
    s+='These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.\n\n'
    s+=table(a['requirements'],['id','statement','rationale','verification','evidence'],['ID','Requirement / gate','Engineering rationale','Verification method','Basis / required evidence'])
    s+='## 3. Architecture and controlled interfaces\n\n'+prose(a['architecture'])
    s+=figure(doc,directory/'figures/architecture.svg',pid+' engineering architecture')+'\n\n'+a['figure_caption']+'\n\n'
    s+=link(doc,directory/'figures/architecture.mmd','Editable engineering diagram source')+'\n\n'
    s+='## 4. Mathematical model and derivation\n\n### Governing equations\n\n'
    for e in m['equations']:s+=equation(e)
    s+='### Variables, units and conventions\n\n'+bullets(m['variables'])
    s+='### Assumptions and boundary conditions\n\n'+bullets(m['assumptions'])
    for step in a['derivation']:
        s+=f'### Derivation step {step["step"]}\n\n'+equation(step['equation'])+step['explanation']+'\n\n'
    s+='### Inference or simulation procedure\n\n'+m['method']+'\n\n### Validity domain and fidelity limits\n\n'+m['limitations']+'\n\n'
    s+='## 5. Data specifications and provenance\n\n'
    s+=figure(doc,directory/'figures/data-map.svg',pid+' proposed data contract: field names, types, units and meanings')+'\n\n'
    s+='**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. '+link(doc,directory/'data/README.md','Open the data blueprint and downloads')+'.\n\n'
    s+=table(a['data_dictionary'],['field','type','unit','meaning','quality_rule'],['Field','Type','Unit','Physical / statistical meaning','Quality and missing-data rule'])
    s+=' · '.join([link(doc,directory/'data/schema.json','Machine-readable record schema'),
                    link(doc,directory/'data/acquisition.csv','Empty acquisition CSV'),
                    link(doc,directory/'data/dictionary.csv','Field dictionary CSV')])+'\n\n'
    s+='The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.\n\n'
    for d in p['data']:
        s+=f'### {d["source"]}\n\n[Product, archive or reference]({d["url"]})\n\n'
        for k,v in d.items():
            if k not in ['source','url']:s+=f'**{k.replace("_"," ").capitalize()}:** {v}\n\n'
    s+='## 6. Uncertainty, sensitivity and identifiability\n\n'+prose(a['uncertainty'])
    s+='## 7. Engineering trade study\n\n'+table(a['trade_study'],['option','advantage','limitation','decision_rule'],['Alternative','Benefit','Cost / limitation','Decision rule'])
    s+='## 8. Verification and validation cases\n\n'
    s+=table(a['verification_cases'],['id','case','expected','method','evidence'],['Case ID','Stimulus / condition','Expected result / criterion','Method','Evidence artifact'])
    s+='**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.\n\n'
    s+='### Additional scientific validation gates\n\n'+bullets(p['validation'])
    s+='## 9. Implementation and reproducible work packages\n\n'
    s+=''.join(f'{i+1}. {v}\n' for i,v in enumerate(a['implementation']))+'\n'
    s+='### Investigation sequence\n\n'+''.join(f'{i+1}. {v}\n' for i,v in enumerate(p['plan']))+'\n'
    s+='### Resources and interfaces to expertise\n\n'+bullets(p['resources'])
    s+='## 10. Failure modes and interpretation controls\n\n'
    s+=table(a['failure_modes'],['mode','effect','detection','mitigation'],['Failure mode','Effect on result','Detection / evidence','Design response'])
    s+=bullets(p['risks'])
    s+='## 11. Required engineering outputs\n\n'+bullets(p['deliverables'])
    s+='### Scientific result figures to produce during execution\n\n'+str(p['visual'].get('description',p['visual']))+'\n\n'
    if pid in DEMOS:
        s+='### Included shared numerical starting point\n\n'
        s+=figure(doc,ROOT/'models/figures'/f'{DEMOS[pid]}.svg',pid+' shared reduced-model or catalog demonstration')+'\n\n'
        s+=link(doc,ROOT/'models/README.md','Executable formulation, parameters, tabular outputs, provenance and verification')+'. This shared demonstration has a narrower domain than the project model above. Its own caption and methods identify synthetic parameters or the separately retrieved public catalog; it is not a completed result of the original project.\n\n'
    if pid in DATA_FIGURES:
        s+='### Data diagnostic\n\n'+figure(doc,ROOT/'data/figures'/f'{DATA_FIGURES[pid]}.svg',pid+' data diagnostic')+'\n\n'+plot_caption(pid)+'\n\n'
        s+=link(doc,ROOT/'data/figures/README.md','Inputs, downloadable figure and provenance')+'\n\n'
    if p.get('subprojects'):
        s+='### Both retained research work packages\n\n```json\n'+json.dumps(p['subprojects'],ensure_ascii=False,indent=2)+'\n```\n\n'
    s+='## 12. Cited technical and scientific resources\n\n'
    for src in merged_sources(p,a):s+=f'- [{src["title"]}]({src["url"]}) — {src.get("support","Technical model or data context.")}\n'
    s+='\nFramework and evidence rules: '+', '.join(link(doc,ROOT/'engineering'/f,label) for f,label in [('ENGINEERING_STANDARD.md','engineering documentation standard'),('MODEL_ASSURANCE.md','model assurance'),('UNCERTAINTY_AND_DECISION_RULES.md','uncertainty procedure'),('DATA_MANAGEMENT.md','data management')])+'. NASA-inspired names are creative identifiers; requirements and results are not NASA certification.\n'
    return s

def companions(p,a):
    """Browsable project-local data and figure collections; no duplicate raw data."""
    directory=project_directory(p);pid=p['id']
    doc=directory/'data/README.md'
    s=f'# {pid} · Data blueprint\n\n'+link(doc,project_document(p),p['name'])+' · '+link(doc,directory/'figures/README.md','Figure gallery')+' · '+link(doc,ROOT/'data/README.md','Data atlas')+'\n\n'
    s+=figure(doc,directory/'figures/data-map.svg',pid+' proposed field inventory')+'\n\n'
    s+=f'**PROPOSED CONTRACT · {len(a["data_dictionary"])} fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.\n\n'
    s+='| Download | What it contains |\n| --- | --- |\n'
    s+='| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |\n| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |\n| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |\n\n'
    s+='## Field reference\n\n'+table(a['data_dictionary'],['field','type','unit','meaning','quality_rule'],['Field','Type','Unit','Meaning','Quality / missingness'])
    s+='## Acquisition and provenance\n\nNull means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.\n\n'
    for d in p['data']:
        s+='- '+f'[{d["source"]}]({d["url"]})'+' — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.\n'
    s+='\n'+link(doc,ROOT/'engineering/DATA_MANAGEMENT.md','Controlled data-management procedure')+'\n\n'
    if pid in DEMOS or pid in DATA_FIGURES:
        s+='## Included evidence to explore\n\n'
        if pid in DATA_FIGURES:
            s+=figure(doc,ROOT/'data/figures'/f'{DATA_FIGURES[pid]}.svg',pid+' included data diagnostic')+'\n\n'+plot_caption(pid)+'\n\n'
        s+=link(doc,ROOT/'data/README.md','Data atlas: tables, model definitions and provenance')+'. Shared reduced-model evidence has a narrower domain than this project contract.\n'
    write(doc,s)
    doc=directory/'figures/README.md'
    s=f'# {pid} · Figure gallery\n\n'+link(doc,project_document(p),p['name'])+' · '+link(doc,directory/'data/README.md','Data blueprint')+' · '+link(doc,ROOT/'data/figures/README.md','Data diagnostic gallery')+'\n\n'
    s+='## Engineering architecture\n\n![Engineering architecture](architecture.svg)\n\n'+a['figure_caption']+'\n\n[SVG](architecture.svg) · [Editable Mermaid source](architecture.mmd)\n\n'
    s+='## Data blueprint\n\n![Proposed data contract](data-map.svg)\n\n**Proposed contract · observations pending.** Every field, type, unit and meaning comes from the controlled dictionary. [Open SVG](data-map.svg) · '+link(doc,directory/'data/dictionary.csv','Download dictionary')+'\n\n'
    s+='## Mission profile\n\n![Engineering mission profile](mission-profile.svg)\n\nThe scientific question, hypothesis, model boundary and document metadata are drawn from controlled sources. Proposed work remains distinguished from acquired evidence. [Open SVG](mission-profile.svg)\n\n'
    if pid in DATA_FIGURES:
        stem=DATA_FIGURES[pid]
        s+='## Data diagnostic\n\n'+figure(doc,ROOT/'data/figures'/f'{stem}.svg',pid+' data diagnostic')+'\n\n'+plot_caption(pid)+'\n\n'
        s+=' · '.join(link(doc,ROOT/'data/figures'/f'{stem}.{ext}',label) for ext,label in [('svg','SVG'),('png','PNG'),('provenance.json','Figure provenance')])+'\n\n'
    if pid in DEMOS:
        s+='## Original numerical view\n\n'+figure(doc,ROOT/'models/figures'/f'{DEMOS[pid]}.svg',pid+' included numerical demonstration')+'\n\n'
        s+=link(doc,ROOT/'models/README.md','Model formulation, data, assumptions and executed numerical checks')+'\n\n'
    s+='## Planned scientific result\n\n'+str(p['visual'].get('description',p['visual']))+'\n\nThis final scientific result remains an execution deliverable; the design diagrams do not establish an empirical finding.\n'
    write(doc,s)

def build():
    projects=json.loads((ROOT/'registry/projects.json').read_text(encoding='utf-8'))
    annexes=json.loads((ROOT/'registry/engineering_annexes.json').read_text(encoding='utf-8'))
    originals=json.loads((ROOT/'registry/original_titles.json').read_text(encoding='utf-8'))
    expected=[f'{s}{i+1:02}' for s,titles in originals.items() for i in range(len(titles))]
    assert [p['id'] for p in projects]==expected
    assert [a['id'] for a in annexes]==expected
    assert len(projects)==117
    for p in projects:assert p['original_title']==originals[p['session']][int(p['id'][1:])-1],p['id']
    dump(ROOT/'registry/project_paths.json',[{'id':p['id'],'name':p['name'],'session':p['session'],
         'directory':relative(ROOT/'README.md',project_directory(p)),
         'document':relative(ROOT/'README.md',project_document(p))} for p in projects])
    from build_visual_design import generate
    generate(ROOT,ROOT/'assets',co_locate=True)
    from build_mission_profiles import generate as generate_profiles
    from build_data_inventory import generate as generate_inventory
    generate_inventory(ROOT)
    connections=mission_connections(projects,annexes)
    all_projects={p['id']:p for p in projects}
    lookup={a['id']:a for a in annexes}
    mission_control(projects,lookup)
    requirements=[];tests=[];sources={};counts={};words=0
    for i,p in enumerate(projects):
        a=lookup[p['id']]
        s=record(p,a,projects[i-1] if i else None,projects[i+1] if i+1<len(projects) else None,
                 connections[p['id']],all_projects)
        write(project_document(p),s)
        # Portrait flow preserves the graph while keeping document labels legible.
        diagram=re.sub(r'^(flowchart|graph) LR\b',r'\1 TB',a['mermaid'],count=1,flags=re.M)
        write(project_directory(p)/'figures/architecture.mmd',diagram)
        contracts(p,a)
        companions(p,a)
        words+=len(s.split())
        requirements.extend({'project_id':p['id'],**r,'execution_status':'specified; evidence pending'} for r in a['requirements'])
        tests.extend({'project_id':p['id'],**r,'execution_status':'specified; not executed here'} for r in a['verification_cases'])
        for src in merged_sources(p,a):
            sources.setdefault(src['url'],{'title':src['title'],'url':src['url'],'projects':[]})['projects'].append(p['id'])
    index='# ATLAS engineering document register\n\nAll **117 original projects**, in the supplied **A–I order**. Each entry opens its complete engineering design and analysis record. D03 retains two separate research work packages.\n\n'
    index+='The nine session handbooks combine the same records for continuous reading. The project files provide requirement tables, derivations, data contracts, uncertainty, trades, verification cases, failure analysis, implementation artifacts and cited sources.\n\n'
    for session,title in SESSIONS.items():
        selected=[p for p in projects if p['session']==session]
        counts[session]=len(selected)
        index+=f'## Session {session}: {title}\n\n[![Session {session}](assets/sessions/{session}.svg)](research/{session}/README.md)\n\n[Browse Session {session}](research/{session}/README.md) · [Read the complete engineering handbook](handbooks/SESSION_{session}.md)\n\n'
        intro=f'# SESSION {session}: {title.upper()}\n\n## ATLAS engineering handbook · Revision 4\n\n![Session {session}](../assets/sessions/{session}.svg)\n\n{len(selected)} original projects, preserved in their supplied order. Each numbered record opens with a detailed mission profile before its complete design basis, model, data contract and verification plan.\n\n[All engineering documents](../ENGINEERING_DOCUMENTATION.md) · [Session gallery](../research/{session}/README.md) · [Documentation standard](../engineering/ENGINEERING_STANDARD.md)\n\n'
        contents='## Ordered contents\n\n'
        session_doc=ROOT/'research'/session/'README.md'
        session_index=f'# Session {session} · {title}\n\n![Session {session}](../../assets/sessions/{session}.svg)\n\n[Continuous handbook](../../handbooks/SESSION_{session}.md) · [All sessions](../README.md) · [Data atlas](../../data/README.md)\n\n'
        field_count=sum(len(lookup[p['id']]['data_dictionary']) for p in selected)
        requirement_count=sum(len(lookup[p['id']]['requirements']) for p in selected)
        case_count=sum(len(lookup[p['id']]['verification_cases']) for p in selected)
        session_index+=f'**{len(selected)} projects · {field_count} defined fields · {requirement_count} proposed requirements · {case_count} specified cases.** All projects retain their supplied order. Data maps describe proposed acquisition, while included numerical plots carry their own evidence labels.\n\n'
        session_index+='| ID | Mission profile & engineering record | Original investigation | Explore |\n| --- | --- | --- | --- |\n'
        book=[]
        for p in selected:
            index+=f'{int(p["id"][1:])}. '+link(ROOT/'ENGINEERING_DOCUMENTATION.md',project_document(p),p['id']+' · '+p['name'])+' — '+p['original_title']+'\n'
            session_index+='| '+p['id']+' | '+link(session_doc,project_document(p),p['name'])+' | '+cell(p['original_title'])+' | '+link(session_doc,project_directory(p)/'figures/mission-profile.svg','Profile')+' · '+link(session_doc,project_directory(p)/'data/README.md','Data')+' · '+link(session_doc,project_directory(p)/'figures/README.md','Figures')+' |\n'
            contents+=f'{int(p["id"][1:])}. [{p["id"]} · {p["name"]}](#{p["id"].lower()}) — {p["original_title"]}\n'
            body=project_document(p).read_text(encoding='utf-8')
            body=re.sub(r'^(#{1,6}) ',r'#\1 ',body,flags=re.M)
            body=rebase_markdown(body,project_document(p),ROOT/'handbooks'/f'SESSION_{session}.md',local_anchors_to_source=True)
            book.append(f'<a id="{p["id"].lower()}"></a>\n\n'+body+'\n---\n\n')
        session_index+='\n## Visual field guide\n\n'
        for p in selected:
            if p['id'] in DATA_FIGURES:
                session_index+='### '+p['id']+' · '+p['name']+'\n\n'+figure(session_doc,ROOT/'data/figures'/f'{DATA_FIGURES[p["id"]]}.svg',p['name']+' data diagnostic')+'\n\n'+plot_caption(p['id'])+'\n\n'
        if not any(p['id'] in DATA_FIGURES for p in selected):
            p=selected[0]
            session_index+=figure(session_doc,project_directory(p)/'figures/data-map.svg',p['id']+' proposed data map')+'\n\nA visual specification for '+link(session_doc,project_document(p),p['id']+' · '+p['name'])+'. Project-specific observations remain pending. Every project above has its own data map and engineering architecture.\n'
        session_index+='\n## Mission profile spotlight\n\n'+figure(session_doc,project_directory(selected[0])/'figures/mission-profile.svg',selected[0]['name']+' engineering profile')+'\n\n'+link(session_doc,project_document(selected[0]),'Enter '+selected[0]['id']+' engineering dossier')+' · '+link(session_doc,ROOT/'MISSION_CONTROL.md','Mission control: every profile and reading path')+'\n'
        write(session_doc,session_index)
        write(ROOT/'handbooks'/f'SESSION_{session}.md',intro+contents+'\n---\n\n'+''.join(book))
        index+='\n'
    write(ROOT/'ENGINEERING_DOCUMENTATION.md',index)
    write(ROOT/'registry/PROJECTS.md',rebase_markdown(index,ROOT/'ENGINEERING_DOCUMENTATION.md',ROOT/'registry/PROJECTS.md'))
    for filename,rows,fields in [
        ('requirements.csv',requirements,['project_id','id','statement','rationale','verification','evidence','execution_status']),
        ('verification_cases.csv',tests,['project_id','id','case','expected','method','evidence','execution_status'])]:
        with (ROOT/'registry'/filename).open('w',encoding='utf-8',newline='') as f:
            w=csv.DictWriter(f,fieldnames=fields,lineterminator='\n');w.writeheader();w.writerows(rows)
    dump(ROOT/'registry/sources.json',list(sources.values()))
    with (ROOT/'registry/source_index.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.writer(f,lineterminator='\n');w.writerow(['title','url','project_ids'])
        for src in sources.values():w.writerow([src['title'],src['url'],' '.join(src['projects'])])
    audit={'revision':4,'date':'2026-10-02','listed_entries':117,'sessions':counts,
           'original_titles_exact':True,'original_order_exact':True,'unique_names':len({p['name'].casefold() for p in projects})==117,
           'engineering_records':117,'session_handbooks':9,'requirements':len(requirements),'specified_verification_cases':len(tests),
           'record_schema_count':117,'empty_csv_templates':117,'dictionary_csv_count':117,
           'unique_source_urls':len(sources),'engineering_record_words':words,
           'data_field_maps':117,'local_data_galleries':117,'local_figure_galleries':117,
           'session_cards':9,'additional_data_diagnostics':9,
           'mission_profiles':117,'mission_connection_register_entries':117,
           'content_sha256':hashlib.sha256((ROOT/'registry/projects.json').read_bytes()).hexdigest(),
           'annex_sha256':hashlib.sha256((ROOT/'registry/engineering_annexes.json').read_bytes()).hexdigest(),
           'content_hash_basis':'UTF-8 canonical LF repository bytes',
           'evidence_state':'Engineering design documentation; specified tests are not completed empirical tests.',
           'website_removed':not (ROOT/'web').exists()}
    dump(ROOT/'evidence/coverage_audit.json',audit)
    # Profile provenance covers the final registers, including connections.
    generate_profiles(ROOT)
    print(json.dumps(audit,indent=2))

if __name__=='__main__': build()
