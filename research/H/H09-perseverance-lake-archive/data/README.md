# H09 · Data blueprint

[PERSEVERANCE LAKE ARCHIVE](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![H09 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| crism_product | string | none | Actual target/level/version identity. | Terby/basin coverage and masks verified. |
| reflectance_spectrum | nullable float[] | dimensionless | Corrected native spectral observations. | Wavelength/geometry and covariance retained. |
| band_depth | nullable float[] | dimensionless | Declared continuum feature metric. | Continuum alternatives and artifact flags saved. |
| mineral_fraction | float[][] | declared fraction basis | Posterior compatible compositions. | Nonnegative/simplex and library support checked. |
| optical_size | float[] | micrometre | Effective radiative-transfer particle size. | Distinct from geological sieve distribution. |
| thermal_constraint | nullable record | K and inertia units | Supported temperature/thermophysical evidence. | Time, rocks/porosity/layering retained. |
| model_prior | float vector | 0–1 | p(M) for mixing/transport/alteration families. | Normalized and sensitivity documented. |
| joint_covariance | matrix | mixed | Spectral/thermal/registration uncertainty. | Correlated errors and native support included. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [PDS CRISM archive](https://pds-geosciences.wustl.edu/missions/mro/crism.htm) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [HiRISE images and DTM discovery](https://hirise.lpl.arizona.edu/dtm/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [PDS Odyssey THEMIS thermal image products](https://pds.nasa.gov/ds-view/pds/viewProfile.jsp?dsid=ODY-M-THM-5-IRGEO-V2.0) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)

## Included evidence to explore

![H09 included data diagnostic](../../../../data/figures/15_spectral_information_and_noise.svg)

Synthetic spectral-mixture estimator distributions under the same known band-noise level. Separated endmembers give narrow noise-driven fraction estimates; near-identical endmembers give a broad unconstrained distribution with unphysical values preserved as an identifiability diagnostic. Central 95% noise-realization intervals are descriptive simulation intervals, not posteriors or uncertainty bounds for measured Mars mineral abundance.

[Data atlas: tables, model definitions and provenance](../../../../data/README.md). Shared reduced-model evidence has a narrower domain than this project contract.
