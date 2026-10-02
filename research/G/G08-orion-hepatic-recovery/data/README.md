# G08 · Data blueprint

[ORION HEPATIC RECOVERY](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![G08 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| study_subject | string | 1 | De-identified subject/species context. | Group and source provenance required. |
| observation_time | vector<float64> | day | Time from documented reference event. | No inferred clinical procedure details. |
| volume_observed | nullable<float64> | m^3 | Imaging volume estimate. | Segmentation covariance and reference required. |
| cell_states | vector<float64>[3] | cell | Q, P and R model populations. | Nonnegative; modeled versus measured labeled. |
| mediator_signals | nullable<record> | declared | C/GF normalized or native signals. | Measured/latent status and unit mapping mandatory. |
| cell_volume | nullable<float64> | m^3/cell | Mean size contribution. | Unknown not fixed silently. |
| subject_covariance | matrix<float64> | mixed | Repeated observation/parameter uncertainty. | Positive semidefinite with ordered units. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [Original liver-regeneration model](https://pmc.ncbi.nlm.nih.gov/articles/PMC2712210/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Human live-donor model study](https://pmc.ncbi.nlm.nih.gov/articles/PMC6289189/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
