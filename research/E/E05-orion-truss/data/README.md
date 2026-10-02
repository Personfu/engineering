# E05 · Data blueprint

[ORION TRUSS](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![E05 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| icd_revision | nullable<string> | 1 | Controlling deployer interface document. | Missing blocks final dimension acceptance. |
| load_case | record | N,N m | Mission/provider load vector and frame. | Source, environment and factor provenance. |
| material_allowable | record | Pa | Temperature-specific failure allowable. | Reduction/FOS history required. |
| joint_stiffness | nullable<record> | N/m,N m/rad | Fastener/contact compliance. | Distribution/covariance and source retained. |
| component_mass_map | array<record> | kg,m | Mass/inertia positions. | Harness/support allowances explicit. |
| cad_clearances | record | m | Rail and access margins. | Tolerance covariance and protected regions. |
| analysis_margin | nullable<record> | 1 | Mode/stress/interface margins. | Pending inputs yield null, not zero pass. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [NASA Small Spacecraft Structures](https://www.nasa.gov/smallsat-institute/sst-soa/structures-materials-and-mechanisms/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [GSFC-STD-7000 GEVS](https://standards.nasa.gov/standard/GSFC/GSFC-STD-7000) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
