# C02 · Data blueprint

[HUBBLE NIGHTFALL LAB](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![C02 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| scene_seed | uint64 | 1 | Random stream seed and generator version. | Unique scenario ID; preserve independent noise substreams. |
| sky_rate | float64[h,w] | electron s^-1 pixel^-1 | Object-free inserted sky. | Nonnegative; reference coordinate recorded. |
| source_catalog | table | mixed declared | Flux, morphology and positions. | Flux convention and truncated wings documented. |
| detector_frame | float64[h,w] | electron | Noisy exposure before resampling. | Missing pixels use mask, never sky-valued fill. |
| resample_operator | sparse<float64> | 1 | Mapping from detector to analysis pixels. | Row normalization checked for uniform sky. |
| sky_estimate | struct<float64,cov> | electron s^-1 pixel^-1 | Estimator output with estimand label. | Covariance must include resampling dependence. |
| usable_fraction | float64 | 1 | Area surviving all masks. | Bounded from zero to one; zero area invalidates estimate. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [SKYSURF HLSP](https://archive.stsci.edu/hlsp/skysurf) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Independent synthetic detector scenes](https://arxiv.org/abs/2205.06214) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
