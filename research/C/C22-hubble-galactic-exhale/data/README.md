# C22 · Data blueprint

[HUBBLE GALACTIC EXHALE](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![C22 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| galaxy_id | string | 1 | IFU target and survey selection identity. | Duplicate observations grouped. |
| spectral_cube | float64[l,h,w] | documented flux | Observed spatial spectra. | Masks/LSF/PSF attached; missing spaxels not interpolated as data. |
| cube_cov | covariance | flux^2 | Spectral and resampling uncertainty. | Shared continuum and spatial covariance retained. |
| environment | measurement<float64> | neighbor Mpc^-2 | Declared density or group estimator. | Edge/redshift completeness flags required. |
| host_covariates | measurement<struct> | solar mass, solar mass yr^-1, degree | Mass/SFR/inclination/activity. | Joint covariance and source method retained. |
| wind_probability | float64 | 1 | Component evidence after competing models. | Bounded zero to one; not a secure physical label. |
| velocity_proxy | measurement<float64> | km s^-1 | Declared projected outflow diagnostic. | Unresolved/censored states retained. |
| mass_loading | posterior<float64>&#124;null | 1 | Conditional ionized-rate/SFR ratio. | Null when necessary geometry/density inputs unavailable. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [SDSS MaNGA public data access](https://www.sdss.org/dr20/data_access/get_data/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Wind observation literature](https://arxiv.org/abs/astro-ph/0309119) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
