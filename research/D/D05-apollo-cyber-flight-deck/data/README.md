# D05 · Data blueprint

[APOLLO CYBER FLIGHT DECK](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![D05 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| exercise_id | string | 1 | Isolated replay configuration. | Synthetic-only flag and fixture hash required. |
| report_id | string | 1 | Unique information record. | Append-only; edits create revisions. |
| confidence | enum | 1 | Declared provenance confidence. | Unknown explicit; never inferred from urgency. |
| audience_policy | set<role> | 1 | Permitted synthetic sharing roles. | Empty or missing blocks onward sharing. |
| owner_role | nullable<string> | 1 | Responsible triage/escalation role. | Unassigned remains null and flagged. |
| stage_timestamps | record | s | Exercise intake/decision/recovery times. | Clock/version and censoring required. |
| ground_truth_labels | record | 1 | Fixture routing/safety labels. | Locked before exercise; scorer separated. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [Aviation ISAC public information](https://www.a-isac.com/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
