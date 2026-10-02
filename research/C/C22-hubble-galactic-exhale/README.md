# C22 · HUBBLE GALACTIC EXHALE

**Original project:** Measuring Galactic Wind Frequency and Strength as a Function of Environment

**Session C:** Astronomy & Space Physics

**Document class:** engineering research design and analysis record · **Revision:** 3 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session C](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_C.md) · [← C21](../C21-parker-magnetic-trail/README.md) · [C23 →](../C23-kepler-metal-worlds/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 5 | 4 | 8 | 3 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Purpose and scientific objective

Build an environment-aware census of galactic outflows using spatially resolved spectroscopy and probabilistic wind detection. Separate wind occurrence from wind strength and control for stellar mass, star-formation rate, inclination, AGN activity, and spatial resolution. Observational association with environment is not automatically a causal environmental effect; the deliverable includes overlap diagnostics and sensitivity to galaxy selection.

**Question:** At matched mass, star formation, activity, and viewing angle, does galaxy environment predict outflow incidence, velocity, or a constrained mass-loading proxy?

**Testable hypothesis:** Some apparent environmental trends will weaken after accounting for host properties and wind-detection completeness, while any surviving association will be measurable with appropriately matched comparison samples.

## 1. Design basis and analysis boundary

The galactic-wind census separates wind incidence from conditional strength and tests environmental associations with matched host covariates. Inputs are public IFU cubes, instrumental/PSF response, host measurements and a neighbor/group catalog. Broad emission is a candidate diagnostic requiring rotation, beam-smearing and shock alternatives. Current SDSS access documents point to MaNGA's completed-survey products; exact DR17 reductions remain pinned.

Begin with line-profile likelihoods and rotation controls, then injection-derived detectability and finally environment-conditioned incidence/strength models. Ionized gas is one phase, so mass-loading output is a proxy unless density, geometry and radius are constrained. The design reports overlap and confounding sensitivity; observational association is not presented as a causal environmental effect.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| C22-R1 | Line fits shall include measured line-spread function and PSF-smeared rotation alternatives. | Rotation can mimic broad outflow components. | Rotating-disk no-wind cube injection. | Proposed physical specificity requirement. |
| C22-R2 | Wind labels shall retain probabilities and nondetection limits rather than hard deletion. | Borderline objects influence incidence. | Likelihood normalization and censored-fit integration. | Proposed inclusion contract. |
| C22-R3 | Environment definitions shall specify neighbor magnitude/redshift selection, scale and edge correction. | Environment estimators differ systematically. | Catalog/geometry audit and alternate-scale comparison. | Proposed environment contract. |
| C22-R4 | Synthetic recovery shall span inclination, line width, surface brightness and spatial resolution. | Detection selection correlates with environment/host properties. | Preregistered recovery grid. | Proposed completeness requirement. |
| C22-R5 | Mass loading shall be reported only with its geometry/density assumptions and phase label. | One line does not measure total gas flow. | Rate-unit and provenance audit. | Existing physical proxy caveat. |

## 3. Architecture and controlled interfaces

The cube adapter supplies flux, inverse variance/covariance, masks, spectral resolution, PSF and WCS. A stellar-continuum fitter and narrow/broad emission model share baseline uncertainty. A rotating-disk forward model predicts beam-smeared control spectra. Host-property and environment adapters retain survey weights and neighbor-catalog incompleteness.

A recovery engine injects controlled outflow components before fitting, emitting detectability versus host and observing state. A joint incidence/strength hierarchy uses wind probabilities, upper limits and selection. The optional physical-rate module consumes independent density/column, radius and solid-angle information; when those are missing it returns a proxy. Shared distance/SFR/continuum errors propagate into both covariates and rate ratios.

![C22 engineering architecture](figures/architecture.svg)

Competing rotation and detectability models condition wind evidence; environment associations and geometry-dependent mass loading remain separate products.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

$$
\mathrm{logit}\,p_{{\rm wind},i}=a+b\log\Sigma_{{\rm env},i}+c\log M_{*,i}+d\log\mathrm{SFR}_i+\mathbf q^T\mathbf z_i
$$

$$
v_{\rm out}=|v_{\rm shift}|+k\sigma_{\rm broad}\quad\text{with declared convention}
$$

$$
\dot M_{\rm out}\approx\Omega C_f\mu m_pN_Hr v_{\rm out};\quad\eta=\dot M_{\rm out}/\mathrm{SFR}
$$

### Variables, units and conventions

- Environment Sigma in neighbors Mpc^-2 using a specified redshift-space estimator
- Mass in solar masses; SFR and outflow rate in solar masses yr^-1
- Velocities in km s^-1; projected and deprojected values reported separately
- NH in cm^-2; r in cm; Omega is solid angle; Cf is covering fraction
- k is a chosen line-wing convention, not a universal physical coefficient; eta is dimensionless

### Assumptions and boundary conditions

- Broad emission or blueshifted absorption must be distinguished from beam-smeared rotation, shocks, and instrumental line spread.
- Mass outflow rates are geometry/density dependent and may be reported as proxies when the necessary measurements are absent.

### Derivation step 1

$$
\sigma_{obs}^2=\sigma_{gas}^2+\sigma_{LSF}^2
$$

Gaussian quadrature is a baseline resolution correction; negative inferred variance means unresolved width and requires a bound, not a real negative velocity.

### Derivation step 2

$$
v_{out}=|v_{shift}|+k\sigma_{broad}
$$

This declared line-wing convention yields a projected diagnostic. k is fixed as an analysis choice and varied in sensitivity, not treated as universal speed.

### Derivation step 3

$$
\dot M\approx\Omega C_f\mu m_pN_Hrv
$$

Column times radius times speed and particle mass gives mass per time for the assumed geometry; ionized emission-based alternatives require density/emissivity information.

### Derivation step 4

$$
\operatorname{logit}p_{wind}=a+b\log(\Sigma/\Sigma_0)+c\log(M_*/M_0)+d\log(SFR/SFR_0)+\mathbf q^T\mathbf z
$$

Dimensionless reference ratios define covariates. The fitted environment coefficient is associational and needs selection/overlap assessment.

### Inference or simulation procedure

Select a public IFU sample and reconstruct environment through a well-defined neighbor catalog. Fit stellar continuum and narrow/broad line components with the measured instrumental response; forward model rotation and PSF smearing. Produce probabilistic wind labels instead of dropping borderline objects. Measure detection completeness using synthetic outflows in real cubes. Fit incidence and strength jointly with censoring, survey weights, and host covariates. Check covariate overlap between environments; report associational effects and sensitivity to unmeasured confounders rather than causal language. Use alternative environment scales and group assignments as robustness checks.

### Validity domain and fidelity limits

Inclination, sensitivity, density diagnostics, and aperture coverage vary across surveys. Ionized-gas winds sample one phase and need not describe the total outflow mass or energy.

## 5. Data specifications and provenance

![C22 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| galaxy_id | string | 1 | IFU target and survey selection identity. | Duplicate observations grouped. |
| spectral_cube | float64[l,h,w] | documented flux | Observed spatial spectra. | Masks/LSF/PSF attached; missing spaxels not interpolated as data. |
| cube_cov | covariance | flux^2 | Spectral and resampling uncertainty. | Shared continuum and spatial covariance retained. |
| environment | measurement<float64> | neighbor Mpc^-2 | Declared density or group estimator. | Edge/redshift completeness flags required. |
| host_covariates | measurement<struct> | solar mass, solar mass yr^-1, degree | Mass/SFR/inclination/activity. | Joint covariance and source method retained. |
| wind_probability | float64 | 1 | Component evidence after competing models. | Bounded zero to one; not a secure physical label. |
| velocity_proxy | measurement<float64> | km s^-1 | Declared projected outflow diagnostic. | Unresolved/censored states retained. |
| mass_loading | posterior<float64>&#124;null | 1 | Conditional ionized-rate/SFR ratio. | Null when necessary geometry/density inputs unavailable. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### SDSS MaNGA public data access

[Product, archive or reference](https://www.sdss.org/dr20/data_access/get_data/)

**Fields:** DR17 IFU cubes, variances, masks, resolution, galaxy identifiers

**Access:** Public MaNGA data remain documented in DR17; select exact files and analysis-pipeline versions.

**Role:** Spatially resolved line measurements.

### Wind observation literature

[Product, archive or reference](https://arxiv.org/abs/astro-ph/0309119)

**Fields:** Outflow diagnostics and physical interpretation

**Access:** Open review; use original cited observations for empirical calibration.

**Role:** Physical diagnostic context.

## 6. Uncertainty, sensitivity and identifiability

Beam smearing, continuum subtraction and LSF uncertainty covary with broad-component width and amplitude. Inclination changes both visibility and projected speed; resolution/coverage varies with distance and survey selection. Include injection-derived detectability in incidence, and retain correlated host-parameter errors rather than using exact covariates.

Environment correlates with mass, star formation and activity, so the data may have little covariate overlap. Plot support and compare matched subsets, alternate environment scales and residual confounding sensitivity. Column/density, radius, covering fraction and solid angle often dominate mass-loading uncertainty; report those conditional factors explicitly. The ionized phase cannot close a total multiphase energy budget.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Broad-line census | Simple comparable diagnostic. | Rotation/shock confusion. | Use only with PSF/LSF control and probabilistic labels. |
| Resolved kinematic model | Uses spatial structure to reject rotation. | Computational and low-SNR limitations. | Adopt where independent spatial leverage exists. |
| Matched hierarchical environment fit | Accounts for selection and host covariance. | Residual confounding and poor overlap. | Report association only in supported covariate domain. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| C22-V1 | No-wind rotating disk | False wind evidence is measured under beam smearing. | Forward PSF/LSF cube simulation. | Proposed specificity control. |
| C22-V2 | Instrument-limited line | Inference returns unresolved intrinsic width rather than negative variance. | Inject sigma_gas tending to zero. | Quadrature-resolution limit. |
| C22-V3 | Rate dimensions | Column-radius-speed formula converts consistently to solar masses per year. | SI/cgs rate fixture. | Mass-flux dimensional identity. |
| C22-V4 | Held-out environment/sample | Incidence/strength predictions are checked without redefining wind thresholds. | Group or survey-block holdout. | Proposed association validation. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Hold out galaxies and entire groups; never split neighboring spaxels across training and test.
- Inject synthetic winds and rotating disks to quantify completeness and false broad-component rates.
- Compare independent line diagnostics and alternate density/geometry assumptions; report interval coverage in forward mocks.

## 9. Implementation and reproducible work packages

1. Freeze IFU, response and neighbor-catalog manifests.
2. Implement continuum/line/rotation response models.
3. Build probabilistic component and unresolved-width outputs.
4. Run host/resolution-stratified synthetic wind recovery.
5. Fit selection-aware incidence/strength with overlap diagnostics.
6. Publish conditional rate assumptions, environment sensitivities and sample holdouts.

### Investigation sequence

1. Freeze galaxy sample, environment definitions, wind evidence rules, and causal-language limits.
2. Fit spectra with PSF/rotation controls and preserve uncertain labels.
3. Estimate completeness and fit adjusted incidence/strength associations.
4. Publish environment comparisons restricted to covariate overlap with sensitivity analyses.

### Resources and interfaces to expertise

- IFU reduction/fitting tools, galaxy/environment catalogs, PSF and line-spread modeling, hierarchical sampler.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| Rotation called outflow | Inflated incidence. | Spatial velocity residual and control fit. | PSF-smeared alternatives and probabilistic labels. |
| Poor environment overlap | Extrapolated environmental coefficient. | Covariate support diagnostics. | Restrict domain or report nonidentifiability. |
| Proxy called total mass loss | Overstated feedback. | Missing density/phase/geometry metadata. | Retain proxy or conditional ionized rate. |

- Selection, PSF smearing, and AGN contamination can imitate winds; poor covariate overlap prevents defensible environmental comparisons.

## 11. Required engineering outputs

- Wind evidence catalog, completeness maps, adjusted environmental associations, and qualified mass-loading proxies.

### Scientific result figures to produce during execution

Environment bins with adjusted incidence/velocity intervals, host-covariate overlap, and linked observed versus rotation-only spectral maps.

## 12. Cited technical and scientific resources

- [SDSS current data-access guide](https://www.sdss.org/dr20/data_access/get_data/) — MaNGA cube and catalog discovery.
- [Veilleux, galactic-wind physics](https://arxiv.org/abs/astro-ph/0309119) — Outflow diagnostics and physical context.
- [SDSS release publications](https://sdss.org/science/publications/data-release-publications/) — MaNGA public release provenance.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
