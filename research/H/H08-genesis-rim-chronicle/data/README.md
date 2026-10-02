# H08 · Data blueprint

[GENESIS RIM CHRONICLE](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![H08 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| specimen_section | string | none | Nested meteorite/section identity. | Curator and preparation lineage required. |
| alteration_indicator | nullable record | declared | Independent alteration/heating evidence. | Not inferred from target thickness. |
| core_radius | float[] | micrometre | Observed/3D core-size distribution. | Sectioning correction and uncertainty saved. |
| rim_interval | nullable float[2] | micrometre | Boundary-supported thickness range. | Below-resolution censor limit retained. |
| porosity | nullable float[] | 0–1 | Present or scenario rim void fraction. | Initial/current distinction explicit. |
| dust_growth_inputs | record | kg/m³ m/s fraction | Accretion scenario parameters. | Source range and covariance required. |
| annotation_covariance | matrix | micrometre² | Boundary and registration uncertainty. | Shared labeler/section effects included. |
| mechanism_weight | float vector | 0–1 | Accretion/modification/mixed compatibility. | Model priors and specimen holdout saved. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [Published CM rim study and three supporting appendices](https://onlinelibrary.wiley.com/doi/10.1111/maps.14076) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Porous aggregate rim-formation model](https://arxiv.org/abs/2105.06051) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
