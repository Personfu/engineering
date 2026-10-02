# C21 · Data blueprint

[PARKER MAGNETIC TRAIL](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![C21 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| epoch | int64/float64 | CDF-declared time | Sample time with leap/time metadata. | Monotonic; adapter performs documented conversion. |
| magnetic_rtn | float64[n,3] | nT | Field in radial-tangential-normal coordinates. | Coordinate definition and quality flags required. |
| plasma_velocity | float64[m,3]&#124;null | km s^-1 | Compatible plasma moments. | Missing cadence remains separate; no forward-fill across gaps. |
| mass_density | measurement<float64>&#124;null | kg m^-3 | Density for Alfvén-speed calculation. | Composition approximation and positive support. |
| reference_field | float64[n,3] | nT | Robust local background. | Window/configuration and excluded events recorded. |
| event_interval | struct<time,time> | s | Start/end of detected interval. | Gap boundaries split events. |
| alfvenicity | measurement<float64>&#124;null | 1 | Declared velocity/field relation metric. | Null for inadequate plasma overlap. |
| exposure_mask | bool[n] | 1 | Usable time for each classification. | Cadence-weighted interval duration; gaps excluded. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [NASA CDAWeb/SPDF PSP discovery](https://cdaweb.gsfc.nasa.gov/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [FIELDS team resident archive](https://fields.ssl.berkeley.edu/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
