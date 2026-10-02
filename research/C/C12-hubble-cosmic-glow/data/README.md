# C12 · Data blueprint

[HUBBLE COSMIC GLOW](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![C12 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| visit_filter | string[2] | 1 | Exposure group and filter identity. | Versioned product IDs and sky history required. |
| sky_rate | measurement<float64> | electron s^-1 pixel^-1 | Measured object-free sky estimator. | Retain estimator quality and usable area. |
| solid_angle | measurement<float64> | sr pixel^-1 | Pixel area for intensity conversion. | Distortion-dependent area convention recorded. |
| solar_geometry | struct<float64> | degree | Solar elongation and ecliptic coordinates. | Computed at exposure epoch. |
| dust_proxy | measurement<float64> | map-documented | Galactic dust-column tracer. | Map version and beam recorded. |
| calibration_cov | float64[n,n] | mixed intensity^2 | Visit/filter systematic covariance. | Positive semidefinite; shared modes retained. |
| component_intensity | posterior<float64[components]> | MJy sr^-1 | Foreground/instrument decomposition. | All terms share bandpass convention. |
| diffuse_residual | posterior<float64> | MJy sr^-1 | Conditional residual or bound. | May be negative under noise/model; no forced detection. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [SKYSURF release](https://archive.stsci.edu/hlsp/skysurf) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [SKYSURF-4 published measurement study](https://arxiv.org/abs/2210.08010) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
