# A03 · Data blueprint

[CHANDRA VORTEX CORE](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![A03 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| star_id | string | 1 | Object and compatible observation group. | Never merge unrelated cooling/timing stars. |
| age_likelihood | distribution_record | s | Age probability or censoring bound. | Missing null; preserve upper/lower limits. |
| temperature_inf | nullable<float64> | K | Redshifted surface estimate. | Atmosphere version and covariance required. |
| gap_profile | array<radius,energy> | m,J | Pairing hypothesis over radius. | Channel and EOS mapping required. |
| inertias | pair<float64> | kg m^2 | Coupled/superfluid effective inertias. | Positive; entrainment convention documented. |
| omega_observed | nullable<float64> | rad s^-1 | Crust rotation at timing epoch. | Epoch scale and error required. |
| observable_covariance | matrix<float64> | mixed | Covariance for ordered observations. | Units per row; positive semidefinite. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [NSCool author's code resource](https://www.astroscu.unam.mx/neutrones/NSCool/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Published cooling and dynamics constraints](https://arxiv.org/abs/2103.10218) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
