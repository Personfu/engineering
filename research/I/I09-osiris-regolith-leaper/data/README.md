# I09 · Data blueprint

[OSIRIS REGOLITH LEAPER](../README.md) · [Figure gallery](../figures/README.md) · [Data atlas](../../../../data/README.md)

![I09 proposed field inventory](../figures/data-map.svg)

**PROPOSED CONTRACT · 8 fields · no project observations acquired.** The acquisition CSV contains column headers only. The diagram is a visual record specification, not measured data.

| Download | What it contains |
| --- | --- |
| [Acquisition CSV](acquisition.csv) | Empty columns ready for controlled acquisition |
| [Field dictionary](dictionary.csv) | Names, source types, units, meanings and quality rules |
| [JSON Schema](schema.json) | Nullable record structure with unit and quality metadata |

## Field reference

| Field | Type | Unit | Meaning | Quality / missingness |
| --- | --- | --- | --- | --- |
| body_manifest | struct | m, kg, rad s^-1 | Shape/mass/spin and frame. | Independent gravity/density source required. |
| terrain_case | struct | m, radian | Local geometry and seeded obstacles. | Prior/support and OOD flags. |
| robot_state | float64[] | m, m s^-1, radian | Translation and attitude/rate. | Quaternion convention/norm or rotation matrix validity. |
| contact_parameters | distribution<struct> | 1, N or J | Restitution/friction and optional cohesion. | Passive-domain constraints; unsupported parameters marked. |
| actuation_contract | enum+limits | N s, N m s | Foot or momentum-exchange bounds. | No cross-concept default assumptions. |
| wheel_momentum | float64[] | kg m^2 s^-1 | Available/stored wheel state. | Limit and saturation events retained. |
| trajectory_cov | distribution<trace> | mixed state | Gravity/contact/terrain ensemble. | Missing contact events flagged; correlated draws preserved. |
| hop_outcome | struct<bool,float> | 1 | Boundedness, landing validity, science gain. | Definition/version and ensemble count attached. |

## Acquisition and provenance

Null means missing or unknown; record its cause. Preserve product identifier, retrieval timestamp, source hash, calibration, coordinate and time frame, covariance basis, selection rules and every transformation. JSON Schema checks structure; physical bounds and the quality rules above require domain validation.

- [JPL Hedgehog research overview](https://www.jpl.nasa.gov/news/hedgehog-robots-hop-tumble-in-microgravity/) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Hari et al. (2026) hopper preprint](https://arxiv.org/abs/2603.10670) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.
- [Proposed small-body scenario manifest](https://naif.jpl.nasa.gov/naif/tutorials.html) — archive or acquisition resource; inclusion here does not assert that its data have been retrieved.

[Controlled data-management procedure](../../../../engineering/DATA_MANAGEMENT.md)
