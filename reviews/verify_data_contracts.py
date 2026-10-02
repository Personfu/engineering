"""Check structural schema validity and scientific encoding regression fixtures.

Fixtures are synthetic interface values, not acquired project measurements.
Physical/ICD domain rules require additional project-specific checks.
"""
import json
import unittest
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parents[1]

class DataContracts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schemas={p.stem.split('.')[0]:json.loads(p.read_text(encoding='utf-8')) for p in (ROOT/'data/contracts').glob('*.schema.json')}

    def field(self,pid,field):
        return Draft202012Validator(self.schemas[pid]['properties'][field])

    def test_all_contracts_are_valid_and_unknowns_are_explicit(self):
        self.assertEqual(len(self.schemas),117)
        for pid,schema in self.schemas.items():
            with self.subTest(id=pid):
                Draft202012Validator.check_schema(schema)
                validator=Draft202012Validator(schema)
                validator.validate(dict.fromkeys(schema['properties'],None))
                self.assertFalse(validator.is_valid({}),'Absent fields must be explicit nulls, not silently absent.')
                self.assertFalse(validator.is_valid({**dict.fromkeys(schema['properties'],None),'uncontrolled_field':0}))

    def test_exact_two_by_two_covariance_shape(self):
        validator=self.field('B24','position_covariance')
        validator.validate([[4.0,0.1],[0.1,9.0]])
        for invalid in [1,[4,9],[[4,0,0],[0,9,0]],[[4,0]],[[4,'unknown'],[0,9]]]:
            self.assertFalse(validator.is_valid(invalid),invalid)

    def test_scenario_raster_rank(self):
        validator=self.field('B12','basal_surface')
        validator.validate([[[1.0,2.0],[3.0,4.0]],[[2.0,3.0],[4.0,5.0]]])
        for invalid in [3,[1,2],[[1,2],[3,4]]]:self.assertFalse(validator.is_valid(invalid))

    def test_coefficient_row_column_contract(self):
        validator=self.field('D03','aero_coefficients')
        validator.validate([[0.2,0.03],[0.3,0.04]])
        for invalid in [[0.2,0.03],[[0.2]],[[0.2,0.03,0.4]]]:self.assertFalse(validator.is_valid(invalid))

    def test_sparse_operator_representation(self):
        validator=self.field('C02','resample_operator')
        validator.validate({'shape':[2,2],'row':[0,1],'col':[0,1],'data':[1.,1.]})
        for invalid in [1.0,{'shape':[2,2],'row':[0],'col':[0]}, {'shape':[2,2],'row':[-1],'col':[0],'data':[1]}]:
            self.assertFalse(validator.is_valid(invalid))

    def test_complex_tensor_preserves_numeric_components(self):
        validator=self.field('C25','whitened_tiles')
        validator.validate([[[{'real':1.,'imag':0.5}]]])
        for invalid in [[[['1+0.5i']]],[[[{'real':1.}]]],[[[{'real':1.,'imag':'0.5'}]]]]:
            self.assertFalse(validator.is_valid(invalid))

    def test_record_array_container_is_not_scalar(self):
        validator=self.field('E06','conductance_edges')
        validator.validate([{'from':'node_1','to':'node_2','conductance':1.0}])
        for invalid in [{'from':'node_1'},'node_1',1.0]:self.assertFalse(validator.is_valid(invalid))

    def test_distribution_records_preserve_representation(self):
        validator=self.field('C06','orbital_phase')
        validator.validate({'representation':'empirical','samples':[0.1,0.2,0.3],'weights':[1,1,1]})
        validator.validate({'representation':'unidentified'})
        for invalid in [0.2,{'samples':[0.2]},{'representation':'known','samples':[0.2]}, {'representation':'empirical','samples':['0.2']}]:
            self.assertFalse(validator.is_valid(invalid))

if __name__=='__main__':unittest.main(verbosity=2)
