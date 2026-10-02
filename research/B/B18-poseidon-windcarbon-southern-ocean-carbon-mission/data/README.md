# B18 · Data blueprint

[POSEIDON WINDCARBON — Southern Ocean Carbon Mission](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![B18 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| platform_key | string | none | Ship/float/profile identity. | Calibration and data-level provenance required. |
| pco2_water | nullable float | microatm | Measured/derived surface pCO2. | Input covariance and method retained. |
| wind_speed | nullable float | m/s | Declared transfer-law wind average. | Vector averaging/cadence explicit. |
| solubility | float | mol/m³/atm | Temperature/salinity-dependent K0. | Formula/version and covariance saved. |
| transfer_velocity | float[] | m/s | Gas-transfer formulation ensemble. | Validity domain and wind source retained. |
| mixed_layer_depth | nullable float | m | Inventory support depth. | Definition and profile uncertainty required. |
| air_sea_flux | nullable float | mol C/m²/s | Signed ocean-to-air exchange. | No sign inversion during integration. |
| coverage_covariance | record | mixed | Area-time support and joint flux error. | Gap-fill covariance separate from observations. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [NOAA OCADS SOCCOM cruise data](https://www.ncei.noaa.gov/access/ocean-carbon-acidification-data-system/oceans/SOCCOM/SOCCOM.html) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Extratropical storms induce carbon outgassing over the Southern Ocean](https://www.nature.com/articles/s41612-024-00657-7) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Copernicus ERA5 hourly single-level time-series data](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels-timeseries?tab=download) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
