# B23 · Data blueprint

[HYDRA MISSION CONTROL — Watershed Decisions Under Uncertainty](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![B23 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| gauge_key | string | none | Station and rating-version identity. | Station changes and qualifiers retained. |
| discharge | nullable float | m³/s | Observed reference flow. | Rating/measurement uncertainty saved. |
| catchment_area | float | m² | Depth-volume conversion support. | Boundary version and positivity checked. |
| forcing_vector | nullable record | mm/day | Precipitation/ET/deep-loss terms. | Coverage and covariance retained. |
| issued_at | datetime | UTC | Forecast creation/availability time. | No future observations in replay. |
| forecast_ensemble | float[][] | m³/s or mm | Dated horizon-member states. | Member dependence and model key recorded. |
| loss_parameters | record | declared currency/service units | Stakeholder action consequences. | Approval/version and uncertainty explicit. |
| decision_regret | float[] | same as loss | Held-out policy performance. | Oracle comparator limited to scoring. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [USGS Water Data API documentation](https://api.waterdata.usgs.gov/docs/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [USGS hydrologic drought decision support system](https://pubs.usgs.gov/of/2014/1003/pdf/ofr2014-1003.pdf) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)

## Included evidence to explore

![B23 included data diagnostic](../../../../data/figures/12_hydrologic_water_ledger.svg)

Synthetic reservoir fluxes and cumulative water accounting. Recharge means effective water entering storage, rather than rainfall. Panel B decomposes all accounted water into cumulative release and remaining storage, bounded by initial storage plus accumulated recharge. The tiny arithmetic residual verifies this implementation's conservation, not watershed predictive accuracy.

[Data atlas: tables, model definitions and provenance](../../../../data/README.md). Shared reduced-model evidence has a narrower domain than this project contract.
