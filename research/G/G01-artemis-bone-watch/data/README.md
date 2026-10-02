# G01 · Data blueprint

[ARTEMIS BONE WATCH](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![G01 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| specimen_id | string | 1 | Geometry/material context and source. | Synthetic/ex vivo category required. |
| sensor_direction | vector<float64>[3] | 1 | Unit vector in specimen axes. | Norm and orientation uncertainty checked. |
| raw_observable | record | native | Wavelength/resistance/native readout. | Units/channel calibration required; missing null. |
| temperature | nullable<float64> | K | Local sensor temperature. | Reference and covariance retained. |
| attachment_transfer | matrix<float64> | native/strain | Identified H coefficients. | Calibration provenance and rank required. |
| strain_reference | nullable<vector<float64>> | 1 | Independent reference tensor/projections. | Coordinate/shear basis and uncertainty recorded. |
| strain_estimate | record | 1 | Identifiable components and covariance. | Unobserved components null; regularization flag required. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [FBG femur strain study](https://pmc.ncbi.nlm.nih.gov/articles/PMC7552668/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Interfacial load monitoring using impedance tomography](https://arxiv.org/abs/1912.04723) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
