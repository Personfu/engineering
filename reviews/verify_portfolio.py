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
        for file in list((ROOT/'projects').rglob('*.md'))+[ROOT/'README.md',ROOT/'catalog/PROJECTS.md']:
            for target in re.findall(r'\]\(([^)\s]+)\)',file.read_text(encoding='utf-8')):
                if '://' in target or target.startswith('#'):continue
                target=target.split('#')[0]
                if not (file.parent/target).exists():failures.append((str(file.relative_to(ROOT)),target))
        self.assertEqual(failures,[])
    def test_combined_aeronautics_concepts_retained(self):
        p=next(x for x in self.projects if x['id']=='D03')
        text=json.dumps(p).lower()
        self.assertIn('autorotat',text);self.assertIn('laminar',text)
        self.assertGreaterEqual(len(p.get('subprojects',[])),2)
    def test_offline_explorer_catalog(self):
        html=(ROOT/'web/atlas.html').read_text(encoding='utf-8')
        raw=re.search(r'<script id="catalog" type="application/json">(.*?)</script>',html,re.S).group(1)
        self.assertEqual(len(json.loads(raw)),117)
        for src in re.findall(r'<script[^>]* src="([^"]+)"',html):
            self.assertNotIn('://',src)
            self.assertTrue((ROOT/'web'/src).exists())
        self.assertTrue((ROOT/'web/vendor/katex/LICENSE').exists())
        self.assertIn('aria-live="polite"',html)
if __name__=='__main__':unittest.main(verbosity=2)
