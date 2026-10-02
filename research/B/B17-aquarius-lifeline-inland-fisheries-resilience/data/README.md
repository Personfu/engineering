# B17 · Data blueprint

[AQUARIUS LIFELINE — Inland Fisheries Resilience](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![B17 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| basin_key | restricted string | none | Consented geographic study identity. | Partner authority and scope required. |
| harvest_mass | nullable float | kg/interval | Reported species-group catch. | Coverage and informal-catch uncertainty retained. |
| effort | nullable float | fisher-days | Declared fishing effort. | Gear and access changes documented. |
| aquatic_exposure | nullable record | °C m³/s days | Hydrologic ecological drivers. | Covariance and seasonal support saved. |
| dependence_fraction | nullable float | 0–1 | Approved dietary or income dependence. | Basis/time period explicit. |
| adaptation_cost | float[] | local currency/year | Locally feasible scenario cost. | Price year and distribution retained. |
| release_permission | structured policy | none | Allowed purpose, linkage and aggregation. | Revocation and local standards honored. |
| loss_distribution | float[] | declared | Scenario adaptation outcome ensemble. | Weights and unavailable pathways disclosed. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [FAO impacts of climate change on fisheries and aquaculture](https://www.fao.org/family-farming/detail/en/c/1145404/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [FAO vulnerability of fishing-dependent economies to disasters](https://www.fao.org/4/i3328e/i3328e00.htm) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
