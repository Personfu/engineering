# C30 · ARTEMIS FIRST HORIZONS

**Original project:** The Origins of Supermassive Black Holes

**Session C:** Astronomy & Space Physics

**Document class:** engineering research design and analysis record · **Revision:** 3 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session C](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_C.md) · [← C29](../C29-ace-wind-shock-ledger/README.md) · [D01 →](../../D/D01-x-59-vortex-command/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 6 | 4 | 8 | 4 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Purpose and scientific objective

Compare black-hole seed scenarios using a forward population model constrained by high-redshift luminosity, host properties, and lower-redshift occupation evidence. Keep light remnants, cluster pathways, and heavy direct-collapse seeds as alternatives rather than asserting a single origin for every supermassive black hole. Separate evidence for rapid early growth from evidence that uniquely identifies a seed mechanism.

**Question:** Which combination of seed mass distribution, accretion duty cycle, radiative efficiency, and merger history can explain observed early black holes without violating survey selection and host constraints?

**Testable hypothesis:** Joint faint-population and host constraints will discriminate seed models more effectively than the brightest quasars alone, whose growth histories can erase information about initial masses.

## 1. Design basis and analysis boundary

The origin study compares seed mechanisms through a forward population/observation model. Light-remnant, cluster and heavy-seed branches share growth and selection modules but retain distinct initial distributions and host dependence. UHZ1 is a model-conditioned high-redshift test case: its inferred mass assumes accretion/lensing/SED information and is not universal proof of one seed path.

Begin with analytic constant-growth limits, then stochastic accretion and simplified host assembly, then mergers and survey selection where data justify them. Seed masses, birth times, efficiency, duty cycle, obscuration and lensing are jointly uncertain. TRINITY products can be a population comparator; their inferred relations are not independent new observations. A useful result identifies which observables retain seed information after growth degeneracy.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| C30-R1 | Every seed branch shall share the same documented growth and survey-selection comparison envelope. | Different selection can manufacture seed preference. | Branch configuration and forward-observation audit. | Proposed model-comparison contract. |
| C30-R2 | Mass inferred from assumed Eddington ratio shall be labeled conditional with lambda prior. | Luminosity alone does not measure mass. | Synthetic luminosity/mass inversion fixture. | UHZ1 primary-study convention. |
| C30-R3 | Growth integration shall reproduce constant-parameter exponential mass to 0.5%, a proposed target. | Time/unit errors bias early growth feasibility. | Analytic growth fixture and refinement. | Proposed numerical target. |
| C30-R4 | Host and black-hole mass likelihoods shall include lensing covariance and AGN-classification uncertainty where applicable. | Magnification affects both numerator and host comparisons. | Joint observation-model audit. | Primary lensed-candidate context. |
| C30-R5 | Population rates shall include active fraction, obscuration and flux selection. | Rare luminous detections do not specify seed abundance. | Survey forward-count and zero-detection cases. | Proposed selection requirement. |
| C30-R6 | Forecasts shall remain separate from measured high-redshift constraints. | Prospective merger sensitivity is not an observation. | Product-state/type audit. | Proposed evidence contract. |

## 3. Architecture and controlled interfaces

A seed generator emits initial mass, birth cosmic time and host occupation from a versioned scenario. A host/merger-tree adapter provides assembly and merger delays with stated cosmology. The growth integrator evolves stochastic Eddington ratio, duty states, efficiency and merger mass changes. Each mass history has an energy-accounting ledger.

An emission/obscuration module maps active mass histories into SED/luminosity. A lensing and survey operator produces observed flux, apparent host properties and inclusion probability. Candidate likelihoods include ambiguous classification and conditional mass information. A posterior comparator uses independent low-redshift occupation or high-redshift luminosity constraints without double counting population-model fits.

![C30 engineering architecture](figures/architecture.svg)

Seed scenarios reach observations only through growth, emission and selection, exposing why final luminous masses alone may not identify seed origin.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

$$
L_{\rm Edd}=4\pi GMm_pc/\sigma_T;\quad L=\lambda L_{\rm Edd}
$$

$$
\dot M_{\rm BH}=(1-\epsilon)L/(\epsilon c^2)
$$

$$
M(t)=M_{\rm seed}\exp[\lambda f_{\rm duty}(1-\epsilon)t/(\epsilon t_E)],\quad t_E=\sigma_Tc/(4\pi Gm_p)
$$

### Variables, units and conventions

- Black-hole mass in solar masses; luminosity in erg s^-1
- lambda is Eddington ratio; epsilon radiative efficiency; duty fraction dimensionless
- Cosmic time in yr, derived from a stated cosmology; tE about 0.45 Gyr under the displayed convention
- Seed birth redshift and host-halo mass distributions explicitly model environmental dependence
- Constant-growth expression is an explanatory limit; variable accretion and mergers are integrated in the full model

### Assumptions and boundary conditions

- Black-hole masses inferred assuming Eddington accretion are conditional, not direct mass measurements.
- Include obscuration, lensing uncertainty, active fraction, flux limits, and ambiguous AGN classifications in the observation model.

### Derivation step 1

$$
L_{Edd}=4\pi GMm_pc/\sigma_T
$$

Equate electron-scattering radiation force and gravity for the stated ionized-hydrogen convention; composition/opacity alternatives are additional assumptions.

### Derivation step 2

$$
\dot M_{BH}=(1-\epsilon)L/(\epsilon c^2)
$$

Radiated power corresponds to supplied mass rate L/(epsilon c squared); only the retained fraction grows the hole.

### Derivation step 3

$$
\frac{d\ln M}{dt}=\lambda f_{duty}(1-\epsilon)/(\epsilon t_E),\quad t_E=\sigma_Tc/(4\pi Gm_p)
$$

The duty-averaged constant-parameter limit connects growth to time. Stochastic on/off histories are integrated explicitly instead of assuming all objects share that average.

### Derivation step 4

$$
M(t)=M_{seed}e^{\int g(t)dt},\quad\ln[M/M_{seed}]=\int g(t)dt
$$

Observed final mass constrains seed mass and accumulated growth together. Merger contributions break the simple exponential and require a separate mass ledger.

### Inference or simulation procedure

Construct seed populations on a documented merger-tree or simplified host-assembly framework. Draw physically motivated light, cluster, and heavy-seed distributions and evolve stochastic accretion with efficiency and duty-cycle priors. Add merger mass loss and delays where justified. Forward predict luminosity functions, active black-hole/host ratios, and occupation fractions through survey selection. Compare to independently documented JWST/X-ray candidates with model-dependent mass and lensing uncertainties. Use posterior predictive checks and expected information gain to identify observations most sensitive to seeds rather than growth. Treat potential LISA merger forecasts as forecasts with mission-response assumptions, not measured events.

### Validity domain and fidelity limits

Uncertain accretion can make seed models observationally degenerate; rare bright objects do not define the full population. Spectral AGN identification, host masses, and magnification carry substantial systematics.

## 5. Data specifications and provenance

![C30 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| seed_scenario | enum/version | 1 | Light, cluster or heavy initial model. | Distribution and host-occupation assumptions recorded. |
| birth_mass_time | distribution<float64[2]> | solar mass, yr | Seed initial conditions. | Cosmology/time origin and support required. |
| growth_history | float64[n,fields] | yr, 1, solar mass | Accretion/duty/efficiency and mass evolution. | Efficiency bounds and on/off convention explicit. |
| merger_ledger | table&#124;null | solar mass, yr | Added mass, delay and loss assumptions. | Absent module does not imply measured zero mergers. |
| intrinsic_luminosity | distribution<float64> | erg s^-1 | Active SED/bolometric model. | Bolometric correction and lambda convention. |
| lensing_host_cov | covariance | mixed declared | Magnification/host/BH observation dependence. | Shared lensing errors retained. |
| selection_probability | float64 | 1 | Survey inclusion after obscuration/flux/cadence. | Nonnegative; unsupported domains flagged. |
| seed_evidence | struct | 1 | Conditional model score and predictive checks. | Separate measured constraints from forecasts and reused model products. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### TRINITY population products

[Product, archive or reference](https://github.com/HaowenZhang/TRINITY)

**Fields:** Halo/galaxy/SMBH statistical constraints, redshift-dependent population products

**Access:** Public source; pin commit and avoid treating inferred relations as independent observations.

**Role:** Population comparator and growth constraints.

### UHZ1 heavy-seed candidate studies

[Product, archive or reference](https://arxiv.org/abs/2305.15458)

**Fields:** X-ray and host measurements, redshift, conditional mass and lensing assumptions

**Access:** Open paper; inspect original data and subsequent literature for selected sample.

**Role:** High-redshift multiwavelength test case, not universal seed proof.

## 6. Uncertainty, sensitivity and identifiability

Seed mass, birth time, duty cycle, Eddington ratio and radiative efficiency are exponentially degenerate through integrated growth. Final luminosity constrains active mass times lambda, not mass alone. Lensing and bolometric corrections correlate inferred host and black-hole quantities. Carry these dependencies rather than assigning independent Gaussian masses from the same observations.

Inspect profile/posterior directions along constant accumulated growth, then add occupation and luminosity-function constraints to assess which degeneracies break. Vary host assembly, merger delays and obscuration independently. Forward synthetic surveys reveal when apparent heavy-seed preference comes from active/flux selection. Expected information gain should prioritize constraints on growth or occupation when bright-end masses alone remain seed insensitive.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Analytic constant-growth bounds | Transparent feasibility calculation. | No stochastic selection or mergers. | Use explanatory baseline only. |
| Stochastic population growth | Models duty/efficiency variation and observables. | Prior-sensitive sparse early constraints. | Use primary comparison with selection. |
| Merger-tree evolution | Links seeds to host assembly/merger forecasts. | Tree resolution/delay assumptions. | Add when independent host/occupation information justifies complexity. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| C30-V1 | No accretion/mergers | Mass stays at seed value. | Set lambda or duty to zero. | Growth equation limit. |
| C30-V2 | Constant growth | Numerical history matches exponential within proposed target. | Fixed lambda, efficiency and duty fixture. | Analytic integration. |
| C30-V3 | Radiative bookkeeping | Retained mass and radiated energy obey the chosen efficiency relation. | Integrate supplied mass and luminosity. | Mass-energy accounting. |
| C30-V4 | Synthetic survey holdout | Seed/growth degeneracy and selection recovery are measured without retuning scenario priors. | Held-out host trees/observation fields. | Proposed population validation. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Recover known seed-mixture parameters from blind synthetic selected populations.
- Hold out redshift bins and observatories; predict luminosity and host-ratio distributions.
- Test alternative accretion priors, AGN classifications, magnification, and selection assumptions; report remaining model degeneracy.

## 9. Implementation and reproducible work packages

1. Version seed distributions, cosmology and host assembly inputs.
2. Implement growth/energy ledgers with exponential fixtures.
3. Add stochastic duty/efficiency and justified merger-delay modules.
4. Build luminosity/obscuration/lensing response and classification mixtures.
5. Fit shared-envelope seed branches through survey selection.
6. Publish identifiability, independent-constraint checks and separately labeled forecasts.

### Investigation sequence

1. Define seed alternatives, growth freedoms, cosmology, and survey observation operators before fitting.
2. Assemble source-cited observations with uncertainty and classification probabilities.
3. Forward fit populations and compare predictive performance under equal growth flexibility.
4. Design follow-up targeting faint AGN, host ratios, or occupation measurements that maximally separate viable scenarios.

### Resources and interfaces to expertise

- Population/merger-tree tools, cosmology library, AGN spectroscopy and X-ray expertise, hierarchical sampler.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| Conditional mass treated direct | False seed certainty. | Missing lambda/lensing provenance. | Fit observation likelihood and label assumptions. |
| Growth tuned separately per seed branch | Unfair model comparison. | Branch configuration differences. | Shared growth envelope and explicit scenario priors. |
| Rare active detections treated full population | Biased occupation/seed abundance. | Missing obscuration/selection denominator. | Forward survey selection and supported-domain limits. |

- Conditional masses and flexible accretion histories can exaggerate seed evidence; unavailable faint-population denominators limit discrimination.

## 11. Required engineering outputs

- Seed-growth population simulator, evidence/selection ledger, posterior scenario atlas, and discriminating observation roadmap.

### Scientific result figures to produce during execution

Seed-to-SMBH growth tracks with efficiency/duty-cycle bands, selection-filtered luminosity functions, and observations that discriminate viable scenarios.

## 12. Cited technical and scientific resources

- [Inayoshi et al. (2019), first massive-black-hole assembly](https://arxiv.org/abs/1911.05791) — Seed and growth mechanisms and observational discriminants.
- [Volonteri et al. (2021), massive-black-hole origins](https://arxiv.org/abs/2110.10175) — Seed-to-growth framework and open questions.
- [Bogdan et al. (2023), UHZ1 X-ray candidate](https://arxiv.org/abs/2305.15458) — Specific high-redshift evidence with conditional interpretation.
- [TRINITY population repository](https://github.com/HaowenZhang/TRINITY) — Population comparator; its inferred products are not independent measured seed evidence.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
