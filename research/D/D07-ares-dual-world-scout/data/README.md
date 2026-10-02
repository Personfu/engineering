# D07 · Data blueprint

[ARES DUAL-WORLD SCOUT](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![D07 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| concept_id | string | 1 | Earth or Mars architecture/version. | Environment and external delivery boundary explicit. |
| environment_profile | record | SI | Density, viscosity, gravity and sound speed. | Source/domain and covariance retained. |
| trajectory_state | array<time,position,attitude> | s,m,rad | Concept sensing path. | Frame and time origin required. |
| aero_envelope | record | 1 | Supported coefficient/Re/M range. | No extrapolated capability treated validated. |
| sensor_geometry | record | m,s | Pixel pitch, focal length and exposure. | Calibration/resolution requirement included. |
| subsystem_power | array<record> | W | Time-resolved load ledger. | Missing support load flagged, not zero. |
| return_event_tree | record | 1 | Deployment/acquisition/communication dependencies. | Probability provenance or TBD status required. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [NASA ARES mission-concept research](https://ntrs.nasa.gov/citations/20080030375) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [NASA systems-engineering resource](https://www.nasa.gov/reference/systems-engineering-handbook/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
