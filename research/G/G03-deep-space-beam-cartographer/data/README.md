# G03 · Data blueprint

[DEEP SPACE BEAM CARTOGRAPHER](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![G03 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| configuration_id | string | 1 | Installed/antenna-alone state. | Mount, cabling and surroundings version required. |
| frequency | float64 | Hz | Measurement frequency. | Positive; bandwidth and wavelength convention. |
| angular_coordinate | pair<float64> | rad | Azimuth/elevation in station frame. | Axes/signs and encoder covariance. |
| polarization_basis | enum | 1 | Co/cross or declared linear/circular basis. | Basis transform version required. |
| complex_field | nullable<complex128> | native | Near-field phase/amplitude sample. | Phase reference required; power-only flagged. |
| calibration_ledger | record | dB,rad | Gain/loss/phase corrections. | Shared error terms and drift retained. |
| system_temperature | nullable<float64> | K | Receive-system noise temperature. | Measurement boundary required; absent means no G/T. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [NASA JPL MESA antenna-range technical information](https://www.nasa.gov/jpl/mesa/antenna-range/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [NASA JPL outdoor-range information](https://www.nasa.gov/jpl/mesa/facilities/outdoor-ranges/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
