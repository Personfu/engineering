# H06 · Data blueprint

[MARS ODYSSEY RIDGEWORK](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![H06 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| terrain_product | string | none | DTM/MOLA product identity. | Resolution/datum/coverage retained. |
| centerline_s | float[] | m | Along-strike ridge coordinate. | Local tangent and segment IDs saved. |
| profile_xz | float[][2] | m | Cross-ridge distance/elevation. | Normal orientation and spacing recorded. |
| background_surface | float[] | m | Regional detrending ensemble. | Not treated as exact terrain. |
| morphometrics | float vector | m and dimensionless | Height/width/asymmetry/crest separation. | Joint measurement covariance retained. |
| fault_parameters | record | degrees m | Family-specific dip/depth/slip scenarios. | Units/bounds and source rationale required. |
| profile_covariance | matrix | m² | Correlated terrain/background error. | Along-strike/shared datum terms included. |
| family_probability | float vector | 0–1 | Model posterior weights. | p(M) and prior sensitivity saved. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [HiRISE DTM archive](https://hirise.lpl.arizona.edu/dtm/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [The tectonic architecture of wrinkle ridges on Mars](https://www.sciencedirect.com/science/article/abs/pii/S0019103520303110) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [PDS MOLA topography products](https://pds-geosciences.wustl.edu/missions/mgs/mola.html) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
