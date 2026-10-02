# I04 · ORION SENTINEL CORE

**Original project:** EagleSat Team: On-board Computer Subsystem

**Session I:** Aerospace Technology

**Document class:** engineering research design and analysis record · **Revision:** 3 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session I](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_I.md) · [← I03](../I03-saturn-channel-atlas/README.md) · [I05 →](../I05-pioneer-aerodrift/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 6 | 4 | 8 | 2 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Purpose and scientific objective

Create a fault-aware on-board-computer reference architecture around the original EagleSat FPGA/soft-core concept. Connect scientific data production to scheduling, power states, memory integrity, and explicit recovery behavior. The research question is not whether redundancy exists on a block diagram; it is whether the spacecraft retains a bounded, observable scientific service when individual faults and shared dependencies are represented in a testable model.

**Question:** Does an FPGA-assisted redundant architecture recover from isolated faults without missing critical deadlines or corrupting the authoritative scientific record?

**Testable hypothesis:** Selective hardware offload and independently monitored recovery will outperform blanket replication when voter faults, shared clocks, memory errors, and power cycling are included.

## 1. Design basis and analysis boundary

The EagleSat on-board-computer architecture is a local scheduling, integrity and recovery demonstrator for an FPGA/soft-core concept. Actual board inventory, toolchain, radiation susceptibility and execution times are TBD. The scientific service is a sequence of authoritative acquisition records preserved across simulated resets, not a nominal redundancy block diagram. NASA avionics context informs trades without establishing flight reliability.

Begin with deterministic tasks and buffers, add bounded blocking and fault/state transitions, then hardware-in-the-loop only with verified board interfaces. Independent lane errors are separated from voter, shared-memory, clock and power failures. The architecture defines what science can continue in degraded states and which deadlines or data become unsupported. Every test fault is an emulator/logical event, not radiation qualification.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| I04-R1 | Every critical task shall have measured or justified worst-case execution, blocking, period and deadline bounds. | Response-time analysis needs bounded inputs. | Task manifest and execution-trace audit. | Proposed scheduling contract. |
| I04-R2 | All accepted schedules shall satisfy R_i<=D_i or explicitly declare infeasibility. | A mean runtime cannot guarantee critical service. | Fixed-point response analysis and worst-case replay. | Existing fixed-priority model. |
| I04-R3 | Science record IDs shall remain unique and recoverable across reset/duplicate replay. | Reset can corrupt or duplicate authoritative data. | Idempotent journal/reset fixture. | Proposed integrity requirement. |
| I04-R4 | Buffer overflow shall yield a recorded loss/degradation state rather than silent truncation. | Finite storage affects useful science availability. | Burst-production/downlink-gap replay. | Proposed service contract. |
| I04-R5 | TMR claims shall include voter and common-resource fault paths. | Independent-lane math omits shared failures. | Common-clock/voter emulator faults and fault-tree audit. | Existing TMR limitation. |
| I04-R6 | Recovery time and degraded-science availability shall be reported separately from nominal uptime. | Booted electronics need not deliver useful science. | State-tagged trace integration. | Proposed availability metric. |

## 3. Architecture and controlled interfaces

Subsystem adapters emit typed sample packets and bounded task releases. A scheduler maps tasks to soft-core/FPGA resources with explicit bus, DMA and interrupt blocking. A buffer/journal service stores sequence-numbered scientific records with integrity checks and a committed-record boundary. A downlink simulator consumes records under intermittent capacity without altering their source timestamps.

The fault manager implements boot, nominal, science, safe and recovery states with observable reasons. Redundant lanes and voter have distinct fault interfaces; shared dependencies are injected separately. A monotonic event ledger preserves reset generation and clock quality. Availability calculation counts only scientifically valid service states and includes startup/recovery losses, allowing board-specific timing evidence to replace emulator assumptions later.

![I04 engineering architecture](figures/architecture.svg)

Scheduling, committed scientific records and shared-fault recovery are connected through explicit timing and storage boundaries rather than a nominal redundancy claim.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

$$
R_i=C_i+B_i+\sum_{j\in hp(i)}\lceil R_i/T_j\rceil C_j;\quad R_i\le D_i
$$

$$
p_{\rm TMR}=3p^2-2p^3
$$

$$
\dot B=r_{\rm science}-r_{\rm downlink};\quad 0\le B\le B_{\max}
$$

$$
A=T_{\rm useful}/T_{\rm mission}
$$

### Variables, units and conventions

- Response R, execution C, blocking B_i, period T, and deadline D in s; hp(i) is the set of higher-priority tasks.
- p is independent per-lane failure probability in a stated interval; pTMR excludes voter and shared-resource failures.
- Data buffer B in bytes; science and downlink rates in bytes s^-1. Buffer B and task blocking B_i are distinct quantities.
- Availability A is useful-science time fraction, with boot, degraded mode, and recovery time included.

### Assumptions and boundary conditions

- Fixed-priority response-time analysis requires bounded execution, blocking, and preemption assumptions.
- Triple modular redundancy gains are conditional on fault independence; common-mode failures are explicitly added to the fault tree.

### Derivation step 1

$$
R_i=C_i+B_i+\sum_{j\in hp(i)}\lceil R_i/T_j\rceil C_j
$$

This displayed fixed-priority, single-processor response-time bound assumes zero release jitter, bounded blocking and the specified preemption/task model. Iterate from C_i+B_i to a fixed point and stop as infeasible if it exceeds the deadline. With supported bounded interfering-task jitter J_j, use ceil((R_i+J_j)/T_j) C_j and document the event model; do not claim general scheduling coverage.

### Derivation step 2

```text
p_{TMR}=3p^2(1-p)+p^3=3p^2-2p^3
```

Two or three failed independent lanes defeat majority voting. Add voter and common-mode paths separately rather than folding them into independent p.

### Derivation step 3

$$
B(t)=B(0)+\int(r_{science}-r_{downlink})dt-L(t)
$$

Buffer occupancy in bytes obeys conservation; L is explicitly recorded rejected/lost data, with occupancy bounded by physical capacity.

### Derivation step 4

$$
A_{science}=\int\mathbf1_{valid\ service}(t)dt/T
$$

Useful-science availability differs from processor uptime; denominator and validity rules are part of the metric.

### Inference or simulation procedure

Define an interface contract for each subsystem and map tasks to a soft-core processor or FPGA logic using timing evidence. Specify a finite-state operational model with boot, nominal, science, safe, and recovery states. Simulate scheduled science acquisition, intermittent downlink, corrected memory errors, and isolated logical faults in a local test bench. Inject declared software/emulator faults into representative interfaces and log every transition with sequence number and clock quality. Measure the effect of a voter or shared-clock failure separately from independent lane errors. Use a stable packet schema and idempotent record handling so reset recovery does not create duplicate scientific observations.

### Validity domain and fidelity limits

Logic simulation and software fault injection do not reproduce radiation susceptibility, latch-up, thermal effects, or flight qualification. The historical MicroBlaze concept is retained as context; device and toolchain choices require an actual board inventory.

## 5. Data specifications and provenance

![I04 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| task_spec | struct | s | C,blocking,period,deadline and priority. | Measured/bounded status; task blocking not buffer bytes. |
| task_trace | table | s | Release/start/end and missed deadlines. | Monotonic clock/reset generation recorded. |
| science_record | struct | bytes, sequence | Authoritative sample payload and checksum. | Unique source ID; missing sample explicitly marked. |
| buffer_state | uint64 | byte | Committed plus queued occupancy. | Capacity/loss counters; no silent wrap. |
| fault_event | enum+time | 1, s | Lane/voter/clock/memory/power emulator event. | Fault scope and independence assumption explicit. |
| operational_state | enum | 1 | Boot/science/safe/recovery state. | Transition cause and valid-service flag. |
| timing_uncertainty | distribution<struct> | s | Clock/WCET/jitter uncertainty. | Retain shared-clock correlations. |
| availability_recovery | measurement<struct> | 1, s | Science fraction and recovery latency. | Exclude invalid records from useful service. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### NASA small-spacecraft avionics reference

[Product, archive or reference](https://www.nasa.gov/smallsat-institute/sst-soa/small-spacecraft-avionics/)

**Fields:** Architecture trade considerations, processors, fault-management context

**Access:** Public survey; vendor specifications and exact EagleSat board details require verification.

**Role:** Architecture comparator, not proof of flight reliability.

### Proposed local test-bench trace dataset

[Product, archive or reference](https://www.nasa.gov/reference/systems-engineering-handbook/)

**Fields:** Task release/deadline, state, reset reason, memory event, packet sequence, power mode, fault label

**Access:** Generate deterministic synthetic workloads and release seeds; no mission records are supplied.

**Role:** Deadline, integrity, and recovery evaluation.

## 6. Uncertainty, sensitivity and identifiability

WCET, interrupt interference and shared-bus blocking determine deadline margins; emulator timings are not flight timings. Measure each resource path and sweep release phasing to locate worst cases. Clock uncertainty affects both task order and scientific timestamps. Maintain distinct analysis versus measured bounds so unknown hardware performance cannot become a guarantee.

Independent logical errors, common resource failure and recovery latency interact with integrity and availability. TMR probability improvement is conditional on independence, while voters and common power can dominate. Use deterministic fault schedules and parameterized event-rate sensitivity rather than invented failure probabilities. Compare authoritative record counts/checksums with expected manifests after resets and overflow.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Single soft-core with watchdog/journal | Simple state/integrity implementation. | One execution lane remains vulnerable. | Use required baseline for measured recovery. |
| FPGA-assisted acquisition and buffering | Can bound timing-critical paths. | Toolchain/resource and shared-bus complexity. | Adopt with actual timing/interface evidence. |
| Replicated lanes with voter | Tolerates some independent faults. | Common-mode/voter and power costs. | Choose only when measured service benefit exceeds shared-dependency risk. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| I04-V1 | No higher-priority tasks | Response bound reduces to C+B. | Analytic scheduler fixture. | Response-time equation. |
| I04-V2 | Perfect independent lanes | TMR failure tends to zero as p tends to zero and equals one at p=1. | Polynomial boundary/Monte Carlo fixture. | Voting combinatorics. |
| I04-V3 | Reset with duplicate packets | Committed unique scientific record set is unchanged by duplicate replay. | Journal checkpoint/reset integration. | Idempotent integrity requirement. |
| I04-V4 | Shared-clock fault | Fault is reported as common mode rather than masked by three lanes. | Deterministic emulator scenario. | Declared redundancy boundary. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Require zero missed critical deadlines within the declared tested workload envelope; report that envelope and observed sample count.
- Check packet ordering, duplicate suppression, and data provenance across resets using an independent log reconciler.
- Report recovery-time distribution, useful-science availability, and common-mode failure sensitivity; distinguish confidence bounds from guaranteed reliability.

## 9. Implementation and reproducible work packages

1. Inventory board/toolchain or mark architecture emulator-only.
2. Create task/resource/blocking and scientific packet contracts.
3. Implement response-time analyzer and deterministic workload simulator.
4. Build committed-record journal and finite-buffer loss accounting.
5. Implement observable fault/recovery state machine with lane/common modes.
6. Release expected-record manifests, deadline traces and service-availability comparisons.

### Investigation sequence

1. Build a requirements-to-interface-to-test matrix and freeze critical service definitions.
2. Profile task execution and buffer behavior before choosing offload or redundancy boundaries.
3. Implement reproducible local fault campaigns with isolated-lane and common-mode cases.
4. Hold out fault timing and science workload combinations, then document residual failure modes.

### Resources and interfaces to expertise

- FPGA/soft-core simulation tools, board emulator or development board, timing instrumentation, systems engineer, and independently reviewed interface definitions.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| WCET treated as average | Missed critical deadline. | Tail trace exceeds bound. | Measure/bound paths and reject unsupported schedule. |
| Reset corrupts journal boundary | Missing/duplicate authoritative science. | Manifest/checksum/sequence reconciliation. | Atomic commit and idempotent replay. |
| Voter/common resource ignored | Overstated redundancy availability. | Common-mode fault-tree gap. | Explicit shared paths and degraded-state behavior. |

- Shared power, clocks, or voters can invalidate redundancy claims. Late interface changes can create unbounded blocking and undocumented packet incompatibility.

## 11. Required engineering outputs

- Architecture trade study, timing budget, state-machine specification, packet schema, fault-campaign fixtures, and recovery evidence dashboard.

### Scientific result figures to produce during execution

An FPGA/soft-core architecture linked to a timeline of injected fault, detection, safe-state entry, recovery, and science-record continuity.

## 12. Cited technical and scientific resources

- [NASA Small Spacecraft Avionics](https://www.nasa.gov/smallsat-institute/sst-soa/small-spacecraft-avionics/) — On-board-computer architecture and fault-management context.
- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — Interface, requirements, and verification traceability framework.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
