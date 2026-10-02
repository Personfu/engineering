# D03 · INGENUITY DESCENT & BUBBLE LAB

**Original project:** Optimizing Autorotating Sensor Probe Design for Space Exploration- Low Frequency Unsteadiness in Laminar Separation Bubbles

**Session D:** Aeronautics

**Document class:** engineering research design and analysis record · **Revision:** 3 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session D](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_D.md) · [← D02](../D02-langley-stall-memory/README.md) · [D04 →](../D04-glenn-sphere-standard/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 5 | 4 | 8 | 3 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Purpose and scientific objective

The supplied line combines two research concepts. Preserve both as coordinated but distinct proposed work packages: D03a, an autorotating sensor-probe feasibility study, and D03b, low-frequency dynamics of laminar separation bubbles. Their scientific connection is low-Reynolds aerodynamics; neither project's success is assumed to validate the other. The aggregate mission asks how aerodynamic unsteadiness changes passive descent robustness.

**Question:** Which rotor geometries admit stable autorotation under exploration-atmosphere conditions, and which low-frequency separation modes change their force/torque uncertainty?

**Testable hypothesis:** A coupled design informed by independently validated low-Reynolds response statistics will predict descent dispersion better than steady blade-element models; feasibility on Mars may remain mass- and deployment-limited.

## 1. Design basis and analysis boundary

The original combined title remains one portfolio entry containing two independently gated engineering packages. D03a models autorotating probe descent, rotor equilibrium and stability in declared atmospheric conditions. D03b analyzes low-frequency unsteadiness in stationary laminar separation bubbles. Each has separate data, acceptance evidence and limitations; shared aerodynamic envelopes are transferred only after a compatibility review.

D03a begins with coupled blade-element torque and vertical force balance, then adds deployment/low-Reynolds discrepancy envelopes. D03b begins with calibrated pressure/velocity spectra and stationarity tests, then conditional POD/modal analysis. A stationary bubble mode is not automatically a rotating-blade forcing model, and matching Reynolds number alone does not establish dynamic similarity.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| D03-R1 | D03a shall solve descent and rotor torque simultaneously with declared positive directions. | Prescribed rotation can hide unstable equilibrium. | Check force/torque residuals; proposed normalized target 10^-6. | Proposed numerical gate. |
| D03-R2 | D03a stability shall use coupled V/Omega Jacobian eigenvalues and parameter uncertainty. | Zero mean torque does not ensure stable autorotation. | Linearize and compare small-perturbation trajectories. | Local dynamical criterion. |
| D03-R3 | D03b spectral claims shall report record duration, window, resolution and stationarity. | Low-frequency drift can imitate a bubble mode. | Repeat segmented spectra and detrending alternatives. | Spectral-analysis contract. |
| D03-R4 | Proposed D03b record target: at least 20 cycles of a candidate lowest resolved mode. | Few cycles produce weak frequency/statistical evidence. | Compare duration to identified peak period and flag insufficient records. | Proposed screening target, not universal guarantee. |
| D03-R5 | Transferred D03b data shall pass a nondimensional compatibility and uncertainty gate. | Stationary/rotating flows differ. | Review Re, Mach, reduced frequency, geometry and rotational effects. | Transfer requirement; no combined validation claimed. |

## 3. Architecture and controlled interfaces

D03a accepts probe mass, rotor inertia, gravity and atmospheric density/viscosity. Blade tables provide C_L/C_D versus local flow state with covariance; blade-element quadrature returns upward force and driving torque. A coupled ODE advances downward-positive V and rotation Omega, while deployment uncertainty remains a separate scenario.

D03b stores stationary airfoil geometry, bubble-length definition and synchronized pressure/velocity arrays. A spectral module produces PSD in native squared units per Hz; POD uses spatial weights and centering. A transfer registry exports only compatible force/torque uncertainty envelopes to D03a, never raw modal frequencies as universal rotor inputs.

![D03 engineering architecture](figures/architecture.svg)

D03a and D03b retain separate physics and acceptance paths. Only a reviewed aerodynamic uncertainty envelope connects them; stationary bubble spectra do not directly establish autorotating-probe performance.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

```text
D03a: m dot(V)=mg-F_z; I_r dot(Omega)=Q_aero-Q_loss.
```

```text
D03a: dF_z=0.5 rho U_rel^2 c_r(C_L cos phi+C_D sin phi)dr; solve torque and descent jointly.
```

```text
D03b: St=f L_b/U_inf; P_xx(f)=Fourier-based power spectrum of a defined pressure/velocity observable.
```

```text
D03b: u'(x,t)=sum_j a_j(t)phi_j(x) for a POD basis; modes are descriptive unless independently linked to a mechanism.
```

### Variables, units and conventions

- Probe mass m, rotor inertia I_r, descent speed V, rotation Omega, local relative speed U_rel, blade chord c_r, flow angle phi.
- Atmospheric density/viscosity, gravitational acceleration, deployed geometry, bubble length L_b, Reynolds number, turbulence intensity, and signal duration.

### Assumptions and boundary conditions

- D03a's blade-element model is a first approximation; reverse flow, low-Reynolds nonlinearities, and deployment transients require extensions.
- D03b baseline is a stationary airfoil experiment; transferring its statistics to rotating blades requires separate tests.

### Derivation step 1

$$
m\dot V=mg-F_z;\quad I_r\dot\Omega=Q_{aero}-Q_{loss}
$$

With downward-positive descent and upward-positive aerodynamic force, equilibrium requires F_z=mg and torque balance. Torque loss is positive resisting rotation.

### Derivation step 2

$$
U_{rel}=\sqrt{V^2+(\Omega r)^2};\quad\phi=\tan^{-1}[V/(\Omega r)]
$$

These first-tier local velocities omit induced/reverse-flow effects. Integrate declared lift/drag projections for force and torque using blade chord and radius.

### Derivation step 3

$$
\delta\dot x=J\delta x;\quad J=\partial[(mg-F_z)/m,(Q_a-Q_l)/I_r]/\partial[V,\Omega]
$$

Eigenvalues with negative real parts imply local stability under the reduced smooth model. Uncertain aerodynamic derivatives require an ensemble, not one nominal eigenvalue.

### Derivation step 4

$$
St=fL_b/U;\quad\int_0^{f_N}P_{xx}(f)df=\operatorname{var}(x)
$$

The bubble frequency is nondimensional only with declared L_b. A consistently normalized one-sided PSD integrates to variance, giving an independent spectral conservation check.

### Derivation step 5

$$
u'(x,t)=\sum_ja_j(t)\phi_j(x)
$$

Weighted POD diagonalizes fluctuation covariance and ranks energy. A large mode or spectral peak is descriptive until independently tied to bubble motion or a mechanism.

### Inference or simulation procedure

D03a searches a constrained mass–geometry–atmosphere space using torque equilibrium, stability derivatives, and Monte Carlo descent. D03b uses pressure/velocity time series to distinguish genuine low-frequency bubble modes from drift and sparse-sampling artifacts. Combine only validated aerodynamic response envelopes in the descent model, then test an independent prototype or higher-fidelity simulation. Maintain separate datasets, acceptance gates, and publications for each package.

### Validity domain and fidelity limits

Matching Reynolds number alone does not match gravity, rotor inertia, density, Mach number, and dynamic similarity. A low-frequency spectral peak does not prove a unique bubble-bursting mechanism.

## 5. Data specifications and provenance

![D03 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| package_id | enum | 1 | D03a or D03b origin. | Never merge datasets without transfer record. |
| atmosphere | record | kg/m^3,Pa s,m/s^2 | Density, viscosity and gravity. | Uncertainty and scenario provenance required. |
| rotor_geometry | array<radius,chord> | m | Blade discretization. | Positive dimensions and deployment state. |
| aero_coefficients | float64[state,2] | 1 | Coefficient rows align to a versioned local-flow-state index; columns are exactly [C_L,C_D]. | State index declares alpha/Re/Mach, row correspondence and interpolation domain; coefficient covariance required. |
| descent_state | pair<float64> | m/s,rad/s | Downward V and Omega. | Directions fixed; failed state null. |
| bubble_length | nullable<float64> | m | Stationary separation-to-reattachment distance. | Method/uncertainty required. |
| pressure_velocity_trace | nullable<record> | Pa,m/s | Synchronized D03b observations. | Sampling/duration/masks required. |
| transfer_envelope | nullable<record> | N,N m | Compatible force/torque perturbation model. | Review ID required; null if unvalidated. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### NAU SEED Mars autorotation concept

[Product, archive or reference](https://www.ceias.nau.edu/capstone/projects/ME/2022/22F_P17MarsSensor/Project/index.html)

**Fields:** Proposed probe concept, feasibility objectives, Earth/Mars similarity questions, and student design context.

**Access:** Public university project; a precedent, not the original user's project or flight-proven hardware.

**Role:** D03a architecture context.

### Original laminar-bubble fluctuation experiment

[Product, archive or reference](https://www.jstage.jst.go.jp/article/jjsass/50/582/50_582_293/_article/-char/en)

**Fields:** Airfoil/Reynolds context, low-frequency velocity fluctuation observations, and phase-averaged behavior.

**Access:** Public research article; request raw time series if not supplemented.

**Role:** D03b benchmark.

## 6. Uncertainty, sensitivity and identifiability

D03a uncertainty includes atmosphere, aerodynamic tables, inertia, deployment and induced-flow discrepancy. Force and torque errors are correlated because they use the same blade coefficients. Rotor equilibrium may vanish or change stability across the ensemble; report those outcomes rather than average them into one viable design.

D03b uncertainty includes finite-record variance, low-frequency drift, probe response and bubble-length definition. Block/segment spectra and spatially weighted modal checks test robustness. Transfer uncertainty additionally covers rotation and geometry mismatch; stationary evidence remains a separate scientific result when that bridge cannot be supported.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Blade-element descent model | Fast coupled equilibrium search. | Low-Re/induced flow limitations. | Use for screening with discrepancy bounds. |
| Higher-fidelity rotor simulation | Resolves unsteady coupling. | Cost and closure uncertainty. | Apply to candidate equilibria and stability failures. |
| Stationary bubble modal study | Controlled mechanism diagnostics. | Not rotor-equivalent by default. | Transfer only after explicit similarity review. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| D03-V1 | D03a zero aerodynamic load | With F_z=0, descent acceleration is g; zero net torque holds Omega. | Analytic ODE fixture. | Sign and dimensional check. |
| D03-V2 | D03a stable linear equilibrium | Small perturbations follow exp(Jt) and decay for negative-real eigenvalues. | Compare integration with matrix exponential. | Local stability derivation. |
| D03-V3 | D03b PSD normalization | Integrated one-sided PSD equals variance within window correction. | Synthetic known-frequency signal and Parseval check. | Spectral conservation; records pending. |
| D03-V4 | D03 package isolation | Missing transfer approval leaves D03a aerodynamic envelope unchanged. | Integration fixture with incompatible D03b geometry. | Transfer contract. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- D03a: conserve torque/energy; recover terminal-force balance; validate descent and spin history in an authorized contained test environment.
- D03b: verify sampling/aliasing control, stationarity, block-bootstrap uncertainty, and repeatability of bubble-length dynamics.
- Coupled gate: held-out descent dispersion improves only when bubble-informed models outperform a steady baseline with uncertainty; otherwise preserve two independent outcomes.

## 9. Implementation and reproducible work packages

1. Create D03a/rotor_manifest.yaml and D03b/bubble_manifest.yaml as distinct contracts.
2. Implement blade_element.py, coupled_descent.py and stability_jacobian.py.
3. Build bubble_spectrum.py with Parseval/window fixtures.
4. Implement weighted_pod.py and segmented_stationarity.ipynb.
5. Create transfer_review.json with dimensionless comparisons and covariance mapping.
6. Publish separate descent_candidates.parquet and bubble_modes.parquet; assemble only approved envelopes.

### Investigation sequence

1. D03a: establish proposed payload mass, survivable descent-speed requirement, deployment reliability, and atmospheric uncertainty.
2. D03a: solve autorotation equilibria, assess local stability, and identify infeasible mass/area combinations before prototype selection.
3. D03b: collect or obtain time series long enough to resolve candidate low-frequency modes across angle and Reynolds number.
4. D03b: compare spectral and modal statistics, then quantify their incremental impact on probe-force uncertainty without equating stationary and rotating flow.

### Resources and interfaces to expertise

- Rotor aerodynamics expertise, low-Reynolds flow facility, atmospheric model, time-series analysis, and appropriately supervised prototype testing.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| Torque sign error | False self-sustaining rotor. | Zero/load and Jacobian fixtures. | Declared positive directions. |
| Drift called low-frequency mode | Unsupported bubble mechanism. | Segmentation/detrending instability. | Longer valid records and stationarity flags. |
| Unreviewed cross-package transfer | False descent robustness. | Missing similarity review ID. | Separate outputs and gated envelope adapter. |

- A Earth demonstration can be physically unlike Mars even at similar Reynolds number.
- The combined source line is ambiguous; explicitly retaining both packages prevents accidental project deletion.

## 11. Required engineering outputs

- D03a feasibility/stability map and descent simulator; D03b spectral/modal bubble atlas; a documented transferability assessment joining them.

### Scientific result figures to produce during execution

Left: descent speed/rotation stability and feasible payload region. Right: bubble time series, spectra, and flow modes. A clearly labeled transferability link shows which aerodynamic statistics enter the probe model.

### Both retained research work packages

```json
[
  {
    "id": "D03a",
    "name": "INGENUITY SEED DESCENT",
    "original_title": "Optimizing Autorotating Sensor Probe Design for Space Exploration",
    "model": "Coupled vertical translation and rotor torque with low-Reynolds blade aerodynamics.",
    "data": "Versioned synthetic atmosphere/descent ensembles and university concept documentation.",
    "validation": "Independent descent/spin histories, equilibrium stability, and dynamic-similarity assessment."
  },
  {
    "id": "D03b",
    "name": "LANGLEY BUBBLE OSCILLATORY",
    "original_title": "Low Frequency Unsteadiness in Laminar Separation Bubbles",
    "model": "Spectral, phase-averaged, and POD description of bubble/wake dynamics.",
    "data": "Pressure/velocity/bubble-length time series with sampling and run metadata.",
    "validation": "Spectral convergence, repeated runs, aliasing checks, and withheld operating points."
  }
]
```

## 12. Cited technical and scientific resources

- [Northern Arizona University SEED Mars Sensor project](https://www.ceias.nau.edu/capstone/projects/ME/2022/22F_P17MarsSensor/Project/index.html) — University-authored autorotating-probe concept and similarity objectives.
- [Experimental Studies of Low Frequency Velocity Disturbances Observed in Short Bubble Formed on Airfoil](https://www.jstage.jst.go.jp/article/jjsass/50/582/50_582_293/_article/-char/en) — Original low-frequency bubble measurements.
- [Bursting and reformation cycle of the laminar separation bubble over a NACA-0012 aerofoil](https://arxiv.org/abs/1807.08681) — Original computational mechanism hypothesis to test against experimental modes.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
