# E07 · DISCOVERY TRIDENT

**Original project:** Glendale Community College (GCC) ASCEND Team

**Session E:** ASCEND

**Document class:** engineering research design and analysis record · **Revision:** 3 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session E](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_E.md) · [← E06](../E06-apollo-thermalis/README.md) · [E08 →](../E08-gateway-powerbench/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 4 | 3 | 7 | 2 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Purpose and scientific objective

Extend the GCC ASCEND concept into three interoperable, independently logged payload modules. The research contribution is a quantified interface and reproducibility strategy: environmental differences across modules are distinguished from sensor bias and clock error. A modular mission archive lets subsequent cohorts compare flights without losing calibration context.

**Question:** Can three student-built modules produce mutually comparable environmental records and recover scientifically useful data after one module fault?

**Testable hypothesis:** Explicit time, unit and calibration interfaces will reduce cross-module disagreement and preserve at least two independent records after a simulated single-module failure.

## 1. Design basis and analysis boundary

The three-module payload is an interoperability and redundant-science system. Its boundary includes independent sensor records, placement/response corrections, clock alignment, shared power and data recovery. Science success requires at least two acceptable mutually comparable records over the declared interval; one surviving module is a distinct lesser outcome.

Begin with a common telemetry dictionary and shared calibration periods, then assess consistency on withheld trajectory segments. Independent availability formulas are reference limits only. Shared environmental, power, clock or calibration faults require conditional/common-cause modeling, and no original GCC telemetry is assumed available.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| E07-R1 | All modules shall emit the same versioned units/time/quality dictionary while retaining native raw values. | Interoperability is more than matching column names. | Cross-module schema and conversion fixtures. | Telemetry interface requirement. |
| E07-R2 | Science success shall require two acceptable records meeting completeness, timing and calibration gates. | At-least-one availability does not satisfy comparison science. | Fault-tree/event scoring checks across all survival combinations. | Corrected two-of-three requirement. |
| E07-R3 | Clock offset, bias and response differences shall be identified or carried as uncertainty. | Misalignment can resemble sensor disagreement. | Shared-period calibration and withheld-segment residuals. | Measurement consistency contract. |
| E07-R4 | Common-cause fault probabilities and conditional availabilities shall be documented or marked TBD. | Shared power invalidates independent reliability products. | Simulated shared-fault and dependency fixtures. | Reliability scope; no actual availability claimed. |

## 3. Architecture and controlled interfaces

Each module adapter retains native units, timestamp, sensor response and quality flags before conversion into a common record. A placement/clock registry distinguishes colocated environmental fields from gradients. Shared calibration estimates clock offset and bias, with covariance across modules rather than treating common reference bias as independent noise.

A record-acceptance gate evaluates completeness and calibration against declared science tolerances, currently TBD. The availability model consumes accepted-record events and shared-fault states, not merely electronics uptime. A recovery comparator combines two or three qualified records and reports one-record-only intervals separately. Fault provenance remains linked to power, clock and data-storage boundaries.

![E07 engineering architecture](figures/architecture.svg)

Science availability is conditioned on record comparability and two surviving acceptable records. A separate dependency branch preserves shared faults; pairwise agreement remains distinct from absolute calibration accuracy.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

```text
z_ij(t)=x(t-delta_t_j)+b_j+epsilon_ij
```

```text
sigma_difference^2=sigma_i^2+sigma_j^2-2*cov(i,j)
```

```text
A_at_least_one=1-product(1-A_j); independent module availability only.
```

```text
A_at_least_two=A1*A2+A1*A3+A2*A3-2*A1*A2*A3; three independent modules, matching the two-of-three science-return requirement.
```

### Variables, units and conventions

- z sensor observation; x common environmental state
- delta_t clock offset s; b calibration bias in measurement units
- A_j: probability that module j supplies an acceptable record over the specified interval; these closed forms require independent module availability. A common-cause fault tree replaces them when dependence is present.

### Assumptions and boundary conditions

- Shared power/environment can make faults correlated; do not use independent availability blindly.
- Compare only colocated fields after sensor response and placement corrections.

### Derivation step 1

$$
z_j(t)=x(t-\delta t_j)+b_j+\epsilon_j
$$

Small clock offsets produce residual approximately -dot(x) delta t plus bias. Shared calibration separates constant bias from time shift only when environmental variation is informative.

### Derivation step 2

$$
Var(z_i-z_j)=\sigma_i^2+\sigma_j^2-2Cov(i,j)
$$

Common noise may cancel in differences while shared bias remains invisible. Agreement alone does not establish absolute accuracy.

### Derivation step 3

$$
A_{\ge2}=A_1A_2+A_1A_3+A_2A_3-2A_1A_2A_3
$$

For independent acceptable-record events, enumerate exactly-two and exactly-three cases. All Ai refer to the same interval and acceptance gate, not generic component availability.

### Derivation step 4

$$
A_{\ge2}=(1-p_c)[a_1a_2+a_1a_3+a_2a_3-2a_1a_2a_3]
$$

In the explicit example where one common event disables all modules with probability p_c and residual events are conditionally independent, ai are conditional availabilities. General dependencies require full joint event probabilities.

### Inference or simulation procedure

Specify a common telemetry dictionary and hardware boundary for each module. Infer clock offset and sensor bias from shared calibration periods, then test consistency on withheld trajectory segments. Model redundant science return using a fault tree with common causes rather than a simple component count.

### Validity domain and fidelity limits

Original GCC telemetry is not supplied. Three modules do not guarantee independent measurements if they share power or calibration bias.

## 5. Data specifications and provenance

![E07 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| module_id | enum | 1 | One of three independent record sources. | Hardware/firmware/calibration version required. |
| native_observation | record | native | Raw sensor values and response status. | No conversion discards original units. |
| common_timestamp | nullable<float64> | s | Aligned time coordinate. | Offset/skew covariance retained. |
| placement_response | record | m,s | Sensor position and lag correction. | Comparable-field domain required. |
| bias_covariance | matrix<float64> | native^2 | Cross-module calibration uncertainty. | Common reference terms included. |
| acceptable_record | bool/unknown | 1 | Science-gate event over interval. | Unknown distinct from failure/pass. |
| fault_dependency | record | 1 | Shared/conditional event structure. | Probability provenance or TBD status. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### Arizona Space Grant ASCEND program

[Product, archive or reference](https://spacegrant.arizona.edu/research/ascend)

**Fields:** Module ID, UTC plus monotonic time, temperature/pressure/acceleration/battery measurements, quality flags, firmware version and calibration references

**Access:** Public reference or archive pointer. Original team measurements are not supplied. Confirm product-level access, version and license; a linked paper does not imply its raw data are downloadable.

**Role:** Comparison/model context; prospective measurement schema is listed separately.

### NASA Systems Engineering Handbook

[Product, archive or reference](https://www.nasa.gov/reference/systems-engineering-handbook/)

**Fields:** Independent benchmark metadata, reference assumptions and calibration context; select actual products before execution.

**Access:** Public reference or archive pointer. Original team measurements are not supplied. Confirm product-level access, version and license; a linked paper does not imply its raw data are downloadable.

**Role:** Comparison/model context; prospective measurement schema is listed separately.

## 6. Uncertainty, sensitivity and identifiability

Clock drift, sensor lag, calibration bias and environmental gradients affect pairwise comparability. Shared references can make modules agree while all are wrong. Reliability uncertainty includes correlated power/environment failures and whether storage survives a module fault; counting three enclosures does not establish independence.

Fit clock/bias on shared periods and validate on rapid-changing withheld segments. Propagate reference covariance into absolute and pairwise residuals separately. Compare independent and common-cause availability scenarios, profiling p_c rather than concealing it. Report how science gates change availability and intervals with only one qualified record.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Three nominally identical modules | Easy schema/common-mode comparison. | Shared design/calibration faults. | Use with explicit common-cause model. |
| Diverse sensor/firmware paths | Can reduce some common failures. | Cross-calibration complexity. | Select when diversity benefit exceeds comparability loss. |
| Shared power versus isolated support | Shared system saves mass. | Common shutdown versus extra resources. | Trade using joint two-record availability, not module count. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| E07-V1 | Independent endpoints | Ai=1 gives A>=2=1; exactly one Ai=1 and others zero gives zero. | Enumerate eight survival states. | Two-of-three algebra. |
| E07-V2 | Common all-module failure | p_c=1 gives zero science availability despite ai=1. | Conditional fault-tree fixture. | Dependency example. |
| E07-V3 | Clock/bias known trace | Injected offsets/bias recover within declared uncertainty, while constant x cannot separate timing. | Synthetic varying/constant environment cases. | Identifiability; original data unavailable. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Proposed gate: >=95% local record completeness and clock agreement within half the fastest science sampling interval.
- Withhold a module during fusion and compare predicted versus observed environmental values.
- Demonstrate reproducible decoding and science summary from a clean checkout.

## 9. Implementation and reproducible work packages

1. Create common_telemetry_schema.json and three native adapters.
2. Build clock_placement_registry.csv and alignment_bias.py.
3. Implement acceptable_record_gate.py with pending science tolerances.
4. Create joint_fault_tree.py and all-survival fixtures.
5. Build withheld_segment_consistency.ipynb using synthetic/available approved records.
6. Publish science_availability.parquet distinguishing two-of-three, one-only and common-fault scenarios.

### Investigation sequence

1. Assign environmental, imaging and power-monitor modules and freeze interface contracts.
2. Run a shared reference trajectory and deliberate offline module-loss replay.
3. Release module-level and fused data with a mission-level reproducibility ledger for the next cohort.

### Resources and interfaces to expertise

- Student module teams, systems mentor and data librarian.
- Independent loggers, reference sensor, synchronized test fixture and configuration repository.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| At-least-one scored success | Overstated comparison capability. | Survival-state audit. | Two-record acceptance event. |
| Shared power ignored | Optimistic availability. | Dependency registry mismatch. | Common-cause fault tree. |
| Agreement mistaken accuracy | Common calibration bias hidden. | Independent reference discrepancy. | Absolute-reference covariance and separate metrics. |

- Common-cause faults can defeat redundancy.
- Incorrect units or duplicated timestamps can silently corrupt comparisons.

## 11. Required engineering outputs

- Versioned analysis configuration, raw-to-derived provenance and uncertainty report.
- Project-specific model comparison, a publication figure with units, and an explicit outcome including inconclusive findings.

### Scientific result figures to produce during execution

Three-lane timeline showing measured fields, missing data and clock corrections; interface graph shows shared dependencies.

## 12. Cited technical and scientific resources

- [Arizona Space Grant ASCEND program](https://spacegrant.arizona.edu/research/ascend) — Program context and flight records, not original team telemetry.
- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — Requirements, interfaces and verification framework.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
