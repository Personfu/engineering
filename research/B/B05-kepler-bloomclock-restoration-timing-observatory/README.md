# B05 · KEPLER BLOOMCLOCK — Restoration Timing Observatory

**Original project:** Phenology Data to Aid Pollinator Restoration

**Session B:** Earth & Environmental Engineering

**Document class:** engineering research design and analysis record · **Revision:** 4 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session B](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_B.md) · [← B04](../B04-aurora-veil-ionospheric-absorption-atlas/README.md) · [B06 →](../B06-solstice-chemistry-tucson-ozone-digital-observatory/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 4 | 4 | 7 | 2 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Mission profile

![B05 engineering mission profile: scientific question, hypothesis, model scope and evidence status](figures/mission-profile.svg)

| Profile panel | Engineering signal | Open the evidence |
| --- | --- | --- |
| Mission identity | Phenology Data to Aid Pollinator Restoration | [Scientific objective](#purpose-and-scientific-objective) |
| Model cockpit | 3 governing expressions; 4 derivation steps; declared assumptions and validity envelope | [Mathematical formulation](#4-mathematical-model-and-derivation) |
| Data blueprint | 7 proposed fields with types, units and quality rules | [Field map & downloads](data/README.md) |
| Verification queue | 4 proposed requirements; 4 specified cases; project execution evidence pending | [Case definitions](#8-verification-and-validation-cases) |
| Figure wall | Architecture, field map, planned result description | [Open full gallery](figures/README.md) |
| Resource library | 2 cited primary resources with support statements | [Cited resources](#12-cited-technical-and-scientific-resources) |

### Model cockpit

**Analysis method:** Model interval-censored onset and duration from repeated phenophase observations. Add weather, elevation and water availability through hierarchical models; compare growing-degree-day and flexible calendar baselines. Use posterior bloom probabilities in a constrained planting optimization with local suitability, water, cost and establishment limits. Treat demand curves as measured or scenario assumptions; evaluate resource-gap robustness rather than presenting flowering overlap as demonstrated reproductive success.

**Operating envelope:** National datasets may omit desert species or have short local records. Flower presence does not directly measure nectar, pollen quality or successful pollination, and restoration establishment changes realized resources.

**Variables and conventions**

- x: planting area or abundance by species, m² or individuals.
- r: floral-resource proxy, resources per area per day, locally calibrated.
- D: demand proxy in the same resource units; not inferred directly from bloom counts.
- T_base: species-specific thermal threshold, °C; moisture includes precipitation/soil-water proxies.

### Artifact wall

![B05 proposed analysis architecture](figures/architecture.svg)

The diagram connects observation intervals to weekly restoration resources and makes establishment and demand assumptions visible. It establishes timing support, while leaving pollinator demographic benefit to independent evidence.

**Scientific result to produce:** Show weekly flowering probabilities by species, aggregate mixture coverage and uncertain gap days; label observed versus projected years.

### Investigation feed · planned work

The feed records proposed work packages. A row becomes executed evidence only with versioned inputs, outputs and a reviewed result.

| Sequence | Evidence state | Engineering work package |
| --- | --- | --- |
| 01 | Planned | Publish phenophase, weather and species-suitability schemas with observation-state definitions. |
| 02 | Planned | Construct interval-censored onset/duration tables and weather coverage reports. |
| 03 | Planned | Implement calendar and thermal/moisture baselines with frozen yearly folds. |
| 04 | Planned | Build joint weekly bloom ensembles and resource conversion assumptions. |
| 05 | Planned | Optimize constrained mixtures and independently calculate shortfall distributions. |
| 06 | Planned | Release species timing cards, extrapolation flags and locally reviewable restoration scenarios. |

### Mission connections

Connections are reading routes based on actual shared resources, supplied sessions or included illustrations. They do not establish physical dependencies, team collaborations or validated results.

| Connected mission | Original investigation | Recorded connection basis |
| --- | --- | --- |
| [B02 · ARTEMIS LIFE RAFTS — Urban Pollinator Constellation](../B02-artemis-life-rafts-urban-pollinator-constellation/README.md) | Urban Biodiversity Life Rafts: A Way to Conserve our Pollinators | Session B; [USA National Phenology Network observational data](https://nn.usanpn.org/data/observational) |
| [B25 · SEEDSTAR GENESIS — Dryland Establishment Forecasting](../B25-seedstar-genesis-dryland-establishment-forecasting/README.md) | Can We Predict Germination Success in Seed Pellets Using Seed Traits? | Session B; [USGS managing to survive despite the weather: seeding decisions](https://www.usgs.gov/publications/managing-survive-despite-weather-seeding-decisions-affecting-simulated-dryland) |
| [B04 · AURORA VEIL — Ionospheric Absorption Atlas](../B04-aurora-veil-ionospheric-absorption-atlas/README.md) | Analysis of Space-based Riometer Measurement Data for Characterization of Radio Propagation Disturbance in the Ionosphere | Session B |
| [B06 · SOLSTICE CHEMISTRY — Tucson Ozone Digital Observatory](../B06-solstice-chemistry-tucson-ozone-digital-observatory/README.md) | The Contribution of Plants and Pollution to Tucson's Urban Ozone Problem | Session B |
| [B03 · ORION CROSSINGS — Gila Monster Road Ecology](../B03-orion-crossings-gila-monster-road-ecology/README.md) | Potential Road Impacts on Gila Monsters in an Urbanizing Environment | Session B |
| [B07 · REGENESIS CLEANFLOW — Environmental Fate and Remediation Model](../B07-regenesis-cleanflow-environmental-fate-and-remediation-model/README.md) | Bioremediation of Insensitive Munitions Compounds | Session B |

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

Turn dated plant and pollinator observations into a decision tool for maintaining floral resources through heat, drought and seasonal transitions. Estimate flowering windows and uncertainty for locally suitable species, then choose restoration mixtures that minimize resource gaps. Keep observed phenophases, climate-model projections and assumed pollinator demand visibly distinct.

**Question:** Which locally adapted planting mixtures retain the most continuous flowering opportunity under observed variability and plausible warming/drought scenarios?

**Testable hypothesis:** Mixtures optimized for complementary, uncertainty-aware bloom windows will leave fewer resource-gap days than mixtures selected from mean flowering dates alone.

## 1. Design basis and analysis boundary

The restoration timing system converts repeated plant phenophase observations and weather into species-specific flowering-window distributions. It then evaluates planting mixtures against a declared weekly floral-resource demand scenario. Flower presence, floral abundance and pollinator reproduction remain distinct endpoints; only the first is directly supported by many phenology records.

The initial model uses interval-censored onset and duration with calendar and growing-degree-day baselines. Moisture and microclimate effects are added only where their metadata overlap observations. Optimization consumes establishment probability, irrigation and local suitability rather than assuming every planted individual survives. National Phenology Network documentation supports observation semantics; thermal thresholds, demand curves and portfolio targets below are proposed choices requiring local calibration.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| B05-R1 | Represent onset between the last valid absence and first presence; never replace the interval with an exact observation date. | Sampling cadence limits timing precision. | Inspect reconstructed onset bounds. | NPN observation semantics. |
| B05-R2 | Proposed resource accounting uses weekly bins and separately reports establishment-year and mature planting scenarios. | Annual overlap hides restoration gaps. | Recompute weekly balance from species matrix. | Proposed design resolution. |
| B05-R3 | Species transfer outside observed temperature, moisture or elevation support shall carry an extrapolation flag. | Desert climate relationships may differ. | Compare deployment envelope with training ranges. | Proposed applicability gate. |
| B05-R4 | Each optimized mixture shall satisfy declared water, area and cost bounds across retained uncertainty draws or disclose violation probability. | Planting advice must remain feasible. | Independent portfolio ledger. | Local constraints TBD. |

## 3. Architecture and controlled interfaces

The observation adapter stores species, site, phenophase, visit date, present/absent status and effort; unknown visits are not absences. Weather joins use site-specific timezone and daily aggregation, then emit temperature °C, precipitation mm and source coverage. A thermal-time module records species-specific base temperature and missing-weather policy.

The onset-duration estimator produces correlated species-week bloom probabilities. A resource adapter converts bloom to a locally calibrated resource proxy and multiplies by establishment survival. The mixture optimizer accepts plant counts or area with explicit units, plus water L/year and cost. Its outputs retain probability of shortfall and unmodeled species; bloom timing alone cannot be exported as validated pollinator demand satisfaction.

![B05 engineering architecture](figures/architecture.svg)

The diagram connects observation intervals to weekly restoration resources and makes establishment and demand assumptions visible. It establishes timing support, while leaving pollinator demographic benefit to independent evidence.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

```text
GDD(t)=Σ_d≤t max[0,T_mean,d−T_base], in °C·day.
```

```text
P(bloom_s,d)=logit⁻¹[a_s+b_s GDD_d+c_s moisture_d+u_site].
```

```text
Gap(x)=Σ_d 1[Σ_s x_s P(bloom_s,d) r_s<D_d], evaluated over posterior/scenario draws.
```

### Variables, units and conventions

- x: planting area or abundance by species, m² or individuals.
- r: floral-resource proxy, resources per area per day, locally calibrated.
- D: demand proxy in the same resource units; not inferred directly from bloom counts.
- T_base: species-specific thermal threshold, °C; moisture includes precipitation/soil-water proxies.

### Assumptions and boundary conditions

- Repeated absence observations are informative; opportunistic presence records alone cannot define exact onset.
- Phenophase observations bracket flowering dates and may have observer/site bias.
- Urban irrigation and microclimate can break temperature-only relationships.

### Derivation step 1

```text
GDD_d=sum_(k<=d) max(0,T_mean,k-T_base) Delta_t.
```

With daily Delta_t=1 day, the accumulation has °C day units; a missing daily temperature is not a zero contribution.

### Derivation step 2

```text
P(L<T_onset<=R)=F_T(R)-F_T(L).
```

L and R are last-absence and first-presence dates. Left/right censoring is handled explicitly when either boundary is unavailable.

### Derivation step 3

```text
R_w(x)=sum_s x_s e_s b_sw r_sw.
```

Plant count x, establishment fraction e, bloom probability b and resource/plant/week r yield resource/week; covariance is retained across species under shared weather.

### Derivation step 4

```text
G(x)=sum_w I[R_w(x)<D_w]; objective=E[G]+lambda Var(G).
```

Demand D has the same resource units. The risk weight is a declared planning preference, and gap count has weeks units.

### Inference or simulation procedure

Model interval-censored onset and duration from repeated phenophase observations. Add weather, elevation and water availability through hierarchical models; compare growing-degree-day and flexible calendar baselines. Use posterior bloom probabilities in a constrained planting optimization with local suitability, water, cost and establishment limits. Treat demand curves as measured or scenario assumptions; evaluate resource-gap robustness rather than presenting flowering overlap as demonstrated reproductive success.

### Validity domain and fidelity limits

National datasets may omit desert species or have short local records. Flower presence does not directly measure nectar, pollen quality or successful pollination, and restoration establishment changes realized resources.

## 5. Data specifications and provenance

![B05 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| phenophase_status | enum | none | present, absent or unknown. | Unknown never treated as absence. |
| onset_bounds | nullable date[2] | calendar day | Observed timing interval. | Store one-sided censoring. |
| daily_temperature | nullable float | °C | Local mean temperature. | Coverage and timezone required. |
| base_temperature | float | °C | Species thermal threshold. | Provenance or scenario tag required. |
| bloom_probability | float[] | none | Weekly flowering ensemble. | Bounds 0–1; joint covariance saved. |
| establishment_fraction | float[] | none | Scenario survival to resource provision. | No default perfect survival. |
| resource_shortfall | float[] | resources/week | Demand minus realized floral proxy. | Demand assumptions linked. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### USA National Phenology Network observational data

[Product, archive or reference](https://nn.usanpn.org/data/observational)

**Fields:** Species, phenophases, observed presence/absence, site and observation dates.

**Access:** Public downloads with documentation; check reuse rules and uneven site effort.

**Role:** Observed timing and interval censoring.

### USGS managing to survive despite the weather: seeding decisions

[Product, archive or reference](https://www.usgs.gov/publications/managing-survive-despite-weather-seeding-decisions-affecting-simulated-dryland)

**Fields:** Weather-window and seedling-survival modeling framework.

**Access:** USGS publication; obtain author data/code where available.

**Role:** Establishment-aware scenario design, not new pollinator measurements.

## 6. Uncertainty, sensitivity and identifiability

Observer cadence determines onset intervals, and opportunistic records produce selection bias toward noticeable flowering. Treat site and observer effects separately when identifiable, and compare calendar versus thermal-time fits on withheld years. Irrigation can decouple flowering from rainfall; missing irrigation metadata contributes model discrepancy rather than a precisely estimated climate effect.

Base temperature, onset intercept and moisture response can trade off, especially within a narrow seasonal range. Profile those parameters and inspect predictive intervals rather than select one thermal threshold as biological truth. Demand and per-flower resources may be assumed, so sensitivity panels should show mixture rankings over both. Correlated drought and establishment losses are propagated through shared scenario draws.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Calendar flowering windows | Transparent and data-light. | Limited climate-shift sensitivity. | Baseline when weather coverage is poor. |
| Thermal/moisture onset model | Connects timing to plausible drivers. | Threshold and moisture parameters may confound. | Adopt only with held-out timing improvement. |
| Direct weekly resource observations | Closest to restoration resource estimand. | More local effort and sparse species coverage. | Prefer when validated resource measurements exist. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| B05-V1 | Thermal threshold | GDD=0 °C day; 2°C above base gives 20 °C day. | Condition/fixture: Ten days at T_mean=T_base. Verification procedure: Exact accumulation fixture.. | Exact accumulation fixture. |
| B05-V2 | Interval probability | Interval probability is 4/10=0.4. | Condition/fixture: Uniform onset over days 1–11; observed bracket 3–7. Verification procedure: Known distribution likelihood check.. | Known distribution likelihood check. |
| B05-V3 | Zero establishment | Realized resources are zero regardless of bloom probability. | Condition/fixture: Set e_s=0 for every species. Verification procedure: Portfolio boundary test.. | Portfolio boundary test. |
| B05-V4 | Year holdout | Report onset interval coverage and weekly shortfall calibration. | Condition/fixture: Reserve complete hot/dry observation years. Verification procedure: Chronological evaluation.. | Chronological evaluation. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Hold out sites and years; evaluate onset/duration error and probability calibration.
- Compare optimized mixtures with equal-cost conventional native mixtures under the same weather and survival draws.
- Measure flowering and pollinator visitation independently; preregister whether evidence supports timing alone or biological benefit.

## 9. Implementation and reproducible work packages

1. Publish phenophase, weather and species-suitability schemas with observation-state definitions.
2. Construct interval-censored onset/duration tables and weather coverage reports.
3. Implement calendar and thermal/moisture baselines with frozen yearly folds.
4. Build joint weekly bloom ensembles and resource conversion assumptions.
5. Optimize constrained mixtures and independently calculate shortfall distributions.
6. Release species timing cards, extrapolation flags and locally reviewable restoration scenarios.

### Investigation sequence

1. Stage 1: inventory local species coverage, calibrate survey definitions and estimate observer/site bias; flag candidates requiring new observations.
2. Stage 2: fit flowering models and evaluate mixtures over historical weather and clearly labeled climate scenarios with irrigation constraints.
3. Stage 3: monitor pilot restoration plots across full seasons and update the resource calendar with realized survival and flowering.

### Resources and interfaces to expertise

- Restoration botanist, phenology observers and local meteorological records.
- rnpn/API tools, hierarchical statistics and a planting optimizer.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| Presence-only onset | Artificially precise flowering dates. | Missing preceding absence records. | Retain censoring and wider bounds. |
| Unit mismatch in resources | Meaningless demand comparison. | Dimensional ledger check. | Require common resource units. |
| Perfect establishment assumption | Overoptimistic floral coverage. | Compare planned and surviving plant counts. | Include establishment scenarios. |

- Extrapolation to species absent from local records.
- Confounding natural phenology with managed irrigation.
- Presenting scenario demand as measured ecological need.

## 11. Required engineering outputs

- Versioned flowering-probability calendar.
- Water/cost constrained mixture recommendations with intervals.
- Observation protocol and establishment-adjusted monitoring report.

### Scientific result figures to produce during execution

Show weekly flowering probabilities by species, aggregate mixture coverage and uncertain gap days; label observed versus projected years.

## 12. Cited technical and scientific resources

- [USA National Phenology Network observational data](https://nn.usanpn.org/data/observational) — Observed plant and animal phenophases and observation documentation; provides timing records, not automatic pollinator abundance estimates.
- [USGS managing to survive despite the weather: seeding decisions](https://www.usgs.gov/publications/managing-survive-despite-weather-seeding-decisions-affecting-simulated-dryland) — Primary simulation research supports weather windows and post-germination survival as distinct constraints.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
