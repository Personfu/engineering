# C16 · ORION STRAIN METROLOGY

**Original project:** Gravitational Wave Calibration Error for Supernovae Core Collapse

**Session C:** Astronomy & Space Physics

**Document class:** engineering research design and analysis record · **Revision:** 3 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session C](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_C.md) · [← C15](../C15-webb-photon-truth/README.md) · [C17 →](../C17-gemini-disk-sentinel/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 5 | 4 | 8 | 2 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Purpose and scientific objective

Quantify how detector amplitude and phase calibration uncertainty changes supernova detection and parameter inference. Use observing-run-specific published calibration products, then draw correlated transfer-function errors rather than independent noise at each frequency. Separate waveform uncertainty, calibration uncertainty, and statistical detector noise so a future weak burst is not assigned misleading astrophysical precision.

**Question:** When does calibration uncertainty become a limiting error for CCSN amplitude, frequency-track, sky-coherence, or memory-related measurements?

**Testable hypothesis:** Marginalizing frequency-correlated calibration functions will restore parameter-interval coverage in affected regimes with modest detection loss compared with ignoring calibration error.

## 1. Design basis and analysis boundary

The calibration experiment quantifies how smooth amplitude/phase response errors alter CCSN detector-band inference. Its boundary includes released strain, epoch-specific uncertainty products, network signals and a stated calibration-function prior. Public pointwise envelopes do not uniquely specify cross-frequency covariance. GWOSC O4 technical details supply release and uncertainty context, while missing covariance is treated as a sensitivity assumption.

Start with constant amplitude and timing-error fixtures, add correlated spline/GP functions, then analyze real-noise injections with ignored and marginalized calibration. Waveform and statistical-noise uncertainty remain separate dimensions. Results outside the declared calibrated band are excluded. A permanent-memory continuation requires its own physical and observation model before entering this experiment.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| C16-R1 | Calibration draws shall use detector, epoch and strain-variant-matched uncertainty products. | A generic envelope can misrepresent the data release. | Manifest and frequency-support audit. | GWOSC O4 technical details. |
| C16-R2 | Pointwise envelopes shall never be labeled measured covariance. | Frequency-independent draws create unrealistic response roughness. | Prior documentation and smoothness diagnostics. | Proposed uncertainty typing rule. |
| C16-R3 | Small-error linearization shall agree with exact transfer to 1% for the chosen perturbation envelope, a proposed target. | Linear uncertainty propagation needs a validated range. | Analytic/exact response comparison. | Proposed numerical target. |
| C16-R4 | Ignored and marginalized analyses shall share waveforms, noise and nuisance priors. | Different inputs confound calibration impact. | Paired-injection hash audit. | Proposed experiment control. |
| C16-R5 | Bias and coverage shall be reported by detector band and network configuration. | Calibration impact depends on morphology and coherence. | Stratified injection and held-out noise tables. | Proposed reporting requirement. |

## 3. Architecture and controlled interfaces

An uncertainty-product adapter emits magnitude/phase envelopes and available correlation metadata. A calibration prior generator produces dimensionless amplitude and radian phase functions with named spline or GP parameters. A waveform/network module projects physical signals before applying each detector's transfer perturbation. A released-noise adapter supplies strain and a matching PSD/band mask.

Paired inference branches either ignore, fix or marginalize the same perturbation realization. Metrics include amplitude bias, timing/frequency-track shifts, normalized mismatch and network coherence. A correlation-length sensitivity branch brackets what cannot be recovered from envelopes alone. Shared calibration functions correlate frequencies and signal parameters; this dependence survives into posterior uncertainty.

![C16 engineering architecture](figures/architecture.svg)

Matched perturbations drive paired inference; the covariance generator is explicitly an assumption when public products provide only envelopes.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

$$
\widetilde h_{k,\rm measured}(f)=[1+\delta A_k(f)]e^{i\delta\phi_k(f)}\widetilde h_{k,\rm true}(f)
$$

$$
p(\theta\mid d)\propto\int p(d\mid\theta,\delta A,\delta\phi)p(\delta A,\delta\phi)p(\theta)d\delta A\,d\delta\phi
$$

$$
\mathcal M=1-\max_{t_c,\phi_c}(h_1\mid h_2)/\sqrt{(h_1\mid h_1)(h_2\mid h_2)}
$$

### Variables, units and conventions

- deltaA dimensionless fractional amplitude error; deltaPhi in radians
- Frequency f in Hz; detector strain dimensionless; PSD in Hz^-1
- Calibration functions modeled by spline or Gaussian-process coefficients with supplied correlation assumptions
- M is normalized mismatch in the declared detector band
- theta includes signal amplitude, time, frequency-track, sky, and polarization; distance assumptions are separate

### Assumptions and boundary conditions

- Use the uncertainty description for the selected detector, epoch, run, and released strain variant.
- Do not equate a pointwise calibration envelope with a known covariance or random independently distributed frequency error.

### Derivation step 1

$$
C_k(f)=[1+\delta A_k(f)]e^{i\delta\phi_k(f)}
$$

C is a dimensionless multiplicative response error under a declared measured-versus-true convention.

### Derivation step 2

$$
\delta\widetilde h\approx[\delta A+i\delta\phi]\widetilde h
$$

First-order expansion separates amplitude and quadrature errors, valid only for small perturbations.

### Derivation step 3

$$
\delta\phi(f)=-2\pi f\Delta t
$$

With exp(-2 pi i f t) Fourier convention, a delayed signal contributes this phase slope; timing and calibration phase can therefore be degenerate.

### Derivation step 4

$$
\Sigma_{cal}\approx J_C\Sigma_cJ_C^T
$$

Calibration coefficient covariance Sigma_c maps through waveform sensitivity J_C into correlated data uncertainty. Marginalization is preferable when nonlinear or posterior-dependent effects are important.

### Inference or simulation procedure

Choose supernova waveform families with distinct durations, spectral peaks, and polarizations. Draw smooth calibration functions consistent with published magnitude/phase uncertainty products and plausible correlation lengths when covariance is unavailable. Inject calibrated signals into real noise, then analyze with ignored, fixed-shift, and marginalized calibration models. Quantify network coherence and parameter bias across distance, detector configuration, and sky location. Repeat for alternate strain releases only when documentation explains their differences. Preserve the calibrated frequency limits and apply time-domain filters consistently to data and signals.

### Validity domain and fidelity limits

Public envelope products may not uniquely specify the underlying calibration posterior. Low-frequency memory analyses are especially sensitive to the observation operator; results outside the stated calibrated band cannot be treated as measured sensitivity.

## 5. Data specifications and provenance

![C16 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| detector_epoch | struct<string,time> | GPS second | Detector and release epoch. | Strain variant and uncertainty product matched. |
| frequency | float64[n] | Hz | Calibration/inference frequency grid. | Within documented calibrated support. |
| amplitude_error | float64[n] | 1 | Fractional transfer perturbation. | Convention and envelope version required. |
| phase_error | float64[n] | radian | Transfer phase perturbation. | Smooth function; unwrap convention explicit. |
| coefficient_cov | float64[m,m]&#124;null | mixed declared | Spline/GP prior covariance. | Null means unavailable measured covariance; assumed version labeled. |
| waveform_id | string | 1 | Physical CCSN simulation provenance. | No split leakage through repeated injections. |
| parameter_shift | float64[q] | parameter-specific | Paired ignored/marginalized bias metric. | Store full posterior and injection truth where defined. |
| mismatch | float64 | 1 | Noise-weighted band-limited normalized difference. | Optimization over time/phase explicitly declared. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### GWOSC O4 technical details

[Product, archive or reference](https://gwosc.org/O4/o4_details/)

**Fields:** Calibration magnitude/phase uncertainties, strain variants, frequency limits

**Access:** Public documentation links uncertainty files; match epoch and release before downloading.

**Role:** Instrument error inputs.

### GWOSC strain

[Product, archive or reference](https://gwosc.org/)

**Fields:** Detector strain, quality masks, GPS timestamps, sample rate

**Access:** Public released products; select untouched test intervals.

**Role:** Real noise and detector response context.

## 6. Uncertainty, sensitivity and identifiability

A constant amplitude calibration error is degenerate with source distance or intrinsic amplitude; a linear phase slope is degenerate with arrival time. Smooth frequency-dependent errors can shift inferred track curvature or polarization coherence. Analyze sensitivity directions jointly with astrophysical nuisance terms, rather than treating calibration variance as a scalar added to every parameter.

Envelope-to-covariance conversion is a model choice unless the calibration posterior supplies correlation. Sweep correlation lengths and coefficient bases constrained to the same envelope, retaining resulting parameter spread as uncertainty. Waveform discrepancy and PSD drift must vary independently so their effects are not attributed to calibration. Coverage is assessed on held-out noise epochs and physical waveform families.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Fixed envelope extremum | Simple conservative perturbation. | May be physically unlikely and not probabilistic. | Use deterministic stress test only. |
| Smooth spline prior | Auditable coefficients and marginalization. | Knot choice and covariance assumptions matter. | Use when matching published structure is possible. |
| Gaussian-process response prior | Flexible correlated functions. | Kernel assumptions can dominate missing covariance. | Use as sensitivity comparator with documented hyperparameters. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| C16-V1 | Zero calibration error | All paired branches recover identical likelihoods up to numerical sampling. | Set deltaA=deltaPhi=0. | Transfer identity. |
| C16-V2 | Constant amplitude error | Signal amplitude scales by 1+deltaA without changing normalized waveform shape. | Noise-free amplitude fixture. | Multiplicative response relation. |
| C16-V3 | Pure time delay | Phase slope equals minus 2 pi f delay and can be absorbed by fitted time within bounds. | Analytic delayed waveform. | Fourier shift theorem. |
| C16-V4 | Held-out epoch/family | Bias and interval coverage are measured under frozen calibration prior choices. | Independent noise and CCSN-family holdout. | Proposed calibration inference validation. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Recover known synthetic calibration curves using calibration-aware inference when identifiable.
- Hold out waveform families and noise epochs; report detection efficiency at fixed false-alarm rate.
- Check 90% astrophysical interval coverage under multiple calibration correlation lengths and coherent/inter-detector error scenarios.

## 9. Implementation and reproducible work packages

1. Resolve release-specific calibration uncertainty files and band limits.
2. Implement explicit measured/true transfer conventions.
3. Build smooth coefficient priors and correlation sensitivity grid.
4. Create amplitude/time-delay and exact-linearization fixtures.
5. Run paired injection/inference branches on held-out noise.
6. Publish coefficient provenance, bias/coverage and band-limited mismatch tables.

### Investigation sequence

1. Freeze a detector/run/release and extract its calibration limits and uncertainty file provenance.
2. Build smooth amplitude/phase draws and identify covariance assumptions explicitly.
3. Run waveform injections with and without calibration marginalization.
4. Derive parameter-specific calibration requirements using validated bias and coverage curves.

### Resources and interfaces to expertise

- Calibration product reader, GW inference tools, waveform registry, metrology collaborator, batch compute.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| Independent frequency perturbations | Artificial rough waveform distortion. | Nonphysical response derivatives. | Use smooth correlated priors and label assumptions. |
| Wrong release envelope | Misestimated uncertainty. | Metadata mismatch. | Pin detector/epoch/strain variant. |
| Calibration absorbed as physics | Biased distance or timing. | Strong posterior calibration/parameter correlation. | Marginalize and report conditional identifiability. |

- Using a newer calibration envelope with an older strain series can produce inconsistent results; inaccessible covariance must remain an explicit limitation.

## 11. Required engineering outputs

- Calibration impact atlas, reproducible injection study, uncertainty assumption ledger, and requirements table.

### Scientific result figures to produce during execution

Amplitude/phase uncertainty curves with parameter bias and coverage versus signal strength, and separate statistical/model/calibration contributions.

## 12. Cited technical and scientific resources

- [GWOSC O4 technical details](https://gwosc.org/O4/o4_details/) — Released calibration products and calibrated-band documentation.
- [CCSN parameter inference study](https://arxiv.org/abs/2201.01397) — Astrophysical waveform-morphology comparator.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
