# B23 · HYDRA MISSION CONTROL — Watershed Decisions Under Uncertainty

**Original project:** Modeling to Make a Difference: Hydrologic Analysis for Improved Decision Support

**Session B:** Earth & Environmental Engineering

**Document class:** engineering research design and analysis record · **Revision:** 4 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session B](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_B.md) · [← B22](../B22-nif-odyssey-comparative-nitrogen-fixation-evolution/README.md) · [B24 →](../B24-viper-voyager-urban-movement-and-habitat-connectivity/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 4 | 4 | 8 | 2 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Mission profile

![B23 engineering mission profile: scientific question, hypothesis, model scope and evidence status](figures/mission-profile.svg)

| Profile panel | Engineering signal | Open the evidence |
| --- | --- | --- |
| Mission identity | Modeling to Make a Difference: Hydrologic Analysis for Improved Decision Support | [Scientific objective](#purpose-and-scientific-objective) |
| Model cockpit | 3 governing expressions; 4 derivation steps; declared assumptions and validity envelope | [Mathematical formulation](#4-mathematical-model-and-derivation) |
| Data blueprint | 8 proposed fields with types, units and quality rules | [Field map & downloads](data/README.md) |
| Verification queue | 4 proposed requirements; 4 specified cases; project execution evidence pending | [Case definitions](#8-verification-and-validation-cases) |
| Figure wall | Architecture, field map, planned result description; included shared illustration | [Open full gallery](figures/README.md) |
| Resource library | 2 cited primary resources with support statements | [Cited resources](#12-cited-technical-and-scientific-resources) |

### Model cockpit

**Analysis method:** Join quality-controlled gauge data, precipitation, evapotranspiration and watershed characteristics. Compare persistence, rainfall-runoff and ensemble alternatives using chronological training windows. Translate forecasts into explicit policies through stakeholder-defined loss functions and stress-test under historical extremes and labeled climate scenarios. Track data latency and missing gauges. Record uncertainty from forcing, parameters, structure and observations separately, then evaluate whether additional complexity changes decisions meaningfully.

**Operating envelope:** Ungauged transfer and changing land cover can invalidate calibration. Historical skill is not guaranteed under new extremes; decision weights and future forcing remain uncertain.

**Variables and conventions**

- P/ET/storage: mm or mm/day; Q: m³/s after catchment-area conversion.
- a: withdrawal/alert/operation decision with stated units.
- L: stakeholder-defined monetary or service/ecological loss.
- Probabilities and intervals: calibrated against withheld events.

### Artifact wall

![B23 included scientific diagnostic](../../../data/figures/12_hydrologic_water_ledger.svg)

Synthetic reservoir fluxes and cumulative water accounting. Recharge means effective water entering storage, rather than rainfall. Panel B decomposes all accounted water into cumulative release and remaining storage, bounded by initial storage plus accumulated recharge. The tiny arithmetic residual verifies this implementation's conservation, not watershed predictive accuracy.

[Exact inputs, transformations and output hashes](../../../data/figures/12_hydrologic_water_ledger.provenance.json)

**Scientific result to produce:** Display observed/forecast flows and intervals, policy actions and accumulated loss for withheld events; allow transparent scenario/weight comparisons.

### Investigation feed · planned work

The feed records proposed work packages. A row becomes executed evidence only with versioned inputs, outputs and a reviewed result.

| Sequence | Evidence state | Engineering work package |
| --- | --- | --- |
| 01 | Planned | Define the real basin/action/loss/deadline contract with authorized stakeholders. |
| 02 | Planned | Create gauge/forcing manifests with rating and availability metadata. |
| 03 | Planned | Implement depth-volume storage and conservation calculators. |
| 04 | Planned | Build persistence and rainfall-runoff ensemble artifacts on chronological folds. |
| 05 | Planned | Replay explicit policies with latency, calibration and regret scoring. |
| 06 | Planned | Release decision tradeoffs, baseline fallback and extreme-scenario limitations. |

### Mission connections

Connections are reading routes based on actual shared resources, supplied sessions or included illustrations. They do not establish physical dependencies, team collaborations or validated results.

| Connected mission | Original investigation | Recorded connection basis |
| --- | --- | --- |
| [B14 · PHOENIX INFILTRATION — Postfire Soil Recovery Observatory](../B14-phoenix-infiltration-postfire-soil-recovery-observatory/README.md) | Soil hydraulic properties three years after the Frye Fire on Mount Graham, Arizona | Session B; Included illustration: 05_hydrologic_reservoir |
| [B22 · NIF ODYSSEY — Comparative Nitrogen-Fixation Evolution](../B22-nif-odyssey-comparative-nitrogen-fixation-evolution/README.md) | Developing a model system using Azotobacter vinelandii to investigate the evolution of nitrogen fixation | Session B |
| [B24 · VIPER VOYAGER — Urban Movement and Habitat Connectivity](../B24-viper-voyager-urban-movement-and-habitat-connectivity/README.md) | Using GIS to Quantify Effects of Land Cover Change on Movement Patterns of Tiger Rattlesnakes in an Urbanizing Environment | Session B |
| [B21 · PROTEUS DRIFTSCAPE — Evolutionary Protein Disorder](../B21-proteus-driftscape-evolutionary-protein-disorder/README.md) | More Effectively Selective Species Have Greater Protein Structural Disorder | Session B |
| [B25 · SEEDSTAR GENESIS — Dryland Establishment Forecasting](../B25-seedstar-genesis-dryland-establishment-forecasting/README.md) | Can We Predict Germination Success in Seed Pellets Using Seed Traits? | Session B |
| [B20 · LUNAR RECLAIMER — Algal Rare-Earth Recovery](../B20-lunar-reclaimer-algal-rare-earth-recovery/README.md) | Rare Earth Metal Recovery from Waste Stream Using Algae | Session B |

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

Build watershed decision support around explicit choices, costs and hydrologic forecast uncertainty. Select one real management use, such as drought withdrawals or flood-response thresholds, before model development. Score success by decision performance as well as hydrograph fit; a statistically stronger forecast can still fail if it arrives too late or obscures tradeoffs.

**Question:** Which model and operating policy reduce decision losses across wet/dry conditions while maintaining calibrated uncertainty?

**Testable hypothesis:** A parsimonious, well-calibrated ensemble may support better decisions than a more complex single forecast, especially when user costs and asymmetric errors are explicit.

## 1. Design basis and analysis boundary

The decision-support design must first select a real basin and management action with stakeholders; both are currently TBD. A drought-withdrawal threshold or flood-alert decision is a possible scoped use, not a claimed deployment. The system joins observed gauges and meteorological forcing to forecast ensembles, then maps them to explicit action losses and data-latency constraints.

Begin with persistence and a parsimonious rainfall-runoff model, then add ensemble forcing and parameter uncertainty if decisions improve on held-out events. USGS records provide observed-water interfaces and a drought decision-support precedent. Hydrologic fit, timely service delivery and decision regret are evaluated separately; stakeholder costs are value judgments rather than quantities inferred from rainfall.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| B23-R1 | Freeze basin boundary, action units, decision horizon, loss function and delivery deadline before model selection. | An accurate late forecast can be useless. | Stakeholder decision-contract review. | Proposed operational-analysis gate. |
| B23-R2 | Gauge records shall retain station/rating changes, units, qualifiers and retrieval/availability times. | Reference flow and operational latency differ. | API metadata and latency audit. | USGS Water Data documentation. |
| B23-R3 | Forecast evaluation shall use chronological whole-event folds and a persistence baseline. | Random time splits leak hydrologic memory. | Fold/dependency audit. | Proposed validation protocol. |
| B23-R4 | Report interval coverage, water-balance residual and decision regret; complexity is accepted only with meaningful held-out decision improvement. | Hydrograph skill alone is insufficient. | Independent scoring and policy replay. | Existing decision-loss model. |

## 3. Architecture and controlled interfaces

A gauge adapter preserves discharge m³/s, qualifier and rating metadata, while forcing adapters deliver precipitation/ET mm/day and observation availability. Catchment area m² converts depth to volume consistently. A state model distinguishes storage, runoff generation and observation error, with missing gauges represented explicitly.

The forecast engine emits timestamped flow/storage ensembles and deadlines. A policy module applies declared action losses to each ensemble, while a replay module evaluates decisions using only information available at the historical issue time. A stakeholder interface records alternative loss weights and constraints. Stale data, unsupported extremes or rating changes propagate degraded-service flags and baseline fallback states, not hidden confidence.

![B23 engineering architecture](figures/architecture.svg)

The diagram links hydrologic ensembles to an explicit stakeholder action and historical information cutoff. Its acceptance evidence includes decision regret and latency, while the real basin and operational policy remain to be defined.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

```text
dS/dt=P−ET−Q−deep_losses, with area/time-consistent units.
```

```text
Q_t=f(S_t,P_t,parameters)+ε_t; observation error is modeled separately.
```

```text
a*=argmin_a Σ_scenario P(scenario|data) L(a,scenario); assess regret and robustness.
```

### Variables, units and conventions

- P/ET/storage: mm or mm/day; Q: m³/s after catchment-area conversion.
- a: withdrawal/alert/operation decision with stated units.
- L: stakeholder-defined monetary or service/ecological loss.
- Probabilities and intervals: calibrated against withheld events.

### Assumptions and boundary conditions

- Rating-curve uncertainty and station changes affect reference streamflow.
- Calibration and operational thresholds must use separate evidence periods.
- Stakeholder losses are value judgments, not inferred from rainfall alone.

### Derivation step 1

```text
dS/dt=P-ET-Q_depth-D; Q_depth=Q_volume/A.
```

Q_volume m³/s divided by area m² gives m/s; multiplying by 86400*1000 converts to mm/day.

### Derivation step 2

```text
S_(t+1)=S_t+Delta t(P_t-ET_t-Q_t-D_t).
```

All fluxes share depth/time units. State bounds and conservation are checked before calibrating runoff parameters.

### Derivation step 3

```text
a*=argmin_a E[L(a,Y)|data].
```

The forecast distribution is converted to a decision only through a declared loss function and action set, not an arbitrary model probability threshold.

### Derivation step 4

```text
For binary alert, alert if p> C_false/(C_false+C_miss); regret=L(a,Y)-min_b L(b,Y).
```

This threshold follows from comparing expected false-alert and missed-event losses. Regret is evaluated retrospectively and must not use future information during action selection.

### Inference or simulation procedure

Join quality-controlled gauge data, precipitation, evapotranspiration and watershed characteristics. Compare persistence, rainfall-runoff and ensemble alternatives using chronological training windows. Translate forecasts into explicit policies through stakeholder-defined loss functions and stress-test under historical extremes and labeled climate scenarios. Track data latency and missing gauges. Record uncertainty from forcing, parameters, structure and observations separately, then evaluate whether additional complexity changes decisions meaningfully.

### Validity domain and fidelity limits

Ungauged transfer and changing land cover can invalidate calibration. Historical skill is not guaranteed under new extremes; decision weights and future forcing remain uncertain.

## 5. Data specifications and provenance

![B23 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| gauge_key | string | none | Station and rating-version identity. | Station changes and qualifiers retained. |
| discharge | nullable float | m³/s | Observed reference flow. | Rating/measurement uncertainty saved. |
| catchment_area | float | m² | Depth-volume conversion support. | Boundary version and positivity checked. |
| forcing_vector | nullable record | mm/day | Precipitation/ET/deep-loss terms. | Coverage and covariance retained. |
| issued_at | datetime | UTC | Forecast creation/availability time. | No future observations in replay. |
| forecast_ensemble | float[][] | m³/s or mm | Dated horizon-member states. | Member dependence and model key recorded. |
| loss_parameters | record | declared currency/service units | Stakeholder action consequences. | Approval/version and uncertainty explicit. |
| decision_regret | float[] | same as loss | Held-out policy performance. | Oracle comparator limited to scoring. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### USGS Water Data API documentation

[Product, archive or reference](https://api.waterdata.usgs.gov/docs/)

**Fields:** Gauge locations, observations, parameter codes and quality qualifiers.

**Access:** Public USGS APIs; record current endpoints, request limits and station coverage.

**Role:** Observed calibration/validation flows.

### USGS hydrologic drought decision support system

[Product, archive or reference](https://pubs.usgs.gov/of/2014/1003/pdf/ofr2014-1003.pdf)

**Fields:** Published drought decision-support structure and operating considerations.

**Access:** Public USGS report; local operating constraints require stakeholder input.

**Role:** Decision framing and policy baseline.

## 6. Uncertainty, sensitivity and identifiability

Forcing, rating-curve, parameter and model errors have different temporal correlation. Preserve rainfall ensembles and station-era uncertainty; compare hydrologic residuals around rating changes. Missing gauges may coincide with extreme events and cannot be treated as random complete-case omissions. Parameter equifinality is assessed through profiles and withheld event response.

Decision rankings depend on loss weights, deadline and event probability calibration. Sweep stakeholder-approved costs and stress-test historical extremes plus labeled climate scenarios. Separate forecast spread from model discrepancy and report regret intervals across whole events. Improved average RMSE may coexist with worse threshold decisions, so added complexity must justify its decision and latency burden.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Persistence forecast | Fast transparent service baseline. | Weak during rapid change/extremes. | Required comparator and fallback. |
| Parsimonious rainfall-runoff ensemble | Balances mechanisms and interpretability. | Parameter/forcing uncertainty remains. | Default hydrologic model. |
| Complex hybrid or distributed model | May improve spatial/extreme response. | Latency and calibration burden increase. | Adopt only with held-out decision benefit. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| B23-V1 | Depth-volume conversion | Q_depth=86.4 mm/day. | Condition/fixture: A=1 km² and Q=1 m³/s. Verification procedure: Independent unit calculation.. | Independent unit calculation. |
| B23-V2 | Closed storage step | Storage increases 4 mm. | Condition/fixture: P=10, ET=2, Q=3, D=1 mm/day for one day. Verification procedure: Conservation arithmetic.. | Conservation arithmetic. |
| B23-V3 | Decision threshold | Alert threshold p>0.1. | Condition/fixture: False-alert cost 1 and missed-event cost 9. Verification procedure: Exact expected-loss comparison.. | Exact expected-loss comparison. |
| B23-V4 | Operational replay | Report skill, coverage, latency failures and regret. | Condition/fixture: Withhold full drought/flood events and enforce historical issue-time availability. Verification procedure: Chronological event replay.. | Chronological event replay. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Use rolling-origin and complete-event holdouts; compare persistence and existing policy baselines.
- Report flow/volume/peak error, interval coverage and decision loss/regret separately.
- Test missing data, latency, rating-curve uncertainty and extremes outside training range; calibrate failure/abstention states.

## 9. Implementation and reproducible work packages

1. Define the real basin/action/loss/deadline contract with authorized stakeholders.
2. Create gauge/forcing manifests with rating and availability metadata.
3. Implement depth-volume storage and conservation calculators.
4. Build persistence and rainfall-runoff ensemble artifacts on chronological folds.
5. Replay explicit policies with latency, calibration and regret scoring.
6. Release decision tradeoffs, baseline fallback and extreme-scenario limitations.

### Investigation sequence

1. Stage 1: define decision owner, lead time, acceptable errors and losses; audit data/rating curves and freeze temporal splits.
2. Stage 2: fit calibrated hydrologic ensembles and compare decision policies across plausible costs and forcing.
3. Stage 3: replay withheld droughts/floods and release an operational prototype with threshold provenance and monitoring ownership.

### Resources and interfaces to expertise

- Hydrologist, decision owner and local operations/ecology reviewers.
- USGS data tools, rainfall-runoff solver, ensemble statistics and versioned loss definitions.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| Future-data replay leakage | Inflated forecast and policy skill. | Availability-time audit. | Past-only replay adapters. |
| Rating change ignored | Biased reference-flow evaluation. | Station-era residual diagnostics. | Versioned observation error. |
| Good RMSE poor decision | Misleading model selection. | Threshold regret and deadline review. | Decision-based acceptance. |

- Overfitting a convenient hydrograph metric.
- Nonstationarity and biased reference flows.
- Unagreed losses or unsupported operational reliance.

## 11. Required engineering outputs

- Watershed data/uncertainty cube.
- Forecast-to-decision notebook and policy comparison.
- Prototype dashboard with alert evidence and limitations.

### Scientific result figures to produce during execution

Display observed/forecast flows and intervals, policy actions and accumulated loss for withheld events; allow transparent scenario/weight comparisons.

### Included shared numerical starting point

![B23 shared reduced-model or catalog demonstration](../../../models/figures/05_hydrologic_reservoir.svg)

[Executable formulation, parameters, tabular outputs, provenance and verification](../../../models/README.md). This shared demonstration has a narrower domain than the project model above. Its own caption and methods identify synthetic parameters or the separately retrieved public catalog; it is not a completed result of the original project.

### Data diagnostic

![B23 data diagnostic](../../../data/figures/12_hydrologic_water_ledger.svg)

Synthetic reservoir fluxes and cumulative water accounting. Recharge means effective water entering storage, rather than rainfall. Panel B decomposes all accounted water into cumulative release and remaining storage, bounded by initial storage plus accumulated recharge. The tiny arithmetic residual verifies this implementation's conservation, not watershed predictive accuracy.

[Inputs, downloadable figure and provenance](../../../data/figures/README.md)

## 12. Cited technical and scientific resources

- [USGS Water Data API documentation](https://api.waterdata.usgs.gov/docs/) — Official observed-water-data endpoints and metadata support quality-controlled gauge extraction.
- [USGS hydrologic drought decision support system](https://pubs.usgs.gov/of/2014/1003/pdf/ofr2014-1003.pdf) — Primary decision-support method supports explicit operations, thresholds and hydrologic uncertainty.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
