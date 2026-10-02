# A02 · Data blueprint

[NEW HORIZONS CRYOPHASE](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![A02 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| bulk_moles | vector<float64>[3] | mol | Conserved species inventory. | Nonnegative; fixed species order. |
| temperature | float64 | K | Surface/equilibrium state. | Positive; extrapolation flag required. |
| pressure | float64 | Pa | Declared environmental pressure. | Vacuum limit branch explicit. |
| interaction_covariance | matrix<float64> | (J/mol)^2 | Fitted excess-parameter covariance. | Symmetric positive semidefinite; unknown null. |
| phase_amounts | vector<float64> | mol | Named phase solution. | Absent phase zero; solver failure null. |
| reflectance | nullable<vector<float64>> | 1 | Instrument-band observation/prediction. | Wavelength and response version required. |
| sublimation_flux | vector<float64>[3] | kg m^-2 s^-1 | Signed outward mass flux. | Missing null, never substituted zero. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [New Horizons Planetary Data System archive](https://pds-smallbodies.astro.umd.edu/data_sb/missions/newhorizons/index.shtml) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Published solid-phase equilibrium study](https://academic.oup.com/mnras/article/474/3/4254/4657184) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)

## Included evidence to explore

![A02 included data diagnostic](../../../../data/figures/16_ideal_binary_phase_regions.svg)

Equilibrium phase regions inferred from the existing ideal-binary liquidus model with invented melting temperatures and fusion enthalpies. Above the liquidus the material is liquid; between the liquidus and eutectic temperature it is liquid plus the indicated pure solid; below the eutectic it is A and B solids. The region labels follow the model assumptions and are not predictions for Pluto's real volatile mixtures.

[Data atlas: tables, model definitions and provenance](../../../../data/README.md). Shared reduced-model evidence has a narrower domain than this project contract.
