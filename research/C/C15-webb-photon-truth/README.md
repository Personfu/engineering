# C15 · WEBB PHOTON TRUTH

**Original project:** Assessing the Performance of the JWST/NIRCam Image Simulator PhoSim-NIRCam

**Session C:** Astronomy & Space Physics

**Document class:** engineering research design and analysis record · **Revision:** 4 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session C](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_C.md) · [← C14](../C14-roman-darkhole-academy/README.md) · [C16 →](../C16-orion-strain-metrology/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 5 | 4 | 8 | 3 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Mission profile

![C15 engineering mission profile: scientific question, hypothesis, model scope and evidence status](figures/mission-profile.svg)

| Profile panel | Engineering signal | Open the evidence |
| --- | --- | --- |
| Mission identity | Assessing the Performance of the JWST/NIRCam Image Simulator PhoSim-NIRCam | [Scientific objective](#purpose-and-scientific-objective) |
| Model cockpit | 3 governing expressions; 4 derivation steps; declared assumptions and validity envelope | [Mathematical formulation](#4-mathematical-model-and-derivation) |
| Data blueprint | 8 proposed fields with types, units and quality rules | [Field map & downloads](data/README.md) |
| Verification queue | 5 proposed requirements; 4 specified cases; project execution evidence pending | [Case definitions](#8-verification-and-validation-cases) |
| Figure wall | Architecture, field map, planned result description | [Open full gallery](figures/README.md) |
| Resource library | 3 cited primary resources with support statements | [Cited resources](#12-cited-technical-and-scientific-resources) |

### Model cockpit

**Analysis method:** Choose public isolated-star exposures across detector positions, filters, flux levels, and wavefront epochs. Reproduce observation metadata and spectral energy distributions in PhoSim-NIRCam; use measured OPD references and contemporary NIRCam PSF documentation. Compare with STPSF and MIRAGE as independently implemented comparators, allowing only training-observation calibration updates. Evaluate encircled energy, radial wings, centroid, PSF moments, saturation onset, ramp statistics, and spatial noise. Propagate simulated raw exposures through the same pipeline version as observations. Maintain a discrepancy ledger with each proposed correction and its expected independent test.

**Operating envelope:** A public exposure may lack complete illumination or attitude metadata. Fitting every calibration parameter to a target can hide simulator error; validation must span different stars and epochs.

**Variables and conventions**

- N_gamma,j is a dimensionless photon/event count; F_lambda in W m^-2 m^-1, A_tel in m^2, t in s and lambda in m. T_j is dimensionless optical/detector throughput times pixel-assignment probability.
- t in s; OPD and wavelength in compatible length units
- PSF encircled energy and ellipticity dimensionless; centroid errors in pixels or mas
- Residual covariance Sigma accounts for detector correlations and mosaic resampling
- theta includes detector position, filter, SED, wavefront epoch, readout mode, and calibration context

### Artifact wall

![C15 proposed analysis architecture](figures/architecture.svg)

Collecting area is explicit in photon generation; ramp and processing interfaces allow simulator errors to be attributed by stage.

**Scientific result to produce:** Observed/simulated PSFs and residuals arranged by detector/filter, with encircled-energy error and held-out astrometric bias.

### Investigation feed · planned work

The feed records proposed work packages. A row becomes executed evidence only with versioned inputs, outputs and a reviewed result.

| Sequence | Evidence state | Engineering work package |
| --- | --- | --- |
| 01 | Planned | Freeze observation/source/wavefront/calibration manifests. |
| 02 | Planned | Implement dimensional photon-count ledger including area. |
| 03 | Planned | Run optical PSF and detector-ramp fixtures. |
| 04 | Planned | Process paired simulated/observed inputs with pinned pipeline. |
| 05 | Planned | Build stage-specific metrics and independent-simulator comparison. |
| 06 | Planned | Publish MC convergence, discrepancy attribution and star/epoch holdouts. |

### Mission connections

Connections are reading routes based on actual shared resources, supplied sessions or included illustrations. They do not establish physical dependencies, team collaborations or validated results.

| Connected mission | Original investigation | Recorded connection basis |
| --- | --- | --- |
| [C14 · ROMAN DARKHOLE ACADEMY](../C14-roman-darkhole-academy/README.md) | Controlling the Unseen: GIG Undergraduate Optical Research | Session C |
| [C16 · ORION STRAIN METROLOGY](../C16-orion-strain-metrology/README.md) | Gravitational Wave Calibration Error for Supernovae Core Collapse | Session C |
| [C13 · HORIZON RING ATLAS](../C13-horizon-ring-atlas/README.md) | Characterizing the Images of Black Hole Shadows | Session C |
| [C17 · GEMINI DISK SENTINEL](../C17-gemini-disk-sentinel/README.md) | Investigating the Planet Detection Limit in Debris Disk Images from the Gemini Planet Imager | Session C |
| [C12 · HUBBLE COSMIC GLOW](../C12-hubble-cosmic-glow/README.md) | SKYSURF: Measuring the Brightness of the Sky | Session C |
| [C18 · REIONIZATION OXYGEN BEACON](../C18-reionization-oxygen-beacon/README.md) | Characterizing High [OIII]/[OII] and High [OIII] Galaxies to Further LyC Study | Session C |

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

Evaluate PhoSim-NIRCam against measured JWST images and contemporary instrument references rather than its original prelaunch predictions alone. The 2019 simulator paper planned commissioning validation; this project closes that loop using frozen public observations. Compare optical PSF morphology, detector artifacts, astrometry, and noise covariance at distinct stages of the exposure-to-mosaic pipeline.

**Question:** Which residuals between PhoSim-NIRCam and flight observations arise from optical path errors, detector physics, calibration files, or downstream resampling?

**Testable hypothesis:** Updating measured wavefront and detector inputs will improve predictive fidelity, but remaining discrepancies will reveal model omissions that cannot be repaired by fitting a single idealized PSF.

## 1. Design basis and analysis boundary

The simulator assessment compares PhoSim-NIRCam with pinned public JWST observations at matched processing levels. Photon generation includes telescope collecting area explicitly, then optical/detector response and ramp processing. Flight PSF documentation provides a contemporary comparator. No prelaunch simulator prediction is treated as measured commissioning performance.

Start with photon-count and analytic aperture fixtures, then isolated-star optical PSFs, then ramps and mosaics. Each exposure reproduces filter, detector position, source SED, readout, wavefront epoch and calibration context where available. Missing illumination or attitude metadata creates a discrepancy category. STPSF or another independent implementation is a comparator rather than unquestioned truth.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| C15-R1 | Photon expectation shall include collecting area, exposure and registered-pixel throughput exactly once. | Flux is per unit area; omitted area breaks dimensional counts. | Unit and area-scaling fixtures. | Corrected governing photon model. |
| C15-R2 | Simulated and observed products shall share ramp/exposure/mosaic level and pipeline context. | Resampling and calibration create apparent simulator residuals. | Product-level and context audit. | Proposed comparison contract. |
| C15-R3 | Monte Carlo PSF metric uncertainty shall be below one-quarter of the observed comparison uncertainty, a proposed target. | Sampling noise must not dominate discrepancy diagnosis. | Repeat-seed variance and photon-count convergence. | Proposed numerical allocation. |
| C15-R4 | Optical/detector corrections shall be fit only on training observations. | Target-specific fitting can conceal simulator error. | Star/epoch holdout manifest. | Proposed validation requirement. |
| C15-R5 | Residual reports shall separate PSF, astrometry, ramp noise and resampling covariance. | A single chi-square cannot locate the faulty module. | Stage-specific metric/covariance outputs. | Proposed diagnostic interface. |

## 3. Architecture and controlled interfaces

An observation manifest links MAST products to readout metadata, source SED and wavefront/calibration references. A photon source converts flux density into incident photons using area and exposure. Optical propagation assigns positions; throughput and quantum efficiency determine registered events. Detector simulation produces charge accumulation and readout ramps with flags.

The same pinned calibration pipeline maps observed and simulated ramps into exposures and mosaics. A stage comparator measures encircled energy, wings, centroids, moments, ramp residuals and spatial covariance. An independent PSF engine receives the same source/wavefront inputs. Model corrections carry module identity and expected withheld-test behavior, allowing a resampling failure to be distinguished from an optical error.

![C15 engineering architecture](figures/architecture.svg)

Collecting area is explicit in photon generation; ramp and processing interfaces allow simulator errors to be attributed by stage.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

```text
N_gamma,j ~ Poisson[t*A_tel*integral F_lambda*T_j(lambda)*lambda/(h*c) d_lambda]; T_j includes the probability that an incident photon is registered in pixel j.
```

$$
P(\lambda)=|\mathcal F\{A\exp[2\pi i\,\mathrm{OPD}/\lambda]\}|^2
$$

$$
r=d-m(\theta);\quad \chi^2=r^T\Sigma^{-1}r
$$

### Variables, units and conventions

- N_gamma,j is a dimensionless photon/event count; F_lambda in W m^-2 m^-1, A_tel in m^2, t in s and lambda in m. T_j is dimensionless optical/detector throughput times pixel-assignment probability.
- t in s; OPD and wavelength in compatible length units
- PSF encircled energy and ellipticity dimensionless; centroid errors in pixels or mas
- Residual covariance Sigma accounts for detector correlations and mosaic resampling
- theta includes detector position, filter, SED, wavefront epoch, readout mode, and calibration context

### Assumptions and boundary conditions

- Distinguish raw ramps, calibrated exposures, and mosaics; compare like processing levels.
- Monte Carlo simulation uncertainty is separate from instrument-model uncertainty.

### Derivation step 1

$$
\mu_j=tA_{tel}\int F_\lambda T_j(\lambda)\lambda/(hc)\,d\lambda
$$

SI flux density W m^-2 m^-1 times area, wavelength integration and exposure gives energy; lambda/(hc) converts it to dimensionless photon count. T_j includes registered-event/pixel probability.

### Derivation step 2

$$
P_\lambda\propto|\mathcal F\{A e^{2\pi i OPD/\lambda}\}|^2
$$

Use compatible lengths for OPD and wavelength. Normalize PSF probability over captured plus explicitly tracked lost flux.

### Derivation step 3

$$
q(t_m)=\int_0^{t_m}\dot q(t)dt+\epsilon_m
$$

Ramp samples share accumulated photon counts, so their covariance is not independent read noise plus independent Poisson noise at every read.

### Derivation step 4

$$
\chi^2=(d-m)^T(\Sigma_{obs}+\Sigma_{MC}+\Sigma_{disc})^{-1}(d-m)
$$

Separate observed covariance, Monte Carlo variance and declared model discrepancy. A fitted discrepancy term cannot be used to claim successful optical prediction.

### Inference or simulation procedure

Choose public isolated-star exposures across detector positions, filters, flux levels, and wavefront epochs. Reproduce observation metadata and spectral energy distributions in PhoSim-NIRCam; use measured OPD references and contemporary NIRCam PSF documentation. Compare with STPSF and MIRAGE as independently implemented comparators, allowing only training-observation calibration updates. Evaluate encircled energy, radial wings, centroid, PSF moments, saturation onset, ramp statistics, and spatial noise. Propagate simulated raw exposures through the same pipeline version as observations. Maintain a discrepancy ledger with each proposed correction and its expected independent test.

### Validity domain and fidelity limits

A public exposure may lack complete illumination or attitude metadata. Fitting every calibration parameter to a target can hide simulator error; validation must span different stars and epochs.

## 5. Data specifications and provenance

![C15 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| exposure_id | string | 1 | MAST program/product identity. | Pin product checksum and processing level. |
| source_sed | float64[nlambda] | W m^-2 m^-1 | Flux spectrum at telescope. | Reference and uncertainty; wavelength in meters internally. |
| collecting_area | measurement<float64> | m^2 | Area consistent with throughput convention. | Do not double-count obscuration in both area and T. |
| throughput_pixel | float64[nlambda,npix] | 1 | Registered photon/pixel probability. | Sum cannot exceed declared total registration probability. |
| wavefront_opd | float64[h,w] | m | Matched optical-path map. | Epoch and pupil coordinate registration required. |
| ramp | float64[nread,h,w] | electron | Simulated/observed accumulated charge. | Read times and saturation masks retained. |
| metric_cov | float64[nmetric,nmetric] | mixed declared | Covariance of PSF/ramp/astrometric metrics. | MC and observation terms separately stored. |
| discrepancy_label | enum | 1 | Optical, detector, calibration or resampling category. | Unknown attribution retained explicitly. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### MAST JWST holdings

[Product, archive or reference](https://archive.stsci.edu/)

**Fields:** NIRCam ramps, calibrated products, quality arrays, exposure and pipeline metadata

**Access:** Public or released data only; freeze program IDs, calibration context, and exact products.

**Role:** Flight benchmark observations.

### STScI NIRCam PSF documentation

[Product, archive or reference](https://jwst-docs.stsci.edu/jwst-near-infrared-camera/nircam-performance/nircam-point-spread-functions)

**Fields:** Measured OPD references, PSF library, encircled energy, pixel scales

**Access:** Public reference page; select matched filter and measured wavefront epoch.

**Role:** Independent optical comparator.

## 6. Uncertainty, sensitivity and identifiability

Source color, wavefront epoch, pointing jitter and detector position can trade off in PSF shape. Photon Monte Carlo uncertainty decreases with simulated counts, while optical-model discrepancy does not. Estimate repeat-seed variance separately and vary SED/OPD/jitter within independently supported uncertainties. Missing attitude metadata should broaden prediction rather than be fitted without constraint.

Ramp covariance, interpixel response and mosaic resampling can imitate optical broadening. Compare stages before fitting corrections, and use sensitivity derivatives of metrics with respect to each module's parameters. Hold out stars and wavefront epochs to identify transferable changes. A correction improving one final mosaic but degrading ramps or independent optical predictions remains unresolved.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Optical PSF-only benchmark | Fast attribution of morphology. | Omits detector/readout effects. | Use first on unsaturated isolated stars. |
| End-to-end ramp simulation | Tests detector and pipeline chain. | Requires detailed metadata and covariance. | Adopt for stage-specific validation once inputs are available. |
| Independent simulator ensemble | Exposes implementation differences. | Shared calibration inputs can create common errors. | Use alongside analytic fixtures and flight holdouts. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| C15-V1 | Area scaling | Doubling collecting area doubles expected photons for fixed F, T and t. | Noiseless expectation and Poisson mean fixture. | Dimensional photon equation. |
| C15-V2 | Zero OPD | PSF reduces to the declared pupil diffraction model. | Analytic aperture comparison. | Fourier propagation limit. |
| C15-V3 | Flux conservation | Captured plus lost/undetected photons matches incident expectation statistically. | Count ledger and repeated seeds. | Photon accounting. |
| C15-V4 | Flight star/epoch holdout | Metric residuals and covariance are reported without fitting that observation. | Freeze optical/detector correction on training stars. | Proposed flight validation. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Hold out detectors or filter families and entire wavefront epochs.
- Compare pixel-level residual statistics and aperture photometry across signal-to-noise levels.
- Require Monte Carlo convergence before attributing residuals to physics; use independent STPSF/MIRAGE comparisons to diagnose error sources.

## 9. Implementation and reproducible work packages

1. Freeze observation/source/wavefront/calibration manifests.
2. Implement dimensional photon-count ledger including area.
3. Run optical PSF and detector-ramp fixtures.
4. Process paired simulated/observed inputs with pinned pipeline.
5. Build stage-specific metrics and independent-simulator comparison.
6. Publish MC convergence, discrepancy attribution and star/epoch holdouts.

### Investigation sequence

1. Audit the currently usable PhoSim-NIRCam code and document version and missing flight-era features.
2. Freeze a train/test matrix by star, detector, filter, and epoch.
3. Run matched simulations and the exact observation processing chain.
4. Fit limited calibration updates and publish unresolved residuals with practical consequences for science use.

### Resources and interfaces to expertise

- PhoSim-NIRCam source, STPSF, MIRAGE, JWST pipeline, compute queue, instrument-calibration expertise.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| Area omitted or duplicated | Incorrect photon rate and noise. | Unit/area-scaling check. | Single throughput-area convention. |
| Mosaic compared to raw model | False PSF/noise discrepancy. | Processing-level mismatch. | Match levels through same pipeline. |
| Overfit wavefront correction | Optimistic target performance. | Failure on new star/epoch. | Training-only correction and sensitivity ledger. |

- Prelaunch defaults and stale calibration files can dominate. Simulator agreement with another simulator alone is insufficient.

## 11. Required engineering outputs

- Flight-validation report, simulator discrepancy atlas, reproducible observation manifest, and recommended domain of use.

### Scientific result figures to produce during execution

Observed/simulated PSFs and residuals arranged by detector/filter, with encircled-energy error and held-out astrometric bias.

## 12. Cited technical and scientific resources

- [Burke et al. (2019), PhoSim-NIRCam](https://arxiv.org/abs/1905.06461) — Original photon-level simulator and planned flight validation.
- [STScI NIRCam PSFs](https://jwst-docs.stsci.edu/jwst-near-infrared-camera/nircam-performance/nircam-point-spread-functions) — Current measured-wavefront and PSF reference.
- [STScI MIRAGE documentation](https://jwst-docs.stsci.edu/jwst-other-tools/mirage-jwst-data-simulator) — Independent ramp-simulation comparator.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
