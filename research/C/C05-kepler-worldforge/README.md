# C05 · KEPLER WORLDFORGE

**Original project:** Exoplanet Classification using Data Mining

**Session C:** Astronomy & Space Physics

**Document class:** engineering research design and analysis record · **Revision:** 4 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session C](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_C.md) · [← C04](../C04-horizon-tidal-echo/README.md) · [C06 →](../C06-pulsar-gemini-watch/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 5 | 4 | 8 | 2 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Mission profile

![C05 engineering mission profile: scientific question, hypothesis, model scope and evidence status](figures/mission-profile.svg)

| Profile panel | Engineering signal | Open the evidence |
| --- | --- | --- |
| Mission identity | Exoplanet Classification using Data Mining | [Scientific objective](#purpose-and-scientific-objective) |
| Model cockpit | 3 governing expressions; 4 derivation steps; declared assumptions and validity envelope | [Mathematical formulation](#4-mathematical-model-and-derivation) |
| Data blueprint | 8 proposed fields with types, units and quality rules | [Field map & downloads](data/README.md) |
| Verification queue | 5 proposed requirements; 4 specified cases; project execution evidence pending | [Case definitions](#8-verification-and-validation-cases) |
| Figure wall | Architecture, field map, planned result description; included shared illustration | [Open full gallery](figures/README.md) |
| Resource library | 2 cited primary resources with support statements | [Cited resources](#12-cited-technical-and-scientific-resources) |

### Model cockpit

**Analysis method:** Snapshot current PS and PSCompPars schemas and provenance. Build a baseline taxonomy from radius, density where available, orbit, and host properties, then compare a regularized classifier and mixture model. Integrate asymmetric errors with posterior draws; separate unavailable values from censoring and calculated values. Fit transformations, feature selection, class balancing, and imputation inside nested training folds. Split by host system and survey, because multiplanet systems and mission-specific features otherwise leak information. Assess out-of-distribution planets using feature-domain diagnostics and probabilistic abstention.

**Operating envelope:** Discovery methods have different selection functions, and the confirmed-planet catalog lacks a common nondetection denominator. Catalog-based class frequencies are not occurrence rates. Mass-radius overlaps prevent definitive composition identification.

**Variables and conventions**

- Planet mass Mp in Earth masses and radius Rp in Earth radii, converted before density calculation
- Density in g cm^-3; orbital period in days; irradiation in Earth-insolation units
- x is latent physical feature vector; y includes asymmetric uncertainties and upper/lower limits
- c is a preregistered empirical class, not a definitive composition or life label
- q is a soft target distribution; weights are fitted using training data only

### Artifact wall

![C05 included scientific diagnostic](../../../data/figures/10_catalog_values_and_coverage.svg)

Real NASA Exoplanet Archive 200-row saved, query-ordered extract of rows with period and radius. The recorded request uses TOP 200 and ORDER BY pl_name; global first-200 ranking was not independently verified. Panel A preserves discovery-method categories and logarithmic scales; panel B makes the selected fields and nine missing host-metallicity values visible. This extract is not representative and cannot establish occurrence rates or physical class labels.

[Exact inputs, transformations and output hashes](../../../data/figures/10_catalog_values_and_coverage.provenance.json)

**Scientific result to produce:** Interactive mass-radius chart with posterior density contours, class probabilities, missing-data flags, and discovery-method filters.

### Investigation feed · planned work

The feed records proposed work packages. A row becomes executed evidence only with versioned inputs, outputs and a reviewed result.

| Sequence | Evidence state | Engineering work package |
| --- | --- | --- |
| 01 | Planned | Snapshot TAP query, schema and cited reference fields. |
| 02 | Planned | Create physical measurement types separating censoring and minimum mass. |
| 03 | Planned | Implement uncertainty-draw features and unit-aware density calculation. |
| 04 | Planned | Version empirical class definitions and host/survey split manifests. |
| 05 | Planned | Fit and calibrate baselines with nested preprocessing. |
| 06 | Planned | Export probability/abstention cards and catalog-change attribution tables. |

### Mission connections

Connections are reading routes based on actual shared resources, supplied sessions or included illustrations. They do not establish physical dependencies, team collaborations or validated results.

| Connected mission | Original investigation | Recorded connection basis |
| --- | --- | --- |
| [C23 · KEPLER METAL WORLDS](../C23-kepler-metal-worlds/README.md) | Investigating the Relationship Between Exoplanet Occurrence & Host Star Metallicity | Session C; Included illustration: 09_real_exoplanet_sample |
| [C04 · HORIZON TIDAL ECHO](../C04-horizon-tidal-echo/README.md) | A Deep Look at the Nature of Black Holes: Using Tidal Disruption Events to See the Unseeable | Session C |
| [C06 · PULSAR GEMINI WATCH](../C06-pulsar-gemini-watch/README.md) | The First Magnetar in a Binary System? | Session C |
| [C03 · TAURUS MOLECULE TRAIL](../C03-taurus-molecule-trail/README.md) | HCN Mapping of the Taurus Molecular Cloud | Session C |
| [C07 · ARTEMIS MEMORY BRIDGE](../C07-artemis-memory-bridge/README.md) | Taperings and Analytic Continuations of Supernova Gravitational Waves with Memory | Session C |
| [C02 · HUBBLE NIGHTFALL LAB](../C02-hubble-nightfall-lab/README.md) | Image Simulations for Testing the Fidelity of SKYSURF Background Measurement Algorithms | Session C |

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

Create a physically interpretable taxonomy of measured exoplanets without converting incomplete discovery catalogs into unsupported claims about the true planet population. Combine probabilistic mass-radius classes with interpretable machine learning and transparent abstention. Separate observed classification from inferred composition: an uncertain radius or mass does not uniquely determine whether a planet has oceans, a rocky interior, or a habitable environment.

**Question:** Which planetary classes are stable under measurement uncertainty, missing parameters, catalog updates, and changes in discovery method?

**Testable hypothesis:** Uncertainty-integrated classification with host-level splitting and an abstention category will achieve better calibrated labels than deterministic clustering on imputed catalog values.

## 1. Design basis and analysis boundary

The classification system operates on a frozen exoplanet catalog snapshot and explicit empirical class definitions. It returns probability vectors and abstentions for measured planets; it does not infer life, oceans or the survey occurrence distribution. Archive column definitions supply units, limits and provenance. The model preserves the difference between true mass and radial-velocity minimum mass.

The first fidelity level is a transparent radius/orbit taxonomy, followed by uncertainty-integrated classifiers and a latent mixture comparator. Composition-sensitive labels require an independently justified mapping, so radius-density overlaps remain probabilistic. Catalog reference reconciliation is part of engineering, not an afterthought. A planet without measured mass may still receive a radius class while density remains missing.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| C05-R1 | Every feature shall retain reference, inferred/measured status, uncertainty type and censoring flag. | Composite entries can combine incompatible fits. | Snapshot-schema and provenance audit. | NASA Exoplanet Archive column definitions. |
| C05-R2 | Minimum mass shall never populate the true-mass density field without an inclination model. | M sin i differs from M. | Construct minimum-mass fixture and verify density abstention. | Proposed physical typing rule. |
| C05-R3 | Training transformations shall be fit inside host-grouped folds. | Multiplanet siblings and imputation can leak information. | Fold-assignment and preprocessing lineage check. | Proposed leakage requirement. |
| C05-R4 | A class shall be emitted only when probability exceeds a preregistered threshold, initially 0.8 as a proposed target. | Uncertain and unfamiliar planets need abstention. | Validation reliability diagram and threshold sensitivity. | Proposed decision threshold, not physical certainty. |
| C05-R5 | Catalog class fractions shall be labeled as observed-sample summaries. | Confirmed planets lack a searched-star denominator. | Output terminology and selection audit. | Proposed population-scope requirement. |

## 3. Architecture and controlled interfaces

The catalog adapter emits one planet record with source-linked physical fields and asymmetric error/censoring objects. A reconciliation layer selects a coherent reference set or records unresolved conflicts. A posterior-feature sampler converts masses and radii to consistent SI or cgs units before deriving density; minimum masses enter a separate interface.

Training receives host-group and survey identifiers plus latent-feature draws. A probability calibrator uses validation data only. The inference adapter reports class probabilities, domain distance, missingness state and abstention reason. Snapshot diffs identify whether a changed output follows new measurements or model retraining. Missing and censored values remain distinct throughout, preventing imputation from masquerading as observational information.

![C05 engineering architecture](figures/architecture.svg)

The classification path preserves measurement provenance and uncertainty before calibrated probabilities and abstention are exported.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

$$
\rho_p=3M_p/(4\pi R_p^3)
$$

$$
p(c\mid y)=\int p(c\mid x)\,p(x\mid y)\,dx
$$

$$
\mathcal L=-\sum_i\sum_c w_c\,q_{ic}\log p(c\mid y_i)
$$

### Variables, units and conventions

- Planet mass Mp in Earth masses and radius Rp in Earth radii, converted before density calculation
- Density in g cm^-3; orbital period in days; irradiation in Earth-insolation units
- x is latent physical feature vector; y includes asymmetric uncertainties and upper/lower limits
- c is a preregistered empirical class, not a definitive composition or life label
- q is a soft target distribution; weights are fitted using training data only

### Assumptions and boundary conditions

- Prefer internally consistent Planetary Systems references for physical fits; composite tables may mix references.
- Minimum mass M sin i is kept distinct from true mass; inferred catalog quantities receive explicit flags.

### Derivation step 1

$$
\rho=3M/(4\pi R^3)
$$

Convert Earth mass/radius to grams/centimeters before deriving density. A dimensionless Earth-density ratio needs its own named output.

### Derivation step 2

$$
\operatorname{Var}(\ln\rho)=\operatorname{Var}(\ln M)+9\operatorname{Var}(\ln R)-6\operatorname{Cov}(\ln M,\ln R)
$$

First-order propagation shows radius dominates cubically and shared fit covariance matters. Use draws for asymmetric or near-zero uncertainties.

### Derivation step 3

$$
p(c\mid y)=\int p(c\mid x)p(x\mid y)\,dx
$$

The classifier averages over latent physical features, avoiding a falsely exact class from catalog point estimates.

### Derivation step 4

$$
\widehat c=\arg\max_c p_c\quad\text{if }\max_c p_c\ge q_*
$$

A declared abstention threshold q_star controls output coverage. Calibration determines empirical reliability, not physical composition proof.

### Inference or simulation procedure

Snapshot current PS and PSCompPars schemas and provenance. Build a baseline taxonomy from radius, density where available, orbit, and host properties, then compare a regularized classifier and mixture model. Integrate asymmetric errors with posterior draws; separate unavailable values from censoring and calculated values. Fit transformations, feature selection, class balancing, and imputation inside nested training folds. Split by host system and survey, because multiplanet systems and mission-specific features otherwise leak information. Assess out-of-distribution planets using feature-domain diagnostics and probabilistic abstention.

### Validity domain and fidelity limits

Discovery methods have different selection functions, and the confirmed-planet catalog lacks a common nondetection denominator. Catalog-based class frequencies are not occurrence rates. Mass-radius overlaps prevent definitive composition identification.

## 5. Data specifications and provenance

![C05 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| planet_id | string | 1 | Canonical planet and host identifier. | Aliases resolved; host grouping immutable within split. |
| mass | measurement<float64>&#124;null | Earth mass | True-mass posterior summary. | Exclude minimum mass unless typed separately. |
| radius | measurement<float64>&#124;null | Earth radius | Observed or inferred radius. | Asymmetric errors and reference retained. |
| mass_radius_cov | float64[2,2]&#124;null | declared physical^2 | Joint covariance when supplied. | Unknown covariance is explicitly unknown, not assumed measured zero. |
| period | measurement<float64> | day | Orbital period. | Positive with provenance. |
| feature_state | enum[] | 1 | Measured, inferred, censored or missing by field. | No numeric placeholder for missingness. |
| class_probability | float64[c] | 1 | Calibrated empirical probabilities. | Nonnegative, sum one; class-definition version recorded. |
| abstention | struct<bool,reason> | 1 | Insufficient certainty or unsupported feature domain. | Reason survives catalog export. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### NASA Exoplanet Archive PS/PSCompPars

[Product, archive or reference](https://exoplanetarchive.ipac.caltech.edu/docs/API_TD_columns.html)

**Fields:** pl_bmasse, pl_rade, pl_orbper, pl_insol, st_teff, st_met, uncertainty and reference fields

**Access:** Public tables; pin query date and exact columns using documented TAP.

**Role:** Measured feature and provenance source.

### Archive TAP documentation

[Product, archive or reference](https://exoplanet.ipac.caltech.edu/docs/TAP/usingTAP.html)

**Fields:** Query, table name, retrieval format, reproducible parameter selections

**Access:** Public API; comply with service limits and record query text.

**Role:** Reproducible extraction.

## 6. Uncertainty, sensitivity and identifiability

Catalog uncertainties are asymmetric and may be model derived. Mass-radius covariance, inconsistent references and survey-dependent missingness influence class boundaries. Sample physically allowed posteriors, checking the consequences of unknown covariance through sensitivity bounds. A density posterior from independent Gaussian errors can be misleading near zero mass or when radius is correlated with host properties.

A classifier may identify discovery method rather than planetary structure. Compare feature importance and calibration under leave-survey-out testing, and repeat after removing discovery metadata. Examine posterior class entropy as missing features are restored or perturbed. Nonidentifiability should raise abstention, not force a composition label. Selection functions are required for population inference and are outside this confirmed-catalog classifier.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Rule-based empirical bins | Transparent and reproducible. | Sharp boundaries conceal uncertainty. | Use as reference and integrate boundary crossing probabilities. |
| Regularized probabilistic classifier | Supports interactions and calibration. | Labels may embed subjective taxonomy. | Adopt when host/survey holdout reliability improves. |
| Latent mixture model | Can expose overlapping measured groups. | Components need not be physical species. | Use exploratory components and avoid automatic composition naming. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| C05-V1 | Unit consistency | Earth-unit and cgs implementations give the same physical density. | Evaluate matched synthetic mass-radius pairs. | Density dimensional identity. |
| C05-V2 | Radius perturbation | A factor-two radius change at fixed mass yields one-eighth density. | Analytic fixture through full feature sampler. | Cubic density relation. |
| C05-V3 | Minimum-mass record | True density remains unavailable unless inclination information is supplied. | Type-contract integration test. | Declared physical typing rule. |
| C05-V4 | Host/survey holdout | Reliability and abstention coverage are measured without refitting on test hosts. | Grouped nested split and independent survey evaluation. | Proposed transferability check. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Evaluate macro recall, Brier score, reliability diagrams, and abstention coverage on unseen hosts.
- Hold out one discovery method and test whether performance survives survey shift.
- Perturb observations using their errors; report class-switch rate and sensitivity to imputation assumptions.

## 9. Implementation and reproducible work packages

1. Snapshot TAP query, schema and cited reference fields.
2. Create physical measurement types separating censoring and minimum mass.
3. Implement uncertainty-draw features and unit-aware density calculation.
4. Version empirical class definitions and host/survey split manifests.
5. Fit and calibrate baselines with nested preprocessing.
6. Export probability/abstention cards and catalog-change attribution tables.

### Investigation sequence

1. Define classes, allowed features, censoring policy, and minimum confidence for assigning labels.
2. Retrieve a dated catalog snapshot; audit unit consistency and conflicting references.
3. Train baselines and uncertainty-aware models with nested host/system splits.
4. Release calibrated predictions plus ambiguous and out-of-domain categories, and rerun after a later frozen catalog update.

### Resources and interfaces to expertise

- Python, Astropy, pandas, scikit-learn or probabilistic mixture tools; data-provenance reviewer.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| Mixed reference parameters | Inconsistent density or class. | Provenance conflict ledger. | Choose coherent fits or widen uncertainty. |
| Imputation leakage | Inflated validation scores. | Transform fit IDs cross test boundary. | Fit every transform inside training folds. |
| Unfamiliar planet forced into class | Unsupported scientific interpretation. | Feature-domain diagnostic and high entropy. | Abstain and retain measured features. |

- Derived mass estimates, duplicate references, and discovery-method proxies can create false predictive skill.

## 11. Required engineering outputs

- Versioned feature table, model card, calibrated taxonomy atlas, and reproducible query notebook.

### Scientific result figures to produce during execution

Interactive mass-radius chart with posterior density contours, class probabilities, missing-data flags, and discovery-method filters.

### Included shared numerical starting point

![C05 shared reduced-model or catalog demonstration](../../../models/figures/09_real_exoplanet_sample.svg)

[Executable formulation, parameters, tabular outputs, provenance and verification](../../../models/README.md). This shared demonstration has a narrower domain than the project model above. Its own caption and methods identify synthetic parameters or the separately retrieved public catalog; it is not a completed result of the original project.

### Data diagnostic

![C05 data diagnostic](../../../data/figures/10_catalog_values_and_coverage.svg)

Real NASA Exoplanet Archive 200-row saved, query-ordered extract of rows with period and radius. The recorded request uses TOP 200 and ORDER BY pl_name; global first-200 ranking was not independently verified. Panel A preserves discovery-method categories and logarithmic scales; panel B makes the selected fields and nine missing host-metallicity values visible. This extract is not representative and cannot establish occurrence rates or physical class labels.

[Inputs, downloadable figure and provenance](../../../data/figures/README.md)

## 12. Cited technical and scientific resources

- [NASA Exoplanet Archive current column definitions](https://exoplanetarchive.ipac.caltech.edu/docs/API_TD_columns.html) — Table semantics, parameters, and reference structure.
- [NASA Exoplanet Archive TAP guide](https://exoplanet.ipac.caltech.edu/docs/TAP/usingTAP.html) — Supported programmatic retrieval.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
