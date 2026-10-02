# D07 · ARES DUAL-WORLD SCOUT

**Original project:** Suborbital Uncrewed Aerial Vehicles for Earth Surveillance and Mars Exploration

**Session D:** Aeronautics

**Document class:** engineering research design and analysis record · **Revision:** 4 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session D](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_D.md) · [← D06](../D06-langley-mach-atlas/README.md) · [E01 →](../../E/E01-apollo-helioscope/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 4 | 3 | 7 | 2 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Mission profile

![D07 engineering mission profile: scientific question, hypothesis, model scope and evidence status](figures/mission-profile.svg)

| Profile panel | Engineering signal | Open the evidence |
| --- | --- | --- |
| Mission identity | Suborbital Uncrewed Aerial Vehicles for Earth Surveillance and Mars Exploration | [Scientific objective](#purpose-and-scientific-objective) |
| Model cockpit | 4 governing expressions; 4 derivation steps; declared assumptions and validity envelope | [Mathematical formulation](#4-mathematical-model-and-derivation) |
| Data blueprint | 7 proposed fields with types, units and quality rules | [Field map & downloads](data/README.md) |
| Verification queue | 4 proposed requirements; 3 specified cases; project execution evidence pending | [Case definitions](#8-verification-and-validation-cases) |
| Figure wall | Architecture, field map, planned result description | [Open full gallery](figures/README.md) |
| Resource library | 2 cited primary resources with support statements | [Cited resources](#12-cited-technical-and-scientific-resources) |

### Model cockpit

**Analysis method:** Create separate Earth and Mars concept-of-operations diagrams with science traceability. Model sensing geometry and trajectory envelopes using public environmental information and documented aerodynamic data. Compare fixed-wing, rotorcraft, and passive descent only at concept level, including packaging/deployment and communications uncertainty. Use Monte Carlo mission outcomes to estimate usable science return and identify architecture features that are common versus environment-specific.

**Operating envelope:** ARES was a mission concept, not a flown Mars airplane. Concept trade scores depend on requirements and assumptions, and local test flights do not establish entry/deployment or Mars thermal qualification.

**Variables and conventions**

- Vehicle mass, wing/rotor dimensions, lift/drag model, local atmosphere, gravity, flight/trajectory duration, and scientific footprint.
- Sensor resolution, calibration, pointing, onboard processing, communications availability, deployment success, and data-return probability.

### Artifact wall

![D07 proposed analysis architecture](figures/architecture.svg)

Environment-specific trajectory and sensing branches feed a dependent data-return model. The diagram separates concept delivery assumptions from usable science and does not transfer Earth validation into Mars qualification.

**Scientific result to produce:** Separate Earth and Mars mission timelines show delivery and aerial sensing phases; a mass–energy–science-return Pareto plot displays uncertainty and shared interface opportunities.

### Investigation feed · planned work

The feed records proposed work packages. A row becomes executed evidence only with versioned inputs, outputs and a reviewed result.

| Sequence | Evidence state | Engineering work package |
| --- | --- | --- |
| 01 | Planned | Create earth_conops.yaml and mars_conops.yaml separately. |
| 02 | Planned | Build science_traceability.csv and authorized-observation constraints. |
| 03 | Planned | Implement environment_adapter.py and aerodynamic_domain_checker.py. |
| 04 | Planned | Create sensor_footprint.py with GSD/blur fixtures. |
| 05 | Planned | Build subsystem_energy.py and dependent_return_tree.py. |
| 06 | Planned | Publish mission_pareto.ipynb and concept_results.parquet with TBD probabilities and delivery-interface gates. |

### Mission connections

Connections are reading routes based on actual shared resources, supplied sessions or included illustrations. They do not establish physical dependencies, team collaborations or validated results.

| Connected mission | Original investigation | Recorded connection basis |
| --- | --- | --- |
| [E07 · DISCOVERY TRIDENT](../../E/E07-discovery-trident/README.md) | Glendale Community College (GCC) ASCEND Team | [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) |
| [E08 · GATEWAY POWERBENCH](../../E/E08-gateway-powerbench/README.md) | EagleSat Team: Development and Implementation of a Self-Contained Harness for In-House Integration, Verification, and Testing of CubeSat Electric Power Systems | [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) |
| [G07 · HUBBLE SPECTRAL ANCHOR](../../G/G07-hubble-spectral-anchor/README.md) | An Introduction to Systems Engineering: Building a Monochromator Mount | [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) |
| [I04 · ORION SENTINEL CORE](../../I/I04-orion-sentinel-core/README.md) | EagleSat Team: On-board Computer Subsystem | [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) |
| [I06 · SATURN LOADPATH](../../I/I06-saturn-loadpath/README.md) | Designing and Exploring the Structure of Launch Vehicles to Create Optimal Theoretical and Small-Scale Experimental Models | [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) |
| [I10 · GEMINI POINTLOCK](../../I/I10-gemini-pointlock/README.md) | Spacecraft Attitude Control Implementation and Development | [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) |

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

Proposed mission: compare scientific Earth-observation and Mars-atmosphere vehicle concepts under explicit mission requirements. Preserve the supplied suborbital term by separating a suborbital delivery/trajectory phase from atmosphere-supported aerial operation. A single Earth vehicle cannot be presumed transferable to Mars: gravity, density, pressure, Reynolds number, deployment, communications, and recovery constraints all differ.

**Question:** Which mission architectures deliver the greatest verified scientific information per mass, energy, and operational risk for Earth sensing and Mars exploration?

**Testable hypothesis:** An atmosphere-specific design with common software and sensor-interface principles will outperform a single shared airframe concept once environmental and deployment constraints are included.

## 1. Design basis and analysis boundary

The project maintains separate Earth environmental-observation and Mars exploration concepts of operations. Its system boundary includes sensing geometry, atmosphere-compatible flight/descent envelope, energy, packaging/deployment and data return. Suborbital delivery remains a concept-level external interface with its own verification gate; no launch or propulsion construction is specified.

Begin with science footprint and usable-data criteria, then compare fixed-wing, rotorcraft and passive descent under environment-specific density, gravity and thermal assumptions. Historical ARES studies inform concept trades but do not represent a flown Mars airplane. Earth tests can validate local sensing/software interfaces without qualifying Mars deployment or atmosphere.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| D07-R1 | Every concept shall trace a science observable to footprint, calibration and successful data return. | Flight duration alone does not measure science value. | Audit measurement-to-mission requirement links. | Systems-engineering traceability. |
| D07-R2 | Earth/Mars aerodynamic transfer shall retain Re, Mach, gravity and dynamic-similarity limitations. | Matching one nondimensional number is insufficient. | Compare declared regime envelopes and incompatible branches. | Concept-analysis requirement. |
| D07-R3 | Energy accounting shall include payload, avionics and thermal demand as well as propulsion. | Thin-atmosphere concepts can hide support loads. | Integrate a time-resolved ledger; proposed closure target 0.1%. | Proposed numerical target, not mission reserve requirement. |
| D07-R4 | Proposed science-return criterion: only calibrated observations meeting resolution and data-delivery gates count as usable. | Raw acquisition is not verified returned science. | Monte Carlo event tree with separate sensing and return outcomes. | Proposed metric; probabilities TBD. |

## 3. Architecture and controlled interfaces

A science registry defines authorized environmental observables and spatial/temporal resolution. Separate Earth/Mars environment adapters supply density, viscosity, gravity and sound speed. Concept trajectory adapters provide position/attitude/time and compatible aerodynamic envelopes rather than detailed launch design.

A sensor forward model computes ground footprint and blur; an energy ledger accumulates subsystem loads. Deployment and communications event trees retain dependency assumptions. The mission scorer returns several objectives—usable data, mass, energy and failure probability—before any explicitly stated weighting, preserving privacy/airspace constraints for Earth operations.

![D07 engineering architecture](figures/architecture.svg)

Environment-specific trajectory and sensing branches feed a dependent data-return model. The diagram separates concept delivery assumptions from usable science and does not transfer Earth validation into Mars qualification.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

```text
L=0.5 rho V^2 S C_L; D=0.5 rho V^2 S C_D; level-flight baseline requires L approximately mg.
```

```text
Re=rho V c/mu; M=V/a; aerodynamic transfer requires both similarity and compatible operating regimes.
```

```text
E_mission=integral P_prop(t)dt+E_payload+E_avionics+E_thermal.
```

```text
J=expected information gain/(mass*energy) is one proposed normalized metric; report separate objectives to avoid arbitrary weighted rankings.
```

### Variables, units and conventions

- Vehicle mass, wing/rotor dimensions, lift/drag model, local atmosphere, gravity, flight/trajectory duration, and scientific footprint.
- Sensor resolution, calibration, pointing, onboard processing, communications availability, deployment success, and data-return probability.

### Assumptions and boundary conditions

- Earth surveillance means authorized environmental/scientific observation with privacy and airspace constraints.
- Suborbital delivery and atmospheric flight use different models and verification gates; the current project does not provide launch hardware or propulsion design instructions.

### Derivation step 1

$$
V_{min}=\sqrt{2mg/(\rho SC_{L,max})}
$$

The level-flight lift balance yields a screening speed, conditional on supported C_L,max. It is not an envelope for rotorcraft or suborbital motion.

### Derivation step 2

$$
Re=\rho Vc/\mu;\quad M=V/a
$$

The same geometry/speed in different atmospheres changes both flow regimes. Gravity and inertia additionally affect maneuver/descent similarity.

### Derivation step 3

$$
GSD\approx Hp/f;\quad b\approx v_{ground}t_{exp}/GSD
$$

For a nadir small-angle imager, pixel pitch p and focal length f give ground sampling distance. Blur b is in pixels; terrain and attitude need extensions.

### Derivation step 4

$$
E=\int(P_{prop}+P_{payload}+P_{avionics}+P_{thermal})dt
$$

All powers are W and integration is J. Usable science expectation sums observation quality times conditional acquisition/return probability; dependent failures require joint event trees.

### Inference or simulation procedure

Create separate Earth and Mars concept-of-operations diagrams with science traceability. Model sensing geometry and trajectory envelopes using public environmental information and documented aerodynamic data. Compare fixed-wing, rotorcraft, and passive descent only at concept level, including packaging/deployment and communications uncertainty. Use Monte Carlo mission outcomes to estimate usable science return and identify architecture features that are common versus environment-specific.

### Validity domain and fidelity limits

ARES was a mission concept, not a flown Mars airplane. Concept trade scores depend on requirements and assumptions, and local test flights do not establish entry/deployment or Mars thermal qualification.

## 5. Data specifications and provenance

![D07 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| concept_id | string | 1 | Earth or Mars architecture/version. | Environment and external delivery boundary explicit. |
| environment_profile | record | SI | Density, viscosity, gravity and sound speed. | Source/domain and covariance retained. |
| trajectory_state | array<time,position,attitude> | s,m,rad | Concept sensing path. | Frame and time origin required. |
| aero_envelope | record | 1 | Supported coefficient/Re/M range. | No extrapolated capability treated validated. |
| sensor_geometry | record | m,s | Pixel pitch, focal length and exposure. | Calibration/resolution requirement included. |
| subsystem_power | array<record> | W | Time-resolved load ledger. | Missing support load flagged, not zero. |
| return_event_tree | record | 1 | Deployment/acquisition/communication dependencies. | Probability provenance or TBD status required. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### NASA ARES mission-concept research

[Product, archive or reference](https://ntrs.nasa.gov/citations/20080030375)

**Fields:** Atmospheric science mission context, design trade history, and simulated Mars airplane performance.

**Access:** Public NASA paper; use as a historical concept benchmark, not current flight readiness.

**Role:** Mars aerial-system architecture precedent.

### NASA systems-engineering resource

[Product, archive or reference](https://www.nasa.gov/reference/systems-engineering-handbook/)

**Fields:** Mission requirements, architecture trade, verification, and configuration concepts.

**Access:** Public official handbook; not a vehicle flight dataset.

**Role:** Traceable mission-design framework.

## 6. Uncertainty, sensitivity and identifiability

Atmospheric profiles, aerodynamic coefficients, deployment success and communications availability are uncertain and often dependent. Sensor calibration and attitude affect usable science independently of vehicle survival. Mars thermal loads and packaging discrepancy cannot be inferred from a convenient Earth flight test.

Sample environment and subsystem uncertainties jointly, retaining scenario provenance. Sensitivity ranks reveal whether improved payload resolution is useful when data return dominates failure. Report Pareto sets and absolute outcomes before any ratio score; uncertainty in very small denominators makes information-per-energy ratios unstable and unsuitable as sole selectors.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Fixed-wing concept | Potential broad coverage. | Deployment and low-density lift demands. | Choose only if supported aero/packaging envelope meets science. |
| Rotorcraft concept | Localized controllable observations. | Power and thin-atmosphere complexity. | Compare useful data under independently sourced envelope. |
| Passive descent concept | Simple propulsion boundary. | Limited path control and revisit. | Use when footprint/return gates are met without maneuver requirements. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| D07-V1 | Level-flight scaling | At fixed mass/area/C_L, required speed scales rho^-1/2. | Compare analytic Earth/Mars scenario ratios. | Lift-balance identity. |
| D07-V2 | Zero mission duration | Integrated variable energy is zero; fixed deployment cost remains separately recorded. | Ledger endpoint fixture. | Energy-boundary definition. |
| D07-V3 | Certain/failed return | Conditional return probability one preserves acquired usable data; zero returns none. | Event-tree synthetic extremes. | Probability accounting; real probabilities TBD. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Validate atmosphere and sensing calculations against known limiting cases and documented instrument characteristics.
- Require architecture ranking to remain interpretable under mass, density, wind, communication, and deployment sensitivity sweeps.
- Use hardware-in-the-loop or simulated mission rehearsals to test data integrity and failure recovery before any authorized field activity.

## 9. Implementation and reproducible work packages

1. Create earth_conops.yaml and mars_conops.yaml separately.
2. Build science_traceability.csv and authorized-observation constraints.
3. Implement environment_adapter.py and aerodynamic_domain_checker.py.
4. Create sensor_footprint.py with GSD/blur fixtures.
5. Build subsystem_energy.py and dependent_return_tree.py.
6. Publish mission_pareto.ipynb and concept_results.parquet with TBD probabilities and delivery-interface gates.

### Investigation sequence

1. Define two separate proposed science objectives and environmental operating envelopes.
2. Decompose delivery, deployment, aerial sensing, communications, and recovery/end-of-mission interfaces.
3. Evaluate architecture trades using uncertainty ranges, science resolution, and probability of usable data return.
4. Produce an authorization-aware demonstration roadmap with independent ground, contained, and approved flight stages appropriate to each concept.

### Resources and interfaces to expertise

- Aerodynamics, mission design, environmental remote sensing, communications, and qualified aviation/facility collaborators.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| Earth test overgeneralized | False Mars qualification. | Similarity/domain audit. | Separate validation claims. |
| Support loads omitted | Underestimated energy/mass. | Subsystem ledger completeness. | Named payload/thermal/avionics entries. |
| Science acquired equated returned | Inflated mission value. | Return-event audit. | Count only data meeting delivery and calibration gates. |

- Mislabeling ordinary atmospheric flight as suborbital can obscure incompatible requirements.
- Atmospheric uncertainty and deployment reliability may dominate idealized aerodynamic performance.

## 11. Required engineering outputs

- Dual-world concept study, science-to-requirement matrix, mass/energy/data budgets, mission-return trade map, and staged verification roadmap.

### Scientific result figures to produce during execution

Separate Earth and Mars mission timelines show delivery and aerial sensing phases; a mass–energy–science-return Pareto plot displays uncertainty and shared interface opportunities.

## 12. Cited technical and scientific resources

- [Design of a Mars Airplane Propulsion System for the ARES Mission Concept](https://ntrs.nasa.gov/citations/20080030375) — Original NASA aerial Mars mission concept and historical system trade context.
- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — Official mission-to-requirement, trade, verification, and lifecycle framework.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
