# G04 · Data blueprint

[ARTEMIS CARTILAGE MATRIX](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![G04 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| target_region | record | 1 | Anatomical region and published response context. | Population/test mode required; no universal target. |
| geometry | record | m | Construct/test domain dimensions. | Tolerance and boundary conditions retained. |
| solid_parameters | record | Pa,1 | Moduli and Poisson response. | Physical range/source and covariance required. |
| intrinsic_permeability | float64 | m^2 | Darcy material permeability. | Positive; never mislabeled conductivity. |
| fluid_viscosity | float64 | Pa s | Fluid dynamic viscosity. | Temperature/context recorded. |
| relaxation_curve | nullable<array<time,stress>> | s,Pa | Published/model relaxation observation. | Load history and digitization error retained. |
| cure_field | nullable<array<float64>> | 1 | Hypothesized material-state heterogeneity. | Uncalibrated fields labeled proposed; null allowed. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [Photopolymerized nanocomposite cartilage-damage study](https://pmc.ncbi.nlm.nih.gov/articles/PMC4950507/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Photoreactive adhesive-hydrogel composite study](https://pmc.ncbi.nlm.nih.gov/articles/PMC3972413/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
