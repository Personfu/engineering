# I04 · Data blueprint

[ORION SENTINEL CORE](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![I04 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| task_spec | struct | s | C,blocking,period,deadline and priority. | Measured/bounded status; task blocking not buffer bytes. |
| task_trace | table | s | Release/start/end and missed deadlines. | Monotonic clock/reset generation recorded. |
| science_record | struct | bytes, sequence | Authoritative sample payload and checksum. | Unique source ID; missing sample explicitly marked. |
| buffer_state | uint64 | byte | Committed plus queued occupancy. | Capacity/loss counters; no silent wrap. |
| fault_event | enum+time | 1, s | Lane/voter/clock/memory/power emulator event. | Fault scope and independence assumption explicit. |
| operational_state | enum | 1 | Boot/science/safe/recovery state. | Transition cause and valid-service flag. |
| timing_uncertainty | distribution<struct> | s | Clock/WCET/jitter uncertainty. | Retain shared-clock correlations. |
| availability_recovery | measurement<struct> | 1, s | Science fraction and recovery latency. | Exclude invalid records from useful service. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [NASA small-spacecraft avionics reference](https://www.nasa.gov/smallsat-institute/sst-soa/small-spacecraft-avionics/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Proposed local test-bench trace dataset](https://www.nasa.gov/reference/systems-engineering-handbook/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
