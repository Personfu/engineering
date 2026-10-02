# C11 · Data blueprint

[ORION CORE INFERENCE](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![C11 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 7 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| simulation_id | string | 1 | Unique physical model/progenitor identifier. | Independent of injection seed; required split key. |
| polarizations | float64[n,2] | strain | Reference-distance waveform. | Reference distance and extraction convention required. |
| network_epoch | int64 | GPS second | Injection/noise origin. | Time conversions pinned; gaps masked. |
| noise_psd | float64[nf,k] | strain^2 Hz^-1 | Local one-sided detector PSD. | Positive, frequency support recorded. |
| physics_metadata | struct | mixed declared | Transport, EOS, resolution, progenitor. | Unknown fields explicit; never inferred from file name. |
| track_parameters | posterior<struct> | Hz, Hz s^-1, s | Observable chirplet/frequency-track quantities. | Covariance and multimodality retained. |
| physical_target | posterior<struct>&#124;null | declared | Simulation-conditioned stellar/remnant quantity. | Null under unsupported-domain flag. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [GWOSC released strain](https://gwosc.org/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Published CCSN model studies](https://arxiv.org/abs/2201.01397) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
