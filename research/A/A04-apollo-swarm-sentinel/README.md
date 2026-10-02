# A04 · APOLLO SWARM SENTINEL

**Original project:** Target Detection Using Algorithmic Matter

**Session A:** Math, Physics & Chemistry

**Document class:** engineering research design and analysis record · **Revision:** 4 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session A](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_A.md) · [← A03](../A03-chandra-vortex-core/README.md) · [A05 →](../A05-voyager-cilia-array/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 4 | 3 | 7 | 3 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Mission profile

![A04 engineering mission profile: scientific question, hypothesis, model scope and evidence status](figures/mission-profile.svg)

| Profile panel | Engineering signal | Open the evidence |
| --- | --- | --- |
| Mission identity | Target Detection Using Algorithmic Matter | [Scientific objective](#purpose-and-scientific-objective) |
| Model cockpit | 4 governing expressions; 4 derivation steps; declared assumptions and validity envelope | [Mathematical formulation](#4-mathematical-model-and-derivation) |
| Data blueprint | 7 proposed fields with types, units and quality rules | [Field map & downloads](data/README.md) |
| Verification queue | 4 proposed requirements; 3 specified cases; project execution evidence pending | [Case definitions](#8-verification-and-validation-cases) |
| Figure wall | Architecture, field map, planned result description | [Open full gallery](figures/README.md) |
| Resource library | 3 cited primary resources with support statements | [Cited resources](#12-cited-technical-and-scientific-resources) |

### Model cockpit

**Analysis method:** Start with static object detection on a connected lattice, then extend to boundary localization and fault-aware information flow. State invariants for connectivity and evidence provenance. Prove termination and correctness under stated scheduler assumptions. Monte Carlo experiments explore noise and failures outside the proof's ideal conditions. A small robot or software-agent demonstration validates only the primitives it actually implements.

**Operating envelope:** Theoretical round complexity is not physical time. Constant-memory restrictions may preclude exact global statistics, and connectivity guarantees can fail when arbitrary particles disappear.

**Variables and conventions**

- n particles, local degree, observation y, bounded states, communication budget, activation schedule, failed-particle fraction.
- Target geometry, sensor sensitivity/specificity, correlation length, connectivity, detection latency, movement energy.

### Artifact wall

![A04 proposed analysis architecture](figures/architecture.svg)

Bounded particle computation is separated from the full-information oracle. Scheduler and connectivity monitors delimit correctness claims and leave physical latency unqualified.

**Scientific result to produce:** Particles change color with local confidence, connectivity is overlaid, target boundaries appear only after the decision rule fires, and a sidebar shows false alarms, rounds, and energy.

### Investigation feed · planned work

The feed records proposed work packages. A row becomes executed evidence only with versioned inputs, outputs and a reviewed result.

| Sequence | Evidence state | Engineering work package |
| --- | --- | --- |
| 01 | Planned | Create lattice_schema.json and sensor_models.yaml. |
| 02 | Planned | Implement scheduler.py with fair/unfair replay policies. |
| 03 | Planned | Encode detector_transition.csv as executable bounded rules. |
| 04 | Planned | Build provenance_oracle.py independently of particle memory. |
| 05 | Planned | Add graph_invariants.py and exhaustive small-state fixtures. |
| 06 | Planned | Publish trials.parquet and sensitivity notebooks with seeds and assumption flags. |

### Mission connections

Connections are reading routes based on actual shared resources, supplied sessions or included illustrations. They do not establish physical dependencies, team collaborations or validated results.

| Connected mission | Original investigation | Recorded connection basis |
| --- | --- | --- |
| [A03 · CHANDRA VORTEX CORE](../A03-chandra-vortex-core/README.md) | Superfluidity of Neutron Star Matter | Session A |
| [A05 · VOYAGER CILIA ARRAY](../A05-voyager-cilia-array/README.md) | Artificial Cilia Creation for Advanced Sensor Devices | Session A |
| [A02 · NEW HORIZONS CRYOPHASE](../A02-new-horizons-cryophase/README.md) | Theory and simulation investigation of eutectic phase behavior on Pluto | Session A |
| [A06 · APOLLO PORIN INSIGHT](../A06-apollo-porin-insight/README.md) | Purification of the P66 Outer Membrane Protein of the Bacterium Borrelia burgdorferi | Session A |
| [A01 · ARTEMIS FRACTAL NAVIGATOR](../A01-artemis-fractal-navigator/README.md) | New Methods for the Iteration and Visualization of Mandelbrot and Julia Sets | Session A |
| [A07 · ORION CHROMATIN ATLAS](../A07-orion-chromatin-atlas/README.md) | Properties of Chromatin Extracted by Salt Fractionation from a Cancerous and Non-cancerous Esophageal Cell Line | Session A |

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

Proposed mission: study how locally communicating programmable particles recognize a benign environmental target, share evidence, and collectively mark its boundary. Define the target as an inert test object or scientific feature. The contribution is a provable distributed algorithm plus an honest translation gap between the geometric amoebot model and realizable robot hardware.

**Question:** Which local sensing and communication rules permit reliable target detection despite asynchronous activation, sensor noise, particle failures, and limited memory?

**Testable hypothesis:** Sequential evidence accumulation with connectivity-preserving coordination will reduce false collective detections relative to single-particle thresholds at comparable detection delay, within a defined noise model.

## 1. Design basis and analysis boundary

The engineered system is a finite-memory detector on a time-dependent hexagonal particle graph. Observations have particle/time provenance and a declared noise model. Scheduler, sensing, bounded-state updates and messages define the boundary; computational rounds become physical time or energy only through separately measured adapters.

Begin with a connected static graph and independent observations, then challenge asynchronous activation, correlated sensing and failures. Formal proofs apply only under declared scheduler/connectivity assumptions. The implementation decision compares realizable finite-state evidence rules with a full-provenance likelihood oracle that intentionally exceeds particle memory.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| A04-R1 | Every rule shall enumerate its finite state count, message alphabet and scheduler assumptions. | Unbounded likelihood accumulation cannot support constant-memory claims. | Inspect transition table and model-check small instances. | Amoebot model contract. |
| A04-R2 | Proposed independent-case false-alarm target is 0.01, with binomial interval and sample count. | Threshold quality depends on a declared null model. | Held-out target-absent Monte Carlo trials. | Design target; measured performance unknown. |
| A04-R3 | Check graph connectivity after every permitted movement. | Disconnected components lose global evidence. | Assert invariants and enumerate small graph moves. | Declared legal-motion assumptions. |
| A04-R4 | The offline evaluator shall count each observation only once. | Cycles can recirculate evidence into false confidence. | Replay duplicate message IDs and compare single delivery. | Provenance requirement; bounded approximations flag residual error. |

## 3. Architecture and controlled interfaces

The simulator builds axial hex coordinates and neighbor-port labels. An event scheduler supplies seed, activation index and optional simulated seconds. The transition engine consumes bounded sensor symbols and messages; sensor adapters map target geometry to independent or correlated observations.

An offline audit stores full provenance separately from particle state. Graph monitoring records partitions and dead nodes. Declaration records distinguish local detection, propagated agreement and localization. Correlation or fairness violations become explicit assumption flags; they are not silently absorbed into nominal false-alarm statistics.

![A04 engineering architecture](figures/architecture.svg)

Bounded particle computation is separated from the full-information oracle. Scheduler and connectivity monitors delimit correctness claims and leave physical latency unqualified.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

```text
G=(V,E) is the time-dependent adjacency graph of particles on a hexagonal baseline lattice.
```

```text
ell_i(t)=sum_tau log[p(y_i,tau|H_1)/p(y_i,tau|H_0)], with thresholds chosen for specified false-alarm and miss rates.
```

```text
x(t+1)=W(t)x(t)+u(t) is a consensus abstraction; realizable finite-memory rules are analyzed separately.
```

```text
P_D=P(declare target|target present); P_FA=P(declare target|target absent).
```

### Variables, units and conventions

- n particles, local degree, observation y, bounded states, communication budget, activation schedule, failed-particle fraction.
- Target geometry, sensor sensitivity/specificity, correlation length, connectivity, detection latency, movement energy.

### Assumptions and boundary conditions

- Amoebot motion and communication primitives are mathematical abstractions; actual sensors and actuators need separate error models.
- Neighbor measurements may be correlated; independent-sample likelihoods are used only in explicitly independent synthetic cases.

### Derivation step 1

$$
\ell(y)=y\ln(p_1/p_0)+(1-y)\ln[(1-p_1)/(1-p_0)]
$$

Derive the Bernoulli log likelihood ratio. Independent samples add; dependent samples need a joint model, so repeated local messages are not new samples.

### Derivation step 2

$$
A\approx\ln[(1-\beta)/\alpha];\ B\approx\ln[\beta/(1-\alpha)]
$$

Sequential thresholds motivate the reference detector for false alarm alpha and miss beta. Overshoot and quantization mean these are not guarantees for the finite-state asynchronous implementation.

### Derivation step 3

$$
x_{t+1}=Wx_t;\quad\mathbf1^TW=\mathbf1^T
$$

Column stochasticity preserves sums; row stochasticity preserves constants. Mean consensus additionally requires appropriate connectivity and update conditions.

### Derivation step 4

$$
n_{eff}\approx n/[1+(n-1)\rho]
$$

Equicorrelated unit-variance observations give mean variance [1+(n-1)rho]/n. The diagnostic shows why many correlated neighbors may provide little independent information.

### Inference or simulation procedure

Start with static object detection on a connected lattice, then extend to boundary localization and fault-aware information flow. State invariants for connectivity and evidence provenance. Prove termination and correctness under stated scheduler assumptions. Monte Carlo experiments explore noise and failures outside the proof's ideal conditions. A small robot or software-agent demonstration validates only the primitives it actually implements.

### Validity domain and fidelity limits

Theoretical round complexity is not physical time. Constant-memory restrictions may preclude exact global statistics, and connectivity guarantees can fail when arbitrary particles disappear.

## 5. Data specifications and provenance

![A04 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| particle_id | uint32 | 1 | Stable simulated node. | Generation ID prevents identity reuse. |
| axial_position | pair<int32> | lattice step | Hex coordinates. | Neighbor ports match offsets. |
| activation_index | uint64 | event | Scheduler sequence. | Increasing; fairness metadata required. |
| sensor_symbol | nullable<enum> | 1 | Bounded sensor alphabet. | Missing distinct from target absent. |
| message_state | enum | 1 | Finite transition message. | Alphabet version and direction required. |
| provenance_id | string | 1 | Offline observation origin. | Deduplicate before oracle accumulation. |
| declaration | record | 1 | Node, event and decision. | Confidence null if uncalibrated. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### ASU Self-Organizing Particle Systems research framework

[Product, archive or reference](https://labs.engineering.asu.edu/sops/amoebot/)

**Fields:** Formal model definitions, algorithmic primitives, and publication links.

**Access:** Public laboratory resource; locate simulator/code licenses separately.

**Role:** Model foundation, not measurements of a working material.

### Generated target/noise benchmark

[Product, archive or reference](https://arxiv.org/abs/2205.15412)

**Fields:** Lattice layouts, convex/nonconvex targets, activation schedules, observation seeds, failures, and event traces.

**Access:** Generate versioned test cases; linked paper supplies an asynchronous 3D coordination precedent rather than a target benchmark.

**Role:** Controlled robustness evaluation.

## 6. Uncertainty, sensitivity and identifiability

Sensitivity/specificity vary with geometry and common environmental fields. Binomial intervals apply only to independent trial outcomes; common seeds or fields require clustered evaluation. Scheduler fairness and connectivity are discrete applicability assumptions rather than smooth uncertainty parameters.

Sweep correlation length, target size, failure timing and message capacity independently. Compare bounded rules against full-provenance likelihood to attribute loss to sensing versus compression. An unfair schedule tests robustness outside the proof envelope; its failure must be reported with the violated assumption rather than as an unexplained algorithm defect.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Local thresholds | Minimal memory. | Weak global coverage. | Choose only for locally observable targets meeting false-alarm gate. |
| Finite-state tokens | Bounded communication. | Quantization and stale evidence. | Select after asynchronous and duplicate verification. |
| Floating-point oracle | Measures information ceiling. | Not constant-memory deployment. | Retain as offline comparison. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| A04-V1 | No-information limit | p1=p0 yields zero evidence increment. | Evaluate guarded analytic likelihood fixtures. | Bernoulli identity. |
| A04-V2 | Consensus conservation | Doubly stochastic connected fixed W preserves mean. | Compare matrix reference and bounded transition outputs. | Linear identity; quantization differences explicit. |
| A04-V3 | Duplicate and partition replay | Oracle evidence unchanged by duplicate; illegal partition raises fault. | Script message cycles and node losses. | R3/R4; results pending. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Use invariant checking and model checking on small exhaustive systems before large simulations.
- Report receiver-operating curves, localization error, worst-case activation rounds, message counts, and energy estimates.
- Proposed gate: stated false-alarm bounds hold within confidence intervals on unseen noise seeds; publish counterexamples beyond assumptions.

## 9. Implementation and reproducible work packages

1. Create lattice_schema.json and sensor_models.yaml.
2. Implement scheduler.py with fair/unfair replay policies.
3. Encode detector_transition.csv as executable bounded rules.
4. Build provenance_oracle.py independently of particle memory.
5. Add graph_invariants.py and exhaustive small-state fixtures.
6. Publish trials.parquet and sensitivity notebooks with seeds and assumption flags.

### Investigation sequence

1. Specify benign target classes, measurable detection requirements, sensor models, scheduler, and precise particle capabilities.
2. Develop finite-state local rules with explicit message types, evidence expiry, and disconnected-component behavior.
3. Compare threshold-only, leader-assisted, and distributed evidence aggregation baselines across target shapes and noise correlation.
4. Explore 3D and energy-constrained extensions only after the 2D algorithm passes proof and simulation review.

### Resources and interfaces to expertise

- Distributed algorithms expertise, event-driven simulator, property checker, and optional tabletop modular robotics testbed.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| Scheduler starvation | No termination guarantee. | Activation coverage log. | Declare fairness boundary and watchdog. |
| Evidence recirculation | Inflated confidence. | Duplicate provenance count. | Token ownership/expiry with quantified approximation. |
| Graph partition | Incomplete global evidence. | Component monitor. | Legal motion constraints and partition reports. |

- Simulation success is insufficient evidence that programmable matter hardware exists at the modeled scale.
- Unmodeled sensor correlation can create coordinated false positives; retain adversarial noise cases.

## 11. Required engineering outputs

- Formal specification, correctness argument, reproducible simulation suite, error/latency trade study, and boundary-detection animation.

### Scientific result figures to produce during execution

Particles change color with local confidence, connectivity is overlaid, target boundaries appear only after the decision rule fires, and a sidebar shows false alarms, rounds, and energy.

## 12. Cited technical and scientific resources

- [Computing by Programmable Particles — ASU SOPS](https://labs.engineering.asu.edu/sops/amoebot/) — Research group's formal framework and distributed primitives.
- [Asynchronous Deterministic Leader Election in Three-Dimensional Programmable Matter](https://arxiv.org/abs/2205.15412) — Original asynchronous coordination model with explicitly stated geometric and scheduler conditions.
- [Energy-Constrained Programmable Matter Under Unfair Adversaries](https://arxiv.org/abs/2309.04898) — Original framework for accounting for locally distributed energy constraints.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
