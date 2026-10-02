# C29 · ACE WIND SHOCK LEDGER

**Original project:** Energy Balance at Interplanetary Shocks: In-situ Measurement of the Fraction in Energetic Protons with ACE and Wind

**Session C:** Astronomy & Space Physics

**Document class:** engineering research design and analysis record · **Revision:** 3 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session C](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_C.md) · [← C28](../C28-lowell-lunar-lantern/README.md) · [C30 →](../C30-artemis-first-horizons/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 6 | 4 | 8 | 3 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Purpose and scientific objective

Construct a shock-frame energy budget for ACE and Wind events using plasma, magnetic-field, and proton-spectrum measurements. Distinguish measured energetic-particle partial pressure from the total particle pressure and from a complete acceleration efficiency. Use energy-channel coverage, pitch-angle response, shock-normal uncertainty, and upstream/downstream window choice as explicit contributors to the result.

**Question:** What fraction of upstream energy flux appears in the measured downstream energetic-proton component, and which shock correlations survive instrument and shock-frame uncertainty?

**Testable hypothesis:** Some apparent geometry or Mach-number trends will weaken after jointly propagating spectrum, normal, shock-speed, and sampling-window uncertainties, while individual energy budgets remain informative.

## 1. Design basis and analysis boundary

The shock ledger computes band-limited energetic-proton pressure and energy flux in an explicitly inferred shock frame. Plasma, magnetic and proton-response measurements enter with independent quality domains. The David study supplies an event/procedure comparator; it does not justify treating measured finite-energy pressure as total acceleration efficiency. Unknown diffusion/anisotropic transport remains a residual or bounded term.

Begin with isotropic spectra and alternative normal/speed estimates, then joint Rankine-Hugoniot fitting and anisotropy sensitivity. Upstream/downstream windows are part of the model. ACE and Wind encounters may sample different shock patches, so matching events does not force identical budgets. Missing channels, composition and geometry remain documented limitations.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| C29-R1 | All energy-flux terms shall use the same shock frame and normal sign. | Mixed frames do not conserve the proposed budget. | Frame-transform and normal reversal fixtures. | Existing shock-frame model. |
| C29-R2 | Proton integration shall report measured energy bounds and channel-response coverage. | Unmeasured tails prevent total pressure claims. | Response/channel and integration-domain audit. | Primary event-study context. |
| C29-R3 | Numerical pressure/energy integration shall converge to 1%, a proposed target, for analytic spectra. | Channel interpolation can bias partial budgets. | Analytic power-law and grid-refinement fixtures. | Proposed numerical target. |
| C29-R4 | Normal/speed uncertainty shall compare at least two physically applicable estimation methods, a proposed design requirement. | One geometric estimate can dominate flux uncertainty. | Posterior method comparison and window sweep. | Proposed shock-geometry robustness. |
| C29-R5 | Nonadvective particle flux shall be retained as measured, bounded or unknown rather than automatically zero. | Diffusive/anisotropic transport affects efficiency. | Budget-state and pitch-angle evidence audit. | Existing Q_ep caveat. |
| C29-R6 | ACE/Wind comparisons shall retain spacecraft separation and sampling differences. | Related structures need not be identical patches. | Event-association and geometry manifest. | Proposed cross-spacecraft requirement. |

## 3. Architecture and controlled interfaces

CDF adapters emit plasma moments, field vectors and instrument-specific differential proton flux with energy/pitch-angle responses. A unit/response converter produces a declared isotropic intensity or a directional model. Upstream/downstream window selection attaches quality masks and stationarity diagnostics. A geometry engine estimates normal and shock speed, transforming all vector terms into one frame.

The particle integrator emits finite-band pressure and kinetic energy density. The MHD ledger computes kinetic, thermal and magnetic flux with covariance. An energetic transport module adds advective enthalpy and available nonadvective constraints. Joint fitting reports a residual flux instead of forcing closure by assigning missing energy to acceleration.

![C29 engineering architecture](figures/architecture.svg)

Response-aware partial particle integrals enter a common shock-frame ledger with explicit unknown transport and residual energy terms.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

$$
P_{\rm ep}=\frac{4\pi}{3}\int_{p_{\min}}^{p_{\max}}p^3v(p)f(p)\,dp
$$

$$
F_n=u_n[\rho u^2/2+\gamma_gP_g/(\gamma_g-1)+B_t^2/\mu_0]-B_n(\mathbf u_t\cdot\mathbf B_t)/\mu_0
$$

$$
U_{\rm ep}=4\pi\int E(p)p^2f(p)dp;\quad F_{\rm ep}=(U_{\rm ep}+P_{\rm ep})u_n+Q_{{\rm ep},n}
$$

$$
\eta_{\rm ep,band}=\Delta F_{\rm ep,band}/F_{n,\rm upstream}
$$

### Variables, units and conventions

- Pressure in Pa; velocity u in shock-frame m s^-1; density in kg m^-3
- B normal/tangential components in T; energy flux in W m^-2
- f is isotropic phase-space density with its normalization declared; p in kg m s^-1
- Particle spectra in instrument-specific differential-flux units must be converted with documented geometry
- Uep is kinetic energy density in J m^-3; Qep,n is unresolved/nonadvective particle energy flux in W m^-2
- eta_ep,band is band-limited and frame-dependent; include diffusive/anisotropic transport separately when data support it

### Assumptions and boundary conditions

- The displayed pressure integral assumes isotropy; test pitch-angle anisotropy or bound its effect.
- MHD energy flux is a baseline; energetic-particle enthalpy and transport terms must be incorporated consistently when computing Delta F.

### Derivation step 1

$$
j(E)=p^2f(p),\quad dE/dp=v
$$

For an isotropic phase-space density, dn=4 pi p squared f dp and differential intensity j=v(dn/dE)/(4 pi); specify per-energy and SI normalization.

### Derivation step 2

$$
P_{ep,band}=\frac{4\pi}{3}\int_{Emin}^{Emax}p(E)j(E)\,dE
$$

Changing variables in the phase-space pressure integral gives Pa for SI differential intensity. Measured bounds make this a partial pressure.

### Derivation step 3

$$
U_{ep,band}=4\pi\int_{Emin}^{Emax}E\,j(E)/v(E)\,dE
$$

This is kinetic energy density in J m^-3. Use relativistic p(E),v(E) where required by channel energies.

### Derivation step 4

$$
F_{ep,band}=(U_{ep,band}+P_{ep,band})u_n+Q_{ep,n},\quad\eta_{band}=\Delta F_{ep,band}/F_{up}
$$

Positive normal convention is stated; upstream/downstream difference and denominator share the frame. Unknown Q prevents a unique complete efficiency.

### Inference or simulation procedure

Select events with resolved plasma jumps and usable proton spectra on both sides. Estimate normal and shock speed with several conservation/coplanarity methods, then transform into a common frame. Integrate spectra over the measured energy domain and compare alternative thermal-plus-tail decompositions without uncontrolled extrapolation. Fit Rankine-Hugoniot conditions with joint measurement uncertainty and allow unresolved residual energy flux. Sweep upstream/downstream averaging windows and account for instrument cross-calibration. Compare ACE and Wind encounters of related structures when geometry permits; do not assume two spacecraft sampled identical shock patches.

### Validity domain and fidelity limits

Missing low/high-energy channels and unknown diffusion flux prevent a closed acceleration-efficiency measurement. Time averaging samples spatially structured shocks, and shock-normal methods can disagree.

## 5. Data specifications and provenance

![C29 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| event_epoch | float64 | CDF-declared time | Shock candidate and window boundaries. | Time conversions and masks recorded. |
| plasma_state | measurement<struct> | kg m^-3, m s^-1, Pa | Density/velocity/thermal pressure. | Composition/temperature convention and covariance. |
| magnetic_vector | measurement<float64[3]> | T | Field in common coordinates. | Coordinate transform and instrument offsets retained. |
| proton_intensity | measurement<float64[nE,nangle]> | m^-2 s^-1 sr^-1 J^-1 | Response-corrected differential flux. | Energy/pitch-angle bounds; invalid channels absent. |
| shock_geometry | posterior<struct> | 1, m s^-1 | Unit normal and shock speed. | Normal orientation and method identities. |
| particle_budget | posterior<float64[2]> | Pa, J m^-3 | Finite-band pressure and energy density. | Isotropy assumption and integration bounds attached. |
| energy_flux | posterior<float64[terms]> | W m^-2 | MHD and particle components. | Shared frame/covariance and unknown Q state. |
| band_fraction | posterior<float64>&#124;null | 1 | Conditional Delta particle/upstream flux. | Never labeled full efficiency without closure evidence. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### NASA CDAWeb ACE/Wind discovery

[Product, archive or reference](https://cdaweb.gsfc.nasa.gov/)

**Fields:** Plasma density/velocity/temperature, magnetic vectors, proton channels, epochs, quality metadata

**Access:** Public CDF products; resolve exact instrument products and energy responses for each event.

**Role:** Primary shock and energetic-particle measurements.

### David et al. energy-budget studies

[Product, archive or reference](https://arxiv.org/abs/2202.11029)

**Fields:** Event lists, partial-pressure procedures, shock-energy comparison

**Access:** Open paper; recreate the precise energy domain and window definitions.

**Role:** Published event baseline and reproducibility target.

## 6. Uncertainty, sensitivity and identifiability

Normal and speed uncertainty affect u_n, magnetic projections and every energy term coherently. Plasma composition and thermal pressure assumptions contribute shared errors. Integrate over geometry posterior draws rather than perturbing each flux component independently. Alternative upstream/downstream windows diagnose nonstationarity and shock precursor contamination.

Missing low/high-energy channels and pitch-angle coverage limit pressure and diffusion flux. Sweep isotropic versus directional assumptions where response supports it, bounding unsupported terms rather than extrapolating a convenient power law. Test parameter identifiability through synthetic conservation-consistent shocks. Cross-spacecraft disagreement can represent spatial structure or calibration, so retain both possibilities in the ledger.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Isotropic finite-band budget | Auditable measured-domain quantity. | Ignores directional transport. | Use baseline with explicit partial-pressure label. |
| Pitch-angle transport model | Can constrain nonadvective flux. | Incomplete angular response and temporal evolution. | Adopt only where coverage identifies anisotropy. |
| Joint conservation fit | Propagates geometry and plasma covariance. | Closure can be assumption dominated. | Use residual flux and method sensitivities rather than forced exact closure. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| C29-V1 | Zero energetic intensity | Partial pressure and energy density are zero. | Set j(E)=0 through all response conversions. | Integral zero identity. |
| C29-V2 | Analytic power-law spectrum | Numerical finite-band pressure/energy match quadrature references. | Known j(E) with declared relativistic relation. | Integration/convergence target. |
| C29-V3 | Normal/frame consistency | All signed normal fluxes transform consistently under reversed normal convention. | Reverse normal and update sign ledger. | Vector projection convention. |
| C29-V4 | Window/spacecraft holdout | Budgets are compared on alternate windows or a related encounter without forcing equality. | Freeze integration and geometry settings. | Proposed observational robustness. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Reproduce published event estimates within documented conventions before extending the sample.
- Hold out shocks and assess predicted jump conditions; bootstrap at event rather than energy-bin level.
- Repeat across normal estimators, time windows, anisotropy assumptions, and spectral coverage; check energy-unit conversions analytically.

## 9. Implementation and reproducible work packages

1. Resolve versioned plasma/field/proton responses and event windows.
2. Implement unit/directional-intensity adapters.
3. Infer normal/speed with joint posterior and alternative methods.
4. Build finite-band relativistic pressure/energy integrators.
5. Assemble common-frame MHD/particle/residual ledger.
6. Publish window, anisotropy and cross-spacecraft sensitivities without forced closure.

### Investigation sequence

1. Freeze event selection, energy integration band, frame conventions, and conservation equations.
2. Retrieve exact instrument response and quality metadata; build cross-calibration checks.
3. Infer shock parameters and partial energetic-particle fluxes with joint uncertainty.
4. Publish measured-band budgets, unresolved terms, and correlation tests that account for event-level selection.

### Resources and interfaces to expertise

- CDF and plasma tools, instrument response tables, shock-physics expertise, uncertainty sampler.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| Mixed spacecraft/shock frames | False energy residual. | Frame provenance mismatch. | Transform all vectors/fluxes jointly. |
| Partial pressure called total efficiency | Overstated acceleration. | Missing-domain/Q ledger. | Report finite-band conditional fraction. |
| Flux-unit conversion error | Orders-of-magnitude budget error. | Analytic spectrum/unit fixture. | Response-aware SI conversion and dimensional checks. |

- Calling partial pressure a total acceleration efficiency overstates the data; inconsistent frames or differential-flux units can dominate errors.

## 11. Required engineering outputs

- Shock-frame event ledger, band-limited energy-fraction atlas, conservation residuals, and robust correlation analysis.

### Scientific result figures to produce during execution

Upstream/downstream flux-budget bars with unresolved bands, particle spectra and integration limits, and uncertainty-aware Mach/obliquity comparisons.

## 12. Cited technical and scientific resources

- [David et al. (2021), ACE/Wind energy balance](https://arxiv.org/abs/2108.07350) — Original energy-budget analysis.
- [David et al. (2022), extended particle fractions](https://arxiv.org/abs/2202.11029) — Updated energy-domain and uncertainty treatment.
- [NASA CDAWeb](https://cdaweb.gsfc.nasa.gov/) — Measurement archive discovery.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
