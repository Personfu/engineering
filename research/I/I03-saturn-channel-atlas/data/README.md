# I03 · Data blueprint

[SATURN CHANNEL ATLAS](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![I03 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| family_parameters | float64[dimensionless] | 1 | Normalized aspect/curvature/roughness/topology. | Domain bounds and reference geometry documented. |
| budget_type_value | struct | W or kg s^-1 | Held-constant pump/flow comparison. | Do not mix budgets in one ranking. |
| transport_properties | measurement<struct> | kg m^-3, Pa s, W m^-1 K^-1 | Fluid properties in accepted temperature range. | Source and validity recorded. |
| correlation_record | struct | 1 | Nu/friction/loss formulas and regimes. | Darcy/Fanning and developing-flow status explicit. |
| heat_envelope | measurement<array> | W m^-2 | External or known electrical boundary load. | Spatial/temporal covariance; no combustion schedule. |
| pressure_flow | measurement<float64[2]> | Pa, m^3 s^-1 | Hydraulic observations/predictions. | Branch and sensor covariance retained. |
| temperature_field | distribution<array> | K | Wall/coolant thermal response. | Masked sensor locations remain missing. |
| pareto_record | table | 1, W or scaled | Expected/CVaR temperature and pump objectives. | Nondominated status includes uncertainty and scale version. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [NASA cooling analysis reference](https://ntrs.nasa.gov/api/citations/19810012596/downloads/19810012596.pdf) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Proposed normalized inert-coupon library](https://www.nasa.gov/smallsat-institute/sst-soa/structures-materials-and-mechanisms/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
