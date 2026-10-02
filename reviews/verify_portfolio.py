"""Check coverage, source protocols and internal document links; not science validation."""
import json,re,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class PortfolioChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.projects=json.loads((ROOT/'catalog/projects.json').read_text(encoding='utf-8'))
        cls.original=json.loads((ROOT/'catalog/original_titles.json').read_text(encoding='utf-8'))
    def test_exact_original_coverage(self):
        want={f'{s}{i+1:02}':t for s,ts in self.original.items() for i,t in enumerate(ts)}
        self.assertEqual(len(want),117)
        self.assertEqual({p['id']:p['original_title'] for p in self.projects},want)
    def test_unique_ids_and_mission_names(self):
        self.assertEqual(len(self.projects),117)
        for key in ['id','name']:self.assertEqual(len(set(p[key].casefold() for p in self.projects)),117)
    def test_models_and_data_contracts(self):
        for p in self.projects:
            with self.subTest(id=p['id']):
                for key in ['equations','variables','assumptions','method','limitations']:self.assertTrue(p['model'][key])
                self.assertGreaterEqual(len(p['sources']),2)
                self.assertGreaterEqual(len(p['plan']),3)
                self.assertGreaterEqual(len(p['validation']),2)
                self.assertTrue(p['data'])
                for d in p['data']:
                    for key in ['source','url','fields','access','role']:self.assertTrue(d.get(key),key)
    def test_source_links_are_https(self):
        for p in self.projects:
            for s in p['sources']:self.assertTrue(s['url'].startswith('https://'),(p['id'],s['url']))
    def test_each_dossier_has_a_conceptual_figure(self):
        for p in self.projects:
            with self.subTest(id=p['id']):
                file=ROOT/'projects'/p['session']/(p['id']+'.md')
                self.assertTrue(file.exists());self.assertIn(p['original_title'],file.read_text(encoding='utf-8'))
                svg=ROOT/'visuals/projects'/(p['id']+'.svg')
                self.assertTrue(svg.exists());self.assertIn('<desc',svg.read_text(encoding='utf-8'))
    def test_internal_markdown_links(self):
        failures=[]
        for file in ROOT.rglob('*.md'):
            content=file.read_text(encoding='utf-8')
            content=re.sub(r'```.*?```|\$\$.*?\$\$', '', content, flags=re.S)
            for target in re.findall(r'\]\(([^)\s]+)\)',content):
                if '://' in target or target.startswith('#'):continue
                target=target.split('#')[0]
                if not (file.parent/target).exists():failures.append((str(file.relative_to(ROOT)),target))
        self.assertEqual(failures,[])
    def test_combined_aeronautics_concepts_retained(self):
        p=next(x for x in self.projects if x['id']=='D03')
        text=json.dumps(p).lower()
        self.assertIn('autorotat',text);self.assertIn('laminar',text)
        self.assertGreaterEqual(len(p.get('subprojects',[])),2)
    def test_documentation_order_and_no_website(self):
        self.assertFalse((ROOT/'web').exists())
        wanted=[f'{s}{i+1:02}' for s,ts in self.original.items() for i in range(len(ts))]
        self.assertEqual([p['id'] for p in self.projects],wanted)
        register=(ROOT/'ENGINEERING_DOCUMENTATION.md').read_text(encoding='utf-8')
        seen=re.findall(r'\]\(projects/[A-I]/([A-I]\d{2})\.md\)',register)
        self.assertEqual(seen,wanted)
        for session in self.original:
            book=(ROOT/'documentation'/f'SESSION_{session}.md').read_text(encoding='utf-8')
            self.assertEqual(re.findall(r'<a id="([a-i]\d{2})">',book),[x.lower() for x in wanted if x.startswith(session)])
    def test_engineering_contract_and_traceability_coverage(self):
        import csv
        annexes=json.loads((ROOT/'catalog/engineering_annexes.json').read_text(encoding='utf-8'))
        self.assertEqual([a['id'] for a in annexes],[p['id'] for p in self.projects])
        with (ROOT/'catalog/requirements.csv').open(encoding='utf-8') as f:req=list(csv.DictReader(f))
        with (ROOT/'catalog/verification_cases.csv').open(encoding='utf-8') as f:cases=list(csv.DictReader(f))
        self.assertEqual({x['project_id'] for x in req},{p['id'] for p in self.projects})
        self.assertEqual({x['project_id'] for x in cases},{p['id'] for p in self.projects})
        self.assertEqual(len({x['id'] for x in req}),len(req))
        self.assertEqual(len({x['id'] for x in cases}),len(cases))
        for a in annexes:
            with self.subTest(id=a['id']):
                self.assertGreaterEqual(len(a['requirements']),4)
                self.assertGreaterEqual(len(a['derivation']),3)
                self.assertGreaterEqual(len(a['verification_cases']),3)
                schema=json.loads((ROOT/'data/contracts'/(a['id']+'.schema.json')).read_text(encoding='utf-8'))
                with (ROOT/'data/contracts'/(a['id']+'.csv')).open(encoding='utf-8') as f:records=list(csv.reader(f))
                self.assertEqual(len(records),1,'Acquisition template must not invent data')
                self.assertEqual(records[0],list(schema['properties']))
                self.assertTrue((ROOT/'visuals/projects'/(a['id']+'.mmd')).exists())
    def test_rendered_architecture_sources_and_accessibility(self):
        import hashlib,xml.etree.ElementTree as ET
        manifest=json.loads((ROOT/'visuals/engineering_figure_manifest.json').read_text(encoding='utf-8'))
        self.assertEqual(manifest['count'],117)
        self.assertEqual([x['project_id'] for x in manifest['figures']],[p['id'] for p in self.projects])
        for row in manifest['figures']:
            with self.subTest(id=row['project_id']):
                for name in ['source','svg']:
                    path=ROOT/'visuals'/row[name]
                    self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(),row[name+'_sha256'])
                svg=ROOT/'visuals'/row['svg']
                tree=ET.fromstring(svg.read_bytes())
                self.assertEqual(tree.attrib.get('role'),'img')
                self.assertTrue(tree.find('{http://www.w3.org/2000/svg}title').text)
                self.assertTrue(tree.find('{http://www.w3.org/2000/svg}desc').text)
if __name__=='__main__':unittest.main(verbosity=2)
