# A10 · HUBBLE CARINA CLOCK

**Original project:** H-beta Analysis of eta Carinae Radial Velocity during Recent Periastron Passages

**Session A:** Math, Physics & Chemistry

**Document class:** engineering research design and analysis record · **Revision:** 3 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session A](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_A.md) · [← A09](../A09-spitzer-radio-origins/README.md) · [A11 →](../A11-osiris-sulfur-archive/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 4 | 3 | 7 | 2 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Purpose and scientific objective

Proposed mission: use H-beta time series to disentangle orbital motion from wind formation delays and phase-dependent line-profile changes in eta Carinae. The source paper's 2008–2020 baseline provides a concrete reproduction target. Any later periastron analysis requires newly acquired spectra and verified ephemerides; the word recent in the title is preserved without implying that new observations were obtained.

**Question:** Which H-beta velocity estimator and wind-response model most consistently recover orbital behavior across multiple periastron cycles?

**Testable hypothesis:** A wind-convolution model with profile diagnostics will explain systematic departures from instantaneous Keplerian velocity better than a line-centroid-only fit.

## 1. Design basis and analysis boundary

The system converts continuum-normalized H-beta profiles into multiple velocity estimators, then compares a common eccentric orbit with delayed wind formation and cycle-dependent profile terms. Its boundary includes wavelength convention, barycentric correction, aperture and instrument zero point. H-beta velocity is not assumed to equal instantaneous stellar center-of-mass motion.

Reproduce the published bisector baseline before testing centroids and positive response kernels. Begin with a Keplerian orbit and calibrated offsets, then add wind delay only if withheld-cycle prediction improves. Inclination and stellar masses need external information and remain outside a line-only velocity inference.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| A10-R1 | All profiles shall record air/vacuum convention, rest wavelength and barycentric time/correction provenance. | Convention offsets can dominate subtle cycle changes. | Round-trip wavelength/velocity and time tests. | Spectroscopic measurement contract. |
| A10-R2 | Bisector depth and continuum rule shall remain fixed across cycles. | Changing estimator definitions produces false variability. | Replay common synthetic and archived profiles. | Published bisector approach; proposed consistency gate. |
| A10-R3 | Delay kernels shall be nonnegative and integrate to one. | An unconstrained kernel can invent gain or anti-causal response. | Numerical normalization and support checks. | Physical response interpretation. |
| A10-R4 | Proposed selection gate: added wind terms improve withheld-cycle predictive likelihood with uncertainty. | Extra parameters can fit dense periastron sampling only. | Leave-one-cycle-out comparison at unchanged orbit priors. | Proposed model-selection criterion; outcomes unknown. |

## 3. Architecture and controlled interfaces

A spectrum adapter preserves flux, wavelength and spectral covariance plus instrument/aperture metadata. Continuum and contamination masks feed centroid and fixed-depth bisector modules, each returning velocity and covariance. Barycentric correction is applied once using a logged convention.

An orbital module solves Kepler's equation at declared barycentric epochs. A causal convolution uses positive delay weights and integrates orbital velocity; profile nuisance terms capture asymmetry or absorption without changing the orbital definition. The joint fitter shares orbital parameters across cycles while allowing calibrated offsets, then exports full profile and velocity residuals.

![A10 engineering architecture](figures/architecture.svg)

Separate profile estimators compare to an orbit filtered through a causal wind model. Time conventions and nuisance offsets are explicit; line-only fits do not establish inclination or stellar masses.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

```text
v_orb(t)=gamma+K[cos(nu(t)+omega)+e cos omega].
```

```text
M=2pi(t-T_0)/P=E-e sin E; tan(nu/2)=sqrt[(1+e)/(1-e)]tan(E/2).
```

```text
v_line(t)=integral_0^infinity Psi(tau)v_orb(t-tau)dtau+delta v_profile(t), with integral Psi dtau=1.
```

```text
v_D approximately c_light(lambda/lambda_0-1) for small nonrelativistic shifts using a consistent air/vacuum wavelength convention.
```

### Variables, units and conventions

- Period P, eccentricity e, systemic velocity gamma, semi-amplitude K, periastron time T_0, and argument omega.
- H-beta line bisector depth, profile asymmetry, formation-delay kernel Psi, instrumental zero point, and barycentric correction.

### Assumptions and boundary conditions

- Emission from an extended wind need not trace stellar center-of-mass motion instantly.
- Nebular emission, aperture, spectral resolution, and instrument changes enter the nuisance model; a companion detection is a separate claim.

### Derivation step 1

$$
M=2\pi(t-T_0)/P=E-e\sin E
$$

Mean anomaly is dimensionless when t and P share units. Solve for E with a bracketed method near high eccentricity; convert to true anomaly using the correct quadrant.

### Derivation step 2

$$
v=\gamma+K[\cos(\nu+\omega)+e\cos\omega]
$$

Project the Keplerian motion along the sightline. Positive velocity is receding; omega and systemic zero point require one documented convention.

### Derivation step 3

$$
v_{line}(t)=\int_0^\infty\Psi(\tau)v(t-\tau)d\tau+\delta v_{profile}
$$

Psi has inverse-time units and normalized integral. The kernel smooths/delays rapid orbital changes; profile terms remain separately identifiable only with supporting line information.

### Derivation step 4

$$
v_D\simeq c(\lambda/\lambda_0-1);\quad \sigma_v\simeq c\sigma_\lambda/\lambda_0
$$

Nonrelativistic conversion relates wavelength error to velocity error. Common rest-wavelength/calibration errors induce correlated shifts across spectra rather than independent noise.

### Inference or simulation procedure

Reproduce the published bisector approach, then compare centroids and several bisector levels on continuum-normalized spectra. Fit a common orbit plus cycle-specific profile systematics, and test simple positive delay kernels against instantaneous velocities. Preserve full profile residuals to diagnose absorption contamination and colliding-wind effects. Use leave-one-cycle-out prediction to judge whether the model generalizes rather than merely fits dense observations around one event.

### Validity domain and fidelity limits

H-beta may remain an imperfect tracer even with a delay kernel. Inclination and mass estimates require additional constraints, and irregular cadence or instrument zero points can mimic cycle differences.

## 5. Data specifications and provenance

![A10 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| spectrum_id | string | 1 | Instrument/cycle observation key. | Aperture and archive provenance required. |
| epoch_barycentric | float64 | day | Declared barycentric time coordinate. | Time scale explicit; missing epoch rejected. |
| wavelength_grid | vector<float64> | nm | Calibrated spectral coordinate. | Air/vacuum convention and rest lambda required. |
| normalized_flux | vector<float64> | 1 | Continuum-normalized line profile. | Masks and normalization uncertainty retained. |
| bisector_depth | float64 | 1 | Fixed relative profile level. | Definition identical across cycles. |
| velocity_covariance | matrix<float64> | (km/s)^2 | Estimator and calibration covariance. | Shared instrument errors included. |
| delay_kernel | array<time,weight> | day,day^-1 | Causal wind response model. | Nonnegative normalized; unknown parameters TBD. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### Orbital kinematics over three periastra

[Product, archive or reference](https://arxiv.org/abs/2301.00064)

**Fields:** CTIO spectra described for 2008–2020, H-beta bisector velocities, H-alpha variability, and orbital interpretations.

**Access:** Public manuscript; obtain raw/reduced spectra or tabulated velocities from supplements/authors if not archived.

**Role:** Original reproduction target.

### Wind-convolved orbital velocity model

[Product, archive or reference](https://arxiv.org/abs/2003.02783)

**Fields:** Delay-kernel formulation, multilevel Balmer-line fits, and model assumptions.

**Access:** Public research manuscript; raw data reuse and tabulated parameters require product-level checking.

**Role:** Physical systematic-error alternative.

## 6. Uncertainty, sensitivity and identifiability

Continuum placement, nebular contamination, instrument zero points and aperture differences affect estimators jointly. Strongly asymmetric profiles can shift bisectors differently from centroids. Orbital eccentricity, periastron time and kernel delay may be correlated; a longer delay can mimic a phase shift.

Use profile perturbation ensembles and cycle/instrument block resampling. Inspect Fisher/profile-likelihood directions for period–phase–delay degeneracy. Fit one cycle out and compare both velocity predictions and profile residuals; an excellent velocity curve with systematic line-shape error signals missing wind physics rather than a uniquely measured orbit.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Flux centroid | Uses the whole line. | Absorption/asymmetry bias. | Keep as diagnostic with masks. |
| Fixed-depth bisector | Matches published baseline. | Depth choice and blending matter. | Primary reproduction estimator; compare several fixed levels. |
| Causal wind convolution | Represents formation lag. | Phase/delay degeneracy. | Adopt only with normalization and withheld-cycle improvement. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| A10-V1 | Circular orbit | For e=0, velocity is a sinusoid with mean gamma. | Compare Kepler solver against analytic phase. | Keplerian limit. |
| A10-V2 | Instantaneous kernel | A unit impulse at zero delay reproduces orbital velocity. | Refine discrete convolution and compare. | Normalization/causality identity. |
| A10-V3 | Symmetric translated profile | Centroid and symmetric bisector recover the injected wavelength shift. | Replay analytic emission profiles with known contamination variants. | Synthetic measurement fixture; observed performance pending. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Check wavelength standards, barycentric corrections, consistent timestamps, and synthetic injected line shifts.
- Require cycle-held-out predictive improvement and inspect residuals versus bisector depth and profile asymmetry.
- Report posterior covariance and stability to removing contaminated lines; do not infer stellar masses from an unvalidated wind velocity amplitude.

## 9. Implementation and reproducible work packages

1. Create spectra_manifest.csv with time, wavelength and aperture conventions.
2. Implement normalize_and_mask.py preserving profile uncertainty.
3. Build bisector_centroid.py with translated-profile fixtures.
4. Implement kepler_orbit.py and causal_wind_kernel.py.
5. Create joint_cycle_fit.py with instrument-offset priors.
6. Publish leave_cycle_out.ipynb, velocity_covariance.parquet and full profile residuals.

### Investigation sequence

1. Build a spectrum manifest with observation times, instrument, aperture, reduction history, and wavelength convention.
2. Extract velocities with several estimators while retaining profile diagnostics and correlated uncertainty.
3. Fit shared orbital parameters and wind-delay alternatives; compare predictions on excluded phases and cycles.
4. Produce an observing plan for a future or later archival periastron with cadence concentrated where competing models disagree.

### Resources and interfaces to expertise

- High-resolution spectroscopy expertise, spectral-reduction software, orbital Bayesian modeling, and access to a documented spectral archive.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| Correction applied twice | Instrument-dependent velocity offset. | Correction provenance and known epoch replay. | Single correction stage. |
| Kernel unnormalized | Artificial velocity gain. | Integral check. | Constrained normalized weights. |
| Cycle-specific estimator drift | False secular orbit change. | Depth/mask version mismatch. | Immutable estimator configuration. |

- Time-dependent line shape can masquerade as orbital velocity.
- Aperture-dependent nebular contamination complicates cross-instrument comparisons.

## 11. Required engineering outputs

- Calibrated velocity/profile table, orbital-versus-wind model comparison, phase-folded multi-cycle atlas, and observing-priority specification.

### Scientific result figures to produce during execution

Phase-folded H-beta trailed spectra, velocity estimators with uncertainty, instantaneous and wind-delayed orbital curves, and residuals by periastron cycle.

## 12. Cited technical and scientific resources

- [Strawn et al., The orbital kinematics of eta Carinae over three periastra](https://arxiv.org/abs/2301.00064) — Original H-beta bisector investigation over the stated observational baseline.
- [Uncovering the orbital dynamics of stars hidden inside their powerful winds](https://arxiv.org/abs/2003.02783) — Original wind-response convolution model demonstrating line-dependent orbital biases.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
