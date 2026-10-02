# A04 · Data blueprint

[APOLLO SWARM SENTINEL](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![A04 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| particle_id | uint32 | 1 | Stable simulated node. | Generation ID prevents identity reuse. |
| axial_position | pair<int32> | lattice step | Hex coordinates. | Neighbor ports match offsets. |
| activation_index | uint64 | event | Scheduler sequence. | Increasing; fairness metadata required. |
| sensor_symbol | nullable<enum> | 1 | Bounded sensor alphabet. | Missing distinct from target absent. |
| message_state | enum | 1 | Finite transition message. | Alphabet version and direction required. |
| provenance_id | string | 1 | Offline observation origin. | Deduplicate before oracle accumulation. |
| declaration | record | 1 | Node, event and decision. | Confidence null if uncalibrated. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [ASU Self-Organizing Particle Systems research framework](https://labs.engineering.asu.edu/sops/amoebot/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Generated target/noise benchmark](https://arxiv.org/abs/2205.15412) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
