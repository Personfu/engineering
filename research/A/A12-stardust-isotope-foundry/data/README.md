# A12 · Data blueprint

[STARDUST ISOTOPE FOUNDRY](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![A12 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| source_grid_id | string | 1 | Explosion family and yield version. | Mass basis and absent isotopes explicit. |
| isotope_counts | vector<float64> | number per kg ejecta | Endmember yield basis. | Nonnegative; no missing isotope replaced zero. |
| condensation_factor | nullable<vector<float64>> | 1 | Element-specific incorporation hypothesis. | Bounds/provenance required; unknown TBD. |
| beam_fraction | nullable<float64> | 1 | Grain contribution in response model. | Between zero and one; definition recorded. |
| mass50_correction | record | count | Ti/Cr interference attribution. | Joint error retained. |
| reference_ratios | vector<float64> | 1 | Declared isotope standards. | Normalization/fractionation convention required. |
| ratio_covariance | matrix<float64> | 1 | Joint observed ratio uncertainty. | Symmetric positive semidefinite; denominator correlations retained. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [Presolar oxide Ti/Cr grain study](https://pmc.ncbi.nlm.nih.gov/articles/PMC6491047/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Supernova nanoparticle isotope study](https://arxiv.org/abs/1007.4016) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
