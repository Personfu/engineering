# I10 · GEMINI POINTLOCK

**Original project:** Spacecraft Attitude Control Implementation and Development

**Session I:** Aerospace Technology

**Document class:** engineering research design and analysis record · **Revision:** 3 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session I](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_I.md) · [← I09](../I09-osiris-regolith-leaper/README.md) · [I11 →](../I11-hubble-skyvault/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 6 | 4 | 8 | 2 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Purpose and scientific objective

Build on the original one-axis reaction-wheel/turntable experiment with an auditable estimation-and-control loop. Retain the symposium pointing target of plus or minus 0.5 degrees as a proposed bench acceptance criterion, then determine whether it survives encoder calibration, friction, disturbances, wheel saturation, and resets. A subsequent three-axis model is a separate extension with independently verified quaternion conventions and momentum-management assumptions.

**Question:** Can the one-axis platform meet the declared pointing criterion across the full angular range while preserving stability and a bounded wheel-momentum state?

**Testable hypothesis:** A controller that incorporates identified friction, sensor bias, and wheel limits will outperform a nominal proportional-derivative controller during large-angle maneuvers and repeated disturbance recovery.

## 1. Design basis and analysis boundary

The attitude-control annex implements the original one-axis reaction-wheel/turntable plant with estimation, limits and energy metrology. The plus/minus 0.5-degree goal is a proposed bench acceptance criterion, not a flight requirement. Cumulative electrical energy consumed is the integral of measured input draw including losses; it is distinct from stored wheel kinetic energy. Actual inertia, encoder, wheel and actuator bounds remain TBD.

Begin with sign/wrap analytic fixtures, then identified friction/lag and gyro/encoder estimation, then limit-aware control and deterministic resets. A three-axis quaternion extension is a separate model requiring independent convention and momentum-management validation. Bench friction, gravity and readout limits prevent a one-axis result from establishing flight pointing or environmental qualification.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| I10-R1 | Pointing error shall use wrapped angular difference and meet plus/minus 0.5 degrees in the declared settled bench domain, a proposed target. | Raw subtraction fails across angle wrap. | Full-range reference/encoder calibration and held-out maneuvers. | Original goal retained as proposed criterion. |
| I10-R2 | Wheel/body torque signs shall be verified before controller tuning. | Internal torque acts oppositely on body. | Known positive-torque synthetic/low-energy characterization. | Proposed plant-sign contract. |
| I10-R3 | Wheel momentum/torque limits shall be measured and never exceeded in accepted commands. | Pointing can be infeasible under saturation. | Actuator/speed calibration and dropout/saturation replay. | Proposed constraint requirement. |
| I10-R4 | Electrical input energy and wheel mechanical energy shall have separate ledgers. | Losses and body work prevent equality. | Voltage/current versus inertia/speed integration fixtures. | Corrected energy distinction. |
| I10-R5 | Sensor bias, friction and lag uncertainty shall propagate into settling/error claims. | An apparently small angle error can be calibration bias. | Independent sensor/plant holdouts. | Proposed metrology requirement. |
| I10-R6 | Reset/sensor-dropout behavior shall reach a declared observable state without undefined commands. | Estimator/controller history affects recovery. | Deterministic simulator reset and missing-sensor traces. | Proposed bounded-service requirement. |

## 3. Architecture and controlled interfaces

The bench manifest stores verified body/wheel inertia, encoder/gyro calibration and actuator lag/bounds. A wrapped-angle estimator fuses angle and rate with bias covariance. The controller emits bounded wheel torque; the plant maps its opposite torque to body acceleration and tracks wheel momentum. Friction and external disturbances are separate inputs.

Power metrology emits voltage/current and clock-synchronized input draw. An electrical accountant integrates consumption and separately records any returned energy; a mechanical accountant derives wheel kinetic state. Recovery logic resets or freezes estimator/control states with observable quality flags. The benchmark runner records angle/rate, torque, wheel limits, settling and energy under identical maneuver/disturbance scenarios for all control variants.

![I10 engineering architecture](figures/architecture.svg)

Opposite wheel/body torque and momentum limits close the control loop; electrical consumption and wheel kinetic energy remain separate measured/model interfaces.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

$$
e=\operatorname{atan2}[\sin(\theta-\theta_{\rm ref}),\cos(\theta-\theta_{\rm ref})]
$$

$$
I_b\ddot\theta=-u+\tau_d-b\dot\theta;\quad \dot h_w=u
$$

$$
u=\operatorname{sat}(K_pe+K_d\dot\theta)
$$

$$
\dot E_{\rm elec}=P_{\rm elec};\quad |h_w|\le h_{\max}
$$

### Variables, units and conventions

- Angle theta and wrapped error e in rad; reported pointing error also in degrees with explicit conversion.
- Body inertia Ib in kg m^2; wheel torque u and external disturbance taud in N m; wheel momentum hw in N m s.
- Viscous friction b in N m s rad^-1; Kp in N m rad^-1 and Kd in N m s rad^-1; saturation is the measured actuator bound.
- E_elec is cumulative electrical energy consumed [J], the integral of measured electrical input power P_elec [W] including losses. It is not stored wheel kinetic energy. Settling time in s and angular rate in rad s^-1.

### Assumptions and boundary conditions

- Wheel torque acts oppositely on the body; signs are verified experimentally and in a known synthetic case.
- A turntable includes friction and external torque. It approximates one axis and does not establish a frictionless or three-axis space environment.

### Derivation step 1

$$
e=\operatorname{atan2}[\sin(\theta-\theta_{ref}),\cos(\theta-\theta_{ref})]
$$

Wrapped error lies on the declared branch [-pi,pi]; commands at the discontinuity need a stated tie/trajectory convention.

### Derivation step 2

$$
I_b\ddot\theta=-u+\tau_d-b\dot\theta,\quad\dot h_w=u
$$

Positive u increases wheel momentum and applies negative body torque. In the no-external-torque/no-friction limit total angular momentum is conserved.

### Derivation step 3

$$
u=\operatorname{sat}(K_pe+K_d\dot\theta)
$$

With these plant/error signs, positive proportional/damping gains oppose body error/rate locally. Saturation and lag require separate stability/feasibility checks.

### Derivation step 4

$$
E_{elec,draw}=\int\max[V(t)I(t),0]dt,\quad E_{wheel}=h_w^2/(2I_w)
$$

Electrical draw includes motor/driver losses and is not wheel energy. If regeneration occurs, integrate negative electrical flow in a separate returned-energy ledger.

### Inference or simulation procedure

Identify inertia, friction, encoder bias, and actuator lag using low-energy bench characterization. Fuse gyro and angle measurements with an estimator that propagates bias uncertainty. Compare nominal PD control with a limit-aware controller under identical synthetic and bench maneuvers; include deadband, angular wrap, wheel saturation, and actuator quantization. Specify when momentum exhaustion makes the commanded pointing state infeasible. Run deterministic reset and sensor-dropout replays in the simulator. If extending to three axes, use a unit-norm quaternion state, verify body/inertial convention round trips, and separate wheel momentum management from pointing control. The existing one-axis data cannot substantiate the upgraded model.

### Validity domain and fidelity limits

A good turntable result does not establish vacuum compatibility, radiation tolerance, on-orbit disturbance rejection, or flight attitude determination. Constant friction approximation may fail around zero rate.

## 5. Data specifications and provenance

![I10 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| source_time | float64 | s | Synchronized sensor/control/power time. | Clock/reset generation and gaps retained. |
| reference_angle | float64 | radian | Commanded one-axis orientation. | Wrap/trajectory policy version. |
| angle_rate | measurement<float64[2]> | radian, radian s^-1 | Calibrated body angle and rate. | Bias covariance and missing-sensor state. |
| plant_parameters | posterior<struct> | kg m^2, N m s rad^-1, s | Inertia, friction and lag. | Identification conditions and near-zero-rate discrepancy. |
| wheel_state | measurement<struct> | N m s, radian s^-1 | Wheel momentum/speed and limits. | Sign/inertia convention and saturation flag. |
| torque_command | float64 | N m | Requested/applied wheel torque. | Both values retained when saturated. |
| electrical_ledger | measurement<struct> | W, J | Input draw, cumulative consumed/returned energy. | Current sign and power calibration; no mechanical-energy substitution. |
| mechanical_energy | measurement<float64> | J | Wheel kinetic energy from state. | Separate field/inertia covariance. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### NASA small-spacecraft GNC reference

[Product, archive or reference](https://www.nasa.gov/smallsat-institute/sst-soa/guidance-navigation-and-control/)

**Fields:** Attitude sensing, control architecture and actuator considerations

**Access:** Public survey; exact sensor and wheel specifications require board-level verification.

**Role:** Architecture and failure-mode context.

### Proposed turntable characterization dataset

[Product, archive or reference](https://www.nasa.gov/reference/systems-engineering-handbook/)

**Fields:** Time, reference angle, calibrated angle/rate, wheel speed, current, torque estimate, temperature, state and reset marker

**Access:** No bench observations supplied; release synthetic fixtures first and retain calibration files with later measurements.

**Role:** Plant identification and withheld maneuver evaluation.

## 6. Uncertainty, sensitivity and identifiability

Encoder zero/nonlinearity, gyro bias and timing affect angle/rate estimates; friction and actuator lag affect inferred controller margins. Identify them with low-energy independent maneuvers and retain covariance. Static friction near zero rate may invalidate viscous b, so test direction/reversal sensitivity rather than fitting one coefficient to all motion.

Wheel momentum exhaustion couples feasibility to disturbance duration, even when transient pointing is good. Simulate torque quantization, deadband, reset and sensor gaps across identified parameter ranges. Electrical energy uncertainty comes from voltage/current calibration and sampling, while mechanical energy depends on wheel inertia/speed. Keep these budgets separate and assess three-axis extensions only through new quaternion and momentum-management verification.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Nominal PD | Transparent local stability and simple implementation. | Saturation/friction/lag limitations. | Use required baseline under identified plant. |
| Limit-aware controller | Can manage torque/momentum feasibility. | More model dependence and state logic. | Adopt when held-out saturation cases improve without lost stability. |
| Three-axis extension | Explores full attitude architecture. | One-axis data cannot validate it. | Treat as separate simulation with new convention/actuator evidence. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| I10-V1 | Angular wrap | Targets around plus/minus pi yield the short signed error. | Exact trigonometric fixture. | Wrapped-angle identity. |
| I10-V2 | Torque sign/conservation | Positive u accelerates body negatively; body-plus-wheel momentum stays constant without external torque/friction. | No-disturbance synthetic plant. | Internal angular-momentum exchange. |
| I10-V3 | Electrical/mechanical separation | Driver loss can increase cumulative draw without the same wheel-energy increase. | Synthetic power/loss and speed ledger. | Energy accounting distinction. |
| I10-V4 | Withheld maneuver/reset | Pointing/settling and bounded momentum are assessed with frozen plant/controller. | Independent angle/disturbance plus dropout/reset cases. | Proposed bench-domain acceptance. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Verify angular wrapping across zero/360 degrees and compare torque/momentum conservation in a zero-friction simulator.
- Assess the proposed plus/minus 0.5-degree criterion using calibrated maximum steady-state error across a declared angular grid, with confidence intervals.
- Report overshoot, settling, RMS jitter, power, saturation duration, and recovery behavior; a single favorable maneuver is insufficient.

## 9. Implementation and reproducible work packages

1. Verify/calibrate inertia, encoder/gyro, power and actuator limits.
2. Implement wrap/sign/conservation fixtures.
3. Identify friction/lag with independent low-energy maneuvers.
4. Build bias-aware estimator and nominal/limit-aware controllers.
5. Run deterministic saturation/dropout/reset benchmarks.
6. Publish proposed pointing acceptance, separate energy budgets and three-axis evidence gaps.

### Investigation sequence

1. Define pointing, settling, momentum, and power acceptance conditions before tuning gains.
2. Calibrate sensor/frame signs and identify plant parameters with independent uncertainty estimates.
3. Tune on a declared subset of angular commands and disturbance cases.
4. Freeze the controller and test unseen angles, reversals, saturation, and reset recovery; keep any three-axis extension separate.

### Resources and interfaces to expertise

- Inert one-axis bench, encoder/gyro calibration, reaction-wheel emulator or supervised mechanism, control simulation, and GNC mentor.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| Sign error | Unstable positive feedback. | Known-torque response mismatch. | Verify signs before gain tuning. |
| Momentum saturation hidden | Infeasible pointing or long error. | Limit state and applied/requested torque mismatch. | Limit-aware controller and infeasible-state report. |
| Electrical energy replaced by wheel energy | Wrong power budget. | Separate ledger mismatch. | Integrate measured electrical input including losses. |

- Encoder misalignment can mimic excellent pointing, and friction can hide unstable free-space behavior. Saturated wheels remove torque authority without a separate momentum-management mechanism.

## 11. Required engineering outputs

- Plant-identification report, estimator/control code specification, pointing acceptance matrix, saturation/recovery atlas, and staged three-axis extension plan.

### Scientific result figures to produce during execution

Angle command and calibrated response above wheel momentum, torque saturation, and uncertainty; polar error plots cover the full tested one-axis range.

### Included shared numerical starting point

![I10 shared reduced-model or catalog demonstration](../../../models/figures/06_one_axis_attitude.svg)

[Executable formulation, parameters, tabular outputs, provenance and verification](../../../models/README.md). This shared demonstration has a narrower domain than the project model above. Its own caption and methods identify synthetic parameters or the separately retrieved public catalog; it is not a completed result of the original project.

### Data diagnostic

![I10 data diagnostic](../../../data/figures/13_attitude_phase_and_authority.svg)

Synthetic one-axis PD attitude response and actuator authority. The phase portrait is colored by elapsed model time. Requested torque is reconstructed from the recorded states and sidecar gains; the applied torque is clipped to ±8 mN·m. The right panel focuses on the first 40 seconds, while the phase portrait uses the full 120-second record.

[Inputs, downloadable figure and provenance](../../../data/figures/README.md)

## 12. Cited technical and scientific resources

- [NASA Small Spacecraft Guidance, Navigation and Control](https://www.nasa.gov/smallsat-institute/sst-soa/guidance-navigation-and-control/) — Attitude sensor, actuator, and architecture context.
- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — Acceptance criteria and test traceability framework.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
