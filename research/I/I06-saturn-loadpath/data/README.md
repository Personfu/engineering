# I06 · Data blueprint

[SATURN LOADPATH](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![I06 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| cad_mesh_revision | struct<string> | 1 | Linked geometry/mesh/solver identity. | Checksums and units mandatory. |
| material_properties | measurement<struct> | Pa, kg m^-3 | E, density, strength/constitutive pedigree. | Assumed versus certified; temperature domain. |
| joint_model | distribution<struct> | N m^-1, N m rad^-1 | Connection stiffness and slip model. | Perfect connection only as explicit comparator. |
| load_constraint | struct | N, N m, m | Supplied force/moment and fixture boundary. | Coordinate/sign and source documented. |
| imperfection_field | distribution<array> | m | Geometric deviations by mode/location. | Amplitude prior and metrology evidence. |
| response | measurement<struct> | m, strain, Hz | Static and modal model/test quantities. | Sensor/fixture covariance and missing channels. |
| similarity_ledger | table | 1 | Matched/unmatched dimensionless groups. | No full-scale conclusion from unmatched groups. |
| pareto_design | table | kg, m N^-1, 1 | Mass/compliance/uncertainty candidates. | Screening buckling status and manufacturability. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [NASA structures reference](https://www.nasa.gov/smallsat-institute/sst-soa/structures-materials-and-mechanisms/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Proposed inert structural test dataset](https://www.nasa.gov/reference/systems-engineering-handbook/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
