# C06 · Data blueprint

[PULSAR GEMINI WATCH](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![C06 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| arrival_epoch | float64[] | TDB seconds or MJD | Barycentric event times. | Original clock and correction files required. |
| orbital_phase | posterior<float64> | cycle | Phase from a versioned ephemeris. | Wrap consistently; preserve phase covariance. |
| spin_period | measurement<float64> | s | Observed/corrected period with detection context. | Nondetection has no artificial zero period. |
| period_derivative | measurement<float64>&#124;null | s s^-1 | Derivative with explicit intrinsic/observed type. | Do not assign intrinsic type without torque/acceleration treatment. |
| count_spectrum | struct<count,response> | count | Energy-resolved source/background counts. | Poisson likelihood; response and exposure mandatory. |
| burst_localization | distribution<sky> | degree ICRS | Spatial source likelihood. | Normalize and include instrumental systematic uncertainty. |
| radius_ordering | posterior<enum> | 1 | State probability from lc/co/m radii. | Report multimodal state probabilities. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [Weng et al. radio-pulsation publication](https://arxiv.org/abs/2203.09423) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Swift and other HEASARC holdings](https://heasarc.gsfc.nasa.gov/docs/archive.html) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
