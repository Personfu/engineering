# C19 · WEBB YOUNG STAR ATMOSPHERES

**Original project:** Characterizing the Atmospheres of Low Surface Gravity M-dwarfs

**Session C:** Astronomy & Space Physics

**Document class:** engineering research design and analysis record · **Revision:** 4 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session C](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_C.md) · [← C18](../C18-reionization-oxygen-beacon/README.md) · [C20 →](../C20-trinity-accretion-echo/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 5 | 4 | 8 | 3 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Mission profile

![C19 engineering mission profile: scientific question, hypothesis, model scope and evidence status](figures/mission-profile.svg)

| Profile panel | Engineering signal | Open the evidence |
| --- | --- | --- |
| Mission identity | Characterizing the Atmospheres of Low Surface Gravity M-dwarfs | [Scientific objective](#purpose-and-scientific-objective) |
| Model cockpit | 3 governing expressions; 4 derivation steps; declared assumptions and validity envelope | [Mathematical formulation](#4-mathematical-model-and-derivation) |
| Data blueprint | 8 proposed fields with types, units and quality rules | [Field map & downloads](data/README.md) |
| Verification queue | 5 proposed requirements; 4 specified cases; project execution evidence pending | [Case definitions](#8-verification-and-validation-cases) |
| Figure wall | Architecture, field map, planned result description | [Open full gallery](figures/README.md) |
| Resource library | 3 cited primary resources with support statements | [Cited resources](#12-cited-technical-and-scientific-resources) |

### Model cockpit

**Analysis method:** Assemble public young and field M-dwarf spectra with source-specific citations and quality flags. Derive gravity-sensitive alkali, molecular, and continuum indices, then fit atmospheric grids with nuisance continuum/telluric calibration and correlated discrepancy. Include photometry and distance when available to constrain radius and luminosity. Compare field controls matched in spectral type and metallicity, and test unresolved-binary and reddening alternatives. Evaluate gravity against dynamical-mass/radius or well-characterized benchmark systems where available. Keep empirical spectral classification separate from model-derived physical parameters.

**Operating envelope:** Line lists, clouds, magnetic activity, and disequilibrium chemistry can create systematic residuals. Evolutionary-model ages and gravity are not independent benchmarks if they use the same atmosphere assumptions.

**Variables and conventions**

- Teff in K; logg is log10 of g in cm s^-2
- Wavelength in micrometers and flux in documented physical units or declared normalization
- Metallicity [Fe/H] in dex; extinction A_lambda in magnitudes
- Radius in solar radii and distance in pc, converted consistently
- Sigma includes correlated spectral error and a model-discrepancy term; veiling is an additional continuum

### Artifact wall

![C19 proposed analysis architecture](figures/architecture.svg)

Empirical gravity evidence and model-derived gravity remain distinct; absolute flux and independent benchmarks supply additional, explicitly tracked constraints.

**Scientific result to produce:** Temperature-matched young/field spectra with alkali bands, gravity posterior contours, and model-discrepancy residuals.

### Investigation feed · planned work

The feed records proposed work packages. A row becomes executed evidence only with versioned inputs, outputs and a reviewed result.

| Sequence | Evidence state | Engineering work package |
| --- | --- | --- |
| 01 | Planned | Create source and grid pedigree manifests with absolute/normalized flags. |
| 02 | Planned | Implement line-spread/extinction/velocity response operators. |
| 03 | Planned | Compute versioned empirical indices with covariance. |
| 04 | Planned | Fit atmosphere alternatives and optional luminosity scaling. |
| 05 | Planned | Build binary/reddening injections and independent benchmark splits. |
| 06 | Planned | Publish gravity sensitivity, grid-support masks and empirical versus physical outputs. |

### Mission connections

Connections are reading routes based on actual shared resources, supplied sessions or included illustrations. They do not establish physical dependencies, team collaborations or validated results.

| Connected mission | Original investigation | Recorded connection basis |
| --- | --- | --- |
| [C18 · REIONIZATION OXYGEN BEACON](../C18-reionization-oxygen-beacon/README.md) | Characterizing High [OIII]/[OII] and High [OIII] Galaxies to Further LyC Study | Session C |
| [C20 · TRINITY ACCRETION ECHO](../C20-trinity-accretion-echo/README.md) | Predictions for the Observable Autocorrelations of Accreting Black Holes from the Trinity Theoretical Model | Session C |
| [C17 · GEMINI DISK SENTINEL](../C17-gemini-disk-sentinel/README.md) | Investigating the Planet Detection Limit in Debris Disk Images from the Gemini Planet Imager | Session C |
| [C21 · PARKER MAGNETIC TRAIL](../C21-parker-magnetic-trail/README.md) | Identification of Switchback Intervals in Parker Space Probe Data | Session C |
| [C16 · ORION STRAIN METROLOGY](../C16-orion-strain-metrology/README.md) | Gravitational Wave Calibration Error for Supernovae Core Collapse | Session C |
| [C22 · HUBBLE GALACTIC EXHALE](../C22-hubble-galactic-exhale/README.md) | Measuring Galactic Wind Frequency and Strength as a Function of Environment | Session C |

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

Infer temperature, gravity, metallicity, cloud effects, and activity in young M-dwarf spectra while quantifying their degeneracies. Compare empirical young-object templates with atmosphere grids and independent age or luminosity constraints. Gravity-sensitive absorption is valuable, but one triangular H-band feature or weak alkali line is not accepted as a unique low-gravity measurement without dust, metallicity, and multiplicity checks.

**Question:** Which spectral features provide transferable gravity information once temperature, metallicity, dust/cloud opacity, veiling, and unresolved companions are allowed to vary?

**Testable hypothesis:** Joint spectral and luminosity inference with empirical controls will improve gravity calibration over index-only classification, while identifying regimes where atmosphere-grid systematics dominate.

## 1. Design basis and analysis boundary

The M-dwarf analysis derives empirical gravity indicators and atmosphere-model posteriors without conflating those products. Inputs include source-cited spectra, measured line-spread functions, photometry, distance and probabilistic age/group information. SPLAT documentation supplies atmosphere-grid comparison context. A triangular continuum or weak alkali feature is a diagnostic requiring competing cloud, reddening, activity and multiplicity explanations.

Begin with matched empirical young/field templates, then response-convolved grid inference, then joint luminosity/radius information. Spectra are either absolutely calibrated or explicitly normalized; the latter cannot independently recover radius. Benchmark mass/radius information must be independent of the atmosphere assumptions being tested. Unavailable grid resolution or source metadata creates a fit-domain limitation rather than a precise gravity result.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| C19-R1 | Every model spectrum shall be convolved with the measured line-spread function before sampling. | Resolution mismatch changes gravity-sensitive lines. | Constant/line-profile convolution fixtures. | Proposed observation contract. |
| C19-R2 | Grid interpolation shall reproduce held-out grid nodes within 1% in accepted bands, a proposed numerical target. | Interpolation error must not masquerade as atmosphere discrepancy. | Leave-node-out interpolation test. | Proposed numerical target. |
| C19-R3 | Physical logg shall explicitly mean log10(g in cm s^-2). | Gravity conventions can differ by units. | Unit-conversion and g=GM/R squared fixture. | Existing parameter definition. |
| C19-R4 | Gravity claims shall compare cloud/metallicity/reddening and unresolved-binary alternatives. | Single features are not unique gravity measurements. | Matched-control and alternate-model predictions. | Proposed degeneracy requirement. |
| C19-R5 | Benchmark validation shall identify atmosphere/evolution inputs shared with training. | Dependent benchmarks create circular accuracy. | Provenance-dependency audit. | Proposed independence requirement. |

## 3. Architecture and controlled interfaces

A spectrum adapter carries wavelength, flux, mask, covariance and line-spread function. Empirical-template and atmosphere-grid registries retain spectral type, parameter ranges and model pedigree. A response operator includes radial velocity, instrumental broadening, extinction and allowed continuum calibration. Telluric regions remain masked or explicitly modeled.

The likelihood combines spectra with photometry and distance where compatible. Physical radius scaling is active only for absolute-flux inputs. A multiplicity branch adds two model spectra before response convolution, while a veiling term is separate from stellar flux. The exporter reports empirical indices, conditional physical parameters and residual discrepancy separately, preserving which information actually constrained gravity.

![C19 engineering architecture](figures/architecture.svg)

Empirical gravity evidence and model-derived gravity remain distinct; absolute flux and independent benchmarks supply additional, explicitly tracked constraints.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

$$
F_{\lambda,obs}=(R_*/D)^2 F_{\lambda,atm}(T_{\rm eff},g,Z,\mathrm{clouds})10^{-0.4A_\lambda}+F_{\lambda,veil}
$$

$$
g=GM_*/R_*^2;\quad L=4\pi R_*^2\sigma_{\rm SB}T_{\rm eff}^4
$$

$$
\log p(F\mid\theta)=-\frac12 r^T\Sigma^{-1}r-\frac12\log|\Sigma|+\mathrm{const}
$$

### Variables, units and conventions

- Teff in K; logg is log10 of g in cm s^-2
- Wavelength in micrometers and flux in documented physical units or declared normalization
- Metallicity [Fe/H] in dex; extinction A_lambda in magnitudes
- Radius in solar radii and distance in pc, converted consistently
- Sigma includes correlated spectral error and a model-discrepancy term; veiling is an additional continuum

### Assumptions and boundary conditions

- Convolve models to each spectrum’s measured line-spread function and sample them on the observed wavelength grid.
- Young-star or group membership is probabilistic and not equivalent to a precisely known age.

### Derivation step 1

$$
F_{obs}=(R/D)^2F_{atm}10^{-0.4A_\lambda}+F_{veil}
$$

Surface flux and geometric dilution determine absolute flux. A free normalized continuum removes much of the R/D information.

### Derivation step 2

$$
g=GM/R^2,\quad\log g=\log_{10}[g/(1\ \mathrm{cm\,s^{-2}})]
$$

Compute in a consistent unit system; the dimensionless logarithm uses the declared cgs reference.

### Derivation step 3

$$
L=4\pi R^2\sigma_{SB}T_{eff}^4
$$

Luminosity links temperature and radius, but its uncertainty must include missing spectral energy and distance.

### Derivation step 4

$$
r=F_{obs}-\mathcal R(F_{atm}),\quad\log p=-\tfrac12r^T\Sigma^{-1}r-\tfrac12\log|\Sigma|+C
$$

Response R maps models to observed samples. Correlated model discrepancy contributes to Sigma but must remain visible in residual reporting.

### Inference or simulation procedure

Assemble public young and field M-dwarf spectra with source-specific citations and quality flags. Derive gravity-sensitive alkali, molecular, and continuum indices, then fit atmospheric grids with nuisance continuum/telluric calibration and correlated discrepancy. Include photometry and distance when available to constrain radius and luminosity. Compare field controls matched in spectral type and metallicity, and test unresolved-binary and reddening alternatives. Evaluate gravity against dynamical-mass/radius or well-characterized benchmark systems where available. Keep empirical spectral classification separate from model-derived physical parameters.

### Validity domain and fidelity limits

Line lists, clouds, magnetic activity, and disequilibrium chemistry can create systematic residuals. Evolutionary-model ages and gravity are not independent benchmarks if they use the same atmosphere assumptions.

## 5. Data specifications and provenance

![C19 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| source_id | string | 1 | Spectrum/photometry and reference identity. | Duplicate epochs and aliases resolved. |
| wavelength | float64[n] | micrometer | Observed spectral grid. | Air/vacuum and rest/observer frame declared. |
| flux | float64[n] | documented physical or normalized | Spectral measurements. | Normalization type explicit; bad/telluric pixels masked. |
| flux_cov | float64[n,n] | flux^2 | Spectral/calibration covariance. | Shared continuum and model terms stored separately. |
| line_spread | model<float64> | micrometer or velocity | Instrument kernel versus wavelength. | Measured or assumed status required. |
| distance_photometry | struct | pc, declared flux | Independent scaling observations. | Covariance and extinction assumptions retained. |
| gravity_indices | measurement<float64[]> | index-specific | Empirical alkali/molecular/continuum indices. | Window definition/version attached. |
| atmosphere_posterior | posterior<struct> | K, dex, solar radius | Teff/logg/metallicity/cloud/radius parameters. | Grid support and prior dependence reported. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### SpeX Prism Library

[Product, archive or reference](https://www.cass.ucsd.edu/~ajb/browndwarfs/spexprism/library.html)

**Fields:** Spectra, spectral type, observing metadata, quality, original references

**Access:** Public library; verify individual resolution, calibration, and reference.

**Role:** Empirical young/field spectral controls.

### SPLAT modeling documentation

[Product, archive or reference](https://splat.physics.ucsd.edu/splat/splat_model.html)

**Fields:** Atmosphere grids, gravity/temperature parameters, spectral comparison settings

**Access:** Public tool documentation; pin model grid and license.

**Role:** Reproducible atmosphere-grid comparator.

## 6. Uncertainty, sensitivity and identifiability

Temperature, gravity, metallicity and cloud opacity can generate similar broad spectral shapes. Extinction, veiling and continuum calibration further weaken those distinctions. Carry line and continuum covariance and quantify parameter sensitivity by excluding each diagnostic region. Absolute photometry/distance can help radius, but normalized spectra alone cannot provide the same scale constraint.

Line-list errors and activity are structured model discrepancy. Compare atmosphere grids with empirical templates and benchmark systems, tracking shared evolutionary assumptions. Inject binaries or reddening into matched templates to measure gravity bias, then examine posterior correlations and prior sensitivity. If cloud/gravity directions remain nearly collinear, report a gravity range or empirical youth indicator rather than an artificially precise physical value.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Empirical index/template comparison | Minimal atmosphere dependence. | Template coverage and metallicity confounding. | Use as an independent diagnostic product. |
| Atmosphere-grid likelihood | Connects spectra to physical parameters. | Line lists/cloud models and interpolation limits. | Use within validated grid support with discrepancy. |
| Joint spectrum/luminosity fit | Adds radius and scaling information. | Distance, extinction and binary uncertainty. | Adopt only for calibrated flux and compatible independent photometry. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| C19-V1 | Gravity units | SI and cgs calculations produce identical physical g after conversion. | Known mass/radius fixture. | Dimensional gravity identity. |
| C19-V2 | Kernel normalization | Convolving constant flux preserves it. | Wavelength-dependent response fixture. | Normalized line-spread operator. |
| C19-V3 | Binary alternative | A combined spectrum is not automatically assigned single-star gravity with narrow intervals. | Inject two template spectra before convolution. | Proposed multiplicity robustness test. |
| C19-V4 | Independent benchmark | Empirical and physical gravity errors are measured without refitting benchmark-specific calibration. | Mass/radius benchmark holdout with pedigree audit. | Proposed physical validation. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Leave one association or cluster out of training to test age-domain transfer.
- Hold out wavelength windows and check their predicted absorption profiles.
- Use blind injected binary, dusty, reddened, and low-gravity spectra; report gravity bias and coverage by temperature and signal-to-noise.

## 9. Implementation and reproducible work packages

1. Create source and grid pedigree manifests with absolute/normalized flags.
2. Implement line-spread/extinction/velocity response operators.
3. Compute versioned empirical indices with covariance.
4. Fit atmosphere alternatives and optional luminosity scaling.
5. Build binary/reddening injections and independent benchmark splits.
6. Publish gravity sensitivity, grid-support masks and empirical versus physical outputs.

### Investigation sequence

1. Freeze spectral-type domain, gravity conventions, benchmark hierarchy, and telluric masks.
2. Assemble provenance-rich spectra and matched field controls.
3. Fit atmosphere and empirical-template models jointly with photometric constraints.
4. Release gravity identifiability maps and a follow-up priority list for independent mass/radius benchmarks.

### Resources and interfaces to expertise

- SPLAT, atmosphere grids, IRTF/SpeX expertise, photometric and astrometric catalogs, probabilistic sampler.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| Resolution mismatch | Biased alkali/gravity estimates. | Line residuals track instrumental width. | Convolve to measured response. |
| Normalized flux used for radius | Unsupported radius posterior. | Missing absolute calibration flag. | Disable scale-derived radius or use independent flux. |
| Cloud feature called unique low gravity | Misclassified physical state. | Alternative-model comparable fit. | Retain degeneracy and empirical/physical distinctions. |

- Selection based on gravity indicators can inflate success; overlapping spectral data and reference labels must be audited.

## 11. Required engineering outputs

- M-dwarf atmosphere atlas, benchmark comparison, correlated residual library, and qualified gravity classifications.

### Scientific result figures to produce during execution

Temperature-matched young/field spectra with alkali bands, gravity posterior contours, and model-discrepancy residuals.

## 12. Cited technical and scientific resources

- [Gorlova et al. (2003), near-IR gravity indicators](https://arxiv.org/abs/astro-ph/0305147) — Gravity-sensitive spectral features and measurement context.
- [SpeX Prism Library paper](https://arxiv.org/abs/1406.4887) — Empirical spectral-library provenance.
- [SPLAT atmospheric modeling guide](https://splat.physics.ucsd.edu/splat/splat_model.html) — Physical grid parameter conventions.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
