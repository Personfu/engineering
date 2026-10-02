# C25 · Data blueprint

[ORION BURST SENTINEL](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![C25 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| noise_interval | struct<GPS,mask> | s | Quality-qualified released strain interval. | Training/validation/test role immutable. |
| whitened_tiles | complex128[nt,nf,k] | declared normalized | Network time-frequency coefficients. | PSD/window conventions and gap masks required. |
| trial_response | float64[k,2] | 1 | Whitened sky/polarization response. | Condition number and network rank recorded. |
| ranking_score | float64 | 1 or declared | Frozen baseline/ML search statistic. | Threshold/model version attached. |
| background_exposure | float64 | s | Effective valid background time. | Shift dependence and exclusions documented. |
| injection_truth | struct | kpc, degree, s | Waveform, sky, orientation and event time. | Physical-family split key required. |
| efficiency | struct<float64,interval> | 1 | Detected fraction by distance/family/network. | N/k and grouped uncertainty retained. |
| trigger_window | struct&#124;null | GPS s | Independent multimessenger search interval. | Null gives untriggered search; association provenance mandatory. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [GWOSC strain](https://gwosc.org/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [CCSN deep-learning search study](https://arxiv.org/abs/2001.00279) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
