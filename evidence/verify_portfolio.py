"""Check original coverage, migrated navigation and figure provenance.

These are documentation/asset checks, not project empirical validation.
"""
import csv
import hashlib
import html
import json
import re
import sys
import unittest
import xml.etree.ElementTree as ET
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from layout import project_directory, project_document

NS = '{http://www.w3.org/2000/svg}'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


class HTMLReferences(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []
        self.images = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if values.get('id'):
            self.ids.add(values['id'])
        if tag == 'a' and values.get('name'):
            self.ids.add(values['name'])
        for name in ['href', 'src']:
            if values.get(name):
                self.targets.append(values[name])
        if tag == 'img' and values.get('src'):
            self.images.append((values['src'], values.get('alt', '')))


def strip_code(content):
    return re.sub(r'```.*?```|~~~.*?~~~|\$\$.*?\$\$', '', content, flags=re.S)


def references(content):
    content = strip_code(content)
    parser = HTMLReferences()
    parser.feed(content)
    targets = parser.targets + [a or b for a, b in re.findall(r'\]\((?:<([^>]+)>|([^\s)]+))\)', content)]
    return [html.unescape(target) for target in targets], parser


def markdown_anchors(content):
    content = strip_code(content)
    _, parser = references(content)
    anchors = set(parser.ids)
    used = Counter()
    for heading in re.findall(r'^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$', content, flags=re.M):
        heading = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', heading)
        heading = html.unescape(re.sub(r'<[^>]*>', '', heading)).lower()
        slug = ''.join(c for c in heading if c.isalnum() or c in ' _-').replace(' ', '-')
        count = used[slug]
        used[slug] += 1
        anchors.add(slug + (f'-{count}' if count else ''))
    return anchors


def accessible_svg(path):
    tree = ET.fromstring(path.read_bytes())
    assert tree.tag == NS + 'svg', path
    assert tree.attrib.get('role') == 'img', path
    assert tree.find(NS + 'title') is not None and tree.find(NS + 'title').text, path
    assert tree.find(NS + 'desc') is not None and tree.find(NS + 'desc').text, path
    assert len(tree.attrib.get('viewBox', '').split()) == 4, path
    assert all(float(value) > 0 for value in tree.attrib['viewBox'].split()[2:]), path
    ids = {node.attrib['id'] for node in tree.iter() if 'id' in node.attrib}
    assert tree.attrib.get('aria-labelledby') and set(tree.attrib['aria-labelledby'].split()) <= ids, path
    return tree


class PortfolioChecks(unittest.TestCase):
    maxDiff = None

    @classmethod
    def setUpClass(cls):
        cls.projects = read_json(ROOT / 'registry/projects.json')
        cls.original = read_json(ROOT / 'registry/original_titles.json')
        cls.annexes = read_json(ROOT / 'registry/engineering_annexes.json')

    def test_exact_original_coverage(self):
        want = {f'{s}{i+1:02}': t for s, ts in self.original.items() for i, t in enumerate(ts)}
        self.assertEqual(len(want), 117)
        self.assertEqual({p['id']: p['original_title'] for p in self.projects}, want)

    def test_unique_ids_and_mission_names(self):
        self.assertEqual(len(self.projects), 117)
        for key in ['id', 'name']:
            self.assertEqual(len({p[key].casefold() for p in self.projects}), 117)

    def test_models_and_data_contracts(self):
        for p in self.projects:
            with self.subTest(id=p['id']):
                for key in ['equations', 'variables', 'assumptions', 'method', 'limitations']:
                    self.assertTrue(p['model'][key])
                self.assertGreaterEqual(len(p['sources']), 2)
                self.assertGreaterEqual(len(p['plan']), 3)
                self.assertGreaterEqual(len(p['validation']), 2)
                self.assertTrue(p['data'])
                for data in p['data']:
                    for key in ['source', 'url', 'fields', 'access', 'role']:
                        self.assertTrue(data.get(key), key)

    def test_source_links_are_https(self):
        for p in self.projects:
            for source in p['sources']:
                self.assertTrue(source['url'].startswith('https://'), (p['id'], source['url']))

    def test_each_dossier_has_a_conceptual_figure(self):
        for p in self.projects:
            with self.subTest(id=p['id']):
                file = project_document(p)
                self.assertTrue(file.is_file())
                self.assertIn(p['original_title'], file.read_text(encoding='utf-8'))
                accessible_svg(project_directory(p) / 'figures/architecture.svg')

    def test_internal_markdown_and_html_links_and_fragments(self):
        failures = []
        cached_anchors = {}
        for file in ROOT.rglob('*.md'):
            if '.git' in file.parts or 'node_modules' in file.parts:
                continue
            targets, _ = references(file.read_text(encoding='utf-8'))
            for target in targets:
                if urlsplit(target).scheme or target.startswith('//'):
                    continue
                path, _, anchor = target.partition('#')
                destination = (file.parent / unquote(path)).resolve() if path else file
                if not destination.exists():
                    failures.append((str(file.relative_to(ROOT)), target, 'missing path'))
                elif anchor and destination.suffix.lower() == '.md':
                    if destination not in cached_anchors:
                        cached_anchors[destination] = markdown_anchors(destination.read_text(encoding='utf-8'))
                    if unquote(anchor) not in cached_anchors[destination]:
                        failures.append((str(file.relative_to(ROOT)), target, 'missing fragment'))
        self.assertEqual(failures, [])

    def test_combined_aeronautics_concepts_retained(self):
        project = next(p for p in self.projects if p['id'] == 'D03')
        text = json.dumps(project).lower()
        self.assertIn('autorotat', text)
        self.assertIn('laminar', text)
        self.assertGreaterEqual(len(project.get('subprojects', [])), 2)

    def test_documentation_order_and_coherent_project_layout(self):
        self.assertFalse((ROOT / 'web').exists())
        self.assertFalse((ROOT / 'atlas').exists())
        wanted = [f'{s}{i+1:02}' for s, ts in self.original.items() for i in range(len(ts))]
        self.assertEqual([p['id'] for p in self.projects], wanted)
        paths = read_json(ROOT / 'registry/project_paths.json')
        self.assertEqual([row['id'] for row in paths], wanted)
        for p, row in zip(self.projects, paths):
            with self.subTest(id=p['id']):
                self.assertEqual(ROOT / row['directory'], project_directory(p))
                self.assertEqual(ROOT / row['document'], project_document(p))
        register = (ROOT / 'ENGINEERING_DOCUMENTATION.md').read_text(encoding='utf-8')
        seen = re.findall(r'\]\(research/[A-I]/([A-I]\d{2})-[^/)]+/README\.md\)', register)
        self.assertEqual(seen, wanted)
        for session in self.original:
            book = (ROOT / 'handbooks' / f'SESSION_{session}.md').read_text(encoding='utf-8')
            self.assertEqual(re.findall(r'<a id="([a-i]\d{2})">', book),
                             [pid.lower() for pid in wanted if pid.startswith(session)])

    def test_engineering_contract_and_traceability_coverage(self):
        self.assertEqual([a['id'] for a in self.annexes], [p['id'] for p in self.projects])
        with (ROOT / 'registry/requirements.csv').open(encoding='utf-8') as handle:
            requirements = list(csv.DictReader(handle))
        with (ROOT / 'registry/verification_cases.csv').open(encoding='utf-8') as handle:
            cases = list(csv.DictReader(handle))
        for records in [requirements, cases]:
            self.assertEqual({r['project_id'] for r in records}, {p['id'] for p in self.projects})
            self.assertEqual(len({r['id'] for r in records}), len(records))
        self.assertEqual(len(requirements), 527)
        self.assertEqual(len(cases), 434)
        for p, annex in zip(self.projects, self.annexes):
            with self.subTest(id=p['id']):
                self.assertGreaterEqual(len(annex['requirements']), 4)
                self.assertGreaterEqual(len(annex['derivation']), 3)
                self.assertGreaterEqual(len(annex['verification_cases']), 3)
                data = project_directory(p) / 'data'
                schema = read_json(data / 'schema.json')
                with (data / 'acquisition.csv').open(encoding='utf-8', newline='') as handle:
                    records = list(csv.reader(handle))
                self.assertEqual(len(records), 1, 'Acquisition template must not invent data')
                self.assertEqual(records[0], list(schema['properties']))
                self.assertEqual(records[0], [r['field'] for r in annex['data_dictionary']])
                with (data / 'dictionary.csv').open(encoding='utf-8', newline='') as handle:
                    self.assertEqual(list(csv.DictReader(handle)), annex['data_dictionary'])
                for row in annex['data_dictionary']:
                    field = schema['properties'][row['field']]
                    self.assertEqual(field['x-unit'], row['unit'])
                    self.assertEqual(field['x-source-type'], row['type'])
                    self.assertEqual(field['x-quality-rule'], row['quality_rule'])
                self.assertTrue((project_directory(p) / 'figures/architecture.mmd').is_file())

    def test_rendered_architecture_sources_and_accessibility(self):
        manifest = read_json(ROOT / 'evidence/architecture_manifest.json')
        self.assertEqual(manifest['count'], 117)
        self.assertEqual([r['project_id'] for r in manifest['figures']], [p['id'] for p in self.projects])
        for p, row in zip(self.projects, manifest['figures']):
            with self.subTest(id=p['id']):
                for name, filename in [('source', 'architecture.mmd'), ('svg', 'architecture.svg')]:
                    path = ROOT / row[name]
                    self.assertEqual(path, project_directory(p) / 'figures' / filename)
                    self.assertEqual(digest(path), row[name + '_sha256'])
                accessible_svg(ROOT / row['svg'])

    def test_all_field_maps_show_actual_dictionary_values_and_pending_state(self):
        maps = list((ROOT / 'research').rglob('data-map.svg'))
        self.assertEqual(len(maps), 117)
        for p, annex in zip(self.projects, self.annexes):
            with self.subTest(id=p['id']):
                tree = accessible_svg(project_directory(p) / 'figures/data-map.svg')
                self.assertFalse(any(tree.iter(NS + 'script')))
                self.assertFalse(any(tree.iter(NS + 'foreignObject')))
                visible = ''.join(node.text or '' for node in tree.iter(NS + 'text'))
                self.assertIn('PROPOSED DATA CONTRACT', visible)
                self.assertIn('No project observations acquired', visible)
                normalized = ''.join(visible.split())
                for row in annex['data_dictionary']:
                    for key in ['field', 'type', 'unit', 'meaning']:
                        self.assertIn(''.join(str(row[key]).split()), normalized, (p['id'], key))

    def test_document_artwork_manifest_hashes_and_evidence_labels(self):
        manifest = read_json(ROOT / 'assets/visual_design_manifest.json')
        self.assertEqual(manifest['asset_path_base'], 'repository root')
        self.assertEqual(manifest['project_order'], [p['id'] for p in self.projects])
        self.assertEqual(manifest['counts'], {'projects': 117, 'sessions': 9, 'fields': 877,
                                             'requirements': 527, 'planned_verification_cases': 434})
        self.assertEqual(manifest['asset_count'], 127)
        self.assertEqual(len(manifest['assets']), 127)
        for path, expected in manifest['input_hashes'].items():
            self.assertEqual(digest(ROOT / path), expected, path)
        fields = [row for row in manifest['assets'] if row['kind'] == 'proposed_data_contract']
        self.assertEqual([row['project_id'] for row in fields], [p['id'] for p in self.projects])
        for row in manifest['assets']:
            with self.subTest(path=row['path']):
                path = ROOT / row['path']
                self.assertEqual(digest(path), row['sha256'])
                self.assertEqual(path.stat().st_size, row['bytes'])
                self.assertIn(row['kind'], manifest['evidence_labels'])
                accessible_svg(path)

    def test_data_figures_provenance_and_observational_counts(self):
        folder = ROOT / 'data/figures'
        ledger = read_json(folder / 'DATA_FIGURES.json')
        self.assertEqual(digest(ROOT / ledger['renderer']['path']), ledger['renderer']['sha256'])
        figures = ledger['figures']
        self.assertEqual(len(figures), 9)
        self.assertEqual(len({r['id'] for r in figures}), 9)
        observational = []
        ids = {p['id'] for p in self.projects}
        for row in figures:
            with self.subTest(id=row['id']):
                self.assertIn(row['evidence_kind'], ['real_public_catalog_snapshot', 'synthetic_illustrative'])
                if row['evidence_kind'] == 'real_public_catalog_snapshot':
                    observational.append(row)
                self.assertTrue(row['caption'])
                self.assertTrue(row['assumptions_and_limits'])
                self.assertTrue(row['uncertainty_note'])
                self.assertTrue(row['source_assets'])
                self.assertTrue(set(row['linked_projects']) <= ids)
                accessible_svg(ROOT / row['svg'])
                self.assertTrue((ROOT / row['png']).read_bytes().startswith(b'\x89PNG\r\n\x1a\n'))
                self.assertEqual(read_json(ROOT / row['provenance']), row)
                self.assertEqual({asset['path'] for asset in row['output_assets']}, {row['svg'], row['png']})
                for source in row['source_assets'] + row['output_assets']:
                    path = ROOT / source['path']
                    self.assertEqual(digest(path), source['sha256'])
                    self.assertEqual(path.stat().st_size, source['bytes'])
        self.assertEqual(len(observational), 1)
        with (ROOT / 'models/data/exoplanet_sample.csv').open(encoding='utf-8', newline='') as handle:
            rows = list(csv.DictReader(handle))
        summary = observational[0]['derived_summaries']
        self.assertEqual(summary['rows'], len(rows))
        self.assertEqual(summary['rows'], 200)
        self.assertEqual(summary['distinct_host_names'], len({r['hostname'] for r in rows}))
        self.assertEqual(summary['discovery_method_counts'], dict(Counter(r['discoverymethod'] for r in rows)))
        self.assertEqual(summary['available_field_counts'],
                         {key: sum(bool(r[key].strip()) for r in rows)
                          for key in ['pl_orbper', 'pl_rade', 'st_met', 'discoverymethod']})
        self.assertEqual(summary['available_field_counts']['st_met'], 191)

    def test_preserved_scientific_asset_integrity(self):
        manifest = read_json(ROOT / 'models/manifest.json')
        self.assertEqual(len(manifest['assets']), 40)
        for row in manifest['assets']:
            with self.subTest(path=row['path']):
                path = ROOT / 'models' / row['path']
                self.assertEqual(digest(path), row['sha256'])
                self.assertEqual(path.stat().st_size, row['bytes'])
        provenance = read_json(ROOT / 'models/data/exoplanet_sample.provenance.json')
        self.assertEqual(digest(ROOT / 'models/data/exoplanet_sample.csv'), provenance['sha256'])
        self.assertEqual(provenance['rows'], 200)
        history = ROOT / 'archive/astra_forge'
        incoming = read_json(history / 'data/synthetic/manifest.json')
        self.assertEqual(len(incoming), 20)
        for row in incoming:
            with self.subTest(reference=row['id']):
                self.assertIn('SYNTHETIC', row['evidence_class'])
                self.assertEqual(digest(history / row['path']), row['sha256'])

    def test_data_and_figure_hubs_have_legible_previews_and_source_links(self):
        for name, minimum_images in [('data/README.md', 3), ('data/figures/README.md', 9)]:
            with self.subTest(document=name):
                file = ROOT / name
                content = file.read_text(encoding='utf-8')
                targets, parser = references(content)
                images = parser.images + [(source, alt) for alt, source in
                                           re.findall(r'!\[([^\]]*)\]\(([^\s)]+)\)', strip_code(content))]
                self.assertGreaterEqual(len(images), minimum_images)
                self.assertTrue(all(alt.strip() for source, alt in images), 'Preview images need meaningful alt text')
                self.assertIn('synthetic', content.lower())
                self.assertTrue('catalog' in content.lower() or 'observational' in content.lower())
                resolved = {(file.parent / unquote(target.partition('#')[0])).resolve()
                            for target in targets if not urlsplit(target).scheme and not target.startswith('#')}
                self.assertIn(ROOT / 'data/figures/DATA_FIGURES.json', resolved)
        data = (ROOT / 'data/README.md').read_text(encoding='utf-8').lower()
        self.assertTrue('header-only' in data or 'headers only' in data)


if __name__ == '__main__':
    unittest.main(verbosity=2)
