# B06 · SOLSTICE CHEMISTRY — Tucson Ozone Digital Observatory

**Original project:** The Contribution of Plants and Pollution to Tucson's Urban Ozone Problem

**Session B:** Earth & Environmental Engineering

**Document class:** engineering research design and analysis record · **Revision:** 3 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session B](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_B.md) · [← B05](../B05-kepler-bloomclock-restoration-timing-observatory/README.md) · [B07 →](../B07-regenesis-cleanflow-environmental-fate-and-remediation-model/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 4 | 4 | 7 | 2 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Purpose and scientific objective

Quantify how vegetation emissions, anthropogenic precursors, meteorology and imported background air jointly shape Tucson ozone. The design couples an observational meteorology-normalized analysis with a chemistry sensitivity ensemble, avoiding the simplistic conclusion that more vegetation necessarily causes more ozone. Evaluate air-quality consequences together with vegetation’s heat and ecological benefits.

**Question:** When and where do biogenic VOC emissions measurably change ozone sensitivity, after accounting for NOx, weather, fire and regional transport?

**Testable hypothesis:** Vegetation effects will be season- and chemical-regime dependent; hot sunny periods may amplify BVOC emissions while local NOx changes determine the sign and magnitude of ozone response.

## 1. Design basis and analysis boundary

The Tucson ozone analysis has two coupled but distinct components: meteorology-normalized monitoring comparisons and a reduced atmospheric chemistry sensitivity model. Inputs are quality-qualified surface observations, weather, dated vegetation and emissions inventories. The engineering question is how changing plant and anthropogenic precursor emissions alters a stated ozone metric under matched meteorology, including uncertainty from imported background air.

Begin with an observational baseline for maximum daily eight-hour ozone, then a unit-checked box model that exposes production, deposition and transport. Promote to regional-model output only with documented configuration and emissions provenance. The local primary study supplies context, not a reusable source attribution coefficient. Vegetation heat, water and biodiversity benefits remain co-outcomes rather than being collapsed into an ozone-only recommendation.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| B06-R1 | Every ozone record shall retain AQS parameter, method, duration, units, qualifier and local/UTC timestamps. | Mixed averaging durations bias daily maxima. | Audit API fields and daily aggregation. | EPA AQS documentation. |
| B06-R2 | Compute maximum daily eight-hour ozone only from windows satisfying the applicable documented data-completeness rule; rule version must be recorded. | Missing hours must not create false low exposure. | Synthetic missing-window test. | AQS convention; version verified at execution. |
| B06-R3 | Chemistry sensitivity runs shall use identical meteorology and boundary conditions across vegetation/anthropogenic perturbations. | Separates forcing changes from source scenarios. | Compare frozen scenario manifests. | Proposed attribution protocol. |
| B06-R4 | Report plant-emission effects with transport/deposition sensitivity and species-factor ranges; no universal satellite-ratio regime threshold. | Sparse VOC measurements limit inference. | Review uncertainty panels and assumptions. | Existing model limitations. |

## 3. Architecture and controlled interfaces

The monitor adapter preserves concentration ppb and measurement duration; a state converter uses pressure and temperature to produce mol/m³ where kinetic equations require it. Weather includes mixing height m, wind m/s and radiation with source cadence. A land-cover/species adapter supplies leaf area index and uncertain BVOC emission factors, rather than treating NDVI as emission flux.

The meteorology-normalization branch produces residual ozone distributions on chronological holdouts. The chemistry branch integrates precursor, radical and ozone states with a separate boundary-air exchange term. Both join at scenario metrics, without treating their agreement as independent validation. Missing speciated VOC data trigger broad parameter envelopes; HCHO/NO2 columns remain contextual diagnostics with retrieval and surface-column uncertainty.

![B06 engineering architecture](figures/architecture.svg)

The architecture distinguishes observed ozone normalization from conditional chemistry scenarios and shows transport as an explicit interface. It supports bounded source sensitivities without equating vegetation correlations with causal ozone production.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

```text
d[O3]/dt=P(RO2+NO,HO2+NO)−L(O3)−v_d[O3]/h+transport.
```

```text
E_BVOC=ε_species LAI γ_T γ_light γ_water, with units reconciled to mass/area/time.
```

```text
O3_it=a_i+f(T,solar,wind,humidity)+g(NOx,VOC)+season+ε_it.
```

### Variables, units and conventions

- O3 and precursors: ppb or mol/m³ with explicit conversion.
- E: emission flux, mg/m²/hour; LAI: leaf area index, dimensionless.
- v_d: deposition velocity, m/s; h: mixing height, m.
- γ: environmental response factors; transport is not assumed zero.

### Assumptions and boundary conditions

- Satellite HCHO/NO2 column ratios are indirect diagnostics, not universal thresholds for surface chemistry.
- Monitoring sites have different sampling coverage and microenvironments.
- Species-level emission factors are uncertain and drought response is not a constant multiplier.

### Derivation step 1

```text
c_O3=x_O3 P/(R T), with x_O3=ppb*10^-9.
```

The ideal-gas conversion gives mol/m³ from pressure Pa and temperature K, allowing concentration and reaction rates to use consistent units.

### Derivation step 2

```text
E_BVOC=epsilon_s LAI gamma_T gamma_light gamma_water.
```

epsilon is defined per leaf area; LAI converts to ground area. All environmental responses are dimensionless and their empirical validity ranges are retained.

### Derivation step 3

```text
dc_O3/dt=P_chem-L_chem-(v_d/h)c_O3+(c_bg-c_O3)/tau_mix.
```

Every term is mol/m³/s. Deposition and exchange times have s^-1 coefficients; ignoring transport assigns background ozone to local sources.

### Derivation step 4

```text
Delta_O3=metric(c_scenario)-metric(c_baseline).
```

A scenario changes one emission group while fixing meteorology. Interaction effects require a factorial comparison, not addition of independent marginal changes.

### Inference or simulation procedure

Harmonize AQS ozone and precursor records with meteorology, land cover and documented emissions inventories. Fit generalized additive meteorology normalization, then use a reduced chemical box model or established regional-model sensitivity runs to perturb vegetation and anthropogenic sources separately. Bootstrap by season/year, preserve negative-control periods and compare intervention scenarios under identical meteorology. Evaluate effects on maximum daily 8-hour ozone and spatial gradients without claiming full source attribution from correlations.

### Validity domain and fidelity limits

Box models cannot fully resolve basin circulation or regional transport. Sparse speciated VOC observations can make plant attribution weak; green-space policy needs heat, water and biodiversity tradeoffs as well as ozone.

## 5. Data specifications and provenance

![B06 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| ozone_ppb | nullable float | ppb | Qualified surface concentration. | Duration, method and flags retained. |
| timestamp_pair | datetime[2] | UTC local | Measurement and local-day conventions. | DST/site timezone explicit. |
| mixing_height | nullable float | m | Box-model dilution depth. | Positive; source support flagged. |
| bvoc_factor | float[] | mg/m² leaf/hour | Species emission-factor scenarios. | No NDVI substitution; covariance retained. |
| leaf_area_index | float | m²/m² | Leaf-to-ground area ratio. | Sensor/date provenance required. |
| background_ozone | float[] | mol/m³ | Boundary-air concentration scenarios. | Distinct from local monitor truth. |
| scenario_mda8 | float[] | ppb | Eight-hour daily metric ensemble. | Report completeness and model discrepancy. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### EPA AQS Data API documentation

[Product, archive or reference](https://aqs.epa.gov/aqsweb/documents/ramltohtml.html)

**Fields:** Hourly ozone/NO2, station coordinates, sample duration, method and quality qualifiers.

**Access:** Public bulk downloads; API requires registration/key and request limits.

**Role:** Observed outcomes and monitor comparability.

### A long-term (2001–2022) examination of surface ozone concentrations in Tucson, Arizona

[Product, archive or reference](https://pubs.rsc.org/en/content/articlehtml/2025/ea/d5ea00072f)

**Fields:** Published Tucson trends, land-cover/emissions context and methodology.

**Access:** Publisher/index record verified; automated direct retrieval was blocked. Use authorized article/supplement access.

**Role:** Local benchmark and chemistry-regime design.

## 6. Uncertainty, sensitivity and identifiability

Species composition, drought response and emission factors can dominate plant attribution. BVOC, NOx and radical production are nonlinearly coupled, so perturb them factorially and examine interaction terms. Solar radiation, heat and stagnation covary; meteorology normalization must be tested on independent years instead of interpreted as a mechanistic source separation.

Background ozone, deposition velocity and mixing height may compensate for local chemistry rates. Assess identifiability with sensitivity matrices and profiles, anchor parameters only where independent observations exist, and widen discrepancy elsewhere. Bootstrap seasons or episodes, retaining monitor-method shared bias. Surface-column satellite mismatches cannot be fixed by choosing an unsupported universal regime threshold.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Monitoring normalization | Strong connection to observed exposure. | Limited mechanistic source attribution. | Use as the primary observational baseline. |
| Reduced chemical box | Transparent nonlinear sensitivity and units. | Misses basin circulation and spatial gradients. | Use for conditional mechanism screening. |
| Regional-model sensitivity ensemble | Represents transport and spatial chemistry. | High configuration and emissions burden. | Adopt when documented runs and independent validation exist. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| B06-V1 | Ideal-gas conversion | c=10^-9 P/(RT); changing T scales inversely. | Condition/fixture: 1 ppb at declared P and T. Verification procedure: Unit-aware analytic fixture.. | Unit-aware analytic fixture. |
| B06-V2 | Deposition-only box | c(t)=c0 exp(-v_d t/h). | Condition/fixture: Set production, other loss and exchange to zero. Verification procedure: Compare integrator against exact solution.. | Compare integrator against exact solution. |
| B06-V3 | Zero source perturbation | Delta MDA8=0 within numerical tolerance. | Condition/fixture: Identical baseline and scenario inputs. Verification procedure: Scenario-manifest integration test.. | Scenario-manifest integration test. |
| B06-V4 | Episode holdout | Report metric bias, interval coverage and regime-dependent error. | Condition/fixture: Withhold complete ozone episodes and years. Verification procedure: Blocked observational/model evaluation.. | Blocked observational/model evaluation. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Use whole-year and station holdouts with prediction intervals; random hourly splits overstate skill.
- Compare with persistence, weather-only and published local benchmarks.
- Check residual bias on fire, monsoon and high-background days; validate VOC predictions against independent measurements where obtainable.

## 9. Implementation and reproducible work packages

1. Create an AQS/weather/vegetation manifest with averaging and timezone definitions.
2. Implement concentration conversions and data-completeness-aware MDA8 aggregation.
3. Fit meteorology-normalized baselines using chronological episode folds.
4. Develop a chemistry/deposition/exchange model with an explicit dimensional ledger.
5. Run factorial source scenarios and uncertainty profiles under matched weather.
6. Publish ozone, heat, water and ecological tradeoffs with source-attribution limits.

### Investigation sequence

1. Stage 1: reproduce monitor coverage and define emissions/meteorology sources; preregister the periods and pollution endpoints.
2. Stage 2: fit normalization and chemical sensitivity ensembles, quantify source/transport identifiability and test vegetation-emission alternatives.
3. Stage 3: validate withheld summers and deliver planting/emissions scenarios with ozone, cooling and water-use uncertainty.

### Resources and interfaces to expertise

- Atmospheric chemist and local air-quality agency.
- AQS extraction, emissions inventory, weather/reanalysis and validated chemistry software.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| Averaging-duration mix | Biased exposure metric. | Inspect duration histogram. | Standardize before aggregation. |
| No transport term | False local-source attribution. | Residual correlation with winds/background. | Retain boundary exchange uncertainty. |
| Column ratio overinterpreted | Unsupported chemical-regime label. | Compare surface precursor evidence. | Use as contextual diagnostic only. |

- Confounding regional transport with local vegetation.
- Unvalidated satellite chemical-regime thresholds.
- Optimizing ozone while overlooking heat, water or habitat costs.

## 11. Required engineering outputs

- Tucson monitor/emissions data cube.
- Reproducible sensitivity ensemble and uncertainty ledger.
- Species/season policy matrix including co-benefits.

### Scientific result figures to produce during execution

Plot ozone response surfaces for NOx and BVOC changes by season, alongside measured monitor histories and intervention uncertainty.

## 12. Cited technical and scientific resources

- [EPA AQS Data API documentation](https://aqs.epa.gov/aqsweb/documents/ramltohtml.html) — Official monitoring fields, quality flags and access instructions for observed air quality.
- [A long-term (2001–2022) examination of surface ozone concentrations in Tucson, Arizona](https://pubs.rsc.org/en/content/articlehtml/2025/ea/d5ea00072f) — Primary local ozone study supports meteorology, emissions and chemical-regime confounders; effect estimates must be reanalyzed for the proposed design.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
