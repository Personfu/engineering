# A10 · Data blueprint

[HUBBLE CARINA CLOCK](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![A10 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| spectrum_id | string | 1 | Instrument/cycle observation key. | Aperture and archive provenance required. |
| epoch_barycentric | float64 | day | Declared barycentric time coordinate. | Time scale explicit; missing epoch rejected. |
| wavelength_grid | vector<float64> | nm | Calibrated spectral coordinate. | Air/vacuum convention and rest lambda required. |
| normalized_flux | vector<float64> | 1 | Continuum-normalized line profile. | Masks and normalization uncertainty retained. |
| bisector_depth | float64 | 1 | Fixed relative profile level. | Definition identical across cycles. |
| velocity_covariance | matrix<float64> | (km/s)^2 | Estimator and calibration covariance. | Shared instrument errors included. |
| delay_kernel | array<time,weight> | day,day^-1 | Causal wind response model. | Nonnegative normalized; unknown parameters TBD. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [Orbital kinematics over three periastra](https://arxiv.org/abs/2301.00064) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Wind-convolved orbital velocity model](https://arxiv.org/abs/2003.02783) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
