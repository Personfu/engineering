# B04 · Data blueprint

[AURORA VEIL — Ionospheric Absorption Atlas](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![B04 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| platform | enum | none | ground, spacecraft or unresolved. | No spacecraft claim from title. |
| power_raw | nullable float | W or relative | Measured receiver power. | Positive; retain saturation/RFI flags. |
| frequency | float | Hz | Verified receiver channel. | Positive; bandwidth recorded. |
| sidereal_phase | float | rad | Site-relative cosmic-noise phase. | Derived from site and UTC convention. |
| quiet_power | float | same as power | Estimated undisturbed baseline. | Covariance and excluded days retained. |
| path_geometry | structured record | m rad | Antenna/ray weighting definition. | Null blocks link inference. |
| absorption | nullable float | dB | Power-ratio absorption estimate. | Carry baseline covariance and quality mask. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [Spectral characteristics of high-latitude raw 40 MHz cosmic noise signals](https://npg.copernicus.org/articles/23/215/2016/npg-23-215-2016.html) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [NOAA D-Region Absorption Prediction model archive](https://www.ncei.noaa.gov/products/space-weather/ionospheric-program/d-region-absorption-prediction) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
