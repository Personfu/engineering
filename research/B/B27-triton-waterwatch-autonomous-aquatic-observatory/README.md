# B27 · TRITON WATERWATCH — Autonomous Aquatic Observatory

**Original project:** Aquatic Data Analysis from Deployable, Autonomous Boat

**Session B:** Earth & Environmental Engineering

**Document class:** engineering research design and analysis record · **Revision:** 4 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session B](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_B.md) · [← B26](../B26-helios-powerloop-solar-electrolysis-dispatch/README.md) · [B28 →](../B28-astra-biocycle-microalgal-methane-and-net-energy/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 4 | 4 | 8 | 3 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Mission profile

![B27 engineering mission profile: scientific question, hypothesis, model scope and evidence status](figures/mission-profile.svg)

| Profile panel | Engineering signal | Open the evidence |
| --- | --- | --- |
| Mission identity | Aquatic Data Analysis from Deployable, Autonomous Boat | [Scientific objective](#purpose-and-scientific-objective) |
| Model cockpit | 3 governing expressions; 4 derivation steps; declared assumptions and validity envelope | [Mathematical formulation](#4-mathematical-model-and-derivation) |
| Data blueprint | 8 proposed fields with types, units and quality rules | [Field map & downloads](data/README.md) |
| Verification queue | 4 proposed requirements; 4 specified cases; project execution evidence pending | [Case definitions](#8-verification-and-validation-cases) |
| Figure wall | Architecture, field map, planned result description | [Open full gallery](figures/README.md) |
| Resource library | 3 cited primary resources with support statements | [Cited resources](#12-cited-technical-and-scientific-resources) |

### Model cockpit

**Analysis method:** Audit boat logs, GPS timestamps, calibration and response times, then align sensor streams and reject unsupported corrections. Design baseline stratified transects and an adaptive alternative using a Gaussian process or robust spatial interpolator. Pair measurements with independent reference samples and depth profiles where permitted. Propagate sensor, position, drift and interpolation errors into maps; retain blank/flagged areas instead of silently filling all water surfaces.

**Operating envelope:** Spatial covariance may change rapidly with inflows, mixing or blooms. Optical/conductivity proxies cannot establish specific contaminants without validated chemistry; repeated trajectories do not supply independent reference truth.

**Variables and conventions**

- Temperature: °C; conductivity: μS/cm with reference temperature stated.
- DO: mg/L and saturation percent using documented compensation.
- Position: projected m; dead-time t_dead and response tau_response: s; depth: m.
- Energy: Wh; uncertainty: parameter-specific physical units.

### Artifact wall

![B27 proposed analysis architecture](figures/architecture.svg)

The diagram makes time, sensor response and depth part of the observation operator and compares routes within simulator constraints. Its maps remain near-surface and time-supported unless independent profiles and chemistry extend the evidence.

**Scientific result to produce:** Display measured tracks/depths, parameter maps and uncertainty; compare adaptive/uniform coverage with independent reference residuals.

### Investigation feed · planned work

The feed records proposed work packages. A row becomes executed evidence only with versioned inputs, outputs and a reviewed result.

| Sequence | Evidence state | Engineering work package |
| --- | --- | --- |
| 01 | Planned | Create platform/sensor/clock/depth calibration manifests and permitted survey constraints. |
| 02 | Planned | Implement time-position alignment with offset and GPS covariance. |
| 03 | Planned | Build first-order/dead-time response diagnostics and qualified correction artifacts. |
| 04 | Planned | Generate fixed/adaptive equal-budget survey simulations. |
| 05 | Planned | Fit supported spatial models and independent transect/reference holdout reports. |
| 06 | Planned | Release depth/time support masks, uncertainty maps and contaminant-interpretation limits. |

### Mission connections

Connections are reading routes based on actual shared resources, supplied sessions or included illustrations. They do not establish physical dependencies, team collaborations or validated results.

| Connected mission | Original investigation | Recorded connection basis |
| --- | --- | --- |
| [B26 · HELIOS POWERLOOP — Solar Electrolysis Dispatch](../B26-helios-powerloop-solar-electrolysis-dispatch/README.md) | Electrolytic Application of Load-Managing Photovoltaic System | Session B |
| [B28 · ASTRA BIOCYCLE — Microalgal Methane and Net Energy](../B28-astra-biocycle-microalgal-methane-and-net-energy/README.md) | Biogas Production from Microalgae following Freeze-Heat Pretreatment | Session B |
| [B25 · SEEDSTAR GENESIS — Dryland Establishment Forecasting](../B25-seedstar-genesis-dryland-establishment-forecasting/README.md) | Can We Predict Germination Success in Seed Pellets Using Seed Traits? | Session B |
| [B24 · VIPER VOYAGER — Urban Movement and Habitat Connectivity](../B24-viper-voyager-urban-movement-and-habitat-connectivity/README.md) | Using GIS to Quantify Effects of Land Cover Change on Movement Patterns of Tiger Rattlesnakes in an Urbanizing Environment | Session B |
| [B23 · HYDRA MISSION CONTROL — Watershed Decisions Under Uncertainty](../B23-hydra-mission-control-watershed-decisions-under-uncertainty/README.md) | Modeling to Make a Difference: Hydrologic Analysis for Improved Decision Support | Session B |
| [B22 · NIF ODYSSEY — Comparative Nitrogen-Fixation Evolution](../B22-nif-odyssey-comparative-nitrogen-fixation-evolution/README.md) | Developing a model system using Azotobacter vinelandii to investigate the evolution of nitrogen fixation | Session B |

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

Design a quality-controlled aquatic survey and analysis system for an autonomous surface platform. Couple calibration, time synchronization and spatial sampling with uncertainty-aware maps. Distinguish surface measurements from whole-water-column conditions; a dense trajectory can still be biased if sensor response, stratification or calibration drift are ignored.

**Question:** Which survey strategy most efficiently reduces uncertainty in temperature, conductivity, dissolved oxygen and selected water-quality gradients?

**Testable hypothesis:** Adaptive sampling informed by validated spatial covariance may outperform uniform transects under patchy conditions, but calibration drift and sensor lag can erase that advantage.

## 1. Design basis and analysis boundary

The aquatic survey system combines autonomous-surface-platform logs, sensor calibration, position/time synchronization and independent water references. It produces supported near-surface maps at stated depth and time, rather than whole-water-column chemistry or contaminant identification from generic proxies. The present deliverable is survey/analysis design and log replay, with site and platform constraints documented before any field use.

Begin with calibration/time-response auditing and fixed stratified transects, then compare spatial interpolation and adaptive sampling in a simulator. USGS survey and platform reports provide methodological context. Sensor response, clock error and position uncertainty are quantified separately; a dense track can remain biased. Depth profiles and analytical reference samples are separate evidence needed for stratification or specific contamination claims.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| B27-R1 | Every sensor reading shall retain UTC clock basis, depth, calibration version, units and response/quality metadata. | Lag and calibration drift alter spatial maps. | Stream/calibration manifest audit. | Primary survey context. |
| B27-R2 | Time synchronization target shall be derived from allowable spatial error/vessel speed; proposed map target is 1 m where supported. | A fixed clock tolerance is meaningless without speed. | Clock-offset and position propagation check. | Proposed spatial target. |
| B27-R3 | Compare fixed-transect and adaptive surveys under equal travel/energy budgets in simulation, with independent reference holdouts. | More samples are not automatically better coverage. | Budget-matched survey replay. | Proposed design protocol. |
| B27-R4 | Map unsupported depths, regions and times as unobserved/uncertain; no proxy shall be labeled a specific contaminant without validated chemistry. | Surface and proxy limitations matter. | Support-mask and endpoint review. | Existing measurement boundary. |

## 3. Architecture and controlled interfaces

A stream adapter aligns GPS and sensor timestamps while preserving original clocks and offset uncertainty. Sensor channels include temperature °C, conductivity µS/cm with reference temperature and dissolved oxygen mg/L with compensation metadata. Navigation logs provide projected metre positions, energy Wh and permitted geofence/return constraints.

The response module distinguishes a pure dead time from first-order response and calibrates only supported corrections. A spatial estimator consumes measurement variance, position covariance and sampling-time support. Reference samples and depth profiles remain independent validation records. The route simulator proposes variance-reduction sampling within documented limits; missing calibration or rapid temporal changes propagate invalid-map/support flags rather than full-lake interpolation.

![B27 engineering architecture](figures/architecture.svg)

The diagram makes time, sensor response and depth part of the observation operator and compares routes within simulator constraints. Its maps remain near-surface and time-supported unless independent profiles and chemistry extend the evidence.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

```text
dy/dt=[x(position(t−t_dead),depth,t−t_dead)−y]/tau_response; observation adds separately modeled drift and sensor noise. A pure time-shift fit is a qualified approximation, not the general first-order response.
```

```text
x(s)=μ(s)+GP[K(s,s′)], with heteroscedastic measurement error.
```

```text
Next sample=argmax_s expected variance reduction(s)/travel_energy(s), subject to geofence/return constraints.
```

### Variables, units and conventions

- Temperature: °C; conductivity: μS/cm with reference temperature stated.
- DO: mg/L and saturation percent using documented compensation.
- Position: projected m; dead-time t_dead and response tau_response: s; depth: m.
- Energy: Wh; uncertainty: parameter-specific physical units.

### Assumptions and boundary conditions

- Sensor calibration/reference methods remain traceable.
- Surface readings cannot represent deep anoxia without depth observations.
- Navigation/survey plans require site permissions and practical weather/return limits.

### Derivation step 1

```text
dy/dt=(x(s(t),z,t)-y)/tau; H(i omega)=1/(1+i omega tau).
```

A first-order sensor smooths signals rather than merely shifting time. tau is seconds, and inversion at high frequency amplifies noise.

### Derivation step 2

```text
For steady speed v, characteristic spatial lag approximately v tau; clock error adds v Delta t.
```

v m/s times seconds yields metres. Dead-time and response corrections are separately documented to avoid double shifting.

### Derivation step 3

```text
Cov(y) = H K H^T + Sigma_sensor + J_pos Sigma_pos J_pos^T + J_drift Sigma_drift J_drift^T + cross-covariance terms from the joint error model.
```

H represents actual sampling/response support. Position covariance in m^2 cannot be added directly to concentration/temperature variance: J_pos maps uncertain locations into output units through the local field gradient and sensor support. J_drift similarly maps drift parameters. Retain cross terms if errors share clocks, calibration or environmental forcing. A pointwise Gaussian-process approximation is justified only when response effects are negligible or explicitly qualified.

### Derivation step 4

```text
score(s)=expected variance reduction(s)/travel_energy(s).
```

Units are parameter-variance/Wh; geofence and return reserve are hard simulator constraints. The score does not override physical/navigation limits.

### Inference or simulation procedure

Audit boat logs, GPS timestamps, calibration and response times, then align sensor streams and reject unsupported corrections. Design baseline stratified transects and an adaptive alternative using a Gaussian process or robust spatial interpolator. Pair measurements with independent reference samples and depth profiles where permitted. Propagate sensor, position, drift and interpolation errors into maps; retain blank/flagged areas instead of silently filling all water surfaces.

### Validity domain and fidelity limits

Spatial covariance may change rapidly with inflows, mixing or blooms. Optical/conductivity proxies cannot establish specific contaminants without validated chemistry; repeated trajectories do not supply independent reference truth.

## 5. Data specifications and provenance

![B27 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| sensor_time | datetime | UTC | Original and aligned reading times. | Clock source/offset covariance required. |
| position_xy | float[2] | m | Projected vessel location. | CRS and GPS covariance saved. |
| sensor_depth | nullable float | m | Measurement support below surface. | Null cannot imply full-column reading. |
| temperature | nullable float | °C | Calibrated water temperature. | Reference check and drift flags retained. |
| conductivity | nullable float | µS/cm | Specified reference-temperature channel. | Compensation method required. |
| dissolved_oxygen | nullable float | mg/L | Compensated oxygen measurement. | Pressure/salinity metadata retained. |
| response_model | record | s | Dead-time/first-order response description. | Correction support and noise amplification saved. |
| map_covariance | matrix | parameter-unit² | Joint spatial/temporal prediction uncertainty. | Calibration and position covariance included. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### USGS North Saluda Reservoir bathymetric and water-quality mapping

[Product, archive or reference](https://pubs.usgs.gov/sim/3289/pdf/sim3289.pdf)

**Fields:** Primary autonomous reservoir survey, bathymetry and water-quality methods.

**Access:** Public USGS map/report; platform-specific calibration needs new records.

**Role:** Survey and depth-context benchmark.

### Design and development of an autonomous surface vehicle for water-quality monitoring

[Product, archive or reference](https://arxiv.org/abs/2201.10685)

**Fields:** Surface-platform design and reference-comparison methods.

**Access:** Primary author report; dataset availability requires its release statement.

**Role:** Instrumentation/analysis context.

### Water Quality Portal

[Product, archive or reference](https://www.waterqualitydata.us/)

**Fields:** Historical samples, sites, analytes, units and quality metadata.

**Access:** Public Water Quality Portal; coverage/agency methods vary.

**Role:** Independent contextual observations, when temporally comparable.

## 6. Uncertainty, sensitivity and identifiability

Clock offset, sensor lag, calibration drift and GPS errors produce different spatial biases. Estimate them from documented reference/response records and propagate shared calibration error across the track. High-frequency deconvolution is ill-conditioned, so compare qualified forward-response mapping with simple time-shift approximations rather than apply unsupported corrections.

Spatial covariance changes near inflows, stratification or rapidly evolving blooms. Hold out entire transects/reference samples and compare stationary versus region/time-aware models. Travel budget and geofence limit information gain; repeated passes are correlated. Independent depth observations are needed to infer deep anoxia, and chemical reference assays are required before identifying specific pollutants from optical or conductivity proxies.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Fixed stratified transects | Transparent repeatable spatial coverage. | May waste samples in smooth regions. | Required survey baseline. |
| Response-aware spatial model | Accounts for sensor support and noise. | Needs reliable lag/calibration evidence. | Preferred analysis when metadata supports it. |
| Adaptive variance/energy routes | Targets uncertain regions efficiently. | Sensitive to model and navigation constraints. | Use in budget-matched simulation before field consideration. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| B27-V1 | Constant water field | y remains x regardless of tau or route. | Condition/fixture: x is constant and sensor starts at x. Verification procedure: Exact response-model test.. | Exact response-model test. |
| B27-V2 | Step response | y=x+(y0-x)exp(-t/tau); at tau, 63.2% of change is complete. | Condition/fixture: Sensor starts y0; constant new input x after t=0. Verification procedure: Integrator analytic comparison.. | Integrator analytic comparison. |
| B27-V3 | Clock/lag geometry | Clock-induced location shift is 1 m; tau=4 s implies characteristic lag 2 m. | Condition/fixture: v=0.5 m/s and Delta t=2 s. Verification procedure: Independent unit calculation.. | Independent unit calculation. |
| B27-V4 | Transect/reference holdout | Report parameter-specific bias, coverage and unsupported-depth fraction. | Condition/fixture: Reserve complete transects and independent samples. Verification procedure: Blocked map validation.. | Blocked map validation. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Hold out transects/days, keeping serially dependent sensor observations together.
- Evaluate reference bias, RMSE and interval coverage, stratified by speed/depth/environment.
- Inject timing/drift/dropout faults and verify detection; compare variance reduction per Wh with equal-effort uniform sampling.

## 9. Implementation and reproducible work packages

1. Create platform/sensor/clock/depth calibration manifests and permitted survey constraints.
2. Implement time-position alignment with offset and GPS covariance.
3. Build first-order/dead-time response diagnostics and qualified correction artifacts.
4. Generate fixed/adaptive equal-budget survey simulations.
5. Fit supported spatial models and independent transect/reference holdout reports.
6. Release depth/time support masks, uncertainty maps and contaminant-interpretation limits.

### Investigation sequence

1. Stage 1: verify time/calibration/lag and choose permitted survey bounds; define depth and analyte applicability.
2. Stage 2: compare baseline/adaptive sampling in simulation and historical replay with propagated uncertainty.
3. Stage 3: validate co-located independent samples and withheld transects, then release maps with support/quality flags.

### Resources and interfaces to expertise

- Aquatic scientist, sensor-calibration specialist and robotics operator.
- Timestamped navigation/sensor logs, reference methods, GIS and spatial statistics.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| Blind time shift | Distorted map near sharp gradients. | Response-model and residual review. | Forward response or qualified correction. |
| Surface mapped whole column | False deep-water condition. | Depth/support audit. | Publish depth-limited maps. |
| Drift mistaken spatial plume | False environmental hotspot. | Reference/return-pass disagreement. | Calibration covariance and drift flags. |

- Sensor drift/lag and inconsistent compensation.
- Surface-to-depth or proxy-to-contaminant overclaiming.
- Coverage bias, weather/return failure or unauthorized sampling.

## 11. Required engineering outputs

- Calibrated aquatic data cube and quality flags.
- Survey-efficiency and uncertainty notebook.
- Supported water-quality maps and mission-data protocol.

### Scientific result figures to produce during execution

Display measured tracks/depths, parameter maps and uncertainty; compare adaptive/uniform coverage with independent reference residuals.

## 12. Cited technical and scientific resources

- [USGS North Saluda Reservoir bathymetric and water-quality mapping](https://pubs.usgs.gov/sim/3289/pdf/sim3289.pdf) — Primary autonomous-survey example supports georeferenced water-quality and depth observations; platform transfer requires fresh calibration.
- [Design and development of an autonomous surface vehicle for water-quality monitoring](https://arxiv.org/abs/2201.10685) — Primary platform-design report motivates co-located reference measurements and sensor validation.
- [Water Quality Portal](https://www.waterqualitydata.us/) — Official multiagency sample archive supplies historical aquatic observations with method/unit qualifiers.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
