# F02 · DISCOVERY QUILL

**Original project:** The Impact and Importance of Science Writing

**Session F:** Education & Public Outreach

**Document class:** engineering research design and analysis record · **Revision:** 4 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session F](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_F.md) · [← F01](../F01-apollo-voicelink/README.md) · [G01 →](../../G/G01-artemis-bone-watch/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 4 | 3 | 7 | 3 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Mission profile

![F02 engineering mission profile: scientific question, hypothesis, model scope and evidence status](figures/mission-profile.svg)

| Profile panel | Engineering signal | Open the evidence |
| --- | --- | --- |
| Mission identity | The Impact and Importance of Science Writing | [Scientific objective](#purpose-and-scientific-objective) |
| Model cockpit | 3 governing expressions; 4 derivation steps; declared assumptions and validity envelope | [Mathematical formulation](#4-mathematical-model-and-derivation) |
| Data blueprint | 7 proposed fields with types, units and quality rules | [Field map & downloads](data/README.md) |
| Verification queue | 4 proposed requirements; 3 specified cases; project execution evidence pending | [Case definitions](#8-verification-and-validation-cases) |
| Figure wall | Architecture, field map, planned result description | [Open full gallery](figures/README.md) |
| Resource library | 3 cited primary resources with support statements | [Cited resources](#12-cited-technical-and-scientific-resources) |

### Model cockpit

**Analysis method:** Build paired articles from the same source claims and obtain blind expert accuracy ratings. Randomize audience exposure, measure immediate and delayed understanding, and assess confidence calibration. Compare across topics and reading contexts; publish failures of appealing prose to improve understanding.

**Operating envelope:** A convenience sample does not represent every audience. Format, reading time and visual complexity must be separated to avoid confounding.

**Variables and conventions**

- Y rubric-scored comprehension; p confidence 0-1; y correctness 0 or 1
- beta adjusted format effect; reader/topic random effects
- Delayed interval fixed before recruitment; engagement counts are secondary

### Artifact wall

![F02 proposed analysis architecture](figures/architecture.svg)

Source-linked claim equivalence and independent factual review precede audience comparison. Retention and probability calibration are separate outcomes, with topic holdout and delayed attrition limiting format claims.

**Scientific result to produce:** Format comparison of delayed comprehension and confidence calibration; source-to-claim map identifies what each sentence supports.

### Investigation feed · planned work

The feed records proposed work packages. A row becomes executed evidence only with versioned inputs, outputs and a reviewed result.

| Sequence | Evidence state | Engineering work package |
| --- | --- | --- |
| 01 | Planned | Create primary_source_claims.csv and article_claim_graph.json. |
| 02 | Planned | Draft matched article variants with immutable uncertainty statements. |
| 03 | Planned | Build blind_expert_accuracy_rubric.yaml and accessibility_burden_review.md. |
| 04 | Planned | Create consented_assignment_schema.json and preregistered_assessments.yaml. |
| 05 | Planned | Implement rubric_brier_scoring.py and reader_topic_effects.py. |
| 06 | Planned | Publish heldout_topic_attrition.ipynb and a findings template reporting negative calibration outcomes. |

### Mission connections

Connections are reading routes based on actual shared resources, supplied sessions or included illustrations. They do not establish physical dependencies, team collaborations or validated results.

| Connected mission | Original investigation | Recorded connection basis |
| --- | --- | --- |
| [F01 · APOLLO VOICELINK](../F01-apollo-voicelink/README.md) | Communication and Exploration | Session F; [NASA educational outreach evaluation framework](https://ntrs.nasa.gov/citations/20000033841) |

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

Transform science writing into an experimentally evaluated translation of evidence for multiple audiences. Keep accuracy and uncertainty calibration central while comparing narrative structure, visual support and reading demands. The final product includes a reusable editorial rubric and source-linked examples whose effectiveness is measured rather than inferred from engagement counts.

**Question:** Which science-writing formats improve retained understanding and calibrated confidence while preserving factual accuracy and uncertainty?

**Testable hypothesis:** A claim-evidence-uncertainty structure will improve delayed comprehension over an equally accurate conventional summary, although preference and learning gains may diverge.

## 1. Design basis and analysis boundary

The science-writing evaluation system compares article formats built from the same verified source claims and uncertainty statements. Its boundary includes claim traceability, factual expert review, reading burden/accessibility, audience assignment and immediate/delayed comprehension/confidence. Engagement counts are secondary; appealing prose cannot be assumed to improve understanding or calibrated confidence.

Begin with paired source-linked articles and blind accuracy review, then preregistered reader/topic comparisons. Separate format from reading time, visual complexity and factual content. Published uncertainty-communication experiments motivate explicit uncertainty presentation, but their trust findings are not substituted for this project's retention or calibration results.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| F02-R1 | Every factual article claim shall link to a primary source location and declared uncertainty. | Format comparisons are invalid if facts change. | Claim graph and blind expert accuracy audit. | Source-linked content requirement. |
| F02-R2 | Formats shall match factual claim set and approximate reading burden; deviations are recorded. | Length/complexity can masquerade as format effect. | Claim-set equality, accessibility and time-budget review. | Controlled comparison contract. |
| F02-R3 | Comprehension rubrics and confidence questions shall be fixed before exposure, with confidence in [0,1]. | Outcome changes after reading bias results. | Score/range fixtures and preregistration audit. | Measurement requirement. |
| F02-R4 | Proposed selection gate: retained adjusted understanding improves without worse expert accuracy or confidence calibration. | A format can engage readers while misleading them. | Joint delayed-score/Brier/accuracy intervals on held-out topics. | Proposed criterion; no format superiority claimed. |

## 3. Architecture and controlled interfaces

A source registry stores primary references, claim IDs and evidence locations. Article variants map each paragraph/visual to that claim graph; an expert-review adapter records accuracy and uncertainty fidelity independently of reader outcomes. Accessibility review and reading-burden metadata accompany format identity.

A consented assignment registry maps pseudonymous reader/topic exposures to baseline, immediate and fixed-delay assessments. Rubric scoring produces correctness and comprehension totals; confidence remains a probability attached to the exact item. Mixed-effects analysis shares reader/topic covariance and accounts for attrition rather than discarding failed delayed responses.

![F02 engineering architecture](figures/architecture.svg)

Source-linked claim equivalence and independent factual review precede audience comparison. Retention and probability calibration are separate outcomes, with topic holdout and delayed attrition limiting format claims.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

```text
Y_post=alpha+beta*format+gamma*Y_pre+u_topic+u_reader+epsilon
```

```text
Brier=(1/N)*sum(p_i-y_i)^2
```

```text
retention=Y_delayed-Y_pre
```

### Variables, units and conventions

- Y rubric-scored comprehension; p confidence 0-1; y correctness 0 or 1
- beta adjusted format effect; reader/topic random effects
- Delayed interval fixed before recruitment; engagement counts are secondary

### Assumptions and boundary conditions

- Randomize formats with equal factual content, source basis and approximate reading burden.
- Consent and accessibility review precede human participant work.

### Derivation step 1

$$
Y_{post}=\alpha+\beta F+\gamma Y_{pre}+u_{topic}+u_{reader}+\epsilon
$$

Format effect beta is baseline adjusted. Reader/topic clustering matters when observations repeat; rubric scale and model family must match the score distribution.

### Derivation step 2

$$
Brier={1\over N}\sum_i(p_i-y_i)^2
$$

For binary correctness y and confidence p in [0,1], score lies between zero and one and lower is better. Accuracy alone does not measure overconfidence.

### Derivation step 3

$$
\partial E[(p-y)^2]/\partial p=2(p-q)
$$

If true correctness probability is q, expected Brier loss is minimized at p=q. This explains why calibrated uncertainty can be preferable to confident guessing.

### Derivation step 4

```text
G_{retention}=Y_{delayed}-Y_{pre}
```

Retention gain uses a fixed delayed interval and comparable items. Missing delayed responses are attrition, not zero learning; sensitivity models address informative missingness.

### Inference or simulation procedure

Build paired articles from the same source claims and obtain blind expert accuracy ratings. Randomize audience exposure, measure immediate and delayed understanding, and assess confidence calibration. Compare across topics and reading contexts; publish failures of appealing prose to improve understanding.

### Validity domain and fidelity limits

A convenience sample does not represent every audience. Format, reading time and visual complexity must be separated to avoid confounding.

## 5. Data specifications and provenance

![F02 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| claim_id | string | 1 | Versioned factual/uncertainty proposition. | Primary source and exact evidence location required. |
| article_variant | record | 1 | Format, topic and claim mapping. | Matched factual set and revisions retained. |
| expert_accuracy | nullable<record> | rubric | Blind factual/uncertainty ratings. | Reviewer agreement and corrections recorded. |
| reader_id | string | 1 | Pseudonymous participant key. | Consented access only; identity separate. |
| assessment_score | nullable<float64> | rubric | Pre/immediate/delayed comprehension. | Timepoint/rubric version and missing reason. |
| item_confidence | nullable<float64> | 1 | Probability of correctness for exact item. | Range zero to one; missing not 0.5. |
| reading_context | record | s,1 | Time, accessibility and exposure conditions. | Burden/visual complexity/attrition metadata. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### NASA educational outreach evaluation framework

[Product, archive or reference](https://ntrs.nasa.gov/citations/20000033841)

**Fields:** Source claim ledger, article version, expert accuracy rubric, randomized condition, reading time, comprehension item scores and confidence

**Access:** Public reference or archive pointer. Original team measurements are not supplied. Confirm product-level access, version and license; a linked paper does not imply its raw data are downloadable.

**Role:** Comparison/model context; prospective measurement schema is listed separately.

### NASA Science Activation

[Product, archive or reference](https://science.nasa.gov/learn/about-science-activation/)

**Fields:** Independent benchmark metadata, reference assumptions and calibration context; select actual products before execution.

**Access:** Public reference or archive pointer. Original team measurements are not supplied. Confirm product-level access, version and license; a linked paper does not imply its raw data are downloadable.

**Role:** Comparison/model context; prospective measurement schema is listed separately.

## 6. Uncertainty, sensitivity and identifiability

Expert-rating disagreement, item difficulty, prior knowledge and reading context affect outcomes jointly. Attrition at the delayed interval can select more engaged readers and exaggerate retention. Source uncertainty is content to communicate, not merely measurement noise to remove from the article.

Block inference by reader and topic, analyze time/complexity covariates and test matched-claim sensitivity. Use held-out topics to assess generalization and missing-not-at-random scenarios for delayed responses. Examine calibration curves alongside Brier scores, retaining cases where comprehension improves but confidence becomes less calibrated.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Plain explanatory prose | Low production/reading overhead. | May leave abstract relationships unclear. | Baseline with full source/uncertainty trace. |
| Narrative/example format | Can support contextual understanding. | Engagement may outpace accuracy. | Select only after delayed and accuracy gates. |
| Source-linked visual/range format | Makes evidence/uncertainty accessible. | Visual complexity and accessibility burden. | Use when matched burden and calibration benefit survive holdout. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| F02-V1 | Matched-claim graph | Variants contain identical required claim IDs; omitted uncertainty fails content gate. | Set-equality and expert-review fixture. | Requirement R1/R2. |
| F02-V2 | Brier endpoints | p=y gives zero; opposite certainty gives one; p=0.5 gives 0.25. | Analytic item-scoring fixtures. | Probability algebra. |
| F02-V3 | Attrition/holdout | Missing delayed score remains missing; topic holdout does not reuse its outcomes for format choice. | Analysis integration fixture. | Data separation; reader results pending. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Proposed gate: no unsupported factual claims under blind expert review.
- Report comprehension change with interval, delayed retention and Brier score; control multiplicity.
- Hold out an entire topic to evaluate transfer and disclose recruitment bias.

## 9. Implementation and reproducible work packages

1. Create primary_source_claims.csv and article_claim_graph.json.
2. Draft matched article variants with immutable uncertainty statements.
3. Build blind_expert_accuracy_rubric.yaml and accessibility_burden_review.md.
4. Create consented_assignment_schema.json and preregistered_assessments.yaml.
5. Implement rubric_brier_scoring.py and reader_topic_effects.py.
6. Publish heldout_topic_attrition.ipynb and a findings template reporting negative calibration outcomes.

### Investigation sequence

1. Choose topics from this portfolio and produce audience-tested accessibility drafts.
2. Pilot comprehension questions for ceiling/floor effects and freeze analysis.
3. Run topic-stratified evaluation and release article templates with uncertainty-language examples.

### Resources and interfaces to expertise

- Science writer, subject specialists, educational evaluator and accessibility reviewer.
- Source ledger, survey platform, readability tools and controlled article versions.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| Facts differ across formats | Confounded writing effect. | Claim-set mismatch. | Source graph and equal content. |
| Confidence mispaired with item | Invalid calibration. | Item-key integrity audit. | Exact exposure/item IDs. |
| Delayed dropouts discarded | Inflated retention. | Attrition pattern report. | Missingness sensitivity and bounded conclusions. |

- Clicks or perceived clarity can rise while understanding falls.
- Removing uncertainty to simplify prose can mislead readers.

## 11. Required engineering outputs

- Versioned analysis configuration, raw-to-derived provenance and uncertainty report.
- Project-specific model comparison, a publication figure with units, and an explicit outcome including inconclusive findings.

### Scientific result figures to produce during execution

Format comparison of delayed comprehension and confidence calibration; source-to-claim map identifies what each sentence supports.

## 12. Cited technical and scientific resources

- [NASA educational outreach evaluation framework](https://ntrs.nasa.gov/citations/20000033841) — Evaluation design context.
- [NASA Science Activation](https://science.nasa.gov/learn/about-science-activation/) — Community engagement and independent evaluation context.
- [van der Bles et al., The effects of communicating uncertainty on public trust in facts and numbers](https://pmc.ncbi.nlm.nih.gov/articles/PMC7149229/) — Primary experimental study verified in this revision evaluates numerical/verbal uncertainty communication in article-like texts. It motivates explicit uncertainty-format testing but does not establish this project's retention or Brier-score effects.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
