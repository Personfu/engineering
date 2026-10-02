import csv
import hashlib
import json
import math
import unittest
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path
from models.reference import (DEMOS,escape,liquidus,orbit,thermal,sphere_drag,attitude,consensus,nlms)

ROOT=Path(__file__).resolve().parents[1]


class NumericalChecks(unittest.TestCase):
    def test_escape_known_cases(self):
        self.assertEqual(escape(0j),0)
        self.assertEqual(escape(-1+0j),0)
        self.assertEqual(escape(3+0j),1)
        self.assertGreater(escape(1+0j),0)
        with self.assertRaises(ValueError):escape(0j,iterations=0)

    def test_liquidus_pure_limit_and_depression(self):
        self.assertAlmostEqual(liquidus(1),270)
        self.assertLess(liquidus(.5),270)
        with self.assertRaises(ValueError):liquidus(0)

    def test_orbit_conservation_and_convergence(self):
        coarse=orbit(steps=300)['rows'];fine=orbit(steps=1200)['rows']
        def drift(rows):return max(abs(r[3]-rows[0][3]) for r in rows)
        self.assertLess(drift(fine),drift(coarse)/10)
        self.assertLess(drift(fine),1e-4)
        self.assertLess(max(abs(r[4]-fine[0][4]) for r in fine),1e-12)
        circle=orbit(e=0)['rows']
        self.assertAlmostEqual(math.hypot(circle[-1][1],circle[-1][2]),1,places=5)
        with self.assertRaises(ValueError):orbit(e=1)

    def test_thermal_exact_decay_and_limit(self):
        rows=thermal(power=0)['rows']
        self.assertEqual(rows[0][1],293.15)
        self.assertTrue(all(rows[i][1]>rows[i+1][1] for i in range(len(rows)-1)))
        self.assertAlmostEqual(rows[-1][1],250+43.15*math.exp(-.08*7200/100))
        with self.assertRaises(ValueError):thermal(conductance=0)

    def test_drag_creeping_limit_and_domain(self):
        re=1e-8
        self.assertAlmostEqual(sphere_drag(re)*re,24,places=4)
        with self.assertRaises(ValueError):sphere_drag(0)
        with self.assertRaises(ValueError):sphere_drag(2000)

    def test_consensus_preserves_mass_and_converges(self):
        rows=consensus()['rows']
        self.assertTrue(all(abs(sum(r[1:])-1)<1e-12 for r in rows))
        self.assertLess(max(rows[-1][1:])-min(rows[-1][1:]),.002)

    def test_attitude_norm_and_settling(self):
        rows=attitude()['rows']
        self.assertTrue(all(abs(r[1]**2+r[2]**2-1)<1e-12 for r in rows))
        self.assertLess(abs(rows[-1][3]),.02)
        self.assertTrue(all(abs(r[5])<=.1 for r in rows))

    def test_adaptive_cancellation_preserves_signal(self):
        rows=nlms()['rows'][300:]
        before=sum((r[2]-r[1])**2 for r in rows)
        after=sum((r[3]-r[1])**2 for r in rows)
        self.assertLess(after,before*.3)

    def test_all_outputs_finite_deterministic_and_labeled(self):
        for name,fn in DEMOS.items():
            with self.subTest(name=name):
                data=fn();self.assertEqual(data,fn())
                self.assertIn('SYNTHETIC',data['evidence_class'])
                self.assertTrue(data['limitations'])
                self.assertTrue(all(len(r)==len(data['columns']) for r in data['rows']))
                self.assertTrue(all(math.isfinite(v) for r in data['rows'] for v in r))


class PortfolioChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.catalog=json.loads((ROOT/'catalog/projects.json').read_text())

    def test_complete_original_inventory(self):
        expected={'A':12,'B':28,'C':30,'D':8,'E':8,'F':2,'G':8,'H':9,'I':13}
        projects=self.catalog['projects']
        with (ROOT/'catalog/projects.tsv').open() as handle:
            supplied=list(csv.DictReader(handle,delimiter='\t'))
        self.assertEqual(Counter(p['session'] for p in projects),expected)
        self.assertEqual([p['title'] for p in projects],[p['title'] for p in supplied])
        self.assertEqual(len({p['name'] for p in projects}),118)
        self.assertEqual(len(list((ROOT/'projects').glob('*.md'))),118)

    def test_dossier_visual_source_and_dependency_integrity(self):
        ids={p['id'] for p in self.catalog['projects']};sources={s['id'] for s in self.catalog['sources']}
        for p in self.catalog['projects']:
            with self.subTest(id=p['id']):
                dossier=(ROOT/p['dossier']).read_text()
                self.assertIn(p['title'],dossier)
                self.assertIn('Scientific validation',dossier)
                self.assertIn('None ingested',dossier)
                self.assertTrue(set(p['sources'])<=sources)
                self.assertTrue(set(p['related'])<=ids)
                self.assertNotIn(p['id'],p['related'])
                ET.parse(ROOT/p['workflow'])
                if p['demo']:self.assertIn(p['demo'],DEMOS)

    def test_synthetic_manifest_hashes(self):
        records=json.loads((ROOT/'data/synthetic/manifest.json').read_text())
        self.assertEqual(len(records),20)
        for record in records:
            raw=(ROOT/record['path']).read_bytes()
            self.assertEqual(hashlib.sha256(raw).hexdigest(),record['sha256'])
            self.assertEqual(len(json.loads(raw)['rows']),record['rows'])
            ET.parse(ROOT/f'visuals/reference/{record["id"]}.svg')

    def test_truthful_no_live_data_state(self):
        self.assertTrue(all(p['data_status']=='NO MEASUREMENTS INGESTED' for p in self.catalog['projects']))
        self.assertEqual(len(self.catalog['sources']),51)
        self.assertIn('blocked',{s['status'] for s in self.catalog['sources']})


if __name__=='__main__':unittest.main()
