# C06 · PULSAR GEMINI WATCH

**Original project:** The First Magnetar in a Binary System?

**Session C:** Astronomy & Space Physics

**Document class:** engineering research design and analysis record · **Revision:** 4 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session C](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_C.md) · [← C05](../C05-kepler-worldforge/README.md) · [C07 →](../C07-artemis-memory-bridge/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 5 | 4 | 7 | 2 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Mission profile

![C06 engineering mission profile: scientific question, hypothesis, model scope and evidence status](figures/mission-profile.svg)

| Profile panel | Engineering signal | Open the evidence |
| --- | --- | --- |
| Mission identity | The First Magnetar in a Binary System? | [Scientific objective](#purpose-and-scientific-objective) |
| Model cockpit | 3 governing expressions; 4 derivation steps; declared assumptions and validity envelope | [Mathematical formulation](#4-mathematical-model-and-derivation) |
| Data blueprint | 7 proposed fields with types, units and quality rules | [Field map & downloads](data/README.md) |
| Verification queue | 5 proposed requirements; 4 specified cases; project execution evidence pending | [Case definitions](#8-verification-and-validation-cases) |
| Figure wall | Architecture, field map, planned result description | [Open full gallery](figures/README.md) |
| Resource library | 2 cited primary resources with support statements | [Cited resources](#12-cited-technical-and-scientific-resources) |

### Model cockpit

**Analysis method:** Build phase-tagged radio and X-ray/gamma-ray likelihoods with exposure windows and nondetections. Compare models through a latent state defined by characteristic-radius ordering; add free-free radio absorption and variable Be-star outflow. Fit orbital ephemeris and superorbital modulation as nuisance parameters. Quantify whether rotational, accretion, or magnetic energy can support observed luminosity under uncertainty. Use localization and population priors to compare burst association with a chance line-of-sight source. Predict a future orbit before assessing its observations.

**Operating envelope:** A detection of pulsations identifies rotation, not magnetic-energy dominance. Radius formulae depend on geometry; sparse detections and strong absorption make state assignment uncertain.

**Variables and conventions**

- P in s and period derivative in s s^-1. Pdot_spin is total physical spin evolution after kinematic correction; Pdot_dipole is its separately identified isolated-dipole component.
- Magnetospheric, corotation, and light-cylinder radii in cm
- Magnetic moment mu in G cm^3; accretion rate in g s^-1
- I in g cm^2; positive rotational-energy loss in erg s^-1, assuming approximately constant I.
- xi parametrizes uncertain magnetosphere coupling; the field estimate assumes isolated dipole braking

### Artifact wall

![C06 proposed analysis architecture](figures/architecture.svg)

Timing corrections, conditional radius states and burst association contribute distinct evidence; the graph does not equate pulsations with a confirmed magnetar.

**Scientific result to produce:** Orbital phase versus inferred emission state with radius-ordering bands, radio visibility, and uncertainty in burst association.

### Investigation feed · planned work

The feed records proposed work packages. A row becomes executed evidence only with versioned inputs, outputs and a reviewed result.

| Sequence | Evidence state | Engineering work package |
| --- | --- | --- |
| 01 | Planned | Create timing/response/localization manifests for source-cited observations. |
| 02 | Planned | Implement orbital-phase sampling and arrival-time correction fixtures. |
| 03 | Planned | Build count-domain broadband and nondetection likelihoods. |
| 04 | Planned | Implement characteristic-radius and energy-budget modules with typed torque terms. |
| 05 | Planned | Fit competing state/absorption hypotheses using common data. |
| 06 | Planned | Publish future-orbit predictions, association sensitivities and conditional field summaries. |

### Mission connections

Connections are reading routes based on actual shared resources, supplied sessions or included illustrations. They do not establish physical dependencies, team collaborations or validated results.

| Connected mission | Original investigation | Recorded connection basis |
| --- | --- | --- |
| [C05 · KEPLER WORLDFORGE](../C05-kepler-worldforge/README.md) | Exoplanet Classification using Data Mining | Session C |
| [C07 · ARTEMIS MEMORY BRIDGE](../C07-artemis-memory-bridge/README.md) | Taperings and Analytic Continuations of Supernova Gravitational Waves with Memory | Session C |
| [C04 · HORIZON TIDAL ECHO](../C04-horizon-tidal-echo/README.md) | A Deep Look at the Nature of Black Holes: Using Tidal Disruption Events to See the Unseeable | Session C |
| [C08 · MARS NILI SPECTRAL VAULT](../C08-mars-nili-spectral-vault/README.md) | Laboratory Analysis of olivine-carbonate mixtures as observed on Mars | Session C |
| [C03 · TAURUS MOLECULE TRAIL](../C03-taurus-molecule-trail/README.md) | HCN Mapping of the Taurus Molecular Cloud | Session C |
| [C09 · EAGLESAT COSMIC PIXEL](../C09-eaglesat-cosmic-pixel/README.md) | EagleSat Team: Determining Particle Energy Using CMOS Sensors | Session C |

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

Reframe the historical question as a hypothesis comparison for the gamma-ray binary LS I +61 303. Reported radio pulsations support a rotating neutron star, while magnetar-like bursts and a flip-flop interpretation require additional evidence. Keep ordinary pulsar-wind and accretion/propeller explanations alongside magnetic-energy-powered activity; the project will not label a magnetar as confirmed merely because a short burst occurred nearby.

**Question:** Can phase-resolved timing, burst localization, and broadband emission distinguish a magnetar-like neutron star from other compact-object models in LS I +61 303?

**Testable hypothesis:** A phase-dependent ejector/propeller model with physically consistent energy budgets will predict radio visibility and high-energy variability better than a phase-independent emitter, but magnetic field strength may remain weakly identified.

## 1. Design basis and analysis boundary

This design compares compact-object energy and state hypotheses for LS I +61 303. Radio pulsations are evidence for a rotating neutron star; they do not establish magnetic-energy-powered activity. The system boundary includes event times, count spectra, orbital ephemerides, observing windows and burst localization, with magnetar, pulsar-wind and accretion/propeller branches retained.

The initial model is phase-resolved observed emission, followed by radius-ordering state hypotheses and energy-budget checks. Dipole-field inference is permitted only as a conditional calculation when intrinsic spin-down is separated from orbital acceleration and interaction torques. Raw radio accessibility, orbital timing accuracy and burst association probability remain TBD. The deliverable can identify which future observations discriminate hypotheses without claiming a confirmed binary magnetar.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| C06-R1 | Spin timing shall include barycentric and orbital corrections or explicitly retain their uncertainty. | Apparent period derivatives can be orbital. | Timing residual and injected acceleration tests. | Radio-pulsation primary study establishes target evidence. |
| C06-R2 | Burst association shall be probabilistic using localization and competing source density. | A nearby short burst is not unique target identification. | Localization likelihood normalization and offset-source fixtures. | Proposed association requirement. |
| C06-R3 | State predictions shall report uncertainty in all three characteristic radii. | A deterministic ordering conceals mass-flow/field ambiguity. | Posterior radius-ordering table. | Proposed state-contract requirement. |
| C06-R4 | Dipole B shall be labeled conditional whenever torque decomposition is unavailable. | Isolated braking assumptions need not hold in a binary. | Parameter provenance and report-rule audit. | Existing governing model caveat. |
| C06-R5 | A future orbit shall be held out for phase-resolved prediction. | Within-orbit fitting can overfit absorption and state changes. | Freeze ephemeris/model before holdout. | Proposed temporal validation. |

## 3. Architecture and controlled interfaces

A timing adapter emits corrected arrival times, exposure windows and instrumental timing offsets. A high-energy adapter preserves photon counts, background and response; burst localization enters a spatial likelihood rather than an automatic target label. An ephemeris service propagates orbital-phase covariance and superorbital nuisance terms.

The state engine samples compact-object mass, spin, magnetic moment, mass inflow and coupling xi, producing posterior probabilities for radius orderings. Energy modules predict rotational or accretion budgets and compare them with bolometric emission under distance/beaming uncertainty. A radio absorption branch modifies detection probability. Nondetection can therefore reflect unavailable exposure or absorption, not absence of the neutron star or a unique change in state.

![C06 engineering architecture](figures/architecture.svg)

Timing corrections, conditional radius states and burst association contribute distinct evidence; the graph does not equate pulsations with a confirmed magnetar.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

$$
r_{\rm lc}=cP/(2\pi);\quad r_{\rm co}=(GMP^2/4\pi^2)^{1/3}
$$

$$
r_m=\xi[\mu^4/(2GM\dot M^2)]^{1/7}
$$

$$
-dE_{\rm rot}/dt=4\pi^2I\dot P_{\rm spin}/P^3;\quad B_{\rm dip}\approx3.2\times10^{19}\sqrt{P\dot P_{\rm dipole}}\ \mathrm G
$$

### Variables, units and conventions

- P in s and period derivative in s s^-1. Pdot_spin is total physical spin evolution after kinematic correction; Pdot_dipole is its separately identified isolated-dipole component.
- Magnetospheric, corotation, and light-cylinder radii in cm
- Magnetic moment mu in G cm^3; accretion rate in g s^-1
- I in g cm^2; positive rotational-energy loss in erg s^-1, assuming approximately constant I.
- xi parametrizes uncertain magnetosphere coupling; the field estimate assumes isolated dipole braking

### Assumptions and boundary conditions

- Do not apply the isolated-dipole field formula as a measurement when orbital acceleration or propeller torques contaminate Pdot.
- Treat burst-source association probabilistically, accounting for instrumental localization.

### Derivation step 1

$$
r_{lc}=cP/(2\pi),\quad r_{co}=(GMP^2/4\pi^2)^{1/3}
$$

The light-cylinder radius follows rotation at c; corotation follows equality of Kepler frequency and spin. Use seconds and cgs consistently.

### Derivation step 2

$$
r_m=\xi(\mu^4/2GM\dot M^2)^{1/7}
$$

The pressure-balance scaling is geometry dependent. Sample xi and mass flow rather than treating r_m as a directly observed surface.

### Derivation step 3

$$
\dot P_{\rm spin}=\dot P_{\rm obs}-Pa_{\rm los}/c-\dot P_{\rm other\,kin};\quad \dot P_{\rm spin}=\dot P_{\rm dipole}+\dot P_{\rm interaction}
$$

Remove orbital and other justified kinematic terms to define total physical spin evolution. Interaction torque is physical spin change and is not removed from the rotational-energy loss. An isolated-dipole field estimate uses only a separately identified dipole contribution and remains conditional when torques are degenerate.

### Derivation step 4

$$
-dE_{\rm rot}/dt=4\pi^2I\dot P_{\rm spin}/P^3
$$

For approximately constant inertia, positive total spin-down gives a positive rotational-energy loss; all physical torques contribute. Compare with emission only after distance, beaming and inertia uncertainty are considered. If inertia changes, include the corresponding dI/dt term.

### Inference or simulation procedure

Build phase-tagged radio and X-ray/gamma-ray likelihoods with exposure windows and nondetections. Compare models through a latent state defined by characteristic-radius ordering; add free-free radio absorption and variable Be-star outflow. Fit orbital ephemeris and superorbital modulation as nuisance parameters. Quantify whether rotational, accretion, or magnetic energy can support observed luminosity under uncertainty. Use localization and population priors to compare burst association with a chance line-of-sight source. Predict a future orbit before assessing its observations.

### Validity domain and fidelity limits

A detection of pulsations identifies rotation, not magnetic-energy dominance. Radius formulae depend on geometry; sparse detections and strong absorption make state assignment uncertain.

## 5. Data specifications and provenance

![C06 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| arrival_epoch | float64[] | TDB seconds or MJD | Barycentric event times. | Original clock and correction files required. |
| orbital_phase | posterior<float64> | cycle | Phase from a versioned ephemeris. | Wrap consistently; preserve phase covariance. |
| spin_period | measurement<float64> | s | Observed/corrected period with detection context. | Nondetection has no artificial zero period. |
| period_derivative | measurement<float64>&#124;null | s s^-1 | Derivative with explicit intrinsic/observed type. | Do not assign intrinsic type without torque/acceleration treatment. |
| count_spectrum | struct<count,response> | count | Energy-resolved source/background counts. | Poisson likelihood; response and exposure mandatory. |
| burst_localization | distribution<sky> | degree ICRS | Spatial source likelihood. | Normalize and include instrumental systematic uncertainty. |
| radius_ordering | posterior<enum> | 1 | State probability from lc/co/m radii. | Report multimodal state probabilities. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### Weng et al. radio-pulsation publication

[Product, archive or reference](https://arxiv.org/abs/2203.09423)

**Fields:** Pulsation period, observing epochs, significance, timing methods

**Access:** Open paper; availability of raw FAST observations must be established.

**Role:** Neutron-star timing evidence.

### Swift and other HEASARC holdings

[Product, archive or reference](https://heasarc.gsfc.nasa.gov/docs/archive.html)

**Fields:** Burst localization, count spectra, event times, exposure, response

**Access:** Public archive discovery; match observation IDs and instrument calibration.

**Role:** Independent high-energy state and association tests.

## 6. Uncertainty, sensitivity and identifiability

Magnetic moment and mass inflow enter r_m in opposing combinations, while orbital absorption can mimic radio state transitions. Luminosity depends on distance and beaming; accretion rates inferred from that luminosity are model dependent. Jointly sample those terms and report whether radius ordering is data constrained or prior dominated. Orbital phase uncertainty matters most near a proposed rapid transition.

Burst-source association introduces a separate uncertainty from compact-object physics. Vary the localization systematic and chance-source prior without changing the pulse likelihood. Test field identifiability by adding synthetic intrinsic spin-down while sweeping orbital acceleration errors. If equivalent timing fits span ordinary and magnetar-strength fields, retain the field range as conditional and prioritize torque-discriminating observations.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Phase-only phenomenology | Fits broadband observations with few assumptions. | Does not explain energy source. | Use as prediction baseline. |
| Pulsar-wind/absorption model | Connects rotation and orbit-dependent detectability. | Outflow geometry and shock emission uncertain. | Prefer when independently constrained wind behavior predicts holdout data. |
| Accretion/propeller or magnetic state model | Tests radius transitions and energy budget. | Mass flow, torques and field are degenerate. | Retain alternatives unless independent timing/energy evidence discriminates. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| C06-V1 | Zero acceleration | Corrected timing recovers an injected intrinsic period derivative. | Synthetic arrivals through known orbit. | Timing-decomposition identity. |
| C06-V2 | Localization offset | Association probability decreases for a source moved away from target under a fixed uncertainty model. | Integrate synthetic localization maps and competing-source hypotheses. | Normalized spatial likelihood. |
| C06-V3 | Radius limits | r_m grows as mass flow decreases and r_lc scales linearly with P. | Parameter-sweep analytic checks. | Displayed characteristic-radius equations. |
| C06-V4 | Unseen orbit | Phase-resolved detection/count predictions are evaluated without updated state thresholds. | Temporal holdout with recorded exposure. | Proposed independent prediction. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Hold out complete orbits and score flux and detection-probability predictions.
- Use noise-only and injected periodic signals to estimate timing false-alarm rates with the full search trials.
- Reassess burst association under alternative localization and background-source priors; publish inconclusive Bayes factors.

## 9. Implementation and reproducible work packages

1. Create timing/response/localization manifests for source-cited observations.
2. Implement orbital-phase sampling and arrival-time correction fixtures.
3. Build count-domain broadband and nondetection likelihoods.
4. Implement characteristic-radius and energy-budget modules with typed torque terms.
5. Fit competing state/absorption hypotheses using common data.
6. Publish future-orbit predictions, association sensitivities and conditional field summaries.

### Investigation sequence

1. Freeze system identity, ephemeris priors, and alternative physical models.
2. Retrieve available event products and reproduce a published phase-folded light curve.
3. Fit timing and luminosity jointly with orbital and absorption uncertainty.
4. Generate phase-specific follow-up predictions that distinguish competing state transitions.

### Resources and interfaces to expertise

- HEASoft, radio timing tools, Bayesian state modeling, high-energy and binary-star expertise.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| Apparent Pdot treated as intrinsic | Unsupported magnetar field claim. | Timing residual correlates with orbital phase. | Fit acceleration and torque alternatives. |
| Burst attached by proximity | False source association. | Localization/alternative-source likelihood. | Carry association probability into hypothesis comparison. |
| Radio nondetection treated as absence | Misclassified state. | Exposure and absorption diagnostics. | Model detectability jointly with intrinsic emission. |

- Timing noise, absorption, and burst-position uncertainty can preserve multiple viable interpretations.

## 11. Required engineering outputs

- Evidence ledger, phase-state probability map, energy-budget comparison, and falsifiable observation plan.

### Scientific result figures to produce during execution

Orbital phase versus inferred emission state with radius-ordering bands, radio visibility, and uncertainty in burst association.

## 12. Cited technical and scientific resources

- [Torres et al. (2011), magnetar-like event and binary hypothesis](https://arxiv.org/abs/1109.5008) — Original hypothesis and flip-flop motivation.
- [Weng et al. (2022), radio pulsations](https://arxiv.org/abs/2203.09423) — Evidence for a rotating neutron star, not definitive magnetar classification.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
