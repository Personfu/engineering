# H01 · VOYAGER STORYWALK

**Original project:** USGS Science Center: Solar System Exhibit Captions

**Session H:** Planetary Science

**Document class:** engineering research design and analysis record · **Revision:** 4 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session H](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_H.md) · [← G08](../../G/G08-orion-hepatic-recovery/README.md) · [H02 →](../H02-osiris-photonforge/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 4 | 4 | 7 | 4 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Mission profile

![H01 engineering mission profile: scientific question, hypothesis, model scope and evidence status](figures/mission-profile.svg)

| Profile panel | Engineering signal | Open the evidence |
| --- | --- | --- |
| Mission identity | USGS Science Center: Solar System Exhibit Captions | [Scientific objective](#purpose-and-scientific-objective) |
| Model cockpit | 3 governing expressions; 4 derivation steps; declared assumptions and validity envelope | [Mathematical formulation](#4-mathematical-model-and-derivation) |
| Data blueprint | 7 proposed fields with types, units and quality rules | [Field map & downloads](data/README.md) |
| Verification queue | 4 proposed requirements; 4 specified cases; project execution evidence pending | [Case definitions](#8-verification-and-validation-cases) |
| Figure wall | Architecture, field map, planned result description | [Open full gallery](figures/README.md) |
| Resource library | 4 cited primary resources with support statements | [Cited resources](#12-cited-technical-and-scientific-resources) |

### Model cockpit

**Analysis method:** Build an inventory from exhibit photographs and staff records, identifying original products through Photojournal or instrument archives. A visually similar image is insufficient identification: verify scene geometry, crop, mission metadata, and processing. Draft three layers: an approximately 40-word observation, an approximately 100-word explanation, and an optional source-backed exploration. Mark enhanced color, mosaic seams, artistic renderings, and uncertain interpretations. Co-design mobile navigation with visitors using screen readers and people with limited bandwidth; provide readable print or staff-accessible alternatives. Randomize two equally accurate caption formats and score an observation-versus-inference task immediately and after a consented follow-up. Estimate effects with hierarchical logistic regression, retaining nonresponses and uncertainty rather than selecting favorable responses.

**Operating envelope:** One exhibit's audience does not represent all museums. Device ownership, language, motivation, and voluntary participation influence estimates. No individual visitor tracking is needed for the basic caption system.

**Variables and conventions**

- Y is a scored comprehension response; T is randomized caption assignment; Delta is an absolute probability difference.
- K is a preregistered prior-knowledge score; visitor and day effects represent clustered observations.
- G is a provenance graph; each image node stores product identifier, mission, acquisition date, processing description, and credit.

### Artifact wall

![H01 proposed analysis architecture](figures/architecture.svg)

The diagram establishes physical-image identity, source-backed captions and separate access channels before visitor evaluation. It provides a reviewable engineering package without claiming an updated exhibit or demonstrated learning benefit.

**Scientific result to produce:** A sample planet image beside observation, inference, scale, and source layers; a separate diagram shows randomized caption evaluation. Proposed outcomes remain unfilled until measured.

### Investigation feed · planned work

The feed records proposed work packages. A row becomes executed evidence only with versioned inputs, outputs and a reviewed result.

| Sequence | Evidence state | Engineering work package |
| --- | --- | --- |
| 01 | Planned | Build a curator-reviewed exhibit inventory with exact image-product matches. |
| 02 | Planned | Create claim/source/processing/scale graph schemas and revision rules. |
| 03 | Planned | Author layered caption artifacts with print and accessible digital specifications. |
| 04 | Planned | Run provenance and assistive-technology task checks before evaluation. |
| 05 | Planned | Preregister clustered assignment, scoring rubric and nonresponse analysis. |
| 06 | Planned | Publish reviewed captions and learning-evidence limitations without claiming prior deployment. |

### Mission connections

Connections are reading routes based on actual shared resources, supplied sessions or included illustrations. They do not establish physical dependencies, team collaborations or validated results.

| Connected mission | Original investigation | Recorded connection basis |
| --- | --- | --- |
| [H02 · OSIRIS PHOTONFORGE](../H02-osiris-photonforge/README.md) | Calibration of Images from the OSIRIS-REx Camera Suite | Session H |
| [H03 · ARTEMIS POLAR COMPASS](../H03-artemis-polar-compass/README.md) | Magnetic Anomalies in the South Polar Region of the Moon | Session H |
| [H04 · STARDUST CARBON ATLAS](../H04-stardust-carbon-atlas/README.md) | Exploring Carbon-bearing Matter in an Antarctic Micrometeorite | Session H |
| [H05 · TERRA SEVEN GENERATIONS](../H05-terra-seven-generations/README.md) | Supporting the Climate Change Department | Session H |
| [H06 · MARS ODYSSEY RIDGEWORK](../H06-mars-odyssey-ridgework/README.md) | Variability of Martian Wrinkle Ridges | Session H |
| [H07 · KEPLER CO ECHO](../H07-kepler-co-echo/README.md) | Increasing CO Gas Detections in Protoplanetary Disks | Session H |

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

Complete the original mobile-caption concept for the USGS Flagstaff solar-system exhibit, then turn it into an evidence-based visitor learning platform. Every displayed image receives an identified mission product, accessible explanation, scale cue, and traceable scientific claim. NASA Photojournal and USGS mission material provide authoritative starting points; proposed audience experiments determine whether captions actually help visitors interpret evidence. This is a new development proposal, not a claim that the historic exhibit or its app has been updated.

**Question:** Which caption structure most improves visitors' ability to explain what an image reveals, without overstating what scientists can infer from its appearance?

**Testable hypothesis:** A short observation-first caption with a clearly labeled inference, physical scale, and optional deeper layer will improve delayed comprehension relative to a factual inventory of the same length.

## 1. Design basis and analysis boundary

The exhibit-caption engineering system is an evidence registry, reviewed caption package and visitor-evaluation protocol for the USGS Flagstaff solar-system exhibit. It first identifies each actual displayed image, then binds observation, interpretation, scale and processing notes to a traceable mission product. A visually similar Photojournal entry is insufficient to establish identity, and no historical exhibit update is claimed.

Begin with staff-approved inventory and printable layered captions; add accessible mobile delivery only as a documented output channel. The fidelity ladder advances from claim/image provenance to usability review and a consented clustered comparison of equally accurate formats. NASA/USGS sources support scientific content, while learning benefit, word budgets and performance targets are proposed design choices requiring visitor evidence.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| H01-R1 | Every scientific caption claim shall have an image/product identifier and reviewed source span; proposed traceability completeness is 100%. | Attractive captions can hide image/claim mismatches. | Graph foreign-key and curator audit. | Photojournal/USGS provenance; proposed target. |
| H01-R2 | Declare enhanced color, mosaics, artistic renderings and uncertain inference in the visible explanatory layer. | Visitors need observation-versus-processing distinctions. | Image-processing label review. | Mission product documentation. |
| H01-R3 | Digital normal text shall meet WCAG 2.2 minimum 4.5:1 contrast where applicable, with keyboard/screen-reader access and a printable alternative. | Device and visual access should not determine learning opportunity. | Contrast and assistive-technology task review. | W3C WCAG 2.2. |
| H01-R4 | Learning evaluation shall randomize companion groups/sessions, retain nonresponses and score comprehension separately from dwell time. | Companion exchange and engagement confound outcomes. | Assignment and missing-outcome audit. | Proposed visitor study design. |

## 3. Architecture and controlled interfaces

An exhibit inventory links physical panel location to product ID, mission, acquisition date, credit and processing. A provenance graph stores atomic claims, reviewed sources and alternative interpretations. Caption records contain observation, explanation and optional exploration layers with scale cues and text alternatives.

The delivery specification uses stable caption identifiers for print and mobile copies, with no individual tracking required for basic access. The evaluation adapter records consented anonymous group assignment, prior-knowledge score and scored response, while session/day keys capture clustering. Unidentified images or unsupported claims block release of that item; optional visitor nonresponse remains a missing outcome rather than a wrong answer.

![H01 engineering architecture](figures/architecture.svg)

The diagram establishes physical-image identity, source-backed captions and separate access channels before visitor evaluation. It provides a reviewable engineering package without claiming an updated exhibit or demonstrated learning benefit.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

```text
Δ_k=P(Y_k=1|T=1)-P(Y_k=1|T=0)
```

$$
\mathrm{logit}\,P(Y_{iv}=1)=\alpha+\beta T_{iv}+\gamma K_i+u_v+u_{\rm day}
$$

$$
G=(V,E),\quad E=\{\mathrm{image}\rightarrow\mathrm{claim}\rightarrow\mathrm{source}\}
$$

### Variables, units and conventions

- Y is a scored comprehension response; T is randomized caption assignment; Delta is an absolute probability difference.
- K is a preregistered prior-knowledge score; visitor and day effects represent clustered observations.
- G is a provenance graph; each image node stores product identifier, mission, acquisition date, processing description, and credit.

### Assumptions and boundary conditions

- Assignment occurs at a visitor-group or session level to avoid contamination from companions exchanging caption versions.
- Dwell time measures engagement opportunity; it is not treated as comprehension or satisfaction.

### Derivation step 1

```text
G=(V,E); E includes image->claim->source and caption->claim.
```

Graph completeness is count of supported claims divided by reviewed displayed claims, with unreviewed items explicitly excluded from confirmed status.

### Derivation step 2

```text
Delta=P(Y=1|T=1)-P(Y=1|T=0).
```

The learning effect is an absolute probability difference, reported in percentage points; it is distinct from odds ratio or relative gain.

### Derivation step 3

```text
logit P(Y_iv=1)=alpha+beta T_iv+gamma K_i+u_group+u_day.
```

Randomized treatment T and prior knowledge K enter a clustered model. Marginal Delta is computed from predicted probabilities rather than equating beta with a percentage change.

### Derivation step 4

```text
DE=1+(m-1)rho; n_eff approximately n/DE.
```

This planning approximation accounts for group mean size m and intraclass correlation rho. Final uncertainty uses actual cluster structure and missing-outcome sensitivity.

### Inference or simulation procedure

Build an inventory from exhibit photographs and staff records, identifying original products through Photojournal or instrument archives. A visually similar image is insufficient identification: verify scene geometry, crop, mission metadata, and processing. Draft three layers: an approximately 40-word observation, an approximately 100-word explanation, and an optional source-backed exploration. Mark enhanced color, mosaic seams, artistic renderings, and uncertain interpretations. Co-design mobile navigation with visitors using screen readers and people with limited bandwidth; provide readable print or staff-accessible alternatives. Randomize two equally accurate caption formats and score an observation-versus-inference task immediately and after a consented follow-up. Estimate effects with hierarchical logistic regression, retaining nonresponses and uncertainty rather than selecting favorable responses.

### Validity domain and fidelity limits

One exhibit's audience does not represent all museums. Device ownership, language, motivation, and voluntary participation influence estimates. No individual visitor tracking is needed for the basic caption system.

## 5. Data specifications and provenance

![H01 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| exhibit_item | string | none | Staff-reviewed physical image/panel key. | Photo/crop geometry match required. |
| mission_product | nullable record | none | Verified image ID and processing provenance. | Null blocks confirmed caption. |
| claim_source | edge record | none | Atomic scientific claim and supporting span. | Reviewer/version required. |
| caption_layers | text record | words | Observation/explanation/exploration text. | Scale and processing labels retained. |
| assignment_group | anonymous string | none | Companion/session randomization unit. | No identifiable visitor tracking. |
| comprehension_score | nullable bool | none | Declared rubric outcome. | Nonresponse stays null. |
| effect_covariance | matrix | probability² | Joint learning-effect uncertainty. | Group/day dependence included. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### NASA Photojournal

[Product, archive or reference](https://science.nasa.gov/photojournal/)

**Fields:** Image identifiers, scientific descriptions, missions, processing notes, credits

**Access:** Public browsing; confirm usage conditions and actual exhibit-image matches individually.

**Role:** Caption evidence and product identity.

### USGS Astrogeology Science Center

[Product, archive or reference](https://www.usgs.gov/centers/astrogeology-science-center)

**Fields:** Center context, planetary mapping resources, visitor information

**Access:** Public context; local exhibit inventory requires staff cooperation.

**Role:** Host requirements and scientifically reviewed interpretation.

## 6. Uncertainty, sensitivity and identifiability

Product identification can fail because of crop, recoloring or mosaic composition. Preserve uncertain matches and seek curator records; a correct mission name alone is insufficient. Scientific interpretations can change, so claim/source revision dates and review status remain part of the engineering release. Accessibility review covers actual task completion as well as automated contrast checks.

Visitor selection, device ownership, language and companion interaction affect generalization. Randomize groups, use cluster-aware intervals and compare bounds for nonresponse rather than select favorable respondents. Dwell time is a process measure only. Prior-knowledge and subgroup effects may be weakly identified, so avoid claiming broad learning superiority from a small local pilot.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Printed layered captions | Accessible without personal devices. | Limited optional depth and updates. | Required baseline/alternative channel. |
| Mobile linked evidence layers | Supports optional source exploration. | Bandwidth/device/accessibility burden. | Use when visitor task review supports it. |
| Facilitated interpretation cards | Allows dialogue and low-device access. | Staffing and session effects vary. | Compare as a distinct delivery scenario. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| H01-V1 | Provenance break | Item is marked unsupported and cannot enter confirmed release. | Condition/fixture: Remove the source edge for one scientific claim. Verification procedure: Graph integrity fixture.. | Graph integrity fixture. |
| H01-V2 | Learning arithmetic | Delta=0.2, or 20 percentage points. | Condition/fixture: Synthetic correct-response rates are 0.8 and 0.6. Verification procedure: Exact effect calculation.. | Exact effect calculation. |
| H01-V3 | Cluster planning | DE=1.6 and n_eff=n/1.6. | Condition/fixture: m=4 and rho=0.2 in the planning approximation. Verification procedure: Independent formula check.. | Independent formula check. |
| H01-V4 | Accessible delivery | Every required caption/source path remains usable; failures are recorded for repair. | Condition/fixture: Review representative print/mobile tasks with keyboard and screen reader plus low bandwidth. Verification procedure: Task-based integration review.. | Task-based integration review. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Require every factual caption claim to resolve to a reviewed source and every image to retain its original credit.
- Test screen-reader order, keyboard navigation, text resizing, offline fallback, and reading on a low-end phone.
- Report effect intervals, attrition by group, and an anonymized scoring rubric; accept a null learning effect as informative.

## 9. Implementation and reproducible work packages

1. Build a curator-reviewed exhibit inventory with exact image-product matches.
2. Create claim/source/processing/scale graph schemas and revision rules.
3. Author layered caption artifacts with print and accessible digital specifications.
4. Run provenance and assistive-technology task checks before evaluation.
5. Preregister clustered assignment, scoring rubric and nonresponse analysis.
6. Publish reviewed captions and learning-evidence limitations without claiming prior deployment.

### Investigation sequence

1. Establish the complete image inventory and unresolved-identification queue before authoring captions.
2. Review each claim with a planetary specialist and each interaction with an accessibility reviewer.
3. Pilot comprehension tasks, define the smallest useful effect, and size the visitor study by simulated power.
4. Publish reviewed captions with version history, source links, and a correction route.

### Resources and interfaces to expertise

- USGS exhibit curator, planetary-science reviewer, accessible web developer, education evaluator, consented visitor pilot.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| Similar image substituted | Incorrect caption identity. | Crop/geometry/product review. | Retain unresolved inventory state. |
| Dwell called comprehension | False learning success. | Outcome/rubric audit. | Separate process and learning metrics. |
| Digital-only access | Excluded visitors. | Alternative-channel task review. | Print and assisted access. |

- Misidentified source images, outdated explanations, caption overload, and exclusion of visitors without phones.

## 11. Required engineering outputs

- A versioned caption registry, mobile walking guide, provenance graph, visitor-study protocol, and evaluated design recommendations.

### Scientific result figures to produce during execution

A sample planet image beside observation, inference, scale, and source layers; a separate diagram shows randomized caption evaluation. Proposed outcomes remain unfilled until measured.

## 12. Cited technical and scientific resources

- [NASA Photojournal](https://science.nasa.gov/photojournal/) — Authoritative mission imagery and accompanying descriptions.
- [USGS Astrogeology Science Center](https://www.usgs.gov/centers/astrogeology-science-center) — Center mission and visitor context.
- [NASA Museum and Informal Education Alliance](https://science.nasa.gov/sciact-team/museum-alliance/) — Informal-learning resources and connection to NASA science; not evidence that this proposed caption format works.
- [W3C Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/) — Primary accessibility criteria supporting text contrast, keyboard/focus access and alternatives; proposed caption-learning outcomes require independent visitor evaluation.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
