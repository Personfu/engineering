# I03 · SATURN CHANNEL ATLAS

**Original project:** Rocket Development Lab Team: Cooling Channel Geometry Analysis for a Regeneratively Cooled Rocket Engine

**Session I:** Aerospace Technology

**Document class:** engineering research design and analysis record · **Revision:** 3 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session I](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_I.md) · [← I02](../I02-apollo-aquatherm/README.md) · [I04 →](../I04-orion-sentinel-core/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 6 | 4 | 8 | 3 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Purpose and scientific objective

Develop a dimensionless design-space atlas for the trade between wall-temperature uniformity, pumping penalty, and uncertainty in cooling-channel behavior. Preserve regenerative-cooling channel research as a comparative thermal-integrity study. Use abstract heated passages and normalized geometric ratios rather than an engine build drawing. Separate correlation calibration on inert water-flow coupons from extrapolation to any reactive propellant or operating engine.

**Question:** Which normalized channel families remain thermally favorable after equal pumping-power comparison, manufacturing uncertainty, and flow maldistribution are included?

**Testable hypothesis:** A geometry selected for maximum nominal convection will not consistently minimize uncertain wall hot spots when pressure loss and branch-flow variability are constrained.

## 1. Design basis and analysis boundary

The channel atlas compares abstract nonreactive heated-passage families using dimensionless geometry and an external thermal-load envelope. It ranks temperature nonuniformity, pumping penalty and uncertainty under equal pumping power or separately labeled equal flow. No engine build drawing or reactive operating point is inferred. Coupon geometry is supplied or verified only for inert validation.

Begin with hydraulic/thermal networks, then conjugate wall-flow models and robust multiobjective search. Aspect, curvature and relative roughness are normalized parameters with a bounded domain. Correlations carry validity and convention metadata. The first experimental gate is an independently approved noncombusting water-flow coupon with known electrical heat, not an engine test. Rankings beyond that fluid/material/domain remain extrapolations.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| I03-R1 | Every comparison shall declare equal pump power, equal flow or another controlled budget. | A channel can appear cooler merely by consuming more pumping work. | Scenario budget and solver constraint audit. | Proposed fair-comparison contract. |
| I03-R2 | Darcy and Fanning friction-factor conventions shall be typed explicitly. | Their factor-four difference biases pressure loss. | Convention conversion and analytic fixture. | Proposed hydraulic interface. |
| I03-R3 | Conjugate heat and pressure calculations shall converge within 1%, a proposed target, in accepted synthetic cases. | Mesh/solver error can reorder Pareto solutions. | Mesh/time/quadrature refinement. | Proposed numerical target. |
| I03-R4 | Manufacturing/roughness and branch-flow uncertainty shall accompany every candidate ranking. | Nominal optima can reverse under small deviations. | Posterior/range ensemble and rank-reversal map. | Proposed robust-design requirement. |
| I03-R5 | CVaR temperature shall report confidence level and reference scale; 0.95 is a proposed comparison choice. | Tail-risk metric is not a safety threshold. | Tail integration and scaling fixtures. | Proposed multiobjective convention. |
| I03-R6 | Validation shall use known-power inert single-phase coupons before model promotion. | Reactive coolant/engine transfer is unsupported. | Material/fluid/domain gate and withheld coupon predictions. | Proposed noncombusting validation gate. |

## 3. Architecture and controlled interfaces

A dimensionless family registry defines aspect, curvature, roughness and branch topology without specifying an engine. A property/correlation service supplies fluid transport properties and Nu/friction validity domains. The hydraulic network solves branch flows under the chosen budget; the conjugate thermal model receives an independently supplied wall heat distribution.

Manufacturing perturbations and correlation discrepancy form an ensemble around each family. A Pareto engine accumulates expected and tail-temperature metrics with pumping work. The coupon adapter brings measured pressure, flow and distributed wall temperature with covariance. Calibration is restricted to those observations; an extrapolation ledger records which model features lack inert evidence or differ from a prospective application.

![I03 engineering architecture](figures/architecture.svg)

Fair hydraulic budgets and external heat loads feed an uncertainty-aware thermal/Pareto atlas, validated only within noncombusting coupon domains.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

$$
D_h=4A_c/P_w;\quad \mathrm{Nu}=hD_h/k_f
$$

$$
\Delta p=f_D(L/D_h)\rho u^2/2+\sum K\rho u^2/2
$$

$$
P_{\rm pump}=\Delta p\,\dot V/\eta_p
$$

$$
\min_{\boldsymbol\xi}\{\mathrm{E}[T^*_{\max}],\mathrm{CVaR}_{0.95}(T^*_{\max}),P^*_{\rm pump}\}
$$

### Variables, units and conventions

- Ac in m^2 is channel cross section; Pw and Dh in m are wetted perimeter and hydraulic diameter.
- Delta p in Pa; length L in m; Darcy friction factor fD and local loss K are dimensionless; density rho in kg m^-3.
- Volumetric flow Vdot in m^3 s^-1; pump efficiency etap dimensionless; pumping power in W.
- xi contains dimensionless aspect, curvature, and roughness ratios; starred temperature and pumping power use explicitly documented reference scales.
- CVaR0.95 is the mean of the hottest 5% of modeled cases; it is a proposed risk metric, not a measured safety limit.

### Assumptions and boundary conditions

- Compare either equal pumping power or equal mass flow and clearly label which is held constant.
- The initial atlas is single-phase and nonreactive. Correlation errors and manufacturing deviations are random variables with justified bounds.

### Derivation step 1

```text
D_h=4A_c/P_w
```

Hydraulic diameter is a geometric scale using cross-sectional area and wetted perimeter. Similar Dh does not guarantee identical local transfer in dissimilar shapes.

### Derivation step 2

$$
\Delta p=[f_D L/D_h+\sum K]\rho u^2/2
$$

Darcy distributed friction and local losses are both dimensionless coefficients multiplying dynamic pressure. Use the same velocity/reference section.

### Derivation step 3

$$
P_{pump}=\Delta p\dot V/\eta_p,\quad h=Nu\,k_f/D_h
$$

Hydraulic work and convection connect geometry to competing objectives; pump efficiency uncertainty affects equal-power comparison.

### Derivation step 4

$$
T^*=(T-T_{in})/\Delta T_{ref},\quad CVaR_{0.95}=E[T^*_{max}\mid T^*_{max}\ge VaR_{0.95}]
$$

For a continuous upper-tail distribution, this defines the hottest-tail mean. Discrete ensembles require quantile/tie handling and sampling uncertainty.

### Inference or simulation procedure

Sweep normalized channel families with a conjugate thermal model and a flow-network comparator. Compute pressure losses and local heat-transfer regimes consistently, distinguishing Darcy and Fanning friction-factor conventions. Calibrate uncertainty with inert coupon data where available. Use multiobjective optimization to identify a Pareto front, then quantify ranking reversal under uncertain roughness, contact resistance, and uneven branch flow. Add geometry only when it produces a testable information gain; the atlas emphasizes robust trends, not a supposedly optimal engine channel.

### Validity domain and fidelity limits

A straight-passage correlation may fail in developing, curved, or strongly heated flow. Surrogate validation does not establish compatibility with cryogenic/reactive fluids, combustion loading, or additive-manufactured material life.

## 5. Data specifications and provenance

![I03 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| family_parameters | float64[dimensionless] | 1 | Normalized aspect/curvature/roughness/topology. | Domain bounds and reference geometry documented. |
| budget_type_value | struct | W or kg s^-1 | Held-constant pump/flow comparison. | Do not mix budgets in one ranking. |
| transport_properties | measurement<struct> | kg m^-3, Pa s, W m^-1 K^-1 | Fluid properties in accepted temperature range. | Source and validity recorded. |
| correlation_record | struct | 1 | Nu/friction/loss formulas and regimes. | Darcy/Fanning and developing-flow status explicit. |
| heat_envelope | measurement<array> | W m^-2 | External or known electrical boundary load. | Spatial/temporal covariance; no combustion schedule. |
| pressure_flow | measurement<float64[2]> | Pa, m^3 s^-1 | Hydraulic observations/predictions. | Branch and sensor covariance retained. |
| temperature_field | distribution<array> | K | Wall/coolant thermal response. | Masked sensor locations remain missing. |
| pareto_record | table | 1, W or scaled | Expected/CVaR temperature and pump objectives. | Nondominated status includes uncertainty and scale version. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### NASA cooling analysis reference

[Product, archive or reference](https://ntrs.nasa.gov/api/citations/19810012596/downloads/19810012596.pdf)

**Fields:** Published heat-transfer definitions, correlations and validity ranges

**Access:** Open technical source; extract assumptions alongside equations.

**Role:** Independent analysis comparator.

### Proposed normalized inert-coupon library

[Product, archive or reference](https://www.nasa.gov/smallsat-institute/sst-soa/structures-materials-and-mechanisms/)

**Fields:** Aspect ratio, relative roughness, Re, Nu, pressure-loss coefficient, wall-temperature distribution, measurement uncertainty

**Access:** Synthetic cases first; any measured coupons require new supervised laboratory work.

**Role:** Model calibration and robustness evidence; no experimental result is claimed.

## 6. Uncertainty, sensitivity and identifiability

Roughness, aspect deviations, contact resistance and flow maldistribution can shift both pressure drop and heat transfer. Correlation errors are shared within a family/regime, not independent point noise. Sample manufacturing uncertainty separately from model discrepancy and evaluate whether two candidates' performance intervals overlap.

Equal-power comparison couples pump efficiency, hydraulic resistance and velocity, so changing geometry alters its own convection regime. Inspect Re/Nu support on every realization. Use coupon holdouts and sensitivity maps to identify where developing or curved flow requires higher fidelity. Report rank-reversal probability and Pareto uncertainty; a nominal optimum is not a robust engine design or validated material-life result.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Flow/thermal network | Fast broad design sweep. | Weak local hotspot/curvature physics. | Use first domain atlas and sensitivity. |
| Conjugate passage model | Resolves local wall and fluid behavior. | Geometry/mesh and turbulence-model dependence. | Use for candidates with independent coupon evidence. |
| Robust Pareto optimization | Exposes pump/thermal/risk tradeoffs. | Tail sampling cost and prior sensitivity. | Use when rank uncertainty is quantified rather than selecting one nominal winner. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| I03-V1 | No heat input | Wall/fluid temperatures remain at common inlet/ambient equilibrium. | Zero-load thermal fixture. | Energy equilibrium. |
| I03-V2 | Pressure-work identity | Pump work equals pressure drop times volume rate divided by efficiency. | Unit-aware hydraulic fixture. | Hydraulic power relation. |
| I03-V3 | Friction convention | Equivalent Darcy/Fanning inputs yield identical pressure drop after factor-four conversion. | Typed coefficient fixture. | Friction-factor convention. |
| I03-V4 | Withheld inert family | Pressure and hotspot predictions are checked before calibration on that coupon. | Known-power noncombusting coupon holdout. | Proposed transport/thermal validation. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Check mesh refinement and conservation; compare circular/fully developed limits with appropriate analytic or reference results.
- Hold out an entire geometry family and report prediction error without refitting.
- Re-rank designs at equal pumping power and evaluate whether nominal improvements exceed combined measurement and modeling uncertainty.

## 9. Implementation and reproducible work packages

1. Create normalized family and controlled-budget manifests.
2. Implement typed friction/Nu and property regime service.
3. Build coupled hydraulic/conservative thermal solvers.
4. Generate manufacturing/maldistribution/discrepancy ensembles.
5. Compute uncertain Pareto fronts and tail metric convergence.
6. Release inert coupon holdouts, rank reversals and extrapolation ledger.

### Investigation sequence

1. Declare comparison constraints and normalized scales; define the tested fluid and material property domain.
2. Verify flow and conduction solvers separately before coupling them.
3. Use a sparse coupon matrix to discriminate correlation error from geometry effects.
4. Freeze the validation matrix, optimize on training cases, and release uncertainty-aware Pareto tables.

### Resources and interfaces to expertise

- Conjugate thermal/flow solver, uncertainty sampler, unit-aware design table, inert flow-loop access, and thermal/manufacturing expertise.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| Unequal budget hidden | Misleading thermal ranking. | Pump/flow constraint audit. | Publish separate budget-specific fronts. |
| Correlation outside regime | Unreliable pressure/Nu prediction. | Realization-level validity flag. | Reject or add validated higher fidelity. |
| Tail sample too small | Unstable CVaR winner. | Bootstrap tail metric and rank changes. | Increase ensemble or report unresolved ordering. |

- Extrapolation and inconsistent pumping constraints can create false improvement. Mesh-induced hot spots and uncertain roughness may dominate small shape changes.

## 11. Required engineering outputs

- Dimensionless channel atlas, regime-validity map, robust Pareto frontier, geometry-family comparison report, and coupon test specification.

### Scientific result figures to produce during execution

A wall-temperature versus normalized pumping-power frontier, colored by channel family, with uncertainty ellipses and a separate correlation-validity map.

## 12. Cited technical and scientific resources

- [NASA cooling technical reference, NTRS 19810012596](https://ntrs.nasa.gov/api/citations/19810012596/downloads/19810012596.pdf) — Cooling-analysis precedent and comparison assumptions.
- [NASA Small Spacecraft Structures, Materials and Mechanisms](https://www.nasa.gov/smallsat-institute/sst-soa/structures-materials-and-mechanisms/) — Material, fabrication, and verification considerations used as systems-method analogies.
- [Published cooling/transport analysis reference](https://ntrs.nasa.gov/citations/19810012596) — Thermal/transport comparison context; selected correlations require independent domain review for inert passages.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
