"""Build engineering records and A-I handbooks from reviewed structured sources.

Run from any directory: python tools/build_engineering_documentation.py
Source records live in catalog/projects.json and catalog/engineering_annexes.json.
This produces documentation and empty data contracts, never project measurements.
Architecture SVG rendering is a separate, optional build step.
"""
import csv
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SESSIONS = json.loads((ROOT/'catalog/sessions.json').read_text(encoding='utf-8'))
DEMOS = {
    'A01':'01_fractal_escape_distance', 'A02':'02_ideal_binary_liquidus',
    'E06':'03_balloon_thermal', 'E03':'03_balloon_thermal', 'I05':'03_balloon_thermal',
    'D04':'04_sphere_drag', 'B14':'05_hydrologic_reservoir', 'B23':'05_hydrologic_reservoir',
    'I10':'06_one_axis_attitude', 'I08':'07_two_body_convergence', 'I12':'07_two_body_convergence',
    'C08':'08_spectral_identifiability', 'H09':'08_spectral_identifiability',
    'C05':'09_real_exoplanet_sample', 'C23':'09_real_exoplanet_sample',
}

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
    dump(ROOT/'data/contracts'/f'{pid}.schema.json',schema)
    # A header-only CSV is an empty acquisition template, not a synthetic result.
    path=ROOT/'data/contracts'/f'{pid}.csv'
    with path.open('w',encoding='utf-8',newline='') as f:
        csv.writer(f,lineterminator='\n').writerow(properties.keys())
    with (ROOT/'data/contracts'/f'{pid}.dictionary.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['field','type','unit','meaning','quality_rule'],lineterminator='\n')
        w.writeheader();w.writerows(annex['data_dictionary'])

def record(project, annex, previous=None, following=None):
    p=project;a=annex;m=p['model'];pid=p['id'];session=p['session']
    nav=['[Engineering document register](../../ENGINEERING_DOCUMENTATION.md)',f'[Session {session} handbook](../../documentation/SESSION_{session}.md)']
    if previous:nav.append(f'[Previous: {previous["id"]}](../{previous["session"]}/{previous["id"]}.md)')
    if following:nav.append(f'[Next: {following["id"]}](../{following["session"]}/{following["id"]}.md)')
    s=f'# {pid} · {p["name"]}\n\n**Original project:** {p["original_title"]}\n\n'
    s+=f'**Session {session}:** {SESSIONS[session]}\n\n'
    s+='**Document class:** engineering research design and analysis record · **Revision:** 2 · **Date:** 2026-10-02\n\n'
    s+='**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.\n\n'
    s+=' · '.join(nav)+'\n\n'
    s+='## Purpose and scientific objective\n\n'+p['summary']+'\n\n**Question:** '+p['question']+'\n\n**Testable hypothesis:** '+p['hypothesis']+'\n\n'
    s+='## 1. Design basis and analysis boundary\n\n'+prose(a['design_basis'])
    s+='## 2. Requirements and verification traceability\n\n'
    s+='These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.\n\n'
    s+=table(a['requirements'],['id','statement','rationale','verification','evidence'],['ID','Requirement / gate','Engineering rationale','Verification method','Basis / required evidence'])
    s+='## 3. Architecture and controlled interfaces\n\n'+prose(a['architecture'])
    s+=f'![{pid} engineering architecture](../../visuals/projects/{pid}.svg)\n\n'+a['figure_caption']+'\n\n'
    s+=f'[Editable engineering diagram source](../../visuals/projects/{pid}.mmd)\n\n'
    s+='## 4. Mathematical model and derivation\n\n### Governing equations\n\n'
    for e in m['equations']:s+=equation(e)
    s+='### Variables, units and conventions\n\n'+bullets(m['variables'])
    s+='### Assumptions and boundary conditions\n\n'+bullets(m['assumptions'])
    for step in a['derivation']:
        s+=f'### Derivation step {step["step"]}\n\n'+equation(step['equation'])+step['explanation']+'\n\n'
    s+='### Inference or simulation procedure\n\n'+m['method']+'\n\n### Validity domain and fidelity limits\n\n'+m['limitations']+'\n\n'
    s+='## 5. Data specifications and provenance\n\n'
    s+=table(a['data_dictionary'],['field','type','unit','meaning','quality_rule'],['Field','Type','Unit','Physical / statistical meaning','Quality and missing-data rule'])
    s+=f'[Machine-readable record schema](../../data/contracts/{pid}.schema.json) · [Empty acquisition CSV](../../data/contracts/{pid}.csv) · [Field dictionary CSV](../../data/contracts/{pid}.dictionary.csv)\n\n'
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
        s+=f'![{pid} shared reduced-model or catalog demonstration](../../models/figures/{DEMOS[pid]}.svg)\n\n'
        s+='[Executable formulation, parameters, tabular outputs, provenance and verification](../../models/README.md). This shared demonstration has a narrower domain than the project model above. Its own caption and methods identify synthetic parameters or the separately retrieved public catalog; it is not a completed result of the original project.\n\n'
    if p.get('subprojects'):
        s+='### Both retained research work packages\n\n```json\n'+json.dumps(p['subprojects'],ensure_ascii=False,indent=2)+'\n```\n\n'
    s+='## 12. Cited technical and scientific resources\n\n'
    for src in merged_sources(p,a):s+=f'- [{src["title"]}]({src["url"]}) — {src.get("support","Technical model or data context.")}\n'
    s+='\nFramework and evidence rules: [engineering documentation standard](../../docs/ENGINEERING_STANDARD.md), [model assurance](../../docs/MODEL_ASSURANCE.md), [uncertainty procedure](../../docs/UNCERTAINTY_AND_DECISION_RULES.md), and [data management](../../docs/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.\n'
    return s

def build():
    projects=json.loads((ROOT/'catalog/projects.json').read_text(encoding='utf-8'))
    annexes=json.loads((ROOT/'catalog/engineering_annexes.json').read_text(encoding='utf-8'))
    originals=json.loads((ROOT/'catalog/original_titles.json').read_text(encoding='utf-8'))
    expected=[f'{s}{i+1:02}' for s,titles in originals.items() for i in range(len(titles))]
    assert [p['id'] for p in projects]==expected
    assert [a['id'] for a in annexes]==expected
    assert len(projects)==117
    for p in projects:assert p['original_title']==originals[p['session']][int(p['id'][1:])-1],p['id']
    lookup={a['id']:a for a in annexes}
    requirements=[];tests=[];sources={};counts={};words=0
    for i,p in enumerate(projects):
        a=lookup[p['id']]
        s=record(p,a,projects[i-1] if i else None,projects[i+1] if i+1<len(projects) else None)
        write(ROOT/'projects'/p['session']/(p['id']+'.md'),s)
        # Portrait flow preserves the graph while keeping document labels legible.
        diagram=re.sub(r'^(flowchart|graph) LR\b',r'\1 TB',a['mermaid'],count=1,flags=re.M)
        write(ROOT/'visuals/projects'/(p['id']+'.mmd'),diagram)
        contracts(p,a)
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
        index+=f'## Session {session}: {title}\n\n[Read the complete Session {session} engineering handbook](documentation/SESSION_{session}.md)\n\n'
        intro=f'# SESSION {session}: {title.upper()}\n\n## ATLAS engineering handbook · Revision 2\n\n{len(selected)} original projects, preserved in their supplied order. Each numbered record has an independently stated design basis, model, data contract and verification plan.\n\n[All engineering documents](../ENGINEERING_DOCUMENTATION.md) · [Documentation standard](../docs/ENGINEERING_STANDARD.md)\n\n'
        contents='## Ordered contents\n\n'
        session_index=f'# SESSION {session}: {title.upper()}\n\n[Complete session handbook](../../documentation/SESSION_{session}.md) · [All sessions](../../ENGINEERING_DOCUMENTATION.md)\n\n'
        book=[]
        for p in selected:
            index+=f'{int(p["id"][1:])}. [{p["id"]} · {p["name"]}](projects/{session}/{p["id"]}.md) — {p["original_title"]}\n'
            session_index+=f'{int(p["id"][1:])}. [{p["id"]} · {p["name"]}]({p["id"]}.md) — {p["original_title"]}\n'
            contents+=f'{int(p["id"][1:])}. [{p["id"]} · {p["name"]}](#{p["id"].lower()}) — {p["original_title"]}\n'
            body=(ROOT/'projects'/session/(p['id']+'.md')).read_text(encoding='utf-8')
            body=re.sub(r'^(#{1,6}) ',r'#\1 ',body,flags=re.M)
            # Rebase relative paths to the handbook directory.
            body=body.replace('(../../','(../')
            body=re.sub(r'\]\(\.\./([A-I])/([A-I]\d{2})\.md\)',r'](../projects/\1/\2.md)',body)
            book.append(f'<a id="{p["id"].lower()}"></a>\n\n'+body+'\n---\n\n')
        write(ROOT/'projects'/session/'README.md',session_index)
        write(ROOT/'documentation'/f'SESSION_{session}.md',intro+contents+'\n---\n\n'+''.join(book))
        index+='\n'
    write(ROOT/'ENGINEERING_DOCUMENTATION.md',index)
    write(ROOT/'catalog/PROJECTS.md',index.replace('(documentation/','(../documentation/').replace('(projects/','(../projects/'))
    for filename,rows,fields in [
        ('requirements.csv',requirements,['project_id','id','statement','rationale','verification','evidence','execution_status']),
        ('verification_cases.csv',tests,['project_id','id','case','expected','method','evidence','execution_status'])]:
        with (ROOT/'catalog'/filename).open('w',encoding='utf-8',newline='') as f:
            w=csv.DictWriter(f,fieldnames=fields,lineterminator='\n');w.writeheader();w.writerows(rows)
    dump(ROOT/'catalog/sources.json',list(sources.values()))
    with (ROOT/'catalog/source_index.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.writer(f,lineterminator='\n');w.writerow(['title','url','project_ids'])
        for src in sources.values():w.writerow([src['title'],src['url'],' '.join(src['projects'])])
    audit={'revision':2,'date':'2026-10-02','listed_entries':117,'sessions':counts,
           'original_titles_exact':True,'original_order_exact':True,'unique_names':len({p['name'].casefold() for p in projects})==117,
           'engineering_records':117,'session_handbooks':9,'requirements':len(requirements),'specified_verification_cases':len(tests),
           'record_schema_count':117,'empty_csv_templates':117,'dictionary_csv_count':117,
           'unique_source_urls':len(sources),'engineering_record_words':words,
           'content_sha256':hashlib.sha256((ROOT/'catalog/projects.json').read_bytes()).hexdigest(),
           'annex_sha256':hashlib.sha256((ROOT/'catalog/engineering_annexes.json').read_bytes()).hexdigest(),
           'content_hash_basis':'UTF-8 canonical LF repository bytes',
           'evidence_state':'Engineering design documentation; specified tests are not completed empirical tests.',
           'website_removed':not (ROOT/'web').exists()}
    dump(ROOT/'reviews/coverage_audit.json',audit)
    print(json.dumps(audit,indent=2))

if __name__=='__main__': build()
