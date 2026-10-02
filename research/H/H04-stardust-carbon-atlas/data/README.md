# H04 · Data blueprint

[STARDUST CARBON ATLAS](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![H04 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| specimen_section | restricted record | none | Target/section/custodian identity. | Allocation and history required. |
| preparation_carbon | nullable record | none | Coatings, adhesives and residues. | Unknown sources remain unresolved. |
| map_coordinates | float[2] | micrometre | Common registered position. | Transform/resolution provenance retained. |
| phase_probability | float vector | 0–1 | Spectroscopy/mineral-map interpretation. | Sum and classification uncertainty checked. |
| isotope_counts | integer[2] | counts | Raw 12C and 13C observations. | Dwell/detector/background metadata required. |
| phase_sensitivity | float vector | dimensionless | Matrix-calibration response factors. | Matched-standard covariance saved. |
| isotope_ratio | nullable float[] | dimensionless | Corrected R posterior samples. | Low-count/censor support retained. |
| registration_covariance | matrix | micrometre² | Joint correlative map uncertainty. | Serial-section discrepancy separate. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [TAM19B-7 custodian and original analytical records](https://link.springer.com/article/10.5047/eps.2008.11.001) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Published Antarctic micrometeorite correlative studies](https://doi.org/10.1016/j.gca.2023.08.023) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
