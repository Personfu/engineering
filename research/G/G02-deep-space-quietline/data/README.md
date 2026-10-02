# G02 · Data blueprint

[DEEP SPACE QUIETLINE](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![G02 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| sample_time | vector<float64> | s | Common desired/reference clock. | Rate and alignment offset covariance required. |
| desired_raw | vector<float64> | native | Science plus interference channel. | ADC units/limits and clipping mask retained. |
| reference_raw | nullable<vector<float64>> | native | Interference witness channel. | Dropout mask; no silent zero fill. |
| filter_weights | array<vector<float64>> | ratio | Saved tapped-delay coefficients. | Ordering, length and update cadence required. |
| adaptation_state | enum | 1 | Adapt, frozen or bypass. | Reason and event time logged. |
| spectral_estimates | record | native^2/Hz | Power/cross spectra and coherence. | Window/normalization and degrees of freedom retained. |
| feature_error | record | 1,rad,s | Amplitude ratio, phase and timing error. | Truth/reference covariance and protected-band definition. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [Stanford adaptive noise-cancellation paper](https://www-isl.stanford.edu/~widrow/papers/j1975adaptivenoise.pdf) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Le and Hensley, RFI Removal from AIRSAR Polarimetric Data](https://airsar.jpl.nasa.gov/documents/workshop2002/papers/T8.pdf) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
