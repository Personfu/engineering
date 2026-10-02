# I08 · VOYAGER FRAMEFORGE

**Original project:** Julia 1.2 Ephemeris and Gravitational Modeling Development

**Session I:** Aerospace Technology

**Document class:** engineering research design and analysis record · **Revision:** 4 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session I](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_I.md) · [← I07](../I07-gateway-catsat-console/README.md) · [I09 →](../I09-osiris-regolith-leaper/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 6 | 4 | 8 | 2 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Mission profile

![I08 engineering mission profile: scientific question, hypothesis, model scope and evidence status](figures/mission-profile.svg)

| Profile panel | Engineering signal | Open the evidence |
| --- | --- | --- |
| Mission identity | Julia 1.2 Ephemeris and Gravitational Modeling Development | [Scientific objective](#purpose-and-scientific-objective) |
| Model cockpit | 4 governing expressions; 4 derivation steps; declared assumptions and validity envelope | [Mathematical formulation](#4-mathematical-model-and-derivation) |
| Data blueprint | 8 proposed fields with types, units and quality rules | [Field map & downloads](data/README.md) |
| Verification queue | 6 proposed requirements; 4 specified cases; project execution evidence pending | [Case definitions](#8-verification-and-validation-cases) |
| Figure wall | Architecture, field map, planned result description; included shared illustration | [Open full gallery](figures/README.md) |
| Resource library | 2 cited primary resources with support statements | [Cited resources](#12-cited-technical-and-scientific-resources) |

### Model cockpit

**Analysis method:** Implement a thin Julia interface over documented SPICE/Horizons conventions and maintain a cached, checksum-tagged reference manifest. Create round-trip transformations and compare state vectors only after matching center, reference frame, aberration correction, and epoch. Add point-mass and spherical-harmonic evaluators with unit tests at analytic limits; a later uniform-density polyhedral evaluator must verify closed mesh orientation and mass consistency. Compare acceleration with numerical potential gradients and external-field Laplace residuals. Benchmark runtime only after correctness, separating kernel loading, interpolation, compilation, and repeated evaluation. Archive Julia 1.2 behavior in compatibility notes instead of making it a requirement for all future work.

**Operating envelope:** Independent outputs may share underlying JPL ephemerides, so agreement is an implementation check rather than independent astronomical validation. Harmonic truncation, uncertain small-body density, and shape resolution limit physical accuracy.

**Variables and conventions**

- Position r and reference radius R in m; time in s with explicit TDB/UTC/other labels; gravitational parameter muk in m^3 s^-2.
- Potential V in m^2 s^-2 uses the positive mu/r convention; acceleration a in m s^-2 is its gradient.
- phi/varphi and lambda in rad; harmonic coefficients and consistently normalized Legendre functions are dimensionless.
- L is harmonic truncation degree; each state carries center, frame, epoch, units, kernel/source version, and interpolation setting.

### Artifact wall

![I08 included scientific diagnostic](../../../data/figures/14_orbit_conservation_and_refinement.svg)

Synthetic two-body conservation and refinement diagnostics from immutable model outputs. Panel A scales relative specific-energy error to parts per million and reports angular-momentum conservation for the stored 400-step-per-period run. Panel B compares three recorded maximum-energy errors with a second-order reference anchored to the coarsest run. This is an integration check, not trajectory prediction validation.

[Exact inputs, transformations and output hashes](../../../data/figures/14_orbit_conservation_and_refinement.provenance.json)

**Scientific result to produce:** A provenance diagram beside state-residual plots and a radial gravity-model disagreement map, with convergence boundaries and reference conventions labeled.

### Investigation feed · planned work

The feed records proposed work packages. A row becomes executed evidence only with versioned inputs, outputs and a reviewed result.

| Sequence | Evidence state | Engineering work package |
| --- | --- | --- |
| 01 | Planned | Create source/checksum and fully typed state/context contracts. |
| 02 | Planned | Implement matched SPICE/Horizons adapters and cached validity checks. |
| 03 | Planned | Build position-velocity frame/time round-trip fixtures. |
| 04 | Planned | Implement point-mass and normalized-harmonic potential/gradient APIs. |
| 05 | Planned | Gate closed-shape evaluator on topology/mass and domain validation. |
| 06 | Planned | Release archival Julia notes, matched-reference residuals and separated runtime benchmarks. |

### Mission connections

Connections are reading routes based on actual shared resources, supplied sessions or included illustrations. They do not establish physical dependencies, team collaborations or validated results.

| Connected mission | Original investigation | Recorded connection basis |
| --- | --- | --- |
| [I12 · PIONEER PHOBOS PATHFINDER](../I12-pioneer-phobos-pathfinder/README.md) | Heuristic Optimization Applied to Orbital Transfers Between Low-Planetary Orbits and Distant Retrograde Orbits | Session I; Included illustration: 07_two_body_convergence; [NASA/JPL NAIF SPICE Tutorials](https://naif.jpl.nasa.gov/naif/tutorials.html); [JPL Horizons System Manual](https://ssd.jpl.nasa.gov/horizons/manual.html) |
| [I09 · OSIRIS REGOLITH LEAPER](../I09-osiris-regolith-leaper/README.md) | Simulation and Evaluation of a Mechanical Hopping Mechanism for Robotic Small Body Surface Exploration | Session I; [NASA/JPL NAIF SPICE Tutorials](https://naif.jpl.nasa.gov/naif/tutorials.html) |
| [I13 · OSIRIS APOPHIS HORIZON](../I13-osiris-apophis-horizon/README.md) | A Study of the Deflection of 99942 Apophis from Earth | Session I; [JPL Horizons System Manual](https://ssd.jpl.nasa.gov/horizons/manual.html) |
| [I07 · GATEWAY CATSAT CONSOLE](../I07-gateway-catsat-console/README.md) | CatSat Groundstation Command and Control | Session I |
| [I06 · SATURN LOADPATH](../I06-saturn-loadpath/README.md) | Designing and Exploring the Structure of Launch Vehicles to Create Optimal Theoretical and Small-Scale Experimental Models | Session I |
| [I10 · GEMINI POINTLOCK](../I10-gemini-pointlock/README.md) | Spacecraft Attitude Control Implementation and Development | Session I |

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

Turn the historical Julia 1.2 ephemeris idea into a reference-quality, unit-aware celestial mechanics library. Preserve Julia 1.2 as an archival compatibility target while choosing a maintained execution environment through a documented support review. The core product is a provenance chain from NASA ephemerides and kernel metadata to state vectors, frame transformations, and gravity calculations, with explicit domain limits for point-mass, spherical-harmonic, and irregular-body models.

**Question:** Can independent ephemeris sources and gravity representations agree within a declared numerical tolerance after frame, center, time scale, units, and model fidelity are aligned?

**Testable hypothesis:** Most large apparent orbit discrepancies in an initial implementation will arise from conventions and metadata rather than floating-point precision; disciplined frame/time checks will expose them.

## 1. Design basis and analysis boundary

The celestial-mechanics library delivers unit-aware state vectors and gravity calculations with explicit source/frame/time provenance. Julia 1.2 is an archival compatibility target, while the execution version and dependency support are chosen and pinned after a separate compatibility review. SPICE/Horizons provide authoritative conventions; agreement between their outputs can share ephemerides and is therefore an implementation check rather than independent astronomical validation.

Begin with geometric state retrieval and point-mass gravity, then harmonics outside their convergence domain, then closed-shape gravity only with independently supplied density/shape. Kernel geometry does not define mass distribution. Each fidelity level declares validity intervals, interpolation and aberration options. Covariance is carried only when sourced; a state-vector response alone never creates measured orbital uncertainty.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| I08-R1 | Every state shall include epoch scale, center, frame, units, aberration option and source checksum/query. | Numerically similar arrays can represent different physical states. | Metadata/round-trip and matched-query audit. | NAIF and Horizons conventions. |
| I08-R2 | Point-mass acceleration and potential-gradient checks shall agree to 10^-6 relative error where conditioned, a proposed target. | Sign/unit errors invalidate all propagations. | Analytic and finite-difference convergence. | Proposed numerical target. |
| I08-R3 | Harmonic coefficients and Legendre functions shall have matching normalization and reference radius. | Normalization mismatch changes gravity magnitude. | Monopole/selected-harmonic fixtures. | Proposed gravity contract. |
| I08-R4 | Harmonic evaluation shall reject points outside its declared convergence validity. | Near irregular bodies the expansion can fail. | Domain-boundary fixtures and validity manifest. | Existing convergence caveat. |
| I08-R5 | Shape-based gravity shall require closed oriented mesh, positive volume and density/mass consistency. | A geometry kernel alone does not supply physical gravity. | Mesh topology and volume/mass checks. | Proposed higher-fidelity gate. |
| I08-R6 | Runtime results shall separate compilation/kernel loading from repeated evaluation. | Warm-cache speed is not first-use latency. | Pinned-version timing categories. | Proposed reproducible benchmark. |

## 3. Architecture and controlled interfaces

A reference adapter stores complete Horizons requests or SPICE kernels with checksums and valid times. The state type carries center/frame/time/units and geometric versus apparent status. Transformation services preserve velocities and time-dependent frame terms. A cache cannot return a state outside the source validity or with mismatched correction metadata.

Gravity evaluators expose a common potential/acceleration interface but distinct point-mass, harmonic and closed-shape domains. Harmonic coefficients, spin frame and density are independent versioned inputs. A comparator matches conventions before computing residuals and numerical derivatives. Archival Julia compatibility fixtures and current execution manifests are separate artifacts so historical API behavior does not silently constrain new calculations.

![I08 engineering architecture](figures/architecture.svg)

State provenance and gravity inputs remain independent; model-domain checks precede correctness and performance comparisons.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

$$
\ddot{\boldsymbol r}=\sum_k-\mu_k(\boldsymbol r-\boldsymbol r_k)/|\boldsymbol r-\boldsymbol r_k|^3
$$

$$
V=\mu/r\{1+\sum_{\ell=2}^{L}(R/r)^\ell\sum_{m=0}^{\ell}\bar P_{\ell m}(\sin\varphi)[\bar C_{\ell m}\cos m\lambda+\bar S_{\ell m}\sin m\lambda]\}
$$

$$
\boldsymbol a=\nabla V;\quad \delta\boldsymbol x=\boldsymbol x_{\rm test}-\boldsymbol x_{\rm reference}
$$

$$
\nabla^2V=0\quad\text{outside the modeled mass}
$$

### Variables, units and conventions

- Position r and reference radius R in m; time in s with explicit TDB/UTC/other labels; gravitational parameter muk in m^3 s^-2.
- Potential V in m^2 s^-2 uses the positive mu/r convention; acceleration a in m s^-2 is its gradient.
- phi/varphi and lambda in rad; harmonic coefficients and consistently normalized Legendre functions are dimensionless.
- L is harmonic truncation degree; each state carries center, frame, epoch, units, kernel/source version, and interpolation setting.

### Assumptions and boundary conditions

- A spherical-harmonic expansion is used only outside its convergence boundary; close to an irregular body, use an independently validated closed-shape gravity model.
- Shape, rotation state, density, and gravity coefficients are independent inputs; SPICE geometry alone does not determine a mass distribution.

### Derivation step 1

$$
V=\mu/r,\quad\nabla V=-\mu\mathbf r/r^3
$$

The positive-potential convention produces inward acceleration. mu has m^3 s^-2 and V has m^2 s^-2.

### Derivation step 2

$$
\mathbf a=\sum_k-\mu_k(\mathbf r-\mathbf r_k)/|\mathbf r-\mathbf r_k|^3
$$

This inertial point-mass equation needs consistent ephemeris centers and geometry; a noninertial origin additionally needs the appropriate indirect/frame acceleration.

### Derivation step 3

$$
V_L=\frac{\mu}{r}\left[1+\sum_{\ell=2}^L(R/r)^\ell\sum_m\bar P_{\ell m}(\sin\varphi)(\bar C_{\ell m}\cos m\lambda+\bar S_{\ell m}\sin m\lambda)\right]
$$

Dimensionless normalized harmonics modify the potential outside the model's supported exterior domain; evaluate derivatives with consistent body-fixed coordinates.

### Derivation step 4

$$
\nabla^2V=0\ \text{outside mass},\quad M=\rho V_{mesh}
$$

Exterior Laplace residual and mesh mass consistency provide independent checks. Density uncertainty remains physical-model uncertainty even when geometric transforms agree.

### Inference or simulation procedure

Implement a thin Julia interface over documented SPICE/Horizons conventions and maintain a cached, checksum-tagged reference manifest. Create round-trip transformations and compare state vectors only after matching center, reference frame, aberration correction, and epoch. Add point-mass and spherical-harmonic evaluators with unit tests at analytic limits; a later uniform-density polyhedral evaluator must verify closed mesh orientation and mass consistency. Compare acceleration with numerical potential gradients and external-field Laplace residuals. Benchmark runtime only after correctness, separating kernel loading, interpolation, compilation, and repeated evaluation. Archive Julia 1.2 behavior in compatibility notes instead of making it a requirement for all future work.

### Validity domain and fidelity limits

Independent outputs may share underlying JPL ephemerides, so agreement is an implementation check rather than independent astronomical validation. Harmonic truncation, uncertain small-body density, and shape resolution limit physical accuracy.

## 5. Data specifications and provenance

![I08 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| state_vector | float64[6] | m, m s^-1 | Position and velocity relative to named center. | No implicit frame/time defaults. |
| epoch_context | struct | s or JD | Time value, scale and conversion pedigree. | Leap/time kernels and source scale required. |
| source_manifest | struct | 1 | Kernel hashes or complete query/output. | Validity intervals and retrieval date. |
| frame_correction | struct | 1 | Reference frame and aberration mode. | Apparent and geometric states distinct. |
| gravity_parameters | struct | m^3 s^-2, m, 1 | mu, radius and coefficient normalization. | Mass/shape/spin provenance independent. |
| mesh_density | measurement<struct>&#124;null | m, kg m^-3 | Closed shape and physical density. | Oriented closed topology and uncertainty. |
| potential_acceleration | float64[4] | m^2 s^-2, m s^-2 | Model output with sign convention. | Singular/out-of-domain locations flagged. |
| state_covariance | float64[6,6]&#124;null | mixed state^2 | Source-supported uncertainty only. | Null if unavailable; synthetic ensembles labeled illustrative. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### NASA/JPL NAIF SPICE tutorials and kernels

[Product, archive or reference](https://naif.jpl.nasa.gov/naif/tutorials.html)

**Fields:** Kernel identifiers, frames, time conversions, geometry and state-vector metadata

**Access:** Public documentation; verify licenses, validity intervals and exact kernel checksums before ingestion.

**Role:** Authoritative convention and transformation reference.

### JPL Horizons reference queries

[Product, archive or reference](https://ssd.jpl.nasa.gov/horizons/manual.html)

**Fields:** State vectors, centers, reference frames, epochs, constants and query metadata

**Access:** Public service; save request/output and retrieval time. Covariance is not assumed to accompany every vector.

**Role:** Independent implementation cross-check with matched conventions.

## 6. Uncertainty, sensitivity and identifiability

Ephemeris interpolation, epoch conversion, frame rotation and aberration settings create implementation residuals. Physical uncertainty includes mu, gravity coefficients, shape resolution and density. Separate these contributions by comparing matched source geometry first, then varying gravity inputs. Common underlying JPL ephemerides mean cross-service agreement cannot reduce actual orbital uncertainty by averaging outputs.

Near-body harmonics can become poorly conditioned or invalid; finite-difference gradients need step-size convergence away from singular surfaces. Inspect coefficient truncation and shape-resolution sensitivity and compare model families only in shared domains. Unavailable covariance stays null. Runtime comparisons record warm/cold paths, version and machine, preventing numerical speed claims from hiding a lower-fidelity approximation.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Point-mass evaluator | Fast analytic limits. | Misses extended-body structure. | Use far-field baseline and unit/sign fixture. |
| Spherical harmonics | Efficient resolved exterior gravity. | Normalization/truncation/convergence limits. | Use inside verified coefficient exterior support. |
| Closed-shape model | Handles near irregular geometry. | Density/mesh and implementation complexity. | Enable after closed-mesh mass and exterior checks. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| I08-V1 | Monopole | Zero higher coefficients reproduces mu/r and inward inverse-square acceleration. | Analytic harmonic/point-mass comparison. | Potential-gradient identity. |
| I08-V2 | Frame round trip | Forward/inverse position-velocity transformation reproduces original state within numerical target. | Time-dependent transform fixture. | Declared frame interface. |
| I08-V3 | Matched Horizons/SPICE geometry | Residuals are computed only with identical center/epoch/correction conventions. | Frozen query/kernel comparison. | Primary convention documentation. |
| I08-V4 | Exterior Laplace/mesh check | Potential Laplacian approaches zero outside mass; mesh mass matches density times volume. | Derivative refinement and topology fixture. | Newtonian exterior field and mass accounting. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Require round-trip frame transformations to remain within a declared floating-point tolerance and test known leap-second boundaries explicitly.
- Compare selected Horizons/SPICE epochs and document every mismatch in convention or model source.
- Verify two-body energy/angular-momentum behavior, harmonic degree convergence, and exterior potential-gradient consistency.

## 9. Implementation and reproducible work packages

1. Create source/checksum and fully typed state/context contracts.
2. Implement matched SPICE/Horizons adapters and cached validity checks.
3. Build position-velocity frame/time round-trip fixtures.
4. Implement point-mass and normalized-harmonic potential/gradient APIs.
5. Gate closed-shape evaluator on topology/mass and domain validation.
6. Release archival Julia notes, matched-reference residuals and separated runtime benchmarks.

### Investigation sequence

1. Freeze the state-object schema, SI boundary rules, kernel manifest, and supported time/frame combinations.
2. Validate vector readers and time conversion before integrating an orbit.
3. Add gravity models in increasing complexity with separate convergence and domain tests.
4. Publish compatibility and runtime benchmarks with the executable environment lockfile.

### Resources and interfaces to expertise

- Julia numerical environment, NAIF kernels, saved Horizons outputs, analytic benchmark fixtures, and astrodynamics review.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| UTC/TDB or km/m mismatch | Wrong geometry/gravity. | Typed metadata/unit audit. | Reject incomplete state contract. |
| Harmonics inside unsupported domain | Unphysical acceleration. | Domain flag/truncation sensitivity. | Use validated shape model or reject. |
| Shape mistaken for mass | Unsupported physical precision. | No density/mu source. | Require independent mass inputs and covariance. |

- UTC/TDB confusion, kilometers/meters mixing, frame-center mismatch, and harmonics evaluated inside their convergence boundary can overwhelm nominal precision.

## 11. Required engineering outputs

- Unit-aware state library, kernel/query manifest, analytic gravity fixtures, compatibility report, performance benchmark, and reproducible error atlas.

### Scientific result figures to produce during execution

A provenance diagram beside state-residual plots and a radial gravity-model disagreement map, with convergence boundaries and reference conventions labeled.

### Included shared numerical starting point

![I08 shared reduced-model or catalog demonstration](../../../models/figures/07_two_body_convergence.svg)

[Executable formulation, parameters, tabular outputs, provenance and verification](../../../models/README.md). This shared demonstration has a narrower domain than the project model above. Its own caption and methods identify synthetic parameters or the separately retrieved public catalog; it is not a completed result of the original project.

### Data diagnostic

![I08 data diagnostic](../../../data/figures/14_orbit_conservation_and_refinement.svg)

Synthetic two-body conservation and refinement diagnostics from immutable model outputs. Panel A scales relative specific-energy error to parts per million and reports angular-momentum conservation for the stored 400-step-per-period run. Panel B compares three recorded maximum-energy errors with a second-order reference anchored to the coarsest run. This is an integration check, not trajectory prediction validation.

[Inputs, downloadable figure and provenance](../../../data/figures/README.md)

## 12. Cited technical and scientific resources

- [NASA/JPL NAIF SPICE Tutorials](https://naif.jpl.nasa.gov/naif/tutorials.html) — Frames, kernels, time, and geometric-state conventions.
- [JPL Horizons System Manual](https://ssd.jpl.nasa.gov/horizons/manual.html) — Ephemeris query options, coordinates, times, and limitations.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
