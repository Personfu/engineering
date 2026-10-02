# B14 · Data blueprint

[PHOENIX INFILTRATION — Postfire Soil Recovery Observatory](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![B14 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| plot_key | string | none | Repeated measurement plot identity. | Burn/terrain provenance required. |
| elapsed_time | float[] | hour | Time since infiltration start. | Monotone; transient window recorded. |
| cumulative_depth | float[] | mm | Volume/contact-area conversion. | Monotone within error; area uncertainty saved. |
| imposed_tension | float | mm head | Device pressure-head condition. | Sign convention and geometry required. |
| sorptivity | float[] | mm/hour^0.5 | Fitted early-time uptake coefficient. | Covariance with late-time coefficient retained. |
| antecedent_moisture | nullable float | m³/m³ | Initial volumetric soil water. | Bounds and measurement method required. |
| soil_carbon | nullable float | mass fraction | Linked carbon assay. | Date/method covariance saved. |
| hydraulic_covariance | matrix | mixed | Joint fitted hydraulic uncertainty. | Separate device, plot and scale terms. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [2021 Arizona NASA Space Grant symposium booklet](https://spacegrant.arizona.edu/sites/spacegrant.arizona.edu/files/AZSGC%20Symposium%20Booklet%202021_website.pdf) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Guidance for parameterizing post-fire hydrologic models with in situ infiltration measurements](https://experts.arizona.edu/en/publications/guidance-for-parameterizing-post-fire-hydrologic-models-with-in-s/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)

## Included evidence to explore

[Data atlas: tables, model definitions and provenance](../../../../data/README.md). Shared reduced-model evidence has a narrower domain than this project contract.
