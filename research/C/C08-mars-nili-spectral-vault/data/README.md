# C08 · Data blueprint

[MARS NILI SPECTRAL VAULT](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![C08 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| sample_id | string | 1 | Unique physical mixture/replicate. | Blind identity hidden during calibration. |
| mass_fraction | float64[k] | 1 | Weighed mineral mass fractions. | Nonnegative and sum one within balance uncertainty. |
| grain_distribution | table | micrometer | Particle-size bins and weights. | Missing tails and sieve convention documented. |
| geometry | float64[3] | degree | Incidence, emergence and phase. | Record instrument frame and sample orientation. |
| reflectance | float64[n] | 1 | Standard-referenced spectrum. | Bad wavelengths remain masked; retain nonphysical noisy values for diagnosis. |
| reflectance_cov | float64[n,n] | 1 | Standard, repeat and detector covariance. | Shared standard uncertainty retained. |
| optical_fraction | posterior<float64[k]> | 1 | Model-conditioned optical mixture weights. | Do not relabel as mass fraction without a justified conversion. |
| detection_probability | float64 | 1 | Recovery probability within a specified scenario. | Use blind/injection uncertainty and state scenario domain. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [USGS Spectral Library Version 7](https://www.usgs.gov/data/usgs-spectral-library-version-7-data) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [PDS MRO CRISM archive](https://pds-geosciences.wustl.edu/missions/mro/crism.htm) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)

## Included evidence to explore

![C08 included data diagnostic](../../../../data/figures/15_spectral_information_and_noise.svg)

Synthetic spectral-mixture estimator distributions under the same known band-noise level. Separated endmembers give narrow noise-driven fraction estimates; near-identical endmembers give a broad unconstrained distribution with unphysical values preserved as an identifiability diagnostic. Central 95% noise-realization intervals are descriptive simulation intervals, not posteriors or uncertainty bounds for measured Mars mineral abundance.

[Data atlas: tables, model definitions and provenance](../../../../data/README.md). Shared reduced-model evidence has a narrower domain than this project contract.
