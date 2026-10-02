# C29 · Data blueprint

[ACE WIND SHOCK LEDGER](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![C29 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| event_epoch | float64 | CDF-declared time | Shock candidate and window boundaries. | Time conversions and masks recorded. |
| plasma_state | measurement<struct> | kg m^-3, m s^-1, Pa | Density/velocity/thermal pressure. | Composition/temperature convention and covariance. |
| magnetic_vector | measurement<float64[3]> | T | Field in common coordinates. | Coordinate transform and instrument offsets retained. |
| proton_intensity | measurement<float64[nE,nangle]> | m^-2 s^-1 sr^-1 J^-1 | Response-corrected differential flux. | Energy/pitch-angle bounds; invalid channels absent. |
| shock_geometry | posterior<struct> | 1, m s^-1 | Unit normal and shock speed. | Normal orientation and method identities. |
| particle_budget | posterior<float64[2]> | Pa, J m^-3 | Finite-band pressure and energy density. | Isotropy assumption and integration bounds attached. |
| energy_flux | posterior<float64[terms]> | W m^-2 | MHD and particle components. | Shared frame/covariance and unknown Q state. |
| band_fraction | posterior<float64>&#124;null | 1 | Conditional Delta particle/upstream flux. | Never labeled full efficiency without closure evidence. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [NASA CDAWeb ACE/Wind discovery](https://cdaweb.gsfc.nasa.gov/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [David et al. energy-budget studies](https://arxiv.org/abs/2202.11029) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
