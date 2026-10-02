# H05 · Data blueprint

[TERRA SEVEN GENERATIONS](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![H05 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| data_authority | policy record | none | Tribal ownership/access/interpretation rules. | Local standards and revocation retained. |
| action_key | string | none | Approved planning option/source. | Feasibility and review status required. |
| daily_air_temperature | nullable float | °C | Observed or scenario Tmax. | Measurement type/calendar explicit. |
| heat_threshold | float | °C | Locally selected planning threshold. | Approval/rationale and version saved. |
| heat_indicators | record | days/year | Exceedance/run-length ensemble. | Missing-day and native-calendar support retained. |
| hazard_layer | nullable geometry | declared | Burn/vegetation/exposure support. | Scale and sensitive-site restrictions saved. |
| implementation_scenario | record | none | Staffing/power/funding conditions. | Assumptions not labeled measured. |
| regret_distribution | float[]/ordinal | declared loss units | Action tradeoffs across scenarios. | Weights/consequence uncertainty and approval explicit. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [ITEP Tribal Hazard Mitigation Planning cohort account](https://itep.nau.edu/wp-content/uploads/2024/07/tribes_ntnlTHMPC.pdf) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [NASA NEX-GDDP-CMIP6](https://www.nccs.nasa.gov/data-collections/nex-gddp-cmip6/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
