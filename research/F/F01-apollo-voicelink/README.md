# F01 · APOLLO VOICELINK

**Original project:** Communication and Exploration

**Session F:** Education & Public Outreach

**Document class:** engineering research design and analysis record · **Revision:** 3 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session F](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_F.md) · [← E08](../../E/E08-gateway-powerbench/README.md) · [F02 →](../F02-discovery-quill/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 4 | 3 | 7 | 3 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Purpose and scientific objective

Preserve Communication and Exploration as a crew teamwork research project. Study multicultural communication and delayed ground contact using consented analog tasks and mixed qualitative/quantitative evidence. The ambition is an adaptive communication protocol that is evaluated on shared task understanding, workload and repair time while respecting cultural and language differences.

**Question:** Which communication practices improve shared task understanding and recovery from misunderstanding under delayed, text-based exploration communication?

**Testable hypothesis:** Structured confirmation and context summaries will reduce unresolved ambiguities without imposing an unacceptable workload penalty, with effects varying by task and crew.

## 1. Design basis and analysis boundary

The engineering system is a consented analog-teamwork study of delayed text communication, shared task understanding and misunderstanding recovery across contextual language/cultural settings. Its boundary includes task/rubric design, message-delivery simulator, protocol assignment, coding and privacy-controlled evidence. Cultural categories describe context and experience, never deterministic participant traits or inherent ability.

Begin with a preregistered crossover comparison and independently scorable analog tasks, then mixed-effects timing/success analysis plus qualitative negative cases. Delay and task order are controlled. Findings are bounded to the participant/task sample; they cannot be transferred directly to ISS crew performance or used to rank cultures.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| F01-R1 | Every success/repair event shall link to a preregistered task rubric and blinded coder evidence. | Subjective impression can favor a preferred protocol. | Codebook audit and blind rescoring. | Analog evaluation requirement. |
| F01-R2 | Crossover assignment shall retain order, practice, task complexity and team clustering. | Learning/carryover can imitate protocol benefit. | Design-rank and order-interaction checks. | Proposed study design, not conducted recruitment. |
| F01-R3 | Sensitive transcripts shall use consented access, pseudonymous team IDs and minimum contextual metadata. | Communication evidence can expose identities. | Inspect planned access/redaction and consent provenance. | Human-subjects boundary; review required before collection. |
| F01-R4 | Proposed benefit criterion: improved task success/resolution with no supported subgroup deterioration under uncertainty. | Aggregate averages can conceal unequal usability. | Team-level interval and context interaction review. | Proposed interpretation gate; no outcome claimed. |

## 3. Architecture and controlled interfaces

A task registry defines objective states, complexity and acceptable repair outcomes. A local communication simulator timestamps sender creation, queued delivery and acknowledgment, separating imposed delay from human resolution time. Protocol variants provide message/checkback structure without changing task information.

A pseudonymous evidence store links consented messages to coded misunderstanding episodes. Independent coders retain disagreement and interview themes. Mixed-effects modules include team, order and language-context variables; qualitative analysis retains discordant cases rather than forcing numerical consensus. Outputs aggregate at appropriate team/context levels and preserve sample limits.

![F01 engineering architecture](figures/architecture.svg)

Objective analog tasks and controlled delays feed independent coding and clustered analysis. Context and negative cases limit generalization; no result is a direct ISS prediction or a ranking of cultures.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

```text
logit(P_success)=beta0+beta1*protocol+beta2*delay+beta3*language_context+u_team
```

```text
T_resolution ~ lognormal(mu,sigma)
```

```text
kappa=(p_observed-p_chance)/(1-p_chance)
```

### Variables, units and conventions

- Delay and resolution time s; success binary with independently defined rubric
- u_team random team effect; beta coefficients estimated
- kappa agreement statistic; not a substitute for qualitative interpretation

### Assumptions and boundary conditions

- Participants consent; identity and sensitive transcripts are controlled, with institutional human-subjects review.
- Analog-task findings are not direct ISS crew-performance predictions.

### Derivation step 1

$$
logit(P_{success})=\beta_0+\beta_pP+\beta_dD+\beta_cC+u_{team}
$$

P is assigned protocol, D declared delay and C contextual variables. Coefficients describe conditional associations under the design; random team effects handle repeated episodes.

### Derivation step 2

$$
\ln T_{resolution}\sim N(\mu,\sigma^2)
$$

Positive times motivate lognormal modeling. Unresolved tasks are right-censored, while imposed transmission delay is recorded separately rather than silently counted as participant confusion.

### Derivation step 3

$$
\kappa=(p_o-p_e)/(1-p_e)
$$

Chance agreement p_e derives from coder marginal labels. When p_e=1 kappa is undefined; prevalence effects mean raw agreement and disagreement examples remain necessary.

### Derivation step 4

$$
\Delta_{protocol}=E[Y\mid P=1,design]-E[Y\mid P=0,design]
$$

Estimate design-adjusted contrasts rather than treating logistic coefficients as probability differences. Crossover/order effects and contextual interactions determine which comparisons are interpretable.

### Inference or simulation procedure

Preregister a crossover analog comparison with order effects, task complexity and team clustering. Combine coded interviews with objective ambiguity-resolution events; keep discordant themes and negative cases. Assess whether protocol benefits are shared across groups rather than maximizing an aggregate success metric.

### Validity domain and fidelity limits

Small crew counts limit inference. Cultural categories are contextual and should not be treated as deterministic participant traits.

## 5. Data specifications and provenance

![F01 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| team_id | string | 1 | Pseudonymous clustered team key. | Identity mapping outside analysis; consent status required. |
| task_id | string | 1 | Versioned analog task/rubric. | Difficulty and crossover order retained. |
| protocol_assignment | enum | 1 | Communication structure condition. | Randomization/carryover record required. |
| message_times | record | s | Create/deliver/acknowledge simulator times. | Clock and imposed-delay separation. |
| context_metadata | nullable<record> | 1 | Consented language/experience context. | Minimum necessary; no deterministic cultural labeling. |
| repair_outcome | record | bool,s | Rubric success and resolution/censoring. | Coder IDs and evidence links retained. |
| code_agreement | record | 1 | Independent labels/agreement summary. | Disagreement and undefined metrics retained. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### NASA delayed team communication research

[Product, archive or reference](https://techport.nasa.gov/projects/23197)

**Fields:** Consented deidentified task rubric, communication condition, message/event timestamps, workload responses, coder decisions and participant-approved themes

**Access:** Public reference or archive pointer. Original team measurements are not supplied. Confirm product-level access, version and license; a linked paper does not imply its raw data are downloadable.

**Role:** Comparison/model context; prospective measurement schema is listed separately.

### NASA educational outreach evaluation framework

[Product, archive or reference](https://ntrs.nasa.gov/citations/20000033841)

**Fields:** Independent benchmark metadata, reference assumptions and calibration context; select actual products before execution.

**Access:** Public reference or archive pointer. Original team measurements are not supplied. Confirm product-level access, version and license; a linked paper does not imply its raw data are downloadable.

**Role:** Comparison/model context; prospective measurement schema is listed separately.

## 6. Uncertainty, sensitivity and identifiability

Small team counts, task difficulty, practice effects and shared participants create correlated observations. Language/context variables may overlap with prior teamwork experience and cannot be interpreted as causal cultural traits. Coder ambiguity and censored failures affect both numerical and qualitative evidence.

Use team-block bootstrap or hierarchical intervals and test protocol-by-context/order interactions without opportunistic subgroup claims. Compare censored-time models and coder definitions. Hold out tasks or teams, retain negative cases and triangulate objective repair events with interviews; uncertainty may support an unresolved protocol comparison.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Unstructured text | Natural baseline. | Ambiguity and repair overhead. | Retain with equal task information. |
| Structured checkback protocol | Explicit shared understanding. | Extra message burden or awkward context fit. | Choose if success/time and usability gate improve. |
| Adaptive team-negotiated protocol | May fit diverse contexts. | Assignment/fidelity harder to compare. | Study separately with documented adaptations. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| F01-V1 | Simulator delay | Delivered timestamp minus send timestamp equals imposed delay before jitter. | Deterministic queue fixture. | Communication interface. |
| F01-V2 | Coder endpoints | Identical nondegenerate labels yield kappa one; all-one marginals produce undefined denominator. | Synthetic codebook fixtures. | Agreement algebra. |
| F01-V3 | Crossover confounding | Protocol perfectly aligned with order triggers aliasing; balanced design permits separate effects. | Known design-matrix fixtures. | Identifiability; study outcomes pending. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Proposed gate: report paired task-completion difference and uncertainty plus workload tradeoff, not a single ranking.
- Double-code a subset and investigate disagreement; retain participant feedback on interpretation.
- Analyze team-level resampling and order/carryover effects; null findings remain valid.

## 9. Implementation and reproducible work packages

1. Create analog_task_rubric.yaml and preregistered_design.json.
2. Build delayed_text_simulator.py with deterministic queue tests.
3. Create consent_access_plan.md and pseudonymous_evidence_schema.json before participant work.
4. Implement codebook_and_agreement.py with undefined cases.
5. Build mixed_effects_success_time.py and censored-time analysis.
6. Publish team_task_holdout.ipynb and a contextual findings template retaining negative cases.

### Investigation sequence

1. Co-design culturally sensitive tasks and an ambiguity-resolution rubric.
2. Pilot the protocol, blind coding where possible and estimate team-level variance.
3. Use held-out teams for confirmatory evaluation and release only consent-compatible derived summaries.

### Resources and interfaces to expertise

- Human-factors researcher, qualitative analyst and participant/community advisor.
- Analog task platform, delay emulator, transcription/coding tools and protected research storage.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| Delay counted as misunderstanding | Biased time interpretation. | Stage-timing audit. | Separate transport and human repair clocks. |
| Culture treated fixed ability | Unsupported harmful inference. | Interpretation/context review. | Contextual variables and within-design limits. |
| Discordant cases removed | False protocol consensus. | Evidence ledger discrepancy. | Retain coder/qualitative negative cases. |

- Reidentification and cultural stereotyping can harm participants.
- A protocol that improves speed may worsen trust or workload.

## 11. Required engineering outputs

- Versioned analysis configuration, raw-to-derived provenance and uncertainty report.
- Project-specific model comparison, a publication figure with units, and an explicit outcome including inconclusive findings.

### Scientific result figures to produce during execution

Paired task outcomes and resolution-time distributions with annotated qualitative themes; no individual performance leaderboard.

## 12. Cited technical and scientific resources

- [NASA delayed team communication research](https://techport.nasa.gov/projects/23197) — Analog research context for communication protocols.
- [NASA educational outreach evaluation framework](https://ntrs.nasa.gov/citations/20000033841) — Evaluation design context.
- [Examination of Communication Delays on Team Performance: Utilizing the ISS as a Test Bed for Analog Research](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20110023266.pdf) — Primary NASA research presentation verified in this revision establishes delayed-team communication/autonomy as a study context. It does not prove a universal protocol effect or multicultural ranking.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
