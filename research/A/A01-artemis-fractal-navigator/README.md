# A01 · ARTEMIS FRACTAL NAVIGATOR

**Original project:** New Methods for the Iteration and Visualization of Mandelbrot and Julia Sets

**Session A:** Math, Physics & Chemistry

**Document class:** engineering research design and analysis record · **Revision:** 4 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session A](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_A.md) · [A02 →](../A02-new-horizons-cryophase/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 4 | 3 | 7 | 2 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Mission profile

![A01 engineering mission profile: scientific question, hypothesis, model scope and evidence status](figures/mission-profile.svg)

| Profile panel | Engineering signal | Open the evidence |
| --- | --- | --- |
| Mission identity | New Methods for the Iteration and Visualization of Mandelbrot and Julia Sets | [Scientific objective](#purpose-and-scientific-objective) |
| Model cockpit | 4 governing expressions; 4 derivation steps; declared assumptions and validity envelope | [Mathematical formulation](#4-mathematical-model-and-derivation) |
| Data blueprint | 7 proposed fields with types, units and quality rules | [Field map & downloads](data/README.md) |
| Verification queue | 4 proposed requirements; 3 specified cases; project execution evidence pending | [Case definitions](#8-verification-and-validation-cases) |
| Figure wall | Architecture, field map, planned result description; included shared illustration | [Open full gallery](figures/README.md) |
| Resource library | 2 cited primary resources with support statements | [Cited resources](#12-cited-technical-and-scientific-resources) |

### Model cockpit

**Analysis method:** Use cardioid and period-two-bulb analytic membership tests, then adaptive quadtree tiles, smooth escape coloring, and perturbation with glitch detection and reference rebasing. Maintain an arbitrary-precision reference renderer for sampled pixels. Track operation counts, wall time, precision escalations, and disagreement maps. An optional extension studies alternative iteration families as explicitly different dynamical systems; it never labels a modified map as the classical set.

**Operating envelope:** Finite images do not determine exact boundary membership. Distance estimates have asymptotic conditions, tile interpolation can miss thin structures, and hardware timings do not transfer automatically to different GPUs.

**Variables and conventions**

- c and z are dimensionless complex coordinates; n is iteration count; N_max is a finite cap.
- p is arithmetic precision in bits; pixel footprint sets requested spatial tolerance; Z is the reference trajectory.

### Artifact wall

![A01 included scientific diagnostic](../../../data/figures/17_fractal_resolution_and_escape.svg)

Finite-grid escape iteration maps from immutable Mandelbrot and Julia outputs. Logarithmic color records the first iteration whose modulus exceeds two. Navy regions identify points that did not escape within 160 iterations; these points are unresolved by this computation and are not certified members. The Julia parameter is c = −0.75 + 0.11i.

[Exact inputs, transformations and output hashes](../../../data/figures/17_fractal_resolution_and_escape.provenance.json)

**Scientific result to produce:** Four synchronized panes: Mandelbrot parameter map, Julia map, complex orbit trace, and pixel-confidence/timing heatmap; captions distinguish certified, escaped, and unresolved pixels.

### Investigation feed · planned work

The feed records proposed work packages. A row becomes executed evidence only with versioned inputs, outputs and a reviewed result.

| Sequence | Evidence state | Engineering work package |
| --- | --- | --- |
| 01 | Planned | Create scenes.yaml with exact bounds, map identity and caps. |
| 02 | Planned | Implement coordinates.py and analytic_certificates.py with orientation fixtures. |
| 03 | Planned | Build direct_reference.py and perturbation.py including derivative/rebase logs. |
| 04 | Planned | Emit pixels.parquet with null-aware evidence fields. |
| 05 | Planned | Create precision_compare.ipynb and stratified failure atlases. |
| 06 | Planned | Publish benchmark_manifest.json with hardware, clocks, hashes and timing samples. |

### Mission connections

Connections are reading routes based on actual shared resources, supplied sessions or included illustrations. They do not establish physical dependencies, team collaborations or validated results.

| Connected mission | Original investigation | Recorded connection basis |
| --- | --- | --- |
| [A02 · NEW HORIZONS CRYOPHASE](../A02-new-horizons-cryophase/README.md) | Theory and simulation investigation of eutectic phase behavior on Pluto | Session A |
| [A03 · CHANDRA VORTEX CORE](../A03-chandra-vortex-core/README.md) | Superfluidity of Neutron Star Matter | Session A |
| [A04 · APOLLO SWARM SENTINEL](../A04-apollo-swarm-sentinel/README.md) | Target Detection Using Algorithmic Matter | Session A |
| [A05 · VOYAGER CILIA ARRAY](../A05-voyager-cilia-array/README.md) | Artificial Cilia Creation for Advanced Sensor Devices | Session A |
| [A06 · APOLLO PORIN INSIGHT](../A06-apollo-porin-insight/README.md) | Purification of the P66 Outer Membrane Protein of the Bacterium Borrelia burgdorferi | Session A |
| [A07 · ORION CHROMATIN ATLAS](../A07-orion-chromatin-atlas/README.md) | Properties of Chromatin Extracted by Salt Fractionation from a Cancerous and Non-cancerous Esophageal Cell Line | Session A |

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

Proposed mission: build a mathematically auditable fractal observatory that joins adaptive iteration, arbitrary precision, and linked Mandelbrot–Julia views. The scientific product is a benchmark of numerical reliability and computational cost, with an interface that exposes uncertainty in boundary classification. Attractive colors are secondary to measuring where a renderer is accurate, where it is unresolved, and why.

**Question:** Can adaptive precision and reference-orbit perturbation reduce deep-zoom runtime while preserving verified pixel classifications and interpretable dynamical features?

**Testable hypothesis:** A proposed error-controlled hybrid will outperform uniform arbitrary-precision iteration on heterogeneous tiles; advantages should shrink near difficult boundaries and must be measured rather than assumed.

## 1. Design basis and analysis boundary

The renderer treats pixels as finite complex-plane footprints. Coordinate parsing, quadratic iteration, error monitoring and certification form the numerical boundary; palettes consume the resulting evidence without changing classifications. Exact decimal scene coordinates prevent an early binary-float conversion from destroying deep-zoom detail. The principal decision is whether a tile can safely reuse a reference orbit or needs direct computation.

The proposed fidelity ladder proceeds from analytic cardioid/bulb membership, through direct finite-cap iteration, to arbitrary-precision perturbation and interval checks. The author perturbation note motivates shared trajectories but does not guarantee acceleration. Julia scenes preserve fixed c and initial z separately; modified maps receive new model identifiers and derived escape tests.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| A01-R1 | Every pixel shall retain certified-interior, certified-exterior, escaped-point or unresolved status. | Finite nonescape is not an interior proof. | Audit status and certificate identifiers. | Mathematical contract; rendering results pending. |
| A01-R2 | Proposed coordinate target: absolute construction error below one eighth of pixel width. | Precision must resolve neighboring pixels. | Compare exact-decimal parsing at doubled precision. | Proposed numerical design tolerance. |
| A01-R3 | Julia scenes shall record fixed c, z0 and a justified escape radius. | Radius two is not a universal arbitrary-Julia bound. | Replay analytic exterior/fixed-point fixtures. | Quadratic-map inequality below. |
| A01-R4 | Proposed benchmark gate: zero contradictory certified classifications; count all unresolved pixels. | Performance gains require auditable fidelity. | Independent precision and certificate comparisons. | Proposed acceptance, not observed performance. |

## 3. Architecture and controlled interfaces

A scene manifest passes decimal strings, plane orientation, cap and precision to a coordinate constructor. The tile manager partitions footprints, applies analytic certificates and requests reference trajectories. Perturbation returns escape iteration, derivative and error diagnostics; rebasing uses a new reference without changing the underlying map.

An independent direct renderer recomputes suspicious and stratified pixels. The classifier distinguishes point escape from whole-footprint certification. The linked Julia adapter shares selected c but carries its own initial-coordinate derivative. Profiling uses monotonic elapsed seconds and library/hardware identifiers; runtime variability never substitutes for numerical confidence.

![A01 engineering architecture](figures/architecture.svg)

Certification, rebasing and independent fallback precede publication. The diagram preserves unresolved finite-cap points and distinguishes point escape from footprint membership.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

```text
z_(n+1)=z_n^2+c; Mandelbrot: z_0=0, vary c; Julia: hold c fixed, vary z_0.
```

```text
D_(n+1)=2 z_n D_n+1 for derivative with respect to c; D_0=0.
```

```text
delta z_(n+1)=2 Z_n delta z_n+(delta z_n)^2+delta c, where Z_n is a high-precision reference orbit.
```

```text
d_ext approximately |z_n| log|z_n|/|D_n| for escaped quadratic Mandelbrot orbits; it is an exterior distance estimator, not an interior certificate.
```

### Variables, units and conventions

- c and z are dimensionless complex coordinates; n is iteration count; N_max is a finite cap.
- p is arithmetic precision in bits; pixel footprint sets requested spatial tolerance; Z is the reference trajectory.

### Assumptions and boundary conditions

- Quadratic analytic maps are the baseline; alternative iterators require separate escape bounds and derivative equations.
- Failure to escape by N_max is unresolved unless a valid interior certificate applies.

### Derivation step 1

$$
\delta z_{n+1}=2Z_n\delta z_n+(\delta z_n)^2+\delta c
$$

Substitute z=Z+delta z and subtract the reference recurrence. The quadratic perturbation term matters after separation grows; dropping it changes the numerical model.

### Derivation step 2

$$
D_{n+1}=2z_nD_n+1;\quad J_{n+1}=2z_nJ_n
$$

The Mandelbrot derivative is with respect to c, D0=0. Julia initial-coordinate sensitivity instead has J0=1 and no additive one.

### Derivation step 3

$$
R>\max(2,|c|),\ |z|>R\Rightarrow |z^2+c|\ge|z|^2-|c|>|z|
$$

The conservative radius gives monotonically growing modulus. Point escape does not certify all coordinates covered by a pixel.

### Derivation step 4

$$
e_{n+1}\lesssim2|z_n|e_n+e_n^2+e_c+e_{round,n}
$$

Propagate absolute complex error and compare it with footprint width. Heuristic glitch detection triggers fallback; rigorous status requires actual bounds.

### Inference or simulation procedure

Use cardioid and period-two-bulb analytic membership tests, then adaptive quadtree tiles, smooth escape coloring, and perturbation with glitch detection and reference rebasing. Maintain an arbitrary-precision reference renderer for sampled pixels. Track operation counts, wall time, precision escalations, and disagreement maps. An optional extension studies alternative iteration families as explicitly different dynamical systems; it never labels a modified map as the classical set.

### Validity domain and fidelity limits

Finite images do not determine exact boundary membership. Distance estimates have asymptotic conditions, tile interpolation can miss thin structures, and hardware timings do not transfer automatically to different GPUs.

## 5. Data specifications and provenance

![A01 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| scene_id | string | 1 | Map and coordinate manifest hash. | Required; alternative maps use new IDs. |
| center_decimal | pair<string> | 1 | Real and imaginary center. | Never cast first to float. |
| footprint_width | float64 | 1 | Complex-plane pixel width. | Positive; height supplied if anisotropic. |
| precision_bits | uint32 | bit | Reference and working precisions. | Both recorded with library version. |
| escape_iteration | nullable<uint64> | iteration | First validated radius crossing. | Null for nonescape; zero is valid. |
| classification | enum | 1 | Evidence-qualified pixel status. | Certificates require bound metadata. |
| error_bound | nullable<float64> | 1 | Absolute coordinate/iteration uncertainty. | Bound versus heuristic flagged; unknown null. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### Self-generated, versioned numerical benchmark

[Product, archive or reference](https://mathr.co.uk/mandelbrot/perturbation.pdf)

**Fields:** Coordinate bounds, complex parameters, precision, iteration caps, escape status, timing, reference errors.

**Access:** Generate locally; the linked author technical note describes perturbation, not a downloadable observational dataset.

**Role:** Controlled truth and reproducibility manifest.

## 6. Uncertainty, sensitivity and identifiability

Coordinate truncation, recurrence amplification and reference cancellation dominate numerical error, while finite caps create classification incompleteness. Exterior distance estimates are asymptotic diagnostics and carry model discrepancy near delicate structures. Neither a smooth color field nor a small estimated distance certifies membership.

Stratify checks by zoom depth, near-parabolic dynamics and escape time. Increase arithmetic precision and iteration cap independently to separate rounding from slow escape. Track disagreement locations, reference rebases and fallback fractions. Timing studies use repeated identical workloads and publish full distributions, including scenes where perturbation loses its advantage.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Uniform arbitrary precision | Independent and straightforward. | Expensive on easy exterior regions. | Retain as comparison branch and fallback. |
| Reference perturbation | Shares expensive trajectory arithmetic. | Glitches and rebasing can erase gains. | Select when monitored error meets coordinate target. |
| Interval adaptive tiles | Certifies finite areas. | Overestimation worsens near boundaries. | Subdivide until exclusion succeeds or declare unresolved. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| A01-V1 | Interior and conjugation | c=0 and c=-1 are bounded; conjugates share escape behavior. | Check predicates and reflected direct trajectories. | Quadratic fixed and period-two orbits. |
| A01-V2 | Julia escape inequality | Modulus increases after the justified radius crossing. | Evaluate exact rational or interval fixtures. | Triangle inequality derivation. |
| A01-V3 | Precision stress | Contradictory certificates fail R4; cap-sensitive nonescape remains unresolved. | Double precision and cap separately; compare direct and perturbation kernels. | Proposed benchmark gate; outcomes TBD. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Certify known analytic regions and test conjugate symmetry; independently recompute stratified pixel samples with higher precision.
- Proposed acceptance: zero disagreements among certified pixels, explicit unresolved labels elsewhere, and report speedups with repeated timing intervals.
- Test sensitivity to doubled iteration caps, changed reference locations, and smaller pixel footprints.

## 9. Implementation and reproducible work packages

1. Create scenes.yaml with exact bounds, map identity and caps.
2. Implement coordinates.py and analytic_certificates.py with orientation fixtures.
3. Build direct_reference.py and perturbation.py including derivative/rebase logs.
4. Emit pixels.parquet with null-aware evidence fields.
5. Create precision_compare.ipynb and stratified failure atlases.
6. Publish benchmark_manifest.json with hardware, clocks, hashes and timing samples.

### Investigation sequence

1. Define 12 proposed benchmark scenes: exterior, analytic interior, near parabolic points, narrow filaments, and progressively deep zooms; publish exact decimal coordinates.
2. Implement baseline and hybrid methods under identical stopping rules, with deterministic seeds and arithmetic library versions.
3. Construct linked panels showing the parameter plane, its selected Julia set, orbit traces, and a separate confidence layer.
4. Profile performance across precision and image size; release negative cases and error-triggered fallback frequencies.

### Resources and interfaces to expertise

- Complex dynamics expertise; CPU arbitrary-precision library; GPU compute where available; accessible palette and keyboard interaction review.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| Early float conversion | Distinct zoom pixels collapse. | Duplicate coordinates with different indices. | Parse decimal strings into arbitrary precision. |
| Glitch ignored | False fine structure. | Error growth and direct discrepancy. | Rebase or recompute; expose unresolved status. |
| Cap interpreted as proof | False interior label. | Absent certificate audit. | Require certification or unresolved status. |

- Unbounded novelty claims: compare against established algorithms before claiming a new method.
- False detail from floating-point rounding: surface fallback and unresolved regions visibly.

## 11. Required engineering outputs

- Open benchmark manifest, numerical renderer, reproducible notebooks, resolution/error atlas, and interactive Mandelbrot–Julia explorer.

### Scientific result figures to produce during execution

Four synchronized panes: Mandelbrot parameter map, Julia map, complex orbit trace, and pixel-confidence/timing heatmap; captions distinguish certified, escaped, and unresolved pixels.

### Included shared numerical starting point

![A01 shared reduced-model or catalog demonstration](../../../models/figures/01_fractal_escape_distance.svg)

[Executable formulation, parameters, tabular outputs, provenance and verification](../../../models/README.md). This shared demonstration has a narrower domain than the project model above. Its own caption and methods identify synthetic parameters or the separately retrieved public catalog; it is not a completed result of the original project.

### Data diagnostic

![A01 data diagnostic](../../../data/figures/17_fractal_resolution_and_escape.svg)

Finite-grid escape iteration maps from immutable Mandelbrot and Julia outputs. Logarithmic color records the first iteration whose modulus exceeds two. Navy regions identify points that did not escape within 160 iterations; these points are unresolved by this computation and are not certified members. The Julia parameter is c = −0.75 + 0.11i.

[Inputs, downloadable figure and provenance](../../../data/figures/README.md)

## 12. Cited technical and scientific resources

- [K. I. Martin, Perturbation techniques applied to the Mandelbrot set](https://mathr.co.uk/mandelbrot/perturbation.pdf) — Author technical note supporting the reference-orbit perturbation approach; browser search located the PDF but full extraction failed.
- [Tan Lei, Similarity between the Mandelbrot set and Julia sets](https://math.univ-angers.fr/~tanlei/papers/similarityMJ.pdf) — Author-hosted original mathematical paper establishing asymptotic similarity near Misiurewicz parameters; it does not certify proposed renderer speed.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
