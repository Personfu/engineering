# I07 · GATEWAY CATSAT CONSOLE

**Original project:** CatSat Groundstation Command and Control

**Session I:** Aerospace Technology

**Document class:** engineering research design and analysis record · **Revision:** 4 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session I](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_I.md) · [← I06](../I06-saturn-loadpath/README.md) · [I08 →](../I08-voyager-frameforge/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 6 | 4 | 8 | 2 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Mission profile

![I07 engineering mission profile: scientific question, hypothesis, model scope and evidence status](figures/mission-profile.svg)

| Profile panel | Engineering signal | Open the evidence |
| --- | --- | --- |
| Mission identity | CatSat Groundstation Command and Control | [Scientific objective](#purpose-and-scientific-objective) |
| Model cockpit | 4 governing expressions; 4 derivation steps; declared assumptions and validity envelope | [Mathematical formulation](#4-mathematical-model-and-derivation) |
| Data blueprint | 8 proposed fields with types, units and quality rules | [Field map & downloads](data/README.md) |
| Verification queue | 6 proposed requirements; 4 specified cases; project execution evidence pending | [Case definitions](#8-verification-and-validation-cases) |
| Figure wall | Architecture, field map, planned result description | [Open full gallery](figures/README.md) |
| Resource library | 2 cited primary resources with support statements | [Cited resources](#12-cited-technical-and-scientific-resources) |

### Model cockpit

**Analysis method:** Define a versioned telemetry dictionary, event ledger, and abstract state machine for simulated commissioning and routine image collection. Build a local packet-replay service with reproducible loss, delay, duplication, and reset patterns. Use Open MCT as an optional visualization framework while keeping telemetry ingestion and reconstruction independently testable. Display source time, receive time, freshness, uncertainty, and provenance beside every engineering value. Reassemble synthetic images using chunk identifiers and integrity checks; diagnose incomplete transfers from the manifest rather than treating a successful socket read as completed science delivery. Evaluate operator tasks using randomized scenario order, including cases where the correct answer is that current state cannot be established.

**Operating envelope:** A public operations description is not an interface-control document or authorization to command CatSat. Local replay verifies software behavior and operator interpretation, not radio-link performance or mission readiness.

**Variables and conventions**

- Buffer B and produced image/data size S in bytes; useful downlink capacity C in bytes s^-1; interval dt in s.
- Telemetry age A in s refers to source-valid time, distinct from reception time; clock uncertainty is included.
- Completeness fraction counts valid unique chunks; expected chunk count comes from a trusted synthetic manifest.
- State s and event e are abstract simulator records. Real radio commands, frequencies, credentials, and flight protocols are outside this package.

### Artifact wall

![I07 proposed analysis architecture](figures/architecture.svg)

All interfaces are owned synthetic records; manifest integrity, timestamp evidence and idempotent reconstruction precede operator display.

**Scientific result to produce:** A pass timeline, freshness-aware telemetry panel, and synthetic image-chunk map that reveal gaps and delayed events without implying live spacecraft control.

### Investigation feed · planned work

The feed records proposed work packages. A row becomes executed evidence only with versioned inputs, outputs and a reviewed result.

| Sequence | Evidence state | Engineering work package |
| --- | --- | --- |
| 01 | Planned | Define synthetic telemetry dictionary, event IDs and image manifests. |
| 02 | Planned | Implement isolated replay with seeded delay/loss/duplicate/reset patterns. |
| 03 | Planned | Build idempotent state ledger and checkpoint recovery. |
| 04 | Planned | Implement manifest-based image assembly and clock-aware freshness. |
| 05 | Planned | Connect optional operator view only to reconstructed contracts. |
| 06 | Planned | Release expected-state fixtures and randomized unknown-state operator scenarios. |

### Mission connections

Connections are reading routes based on actual shared resources, supplied sessions or included illustrations. They do not establish physical dependencies, team collaborations or validated results.

| Connected mission | Original investigation | Recorded connection basis |
| --- | --- | --- |
| [E01 · APOLLO HELIOSCOPE](../../E/E01-apollo-helioscope/README.md) | Phoenix College: Video Streaming and DNA Studies | [NASA AMMOS Open MCT](https://ammos.nasa.gov/openmct/) |
| [I06 · SATURN LOADPATH](../I06-saturn-loadpath/README.md) | Designing and Exploring the Structure of Launch Vehicles to Create Optimal Theoretical and Small-Scale Experimental Models | Session I |
| [I08 · VOYAGER FRAMEFORGE](../I08-voyager-frameforge/README.md) | Julia 1.2 Ephemeris and Gravitational Modeling Development | Session I |
| [I05 · PIONEER AERODRIFT](../I05-pioneer-aerodrift/README.md) | Pico Balloon Platform for Atmospheric Exploration | Session I |
| [I09 · OSIRIS REGOLITH LEAPER](../I09-osiris-regolith-leaper/README.md) | Simulation and Evaluation of a Mechanical Hopping Mechanism for Robotic Small Body Surface Exploration | Session I |
| [I04 · ORION SENTINEL CORE](../I04-orion-sentinel-core/README.md) | EagleSat Team: On-board Computer Subsystem | Session I |

[Machine-readable connection register and ranking rule](../../../registry/mission_connections.json)

### Reading playlist

| Route | Start here | Continue to |
| --- | --- | --- |
| Understand the idea | [Scientific objective](#purpose-and-scientific-objective) | [Design boundary](#1-design-basis-and-analysis-boundary) → [Mathematics](#4-mathematical-model-and-derivation) |
| Inspect the data | [Visual blueprint](data/README.md) | [Provenance](#5-data-specifications-and-provenance) → [Uncertainty](#6-uncertainty-sensitivity-and-identifiability) |
| Make a design decision | [Trade study](#7-engineering-trade-study) | [Failure modes](#10-failure-modes-and-interpretation-controls) → [Required outputs](#11-required-engineering-outputs) |
| Prepare execution | [Requirements](#2-requirements-and-verification-traceability) | [Verification](#8-verification-and-validation-cases) → [Implementation](#9-implementation-and-reproducible-work-packages) |

## Complete engineering dossier

The profile above is a browsing layer. The full design basis, equations, derivations, data contract, uncertainty, trades and controlled case definitions follow.

## Purpose and scientific objective

Extend CatSat ground-station work into a reproducible operations console that connects image downlink, health telemetry, pass planning, and human decision records. The current University of Arizona concept of operations provides mission context; the historical FlatSat integration objective is preserved as a local simulator. All requests and state transitions in this research package are simulated. A mission-owner-approved adapter and operational review would be required before any actual spacecraft interaction.

**Question:** Can operators accurately reconstruct spacecraft and image-transfer state when packets arrive late, out of order, with gaps, or across a simulated restart?

**Testable hypothesis:** An event-sourced console with explicit stale-data indicators and state preconditions will reduce incorrect operator conclusions compared with a display that only shows the latest value.

## 1. Design basis and analysis boundary

The CatSat operations package is an isolated local FlatSat/event-replay simulator. Its boundary contains synthetic health telemetry, inert images, pass-capacity scenarios and abstract operator requests. It cannot contact a live station or spacecraft and contains no real command/radio protocol, credentials or target. Public CatSat operations context supplies research continuity, not operational authorization or an interface-control document.

Begin with deterministic event reconstruction and image manifests, then loss/reorder/reset scenarios and operator-state interpretation. Science validity is distinct from transport receipt. Open MCT is an optional view over independently tested state reconstruction. The operator can correctly conclude that current state is unknown; stale telemetry must not appear fresh because it arrived recently.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| I07-R1 | The simulator shall expose no live-radio/mission adapter or external command transport. | The executable scope is owned synthetic replay. | Dependency/configuration and network-isolation integration check. | Proposed simulator-only boundary. |
| I07-R2 | Every engineering value shall retain source-valid time, receive time, quality and clock uncertainty. | Delayed packets can look current. | Synthetic delay/freshness fixture. | Proposed state-provenance contract. |
| I07-R3 | Image completeness shall count valid unique chunks against a trusted synthetic manifest. | Duplicate receipts do not add science. | Duplicate/corrupt/missing chunk replay. | Proposed integrity requirement. |
| I07-R4 | Abstract request handling shall be idempotent across restart and repeated event IDs. | Replay must reconstruct one authoritative state. | Checkpoint/replay state equivalence test. | Proposed event contract. |
| I07-R5 | Freshness thresholds shall be versioned per field; stale or missing values shall produce unknown/stale states. | One global timer cannot establish all subsystem states. | Threshold and missing-data scenario audit. | Proposed operator evidence requirement. |
| I07-R6 | Operator assessment shall include scenarios where state cannot be established. | Always choosing a state rewards false certainty. | Randomized synthetic-task scoring with unknown answer. | Proposed human-factors validation. |

## 3. Architecture and controlled interfaces

A synthetic scenario manifest defines expected measurements, image chunks, clock errors and abstract events. An isolated replay service applies loss, delay, duplication, corruption and restart patterns. The event ledger records source and receive timestamps with immutable IDs. State reconstruction uses source ordering and quality rules, while request-state transitions are abstract local simulator functions.

The image assembler validates checksum/ID and compares unique chunk sets with the manifest. A freshness service evaluates each telemetry field under clock uncertainty. The operator view consumes these reconstructed contracts and shows unknown/stale evidence states. A test harness compares complete replay with restarted/delayed runs independently of the visualization framework.

![I07 engineering architecture](figures/architecture.svg)

All interfaces are owned synthetic records; manifest integrity, timestamp evidence and idempotent reconstruction precede operator display.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

$$
B_{n+1}=\max(0,B_n+S_n-C_n\Delta t_n)
$$

$$
A_j=t_{\rm now}-t_{{\rm valid},j}
$$

$$
f_{\rm complete}=N_{\rm unique\ valid}/N_{\rm expected}
$$

$$
s_{n+1}=F(s_n,e_n);\quad e_n=(\mathrm{ID},t_{\rm source},t_{\rm receive},\mathrm{quality})
$$

### Variables, units and conventions

- Buffer B and produced image/data size S in bytes; useful downlink capacity C in bytes s^-1; interval dt in s.
- Telemetry age A in s refers to source-valid time, distinct from reception time; clock uncertainty is included.
- Completeness fraction counts valid unique chunks; expected chunk count comes from a trusted synthetic manifest.
- State s and event e are abstract simulator records. Real radio commands, frequencies, credentials, and flight protocols are outside this package.

### Assumptions and boundary conditions

- Transport delivery is distinct from instrument measurement validity and operator interpretation.
- The test bench owns its synthetic events and cannot contact a live ground station or spacecraft.

### Derivation step 1

$$
B_{n+1}=\min[B_{max},\max(0,B_n+S_n-C_n\Delta t_n)]
$$

Finite buffer capacity requires a separate explicit loss counter when unclamped occupancy exceeds Bmax; generated bytes are not silently discarded.

### Derivation step 2

```text
A_j=t_{now}-t_{valid,j}
```

Age uses measurement-valid time, not receive time. Clock uncertainty produces an age interval and can prevent a fresh classification.

### Derivation step 3

```text
f_{complete}=N_{unique,valid}/N_{expected}
```

The trusted synthetic manifest supplies the denominator; duplicates and invalid chunks do not increase the numerator.

### Derivation step 4

$$
s_{n+1}=F(s_n,e_n),\quad F(F(s,e),e)=F(s,e)
$$

Idempotent event processing prevents a replayed ID from executing a second abstract transition. Ordering rules and checkpoint generation are explicit.

### Inference or simulation procedure

Define a versioned telemetry dictionary, event ledger, and abstract state machine for simulated commissioning and routine image collection. Build a local packet-replay service with reproducible loss, delay, duplication, and reset patterns. Use Open MCT as an optional visualization framework while keeping telemetry ingestion and reconstruction independently testable. Display source time, receive time, freshness, uncertainty, and provenance beside every engineering value. Reassemble synthetic images using chunk identifiers and integrity checks; diagnose incomplete transfers from the manifest rather than treating a successful socket read as completed science delivery. Evaluate operator tasks using randomized scenario order, including cases where the correct answer is that current state cannot be established.

### Validity domain and fidelity limits

A public operations description is not an interface-control document or authorization to command CatSat. Local replay verifies software behavior and operator interpretation, not radio-link performance or mission readiness.

## 5. Data specifications and provenance

![I07 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| event_id | string | 1 | Unique synthetic event identity. | Duplicate IDs must have identical payload or conflict state. |
| source_receive_time | float64[2] | s declared scale | Valid measurement and reception times. | Clock uncertainty and restart generation attached. |
| engineering_value | typed scalar&#124;null | dictionary-declared | Synthetic subsystem observation. | Null/invalid/stale separate; no last-value freshness assumption. |
| quality_age | struct | 1, s | Validity/freshness evidence. | Per-field rule and uncertainty interval. |
| image_manifest | struct | byte, chunk count | Expected inert image and integrity identifiers. | Trusted scenario version; never inferred from socket closure. |
| chunk_record | bytes+ID+checksum | byte | Received image segment. | Unique valid chunks only; conflicts flagged. |
| simulator_state | enum+ledger | 1 | Abstract local operation state. | No real command or radio fields. |
| scenario_trace | table | s, 1 | Loss/delay/reset seed and expected outcomes. | Replay deterministic and independently scored. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### University of Arizona CatSat operations concept

[Product, archive or reference](https://catsat.arizona.edu/operations/concept)

**Fields:** Public commissioning and science-operation descriptions

**Access:** Public context only; exact current interfaces, telemetry and operational authority must come from the mission team.

**Role:** Requirements discovery and historical-project continuity.

### Proposed isolated telemetry replay dataset

[Product, archive or reference](https://ammos.nasa.gov/openmct/)

**Fields:** Source/receive timestamps, subsystem state, sequence, quality, image manifest, operator annotation, scenario seed

**Access:** Create entirely synthetic fixture events and inert sample images. No real mission packets are required.

**Role:** Deterministic software and human-factors validation.

## 6. Uncertainty, sensitivity and identifiability

Clock skew and out-of-order delivery can make valid-time ordering ambiguous. Keep source-clock uncertainty and event conflicts rather than silently sorting by receive time. Freshness decisions are robust only when the entire possible age interval lies within its declared bound. Transport corruption and missing chunks affect image completeness separately from scientific measurement validity.

Human interpretation depends on missingness display and evidence traceability. Use randomized scenario order and scoring that rewards unknown when evidence is inadequate. Software validation measures replay/state integrity, not RF link performance or mission readiness. Public operational descriptions may evolve and remain context only; exact mission interfaces would require separate owner-provided evidence beyond this isolated package.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Event-sourced local reconstruction | Deterministic audit/restart behavior. | Ordering/conflict semantics need care. | Use authoritative state layer. |
| Open MCT visualization adapter | Flexible timeline/value presentation. | View correctness does not validate reconstruction. | Use after contract-level tests pass. |
| Simple static scenario reports | Low implementation cost and clear review. | Limited operator interaction. | Use baseline/fixtures alongside any console. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| I07-V1 | Duplicate replay | State and unique-image completeness remain unchanged. | Replay every valid event/chunk twice. | Idempotence/set-count identity. |
| I07-V2 | Delayed fresh-looking packet | Age follows source time and field becomes stale/unknown as appropriate. | Late receive-time injection. | Declared freshness equation. |
| I07-V3 | Restart equivalence | Checkpoint plus replay yields the same authoritative state as uninterrupted run. | Deterministic reset at varied event positions. | Event-ledger integration. |
| I07-V4 | Missing/corrupt image chunk | Completeness stays below one and assembler reports exact missing/conflicting IDs. | Synthetic inert image manifest replay. | Integrity contract. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Reconcile every expected synthetic event and image chunk with an independent reference ledger after delay, duplicate, and reset cases.
- Require the console to distinguish unknown, stale, invalid, and nominal state in all specified simulator scenarios.
- Measure task accuracy, time to recognize data staleness, false-alarm rate, and workload; report sample size and uncertainty instead of claiming universal operator improvement.

## 9. Implementation and reproducible work packages

1. Define synthetic telemetry dictionary, event IDs and image manifests.
2. Implement isolated replay with seeded delay/loss/duplicate/reset patterns.
3. Build idempotent state ledger and checkpoint recovery.
4. Implement manifest-based image assembly and clock-aware freshness.
5. Connect optional operator view only to reconstructed contracts.
6. Release expected-state fixtures and randomized unknown-state operator scenarios.

### Investigation sequence

1. Create an operations-to-telemetry requirements matrix with stale-state and unknown-state behaviors.
2. Implement replay and image reconstruction independently of the display framework.
3. Add simulated request preconditions, approval-record visualization, and a full event audit trail.
4. Run blinded operator scenarios and release the failure cases with reproducible seeds.

### Resources and interfaces to expertise

- Local simulator, versioned schemas, Open MCT or equivalent dashboard, usability evaluator, and mission operations mentor.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| Receipt called valid measurement | False current state. | Age/quality evidence mismatch. | Separate transport and measurement validity. |
| Socket closure called complete image | Incomplete science product accepted. | Manifest chunk reconciliation. | Require unique valid manifest coverage. |
| Simulator accidentally wired to live target | Scope violation. | Dependency/config endpoint isolation audit. | No live adapter; synthetic-only transport types. |

- Arrival order can mislead a display that ignores source time. Similar-looking stale values, incorrect clocks, and incomplete image manifests can conceal a degraded scientific record.

## 11. Required engineering outputs

- Telemetry dictionary, replay fixtures, simulated console, image-completeness report, operator evaluation plan, and mission-adapter requirements.

### Scientific result figures to produce during execution

A pass timeline, freshness-aware telemetry panel, and synthetic image-chunk map that reveal gaps and delayed events without implying live spacecraft control.

## 12. Cited technical and scientific resources

- [University of Arizona CatSat Operations](https://catsat.arizona.edu/operations/concept) — Public mission-operations context; not a live interface specification.
- [NASA AMMOS Open MCT](https://ammos.nasa.gov/openmct/) — Open visualization framework for mission-control-style displays.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
