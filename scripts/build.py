"""Rebuild the checked-in atlas, dossiers, original SVGs, and synthetic samples."""
from __future__ import annotations
import csv
import hashlib
import html
import json
import sys
import textwrap
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from models.reference import DEMOS

SESSIONS={
 'A':'Math, Physics & Chemistry','B':'Earth & Environmental Engineering',
 'C':'Astronomy & Space Physics','D':'Aeronautics','E':'ASCEND',
 'F':'Education & Public Outreach','G':'Exploration Systems Engineering',
 'H':'Planetary Science','I':'Aerospace Technology'}
COUNTS={'A':12,'B':28,'C':30,'D':8,'E':8,'F':2,'G':8,'H':9,'I':13}
# Deliberate project-level mapping. A demo is not silently attached to every
# project that happens to share a broad domain.
LINKS={'A01':'fractal','A02':'phase','A04':'swarm','A05':'mechanics','A10':'spectrum',
 'A11':'mixture','B07':'kinetics','B14':'hydrology','B20':'adsorption','B26':'power',
 'C02':'image','C03':'spectrum','C08':'mixture','C09':'radiation','C12':'image',
 'C26':'suspension','C28':'calibration','D03':'mechanics','D05':'drag',
 'E03':'radiation','E06':'thermal','E08':'power','G01':'mechanics','G02':'adaptive',
 'G03':'antenna','G06':'adsorption','G07':'mechanics','H02':'calibration',
 'H09':'mixture','I01':'thermal','I02':'thermal','I03':'thermal','I05':'power',
 'I06':'mechanics','I08':'orbit','I09':'mechanics','I10':'attitude','I11':'image'}
# Mathematically relevant demonstrations are linked with explicit exclusions.
RELATED=[['A10','C01','C24'],['B01','B09'],['B02','B05','B25'],['B03','B24'],
 ['B14','B23'],['C02','C12','I11'],['C07','C11','C16','C25','C26'],
 ['C05','C23'],['C08','H09'],['C03','H07'],['C04','C13','C20','C30'],
 ['E01','E02','E03','E04','E06','E07','I05'],['E05','E08','I04','I07','I10'],
 ['I01','I02','I03'],['I08','I12','I13'],['F01','F02','H01','H05']]
PAGES={'A':9,'B':11,'C':14,'D':17,'E':19,'F':22,'G':23,'H':24,'I':25}


def write(path, content):
    p=ROOT/path; p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(content,encoding='utf-8')


def source_locator(session,n):
    if session=='A': return f'A-{n+1}'
    if session=='E': return 'E-1-2' if n==1 else f'E-{n+1}'
    if session=='D' and n==8: return 'D-8-9'
    if session=='G' and n==8: return 'G-In Title Only'
    return f'{session}-{n}'


