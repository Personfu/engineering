# I11 · Data blueprint

[HUBBLE SKYVAULT](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![I11 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| exposure_manifest | struct | 1 | HST exposure/filter/detector/reference identity. | Include inaccessible/failed records and selection status. |
| raw_counts | float64[h,w] | electron | Common detector data for branches. | Quality masks retained; missing pixels absent. |
| variant_reference | struct | 1 | Dark/flat/persistence/pipeline files. | Hash and operation order/sky ledger. |
| common_mask | bool[h,w] | 1 | Primary object/artifact exclusions. | Hash identical across paired branches. |
| sky_statistic | measurement<float64> | electron s^-1 sr^-1 | Declared foreground estimator. | Usable area and pixel-solid-angle convention. |
| paired_covariance | float64[nvariant,nvariant] | brightness^2 | Shared exposure/calibration/mask error. | Preserve cross-variant terms. |
| context | struct | degree, pixel, epoch | Filter, geometry, position and epoch. | Missing context flagged before regression. |
| calibration_difference | measurement<float64> | brightness unit | Paired variant effect. | Physical flux conversion version separate. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [MAST SKYSURF high-level science products](https://archive.stsci.edu/hlsp/skysurf) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Windhorst et al. (2022) SKYSURF overview](https://arxiv.org/abs/2205.06214) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
