# B25 · Data blueprint

[SEEDSTAR GENESIS — Dryland Establishment Forecasting](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![B25 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| seed_lot | string | none | Species-linked batch identity. | Viability and storage provenance required. |
| seed_mass | nullable float | mg | Measured lot/species trait. | Method and lot variance retained. |
| viability_fraction | nullable float | 0–1 | Independent viable-seed estimate. | Assay/follow-up uncertainty saved. |
| stage_time | nullable record | days | Germination/emergence/survival event bounds. | Stage-specific censoring required. |
| water_potential | nullable float[] | MPa | Microsite moisture history. | Negative-pressure convention explicit. |
| pellet_key | string | none | Documented material/process identity. | No unmeasured mechanism inferred. |
| transition_covariance | matrix | probability² | Joint stage uncertainty. | Shared lot/weather correlations retained. |
| establishment_cost | nullable float[] | USD/plant | Cost distribution at stated horizon. | Zero-success and price year explicit. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [Developing extruded seed pellets to overcome hydrophobicity and emergence barriers](https://besjournals.onlinelibrary.wiley.com/doi/full/10.1002/2688-8319.12024) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [USGS managing to survive despite the weather: seeding decisions](https://www.usgs.gov/publications/managing-survive-despite-weather-seeding-decisions-affecting-simulated-dryland) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
