# C16 · Data blueprint

[ORION STRAIN METROLOGY](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![C16 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| detector_epoch | struct<string,time> | GPS second | Detector and release epoch. | Strain variant and uncertainty product matched. |
| frequency | float64[n] | Hz | Calibration/inference frequency grid. | Within documented calibrated support. |
| amplitude_error | float64[n] | 1 | Fractional transfer perturbation. | Convention and envelope version required. |
| phase_error | float64[n] | radian | Transfer phase perturbation. | Smooth function; unwrap convention explicit. |
| coefficient_cov | float64[m,m]&#124;null | mixed declared | Spline/GP prior covariance. | Null means unavailable measured covariance; assumed version labeled. |
| waveform_id | string | 1 | Physical CCSN simulation provenance. | No split leakage through repeated injections. |
| parameter_shift | float64[q] | parameter-specific | Paired ignored/marginalized bias metric. | Store full posterior and injection truth where defined. |
| mismatch | float64 | 1 | Noise-weighted band-limited normalized difference. | Optimization over time/phase explicitly declared. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [GWOSC O4 technical details](https://gwosc.org/O4/o4_details/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [GWOSC strain](https://gwosc.org/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
