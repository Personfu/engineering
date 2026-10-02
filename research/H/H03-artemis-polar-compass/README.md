# H03 · ARTEMIS POLAR COMPASS

**Original project:** Magnetic Anomalies in the South Polar Region of the Moon

**Session H:** Planetary Science

**Document class:** engineering research design and analysis record · **Revision:** 3 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session H](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_H.md) · [← H02](../H02-osiris-photonforge/README.md) · [H04 →](../H04-stardust-carbon-atlas/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 4 | 4 | 8 | 3 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Purpose and scientific objective

Produce a defensible south-polar lunar magnetic-field atlas from Kaguya magnetometer observations, with Lunar Prospector as an independent comparison where coverage permits. Preserve the equivalent-source dipole approach and polar map focus. The principal advance is a map of resolution, external-field contamination, and altitude-transfer uncertainty alongside field strength. A magnetic anomaly is a geological clue; this project does not equate orbital anomaly detection with a measured surface shielding benefit for astronauts.

**Question:** Which south-polar anomalies persist across quiet passes and reasonable equivalent-source geometries, and at what spatial resolution can their field be estimated?

**Testable hypothesis:** Cross-orbit regularization with an explicit external-field component will recover stable regional anomalies while reducing apparent small-scale structure produced by irregular altitude and plasma disturbances.

## 1. Design basis and analysis boundary

The south-polar magnetic atlas uses observation-level Kaguya LMAG vector data and independent Lunar Prospector passes where coverage permits. Its engineering outputs are reference-altitude fields, source resolution and external-field/altitude-transfer uncertainty. The equivalent dipole mesh is an inversion representation, not a recovered physical set of isolated lunar magnets.

Begin with quiet-pass selection, ephemeris/frame validation and nuisance-aware inversion. Promote to finer source grids or downward continuation only if projected sensitivity supports them. The reviewed nonpolar 30-km PDS map does not cover the study pole and is excluded as polar input. External-field coefficients are jointly fitted and eliminated before source resolution is assessed; ignoring them overstates internal-field identifiability.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| H03-R1 | Each vector observation shall retain mission/product flags, position, altitude, time, frame and external-condition selection rule. | External contamination and frame errors can mimic anomalies. | Pass/frame metadata audit. | JAXA/PDS archive context. |
| H03-R2 | Compute resolution after covariance-weighted nuisance projection, with rank/gauge constraints documented. | Source-only resolution exaggerates identifiable structure. | Projection/nullspace analytic checks. | Reviewed W_perp/R_m formulation. |
| H03-R3 | Compare missions at matched modeled altitude and report continuation uncertainty separately. | Dipole fields decay rapidly with distance. | Geometry/altitude residual review. | Existing magnetic model. |
| H03-R4 | Do not use the nonpolar 65°S–65°N crustal map as south-pole observations or infer astronaut shielding from orbital anomalies. | Coverage and physical endpoints differ. | Source-domain and claim audit. | PDS coverage limitation. |

## 3. Architecture and controlled interfaces

An observation adapter transforms vectors into a named lunar Cartesian/polar frame, preserving nT originals and SI T conversion. Ephemeris provides observation/source coordinates in metres and reference altitude. Source mesh records dipole depth/spacing; nuisance design H contains declared pass-specific smooth external terms.

The inversion first whitens correlated measurement/environmental covariance, then projects unpenalized nuisance modes before regularized source estimation. Gauge and singular-value diagnostics define supported source combinations. Reference-altitude forward maps carry covariance and averaging kernels, while mission comparison uses matched geometry. Quiet-pass and nuisance-model alternatives propagate map discrepancy; unsupported polar cells remain flagged rather than filled by nonpolar coverage.

![H03 engineering architecture](figures/architecture.svg)

The diagram makes external-field nuisance projection part of source estimation and resolution. It supports an altitude-specific polar magnetic atlas with identifiable-mode masks, while excluding unsupported surface shielding and nonpolar-map substitution.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

$$
\mathbf B(\mathbf r)=\frac{\mu_0}{4\pi}\sum_j\left[\frac{3\mathbf R_j(\mathbf m_j\cdot\mathbf R_j)}{R_j^5}-\frac{\mathbf m_j}{R_j^3}\right]+\mathbf B_{\rm ext}
$$

$$
(\hat{\mathbf m},\hat{\mathbf a})=\arg\min_{\mathbf m,\mathbf a}\;\Vert\mathbf C^{-1/2}(\mathbf G\mathbf m+\mathbf H\mathbf a-\mathbf b)\Vert^2+\lambda\Vert\mathbf L\mathbf m\Vert^2
$$

```text
W_perp = C^-1 - C^-1 H (H^T C^-1 H)^+ H^T C^-1; R_m = (G^T W_perp G + lambda L^T L)^+ G^T W_perp G, after eliminating unpenalized external-field nuisance coefficients.
```

### Variables, units and conventions

- B is magnetic induction in tesla, reported in nanotesla; r and dipole displacement R are meters; m is dipole moment in ampere square meters.
- G maps source moments to measured vector components; H a represents smooth external-field nuisance terms per pass.
- C includes correlated measurement and environmental errors; the resolution matrix R differs from dipole displacement R_j.
- W_perp: covariance-weighted projection after jointly fitting H a; superscript + denotes the Moore-Penrose pseudoinverse. R_m is source resolution under the declared constraints, not the resolution of a source-only fit.

### Assumptions and boundary conditions

- Equivalent dipoles are an inversion representation, not an assertion that physical isolated dipoles exist at the chosen depth.
- A reference-altitude map is modeled; downward continuation toward the surface is unstable and requires strong uncertainty qualification.
- Check rank and impose documented gauge/source constraints before interpreting resolution; uncertainty in the external-field model can reduce identifiable internal-field structure.

### Derivation step 1

```text
B_j=mu0/(4pi)[3 R_j(m_j dot R_j)/R_j^5-m_j/R_j^3].
```

R is metres, dipole moment A m² and B tesla; sum source fields plus external terms in a consistent vector frame.

### Derivation step 2

```text
W_perp=C^-1-C^-1 H(H^T C^-1 H)^+H^T C^-1.
```

Eliminating unpenalized external coefficients yields the covariance-weighted nuisance complement. Check H^T W_perp=0 and numerical rank before interpreting source information.

### Derivation step 3

```text
A=G^T W_perp G+lambda L^T L; m_hat=A^+G^T W_perp b; R_m=A^+G^T W_perp G.
```

R_m is source resolution after nuisance fitting. lambda and L are scaled consistently with moment units, and documented gauge constraints remove unsupported modes.

### Derivation step 4

```text
B_*=G_* m_hat; C_B*=G_* C_m G_*^T+C_model.
```

Continuation to reference altitude uses the source posterior/estimator covariance plus nuisance/depth discrepancy. Near-surface continuation amplifies poorly resolved short wavelengths.

### Inference or simulation procedure

Select south-polar Kaguya LMAG passes using instrument flags, ephemerides, altitude, local time, and evidence of quiet external conditions. Compare several quiet-pass definitions instead of accepting a single threshold. Transform vectors into a documented lunar coordinate frame and invert on a polar mesh, testing source depth, spacing, and regularization. Jointly estimate slowly varying external terms with constraints that prevent them absorbing the crustal signal. Map radial and horizontal components at a declared reference altitude and evaluate spatial sensitivity with synthetic anomaly recovery. Compare independent Lunar Prospector passes at matched altitude rather than judging agreement between maps at different heights. Overlay geological boundaries only after the magnetic inversion is frozen.

### Validity domain and fidelity limits

Source magnetization magnitude, orientation, depth, and lateral extent are nonunique. External currents and sparse low-altitude coverage may dominate some pixels. The commonly cited PDS large-scale 30-km crustal map covers only 65 degrees south to 65 degrees north and cannot supply the polar study area.

## 5. Data specifications and provenance

![H03 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| mag_product | string | none | LMAG/Prospector pass provenance. | Observation-level coverage and flags required. |
| field_vector | nullable float[3] | nT | Measured magnetic components. | Frame/time transformation recorded. |
| position_xyz | float[3] | m | Observation geometry. | Lunar origin/frame and altitude explicit. |
| dipole_moment | float vector | A m² | Equivalent-source estimator. | Depth/grid/gauge not physical truth. |
| nuisance_design | matrix | declared | Pass external-field basis H. | Rank and constraints retained. |
| observation_covariance | matrix | T² | Correlated measurement/environment error. | PSD and unit conversion checked. |
| projected_resolution | matrix | dimensionless | Nuisance-aware R_m. | Supported singular modes documented. |
| reference_map | record | nT | Modeled altitude field and uncertainty. | Altitude/continuation support explicit. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### JAXA DARTS Kaguya archive

[Product, archive or reference](https://darts.isas.jaxa.jp/en/missions/kaguya)

**Fields:** LMAG vector observations, product documentation, geometry and time metadata

**Access:** Public scientific archive; find the appropriate observation-level LMAG products, not the separate conductivity inversion.

**Role:** Primary polar magnetic observations.

### PDS Lunar Prospector holdings

[Product, archive or reference](https://pds-geosciences.wustl.edu/missions/lunarp/index.htm)

**Fields:** MAG/ER archive discovery and mission geometry

**Access:** Magnetometer products are linked through the PPI node; inspect quality and coverage.

**Role:** Independent instrument comparison.

## 6. Uncertainty, sensitivity and identifiability

External fields, spacecraft offsets and quiet-pass selection can absorb or imitate long-wavelength crustal signals. Compare nuisance bases and quiet-condition rules, retaining their discrepancy separately from magnetometer noise. If source modes lie in the nuisance span, the data cannot identify them; a regularization prior does not convert them into measured structure.

Source depth, orientation and lateral extent are nonunique, and downward continuation magnifies short-scale uncertainty. Inspect projected singular values, resolution kernels and synthetic recoverability across grid/depth choices. Compare independent missions only after altitude/frame harmonization. Geological overlays are interpretation after inversion freeze, and orbital field strength alone cannot quantify surface radiation shielding.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Coarse equivalent-source inversion | Stable transparent reference-altitude map. | Smooths unresolved short wavelengths. | Default where projected rank is limited. |
| Finer/deeper source ensembles | Tests depth/spacing discrepancy. | More nullspace and prior dependence. | Adopt only with recoverability evidence. |
| Direct pass-level cross-mission comparison | Independent observation check. | Sparse matched geometry restricts coverage. | Required comparator where overlap exists. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| H03-V1 | Single dipole axis/equator | Axial magnitude is twice equatorial magnitude; direction follows vector formula. | Condition/fixture: Equal distance R from a dipole aligned with z. Verification procedure: Exact field fixture.. | Exact field fixture. |
| H03-V2 | Nuisance projection | H^T W_perp=0 within scaled numerical tolerance. | Condition/fixture: Use full-rank synthetic H and positive-definite C. Verification procedure: Independent matrix calculation.. | Independent matrix calculation. |
| H03-V3 | Shared source/nuisance mode | Projected data sensitivity for that mode is zero; it cannot be called resolved. | Condition/fixture: A column of G lies entirely in span(H). Verification procedure: Nullspace fixture.. | Nullspace fixture. |
| H03-V4 | Independent polar passes | Report vector residuals, coverage and resolution support. | Condition/fixture: Reserve full passes and matched-altitude Prospector observations. Verification procedure: Pass-level holdout comparison.. | Pass-level holdout comparison. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Hold out complete orbits and report vector residuals by altitude and plasma state.
- Inject known dipoles into actual sampling patterns to quantify location bias and resolvable separation.
- Require consistency across independent passes before labeling an anomaly robust; retain low-confidence regions explicitly.

## 9. Implementation and reproducible work packages

1. Freeze observation-level polar product manifests and quiet-pass alternatives.
2. Implement lunar vector/frame/time and nT-to-T adapters.
3. Construct source/nuisance matrices with correlated covariance and gauge checks.
4. Compute projected singular modes, regularized estimates and R_m kernels.
5. Generate dipole recovery/continuation benchmarks and held-out mission comparisons.
6. Publish altitude-specific fields, resolution masks and nonunique geological interpretations.

### Investigation sequence

1. Build orbit manifests and coordinate-conversion checks.
2. Fit a depth/spacing/regularization ensemble using orbit-blocked cross-validation.
3. Generate vector maps with coverage, resolution, and uncertainty layers.
4. Test whether geological associations survive environmental and inversion sensitivity analyses.

### Resources and interfaces to expertise

- SPICE geometry, spherical vector tools, regularized inverse solver, lunar magnetism mentor, GIS polar projection expertise.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| Source-only resolution | False confidence in crustal structure. | Compare projected and unprojected kernels. | Use W_perp before resolution. |
| Unstable downward map | Artificial surface hotspots. | Altitude/depth sensitivity. | Reference-altitude maps with continuation limits. |
| Nonpolar data substituted | Unsupported polar atlas. | Latitude/product-domain audit. | Use verified polar observations. |

- Polar projection distortions, contamination selection bias, downward-continuation instability, and confusing modeled sources with unique geological bodies.

## 11. Required engineering outputs

- A reference-altitude field atlas, orbit-quality catalog, inversion ensemble, and geological interpretation with uncertainty.

### Scientific result figures to produce during execution

Matched-altitude polar maps of field components, posterior spread, sampled orbit tracks, and resolution length; unsampled regions are visibly masked.

## 12. Cited technical and scientific resources

- [JAXA Kaguya DARTS mission archive](https://darts.isas.jaxa.jp/en/missions/kaguya) — LMAG data and instrument-documentation discovery.
- [PDS Lunar Prospector archive](https://pds-geosciences.wustl.edu/missions/lunarp/index.htm) — Independent MAG/ER observation access.
- [PDS lunar crustal magnetic-field-map bundle](https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Alunar-crust-magnetic.field-map) — Explicit nonpolar latitude coverage limitation.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
