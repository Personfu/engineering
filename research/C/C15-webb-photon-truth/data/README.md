# C15 · Data blueprint

[WEBB PHOTON TRUTH](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![C15 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| exposure_id | string | 1 | MAST program/product identity. | Pin product checksum and processing level. |
| source_sed | float64[nlambda] | W m^-2 m^-1 | Flux spectrum at telescope. | Reference and uncertainty; wavelength in meters internally. |
| collecting_area | measurement<float64> | m^2 | Area consistent with throughput convention. | Do not double-count obscuration in both area and T. |
| throughput_pixel | float64[nlambda,npix] | 1 | Registered photon/pixel probability. | Sum cannot exceed declared total registration probability. |
| wavefront_opd | float64[h,w] | m | Matched optical-path map. | Epoch and pupil coordinate registration required. |
| ramp | float64[nread,h,w] | electron | Simulated/observed accumulated charge. | Read times and saturation masks retained. |
| metric_cov | float64[nmetric,nmetric] | mixed declared | Covariance of PSF/ramp/astrometric metrics. | MC and observation terms separately stored. |
| discrepancy_label | enum | 1 | Optical, detector, calibration or resampling category. | Unknown attribution retained explicitly. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [MAST JWST holdings](https://archive.stsci.edu/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [STScI NIRCam PSF documentation](https://jwst-docs.stsci.edu/jwst-near-infrared-camera/nircam-performance/nircam-point-spread-functions) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
