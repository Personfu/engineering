# E04 · Data blueprint

[AURA VERTICAL](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![E04 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| species_basis | record | 1 | CO2/CH4 and dry/wet calibration scale. | Selective analyzer evidence required. |
| gas_reading | nullable<float64> | mol/mol | Native calibrated mole fraction. | ppm/ppb conversion explicit; missing null. |
| water_fraction | nullable<float64> | mol/mol | Compatible water mole fraction. | Between zero and one; unknown blocks conversion. |
| pressure_temperature | record | Pa,K | Analyzer/environment state. | Calibration domain and covariance retained. |
| flight_position | record | m,degree | Altitude/geolocation at timestamp. | Reference datum and horizontal drift retained. |
| response_time | nullable<float64> | s | Transport/sensor lag tau. | Positive and independently sourced or latent flagged. |
| profile_covariance | matrix<float64> | (mol/mol)^2 | Joint profile/measurement uncertainty. | Shared scale/humidity terms retained. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [NOAA greenhouse-gas data](https://gml.noaa.gov/ccgg/data/getdata.php?gas=co2) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [NOAA aircraft CO2 data dictionary](https://erddap.gml.noaa.gov/erddap/info/greenhouse_gases_co2_aircraft_insitu_10_second_values/index.html) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
