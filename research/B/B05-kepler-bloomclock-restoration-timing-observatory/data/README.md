# B05 · Data blueprint

[KEPLER BLOOMCLOCK — Restoration Timing Observatory](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![B05 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| phenophase_status | enum | none | present, absent or unknown. | Unknown never treated as absence. |
| onset_bounds | nullable date[2] | calendar day | Observed timing interval. | Store one-sided censoring. |
| daily_temperature | nullable float | °C | Local mean temperature. | Coverage and timezone required. |
| base_temperature | float | °C | Species thermal threshold. | Provenance or scenario tag required. |
| bloom_probability | float[] | none | Weekly flowering ensemble. | Bounds 0–1; joint covariance saved. |
| establishment_fraction | float[] | none | Scenario survival to resource provision. | No default perfect survival. |
| resource_shortfall | float[] | resources/week | Demand minus realized floral proxy. | Demand assumptions linked. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [USA National Phenology Network observational data](https://nn.usanpn.org/data/observational) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [USGS managing to survive despite the weather: seeding decisions](https://www.usgs.gov/publications/managing-survive-despite-weather-seeding-decisions-affecting-simulated-dryland) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
