# E08 · GATEWAY POWERBENCH

**Original project:** EagleSat Team: Development and Implementation of a Self-Contained Harness for In-House Integration, Verification, and Testing of CubeSat Electric Power Systems

**Session E:** ASCEND

**Document class:** engineering research design and analysis record · **Revision:** 4 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session E](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_E.md) · [← E07](../E07-discovery-trident/README.md) · [F01 →](../../F/F01-apollo-voicelink/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 4 | 4 | 7 | 3 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Mission profile

![E08 engineering mission profile: scientific question, hypothesis, model scope and evidence status](figures/mission-profile.svg)

| Profile panel | Engineering signal | Open the evidence |
| --- | --- | --- |
| Mission identity | EagleSat Team: Development and Implementation of a Self-Contained Harness for In-House Integration, Verification, and Testing of CubeSat Electric Power Systems | [Scientific objective](#purpose-and-scientific-objective) |
| Model cockpit | 4 governing expressions; 4 derivation steps; declared assumptions and validity envelope | [Mathematical formulation](#4-mathematical-model-and-derivation) |
| Data blueprint | 7 proposed fields with types, units and quality rules | [Field map & downloads](data/README.md) |
| Verification queue | 4 proposed requirements; 4 specified cases; project execution evidence pending | [Case definitions](#8-verification-and-validation-cases) |
| Figure wall | Architecture, field map, planned result description | [Open full gallery](figures/README.md) |
| Resource library | 3 cited primary resources with support statements | [Cited resources](#12-cited-technical-and-scientific-resources) |

### Model cockpit

**Analysis method:** Represent the harness as a state machine with independently observed voltage/current and explicit fixture self-checks. Propagate meter gain, offset, sampling skew and harness resistance into power uncertainty. Compare repeated duty-cycle replays; a fault is diagnosed only with evidence separating DUT, stimulus and measurement paths.

**Operating envelope:** Published EPS architectures do not supply this team’s wiring, limit settings or qualification requirements. State-of-charge models depend on chemistry, temperature and aging.

**Variables and conventions**

- V volts; I A; E J; R ohm
- Q_Ah ampere-hours; SOC dimensionless
- r_E J; a calibrated loss/temperature model is required

### Artifact wall

![E08 proposed analysis architecture](figures/architecture.svg)

The isolated state machine gates stimulus on controlled limits and separates wiring, sensing and DUT boundaries. Surrogate replay supports reproducibility without high-energy fault procedures or flight qualification claims.

**Scientific result to produce:** EPS/harness interface schematic and energy balance Sankey using measured data only after acquisition; prospective traceability matrix.

### Investigation feed · planned work

The feed records proposed work packages. A row becomes executed evidence only with versioned inputs, outputs and a reviewed result.

| Sequence | Evidence state | Engineering work package |
| --- | --- | --- |
| 01 | Planned | Create eps_harness_requirements.json with limit provenance and pending status. |
| 02 | Planned | Build local_harness_state_machine.py and interlock fixtures. |
| 03 | Planned | Implement surrogate_source_load.py with benign fault variants. |
| 04 | Planned | Create independent_meter_adapter.py and timing_calibration.py. |
| 05 | Planned | Build harness_loss_energy.py and chemistry_labeled_soc.py. |
| 06 | Planned | Publish repeated_replay.ipynb, fault_hypotheses.parquet and a fixture/DUT evidence matrix. |

### Mission connections

Connections are reading routes based on actual shared resources, supplied sessions or included illustrations. They do not establish physical dependencies, team collaborations or validated results.

| Connected mission | Original investigation | Recorded connection basis |
| --- | --- | --- |
| [E07 · DISCOVERY TRIDENT](../E07-discovery-trident/README.md) | Glendale Community College (GCC) ASCEND Team | Session E; [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) |
| [E05 · ORION TRUSS](../E05-orion-truss/README.md) | EagleSat Team: Design and Refinement of 3U CubeSat Structure | Session E; [GSFC-STD-7000 GEVS](https://standards.nasa.gov/standard/GSFC/GSFC-STD-7000) |
| [D07 · ARES DUAL-WORLD SCOUT](../../D/D07-ares-dual-world-scout/README.md) | Suborbital Uncrewed Aerial Vehicles for Earth Surveillance and Mars Exploration | [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) |
| [G07 · HUBBLE SPECTRAL ANCHOR](../../G/G07-hubble-spectral-anchor/README.md) | An Introduction to Systems Engineering: Building a Monochromator Mount | [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) |
| [I04 · ORION SENTINEL CORE](../../I/I04-orion-sentinel-core/README.md) | EagleSat Team: On-board Computer Subsystem | [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) |
| [I06 · SATURN LOADPATH](../../I/I06-saturn-loadpath/README.md) | Designing and Exploring the Structure of Launch Vehicles to Create Optimal Theoretical and Small-Scale Experimental Models | [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) |

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

Design a self-contained electrical-power-system verification harness as a controlled interface and evidence generator. The advance is automatic association of every measured limit with a requirement, calibration record and hardware revision. Use low-energy surrogates to develop sequencing and fault handling before qualified personnel select battery and flight-power tests.

**Question:** Can a harness verify EPS functional behavior and energy accounting repeatably while distinguishing DUT failure from measurement or fixture faults?

**Testable hypothesis:** Four-wire measurements and independently monitored loads will make bus-loss and protection behavior identifiable across repeated benign test cases.

## 1. Design basis and analysis boundary

The self-contained harness is an isolated EPS verification design with a simulated or low-energy surrogate DUT during development. Its boundary includes stimulus, independent sensing, wiring resistance, interlocks, state machine and fixture self-checks. Approved DUT/fixture limits and battery chemistry remain controlling inputs; no high-energy fault sequence or flight-battery procedure is supplied.

Begin with software replay and reference load/source models, then qualify fixture measurements before interpreting DUT behavior. EPS fault diagnosis requires evidence separating stimulus, harness and measurement paths. Energy and state-of-charge ledgers provide consistency checks, while chemistry/temperature/aging discrepancy prevents ideal coulomb counting from being treated as exact battery health.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| E08-R1 | Stimulus-enabled state shall require valid approved DUT/fixture limits and independent interlock status. | Missing limits cannot define a safe test envelope. | State-machine fixtures block unspecified limits. | Isolated harness contract; limits currently TBD. |
| E08-R2 | DUT terminal voltage shall be observed or corrected with calibrated harness resistance. | Source voltage is not necessarily DUT voltage. | Known-resistance surrogate and independent sense comparison. | Measurement-path requirement. |
| E08-R3 | Proposed energy-closure target: residual within propagated 95% measurement/loss interval. | A fixed tiny residual can ignore meter uncertainty. | Gain/offset/skew/loss ensemble and replay ledger. | Proposed consistency criterion, not EPS efficiency spec. |
| E08-R4 | Fault labels shall retain separate DUT, stimulus, sensor and fixture hypotheses until discriminated. | A single failed voltage reading is not proof of DUT failure. | Inject benign synthetic faults in each path. | Diagnostic requirement; no live fault operation. |

## 3. Architecture and controlled interfaces

A local harness state machine transitions through unpowered, self-check, ready, simulated stimulus, record and shutdown. A requirements adapter validates limits before any hardware-enabled design state. Independent source/DUT measurement adapters carry voltage/current calibration, timestamps and fixture identity.

A wiring model maps source to terminal voltage through resistance and contact uncertainty. Power integration and optional chemistry-labeled SOC estimation feed residual diagnostics. A fixture self-check compares known surrogate behavior to readings. Logs preserve stimulus command, observed response and interlock status independently; actual operational control is outside this computational annex.

![E08 engineering architecture](figures/architecture.svg)

The isolated state machine gates stimulus on controlled limits and separates wiring, sensing and DUT boundaries. Surrogate replay supports reproducibility without high-energy fault procedures or flight qualification claims.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

```text
P=V*I; E=integral V(t)*I(t)dt
```

```text
V_DUT=V_source-I*R_harness
```

```text
SOC_dot=-I/(3600*Q_Ah)
```

```text
r_E=E_in-E_out-DeltaE_stored-E_loss
```

### Variables, units and conventions

- V volts; I A; E J; R ohm
- Q_Ah ampere-hours; SOC dimensionless
- r_E J; a calibrated loss/temperature model is required

### Assumptions and boundary conditions

- Flight battery tests and fault limits are defined by approved DUT/fixture requirements.
- Surrogate power sources and hardware current limiting are used during development; no high-energy fault procedure is supplied.

### Derivation step 1

$$
P=VI;\quad E=\int V(t)I(t)dt
$$

Volt times ampere is W and integration gives J. Voltage/current timing skew biases products during transients; align or propagate it rather than multiply mismatched samples.

### Derivation step 2

$$
V_{DUT}=V_s-IR_h;\quad P_{loss}=I^2R_h
$$

For positive delivery current, harness resistance drops voltage and dissipates W. Kelvin sensing or calibrated correction changes uncertainty, not physical loss.

### Derivation step 3

$$
\dot{SOC}=-I_{dis}/(3600Q_{Ah})
$$

Positive discharge current decreases dimensionless SOC. Ah times 3600 converts capacity to coulombs; charging efficiency and chemistry need additional terms.

### Derivation step 4

$$
r_E=E_{in}-E_{out}-\Delta E_{stored}-E_{loss};\quad Var(P)\approx I^2Var(V)+V^2Var(I)+2 V I\,\operatorname{Cov}(V,I)
$$

The residual is J and should be assessed against joint calibration and loss uncertainty. Meter covariance and offset are retained, particularly at low current.

### Inference or simulation procedure

Represent the harness as a state machine with independently observed voltage/current and explicit fixture self-checks. Propagate meter gain, offset, sampling skew and harness resistance into power uncertainty. Compare repeated duty-cycle replays; a fault is diagnosed only with evidence separating DUT, stimulus and measurement paths.

### Validity domain and fidelity limits

Published EPS architectures do not supply this team’s wiring, limit settings or qualification requirements. State-of-charge models depend on chemistry, temperature and aging.

## 5. Data specifications and provenance

![E08 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| harness_state | enum | 1 | Local verification/simulation state. | Transition/interlock reason logged. |
| approved_limits | nullable<record> | V,A,K | Controlling DUT/fixture envelope. | Missing blocks stimulus-enabled acceptance. |
| source_dut_voltage | pair<float64> | V | Independent source/terminal observations. | Calibration and sense location required. |
| current | float64 | A | Signed delivered/discharge current. | Direction and path defined. |
| sample_clock | record | s | V/I acquisition timing and skew. | Common clock or offset covariance. |
| harness_resistance | nullable<float64> | ohm | Wiring/contact resistance. | Temperature/source and covariance retained. |
| energy_soc_output | record | J,1 | Ledger and optional SOC estimate. | Chemistry/capacity status; unsupported SOC null. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### NASA Small Spacecraft Power

[Product, archive or reference](https://www.nasa.gov/smallsat-institute/sst-soa/power-subsystems/)

**Fields:** DUT/harness revisions, requirement ID, UTC, four-wire voltage, current, load-state ID, temperatures, calibration certificates and event/abort records

**Access:** Public reference or archive pointer. Original team measurements are not supplied. Confirm product-level access, version and license; a linked paper does not imply its raw data are downloadable.

**Role:** Comparison/model context; prospective measurement schema is listed separately.

### GSFC-STD-7000 GEVS

[Product, archive or reference](https://standards.nasa.gov/standard/GSFC/GSFC-STD-7000)

**Fields:** Independent benchmark metadata, reference assumptions and calibration context; select actual products before execution.

**Access:** Public reference or archive pointer. Original team measurements are not supplied. Confirm product-level access, version and license; a linked paper does not imply its raw data are downloadable.

**Role:** Comparison/model context; prospective measurement schema is listed separately.

## 6. Uncertainty, sensitivity and identifiability

Meter gain/offset, sample skew, shunt temperature and wiring/contact resistance correlate with power. Fixture losses and DUT storage changes may be uncertain enough that residual attribution is ambiguous. Coulomb counting accumulates bias and depends on effective capacity, chemistry, temperature and age.

Use independently known surrogate loads to profile sensing versus wiring parameters, then replay duty cycles with gain/skew perturbations. A loss model must be calibrated separately before assigning unexplained energy to the DUT. Publish competing fault hypotheses and confidence, with missing controlled limits preventing claims of flight EPS qualification.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Source-only sensing | Simple fixture. | Cannot separate wiring drop. | Baseline diagnostic only. |
| Independent terminal/Kelvin sensing | Better DUT boundary accuracy. | Extra channels/calibration. | Choose if propagated terminal/power uncertainty improves. |
| Surrogate-first state-machine harness | Repeatable benign fault coverage. | Does not qualify battery behavior. | Development choice until controlled hardware requirements are supplied. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| E08-V1 | Resistive surrogate | V_DUT=Vs-IRh and harness loss I^2Rh. | Analytic low-energy/software fixture. | Circuit law. |
| E08-V2 | No current | Ideal power and resistance loss zero; meter offsets remain uncertainty. | Signed-current endpoint fixture. | Power identity. |
| E08-V3 | Missing limits/interlock | Stimulus-enabled transition rejected and logged. | State-machine integration fixture. | R1; no high-energy fault test. |
| E08-V4 | Known energy flow | Analytic constant-power duration closes ledger within propagated interval. | Replay source/storage/loss model. | Accounting conservation; measured closure TBD. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Proposed gate: measured power uncertainty <2% in the intended benign measurement range; explicitly exclude near-zero readings.
- Energy residual must lie within propagated uncertainty for reference loads.
- Inject software-side missing/out-of-order readings and verify fail-safe test termination in simulation.

## 9. Implementation and reproducible work packages

1. Create eps_harness_requirements.json with limit provenance and pending status.
2. Build local_harness_state_machine.py and interlock fixtures.
3. Implement surrogate_source_load.py with benign fault variants.
4. Create independent_meter_adapter.py and timing_calibration.py.
5. Build harness_loss_energy.py and chemistry_labeled_soc.py.
6. Publish repeated_replay.ipynb, fault_hypotheses.parquet and a fixture/DUT evidence matrix.

### Investigation sequence

1. Create pin-level interface and hazard-reviewed fixture design; derive benign surrogate tests.
2. Verify measurement uncertainty and harness self-test using reference resistive loads.
3. Run approved DUT cases and export signed traceability report with pass/fail/indeterminate outcomes.

### Resources and interfaces to expertise

- Electrical engineer, EPS owner and qualified integration/test personnel.
- Calibrated meters, four-wire fixture, protected low-energy sources, load surrogate and traceability software.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| Fixture drop called DUT undervoltage | Wrong fault label. | Independent terminal comparison. | Sense/correct actual DUT boundary. |
| V/I timing skew | Biased transient energy. | Skew-sensitive replay. | Synchronized acquisition/covariance. |
| Unknown limits accepted | Unsupported verification state. | Manifest/interlock validator. | Block transition until controlled limits exist. |

- A fixture can create the fault it claims to measure.
- Unexpected energy sources and wrong pin revisions must be retired in formal fixture review.

## 11. Required engineering outputs

- Versioned analysis configuration, raw-to-derived provenance and uncertainty report.
- Project-specific model comparison, a publication figure with units, and an explicit outcome including inconclusive findings.

### Scientific result figures to produce during execution

EPS/harness interface schematic and energy balance Sankey using measured data only after acquisition; prospective traceability matrix.

## 12. Cited technical and scientific resources

- [NASA Small Spacecraft Power](https://www.nasa.gov/smallsat-institute/sst-soa/power-subsystems/) — Power architecture context.
- [GSFC-STD-7000 GEVS](https://standards.nasa.gov/standard/GSFC/GSFC-STD-7000) — Environmental verification framework; mission tailoring is required.
- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — Requirements, interfaces and verification framework.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
