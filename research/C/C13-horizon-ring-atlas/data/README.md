# C13 · Data blueprint

[HORIZON RING ATLAS](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![C13 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| baseline_uv | float64[n,2] | wavelength | Sampled Fourier coordinates. | Frequency and station pair attached. |
| visibility | complex128[n] | Jy | Calibrated complex measurements. | Flags retained; missing baselines are absent, never zero. |
| visibility_cov | covariance | Jy^2 | Thermal and calibration covariance. | Separate real/imaginary or complex convention declared. |
| closure_phase | measurement<float64> | radian | Triangle phase sum. | Circular likelihood and covariance with related triangles required. |
| gain_parameters | posterior<complex[]> | 1 | Station gain nuisance terms. | Epoch/group association recorded. |
| ring_metrics | posterior<struct> | microarcsec, 1 | Diameter, width, asymmetry and depression. | Metric definition and reconstruction family attached. |
| source_context | struct | s, microarcsec | Variability/scattering assumptions. | Different target contexts cannot be silently merged. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [EHT Data Products](https://eventhorizontelescope.org/for-astronomers/data) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [EHT M87 imaging publication](https://eventhorizontelescope.org/publications/first-m87-event-horizon-telescope-results-iv-imaging-central-supermassive-black) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
