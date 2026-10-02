# B20 · Data blueprint

[LUNAR RECLAIMER — Algal Rare-Earth Recovery](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![B20 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| element_symbol | enum/string | none | Actual analyzed target or competitor. | Y and Al never conflated. |
| feed_concentration | nullable float | mg/L | Element-specific feed measurement. | Method/limit/recovery required. |
| residual_concentration | nullable float | mg/L | Element-specific dissolved endpoint. | Censoring and matrix effects retained. |
| dry_sorbent_mass | float | g | Dry biomass/media amount. | Moisture correction uncertainty saved. |
| matrix_composition | nullable vector | mg/L | Competing-ion observations. | Species/assay covariance retained. |
| product_mass | nullable vector | mg element | Measured recovered product. | Null prohibits recovery/purity claim. |
| cycle_index | integer | none | Linked reuse cycle identity. | Product/waste lineage required. |
| mass_covariance | matrix | mg² | Joint feed/pool analytical uncertainty. | Include shared dilution and recovery bias. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [Recovering rare earth elements via immobilized red algae from ammonium-rich wastewater](https://pmc.ncbi.nlm.nih.gov/articles/PMC9500351/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Desorption of rare earth elements biosorbed on Euglena mutabilis suspensions and biofilms](https://onlinelibrary.wiley.com/doi/10.1002/cjce.25344) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
