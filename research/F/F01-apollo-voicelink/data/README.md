# F01 · Data blueprint

[APOLLO VOICELINK](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![F01 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| team_id | string | 1 | Pseudonymous clustered team key. | Identity mapping outside analysis; consent status required. |
| task_id | string | 1 | Versioned analog task/rubric. | Difficulty and crossover order retained. |
| protocol_assignment | enum | 1 | Communication structure condition. | Randomization/carryover record required. |
| message_times | record | s | Create/deliver/acknowledge simulator times. | Clock and imposed-delay separation. |
| context_metadata | nullable<record> | 1 | Consented language/experience context. | Minimum necessary; no deterministic cultural labeling. |
| repair_outcome | record | bool,s | Rubric success and resolution/censoring. | Coder IDs and evidence links retained. |
| code_agreement | record | 1 | Independent labels/agreement summary. | Disagreement and undefined metrics retained. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [NASA delayed team communication research](https://techport.nasa.gov/projects/23197) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [NASA educational outreach evaluation framework](https://ntrs.nasa.gov/citations/20000033841) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