def workflow(p):
    name=html.escape(p['name']); question=html.escape(p['question'])
    words=textwrap.wrap(p['question'],width=72)
    q=''.join(f'<tspan x="28" dy="22">{html.escape(w)}</tspan>' for w in words)
    labels=[('OBSERVATION CONTRACT',p['data']),('MODEL & ASSUMPTIONS',p['model']),
            ('INDEPENDENT CHECK',p['validation']),('PROPOSED OUTPUT',p['visual'])]
    boxes=[]
    for i,(title,content) in enumerate(labels):
        x=28+(i%2)*460; y=155+(i//2)*170
        lines=textwrap.wrap(content,width=54)[:5]
        detail=''.join(f'<tspan x="{x+18}" dy="19">{html.escape(w)}</tspan>' for w in lines)
        boxes.append(f'<rect x="{x}" y="{y}" width="430" height="148" rx="8" fill="#101c30" stroke="#264864"/><text x="{x+18}" y="{y+27}" fill="#66d6ee" font-size="12">{html.escape(title)}</text><text x="{x+18}" y="{y+40}" fill="#cfdae6" font-size="12">{detail}</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="545" viewBox="0 0 960 545" role="img" aria-labelledby="t d">
<title id="t">{name} research architecture</title><desc id="d">Conceptual research workflow. No observations or results are depicted. Full details appear in the associated dossier.</desc>
<rect width="960" height="545" fill="#070e1b"/><g font-family="sans-serif"><text x="28" y="35" fill="#91a1b8" font-size="12">ASTRA FORGE / {p['id']} / PROPOSED RESEARCH ARCHITECTURE</text><text x="28" y="69" fill="#edf5ff" font-size="23">{name}</text><text x="28" y="83" fill="#b8c8d9" font-size="14">{q}</text>{''.join(boxes)}<text x="28" y="521" fill="#91a1b8" font-size="12">CONCEPTUAL / NOT TO SCALE / NO MEASURED RESULTS / ORIGINAL FLLC SCHEMATIC</text></g></svg>'''


def plot(name, payload):
    rows=payload['rows']; columns=payload['columns']
    if name in ('fractal','image'):
        index=2 if name=='fractal' else 4
        vals=[r[index] for r in rows]; low=min(vals); high=max(vals)
        nx=64 if name=='fractal' else 32; ny=48 if name=='fractal' else 32
        shapes=[]
        for i,r in enumerate(rows):
            t=(r[index]-low)/(high-low or 1)
            color=f'rgb({int(25+100*t)},{int(40+180*t)},{int(70+150*t)})'
            shapes.append(f'<rect x="{70+(i%nx)*680/nx:.2f}" y="{65+(i//nx)*330/ny:.2f}" width="{680/nx+0.1:.2f}" height="{330/ny+0.1:.2f}" fill="{color}"/>')
        body=''.join(shapes)
        label='complex-plane sample tiles; zero = unresolved' if name=='fractal' else 'synthetic detector pixels; colors encode arbitrary counts'
    else:
        ix=1 if name=='orbit' else 0; iy=2 if name=='orbit' else (3 if name=='radiation' else (3 if name=='attitude' else 1))
        xs=[r[ix] for r in rows]; ys=[r[iy] for r in rows]
        if name in ('drag','hydrology','suspension'): xs=[__import__('math').log10(x) for x in xs]
        lo=min(xs); hi=max(xs); yl=min(ys); yh=max(ys)
        if name=='orbit':
            scale=max((hi-lo)/680,(yh-yl)/330)*1.05
            xm=(lo+hi)/2;ym=(yl+yh)/2
            lo=xm-scale*680/2;hi=xm+scale*680/2
            yl=ym-scale*330/2;yh=ym+scale*330/2
        points=' '.join(f'{70+680*(x-lo)/(hi-lo or 1):.2f},{395-330*(y-yl)/(yh-yl or 1):.2f}' for x,y in zip(xs,ys))
        body=f'<path d="M70 65 V395 H750" stroke="#697e98" fill="none"/><polyline points="{points}" stroke="#69deed" stroke-width="2" fill="none"/>'
        label=f'{columns[ix]} ({lo:.3g} to {hi:.3g}) vs {columns[iy]} ({yl:.3g} to {yh:.3g})'
        if name in ('drag','hydrology','suspension'): label='log10 x-axis / '+label
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 470" role="img" aria-labelledby="t d"><title id="t">{html.escape(name)} educational reference</title><desc id="d">{html.escape(payload["limitations"])}</desc><rect width="820" height="470" fill="#07101e"/><g font-family="sans-serif"><text x="30" y="30" fill="#e3edff" font-size="17">{name.upper()} / SYNTHETIC EDUCATIONAL REFERENCE</text>{body}<text x="30" y="432" fill="#a9bed8" font-size="11">{html.escape(label)}</text><text x="30" y="455" fill="#8ba1ba" font-size="11">Original mathematical visualization; not mission observations or validated research output.</text></g></svg>'


def main():
    with (ROOT/'catalog/projects.tsv').open() as handle:
        rows=list(csv.DictReader(handle,delimiter='\t'))
    with (ROOT/'catalog/sources.tsv').open() as handle:
        sources=list(csv.DictReader(handle,delimiter='\t'))
    assert dict(Counter(p['session'] for p in rows))==COUNTS
    assert len({p['title'] for p in rows})==len(rows)==118
    source_ids={s['id'] for s in sources}; lookup={s['id']:s for s in sources}
    seen=Counter(); manifest=[]
    for model,fn in DEMOS.items():
        data=fn(); write(f'data/synthetic/{model}.json',json.dumps(data,separators=(',',':'))+'\n')
        write(f'visuals/reference/{model}.svg',plot(model,data))
        raw=(ROOT/f'data/synthetic/{model}.json').read_bytes()
        manifest.append({'id':model,'evidence_class':data['evidence_class'],'path':f'data/synthetic/{model}.json','sha256':hashlib.sha256(raw).hexdigest(),'rows':len(data['rows']),'columns':data['columns'],'limitations':data['limitations']})
    write('data/synthetic/manifest.json',json.dumps(manifest,indent=2)+'\n')
    write('atlas/model-data.js','window.ASTRA_MODELS='+json.dumps({name:DEMOS[name]() for name in ['fractal','phase','orbit','thermal','spectrum','radiation','attitude']},separators=(',',':'))+';\n')
    for p in rows:
        session=p['session']; seen[session]+=1; n=seen[session]
        p['id']=f'{session}{n:02}'; p['sources']=p['sources'].split(',')
        assert set(p['sources'])<=source_ids
        p['original_locator']=source_locator(session,n)
        p['provenance_url']=lookup['ASCEND']['url']+f'#page={PAGES[session]}'
        p['model_status']='FORMAL RESEARCH SPECIFICATION / NOT VALIDATED'
        p['data_status']='NO MEASUREMENTS INGESTED'
        p['demo']=LINKS.get(p['id'])
        p['related']=sorted({q for group in RELATED if p['id'] in group for q in group if q!=p['id']})
        p['dossier']=f'projects/{p["id"]}.md'; p['workflow']=f'visuals/projects/{p["id"]}.svg'
        write(p['workflow'],workflow(p))
        bibliography='\n'.join(f'- [{sid}: {lookup[sid]["title"]}]({lookup[sid]["url"]}) — {lookup[sid]["role"]}; review status: **{lookup[sid]["status"]}**. {lookup[sid]["limitations"]}' for sid in ['ASCEND']+p['sources'] if sid in lookup)
        if p['demo']:
            demo=p['demo']; limitation=DEMOS[demo]()['limitations']
            runnable=f'''A narrow **{demo}** reference is runnable; it is not the full research model above.

```bash
python -m models.run --model {demo} --output /tmp/astra-{p['id']}.json
```

{limitation}

![Synthetic reference, not measurements](../visuals/reference/{demo}.svg)

[Synthetic example data](../data/synthetic/{demo}.json) · [Code](../models/reference.py). The full scientific solver and measured-data validation remain pending.'''
        else:
            runnable='''This project has a formal research/evidence model specification and original workflow visual. Its project-specific scientific solver is **not implemented**. Do not replace it with an unrelated reference kernel or claim numerical results. Implement only after equation-level bibliography and inputs pass the model review gate.'''
        related=', '.join(f'[{q}]({q}.md)' for q in p['related']) or 'No dependency is required; retain this project independently.'
        doc=f'''# {p['id']} · {p['name']}

**Original project:** {p['title']}

**Session {session}:** {SESSIONS[session]} · **Family:** {p['family']}

**Historical locator:** [{p['original_locator']} in the 2021 Arizona NASA Space Grant program]({p['provenance_url']}). IDs in this repository follow the user's supplied list, not presentation numbering. The proposed space-inspired name does not rename or appropriate the original authors' research. See the original program for author/mentor credit. This dossier is an original FLLC research extension, not a reproduction of the abstract.

| Evidence layer | State |
|---|---|
| Research architecture | Proposed, formal specification |
| Measurements | None ingested |
| Executable reference | {'Available; educational only' if p['demo'] else 'Project-specific solver pending'} |
| Scientific validation | Pending |
| Deployment / qualification | None |

## Scientific question and value

{p['question']}

The output must let a reviewer inspect the evidence, test a competing explanation and identify the observation that would change the conclusion. A sophisticated visual is useful only when its scale, source and uncertainty are defensible.

## Model and assumptions

{p['model']}

This is the proposed governing formulation. Before research implementation, record the state/input/parameter vectors, units, boundary and initial conditions, observation operator, nuisance terms and parameter identifiability. Select specific primary equation references: archive landing pages below are discovery resources, not proof that this formulation applies. [Shared model and verification standard](../docs/engineering-standard.md).

## Data package and acquisition

{p['data']}

Use [the data contract](../docs/data-contract.md). Each input needs a publisher, primary URL, stable identifier, version, observation/retrieval dates, checksum, license/permission, unit dictionary, calibration, missing-value semantics and coverage limits. Never treat absent measurements, detection limits or unsupported source access as zero values. The registry below distinguishes reviewed resources from blocked or reference-only entries.

## Validation and falsification

{p['validation']}

Validation passes only if independent evidence supports the model in its declared domain, uncertainty is reported and simpler baselines are compared fairly. Establish project-specific tolerances from instrument performance or literature before inspecting final results; do not invent universal NASA thresholds. Report failures and negative findings.

## Original visual architecture

{p['visual']}

![Conceptual research architecture, not observed results](../{p['workflow']})

The shipped diagram is a conceptual specification. The proposed science visualization requires the qualified data above. Raw, calibrated, simulated and inferred states must remain distinguishable, with a visible source/time/uncertainty inspector.

## Executable model state

{runnable}

## Ambitious extension and connected work

{p['extension']}

Related project dossiers: {related}

Preserve independent scientific questions and original identities. Share schemas/calibration tools only where justified; never share results merely because subjects overlap.

## Concrete delivery sequence

1. Inspect the original source and collect project-specific primary literature; record unresolved interpretation and equation references.
2. Qualify the named observations and metadata; keep raw data immutable and permissions explicit.
3. Implement the stated model with an analytic or published benchmark, error handling and convergence checks.
4. Perform the project-specific validation above with independent holdouts and uncertainty decomposition.
5. Generate the proposed visual and an exportable evidence receipt; retain corrections and rejected inputs.

Completion requires a documented answer, calibrated uncertainty, an independently reproducible run and a reviewer-visible limitation statement. No claimed result currently meets that scientific completion gate.

## References and resource review

{bibliography}

Review date: **2026-10-02**. Portal inspection is not dataset use. Original mission names refer to independent educational inspiration; no NASA endorsement or operational applicability is claimed.
'''
        write(p['dossier'],doc)
    catalog={'version':1,'review_date':'2026-10-02','project_count':len(rows),'sessions':SESSIONS,'projects':rows,'sources':sources,'model_count':len(DEMOS)}
    write('catalog/projects.json',json.dumps(catalog,indent=2,ensure_ascii=False)+'\n')
    write('atlas/catalog-data.js','window.ASTRA_CATALOG='+json.dumps(catalog,separators=(',',':'),ensure_ascii=False)+';\n')
    index=['# ASTRA FORGE · complete project index','', '118 original projects preserved. Each name is a proposed FLLC research identity, not an official NASA mission.','']
    for session,title in SESSIONS.items():
        index.extend([f'## Session {session} · {title} ({COUNTS[session]})','','| ID | Proposed name | Original title | Reference |','|---|---|---|---|'])
        for p in rows:
            if p['session']==session:
                index.append(f'| [{p["id"]}](../{p["dossier"]}) | {p["name"]} | {p["title"]} | {p["demo"] or "Specification"} |')
        index.append('')
    write('docs/project-index.md','\n'.join(index)+'\n')
    source_md=['# Source registry','','Inspected means readable context was reviewed, not that a dataset was ingested. All science acquisition remains pending. General portals do not substitute for equation-level bibliography.','','| ID | Resource | Role | Review status |','|---|---|---|---|']
    source_md.extend(f'| {s["id"]} | [{s["title"]}]({s["url"]}) | {s["role"]} | {s["status"]} |' for s in sources)
    write('docs/source-registry.md','\n'.join(source_md)+'\n')
    print(f'Built {len(rows)} dossiers, {len(rows)} workflow SVGs, {len(DEMOS)} reference plots/datasets, {len(sources)} sources.')


if __name__=='__main__': main()
