# B21 · PROTEUS DRIFTSCAPE — Evolutionary Protein Disorder

**Original project:** More Effectively Selective Species Have Greater Protein Structural Disorder

**Session B:** Earth & Environmental Engineering

**Document class:** engineering research design and analysis record · **Revision:** 3 · **Date:** 2026-10-02

**Evidence state:** design basis, mathematical formulation and verification plan documented. Project-specific empirical results remain to be acquired; executable shared model demonstrations have their own recorded checks.

[Session B](../README.md) · [All projects](../../../ENGINEERING_DOCUMENTATION.md) · [Session handbook](../../../handbooks/SESSION_B.md) · [← B20](../B20-lunar-reclaimer-algal-rare-earth-recovery/README.md) · [B22 →](../B22-nif-odyssey-comparative-nitrogen-fixation-evolution/README.md)

| Proposed requirements | Specified verification cases | Defined data fields | Cited resources |
| ---: | ---: | ---: | ---: |
| 4 | 4 | 8 | 2 |

[Explore the data blueprint](data/README.md) · [Open the figure gallery](figures/README.md) · [Download acquisition template](data/acquisition.csv) · [Browse the data atlas](../../../data/README.md)

---

## Purpose and scientific objective

Test the comparative association between selection efficacy and predicted intrinsic disorder using homologous domains and phylogenetically controlled statistics. Reproduce the published corrected codon-bias framework before extending it to new vertebrate clades. Distinguish predicted disorder, measured structure and mutational robustness; none is a direct synonym for another.

**Question:** Does greater selection efficacy predict disorder within homologous protein domains after GC, composition, domain age and phylogeny are controlled?

**Testable hypothesis:** A positive association may persist in matched domains, but predictor calibration, amino-acid composition and shared ancestry could explain part of the cross-species signal.

## 1. Design basis and analysis boundary

The comparative system tests selection-efficacy and predicted disorder associations within homologous protein domains across versioned vertebrate proteomes. Its boundary includes sequence/domain identity, a faithful implementation of the published corrected codon-bias framework, disorder prediction and phylogenetic inference. Predicted disorder, experimentally measured structure and mutational robustness remain distinct endpoints.

Begin by reproducing the primary study's species/domain summary calculations before extending clade coverage. Domain-matched analyses precede whole-proteome averages, which can change through domain composition alone. CAIS normalization must come from the published method/code rather than a newly invented KL proxy. Predictor thresholds, sequence exclusions and clade holdouts are proposed analysis settings, with annotation and composition bias carried into inference.

## 2. Requirements and verification traceability

These are project design requirements or proposed analysis gates. A numerical target is not a NASA requirement unless its controlling source is explicitly identified. “TBD” identifies evidence required before a decision; it is not permission to assume a value. Verification evidence listed here is planned, unless a linked result explicitly records execution.

| ID | Requirement / gate | Engineering rationale | Verification method | Basis / required evidence |
| --- | --- | --- | --- | --- |
| B21-R1 | Freeze proteome, coding-sequence, domain and phylogeny releases with one-to-one identifiers and taxon crosswalks. | Annotation changes can mimic species effects. | Checksum and join-completeness audit. | UniProt documentation. |
| B21-R2 | Reproduce published CAIS normalization exactly on available author benchmarks; proposed numerical tolerance is 10^-8 for identical inputs. | Conceptual codon divergence is not the complete published index. | Reference-vector comparison. | Primary study; proposed computational tolerance. |
| B21-R3 | Separate within-homologous-domain association from changes in domain composition and sequence length. | Proteome mixtures confound comparative effects. | Matched-domain and aggregate decomposition. | Primary comparative context. |
| B21-R4 | Validate across complete clades and multiple supported disorder predictors; thresholds shall be chosen within training analyses. | Related species and predictor biases inflate certainty. | Clade split and predictor-sensitivity audit. | Proposed generalization protocol. |

## 3. Architecture and controlled interfaces

A sequence registry links coding sequences, translated proteins and domain intervals to versioned taxon identifiers. Alignment QC records coverage, gaps and paralog ambiguity. A CAIS adapter implements the primary study's amino-acid/GC correction and retains each intermediate frequency table.

Disorder engines emit per-residue probabilities on original sequence coordinates and masks for unsupported regions. A homologous-domain summarizer stores counts and threshold-sensitive fractions, while a phylogeny adapter emits branch-length covariance in substitutions/site conventions. The comparative estimator uses matched domains, composition covariates and species-related random effects. Missing orthologs and uncertain domain boundaries propagate exclusion/sensitivity states, rather than being imputed as ordered protein.

![B21 engineering architecture](figures/architecture.svg)

The diagram establishes sequence lineage, faithful efficacy-index calculation and homologous-domain comparison with phylogenetic covariance. Its endpoint is predicted disorder association, not measured structure or causal evolutionary advantage.

[Editable engineering diagram source](figures/architecture.mmd)

## 4. Mathematical model and derivation

### Governing equations

```text
D_KL(p||q)=Σ_c p_c log(p_c/q_c), conceptual codon-divergence term; implement published CAIS normalization exactly.
```

```text
Disorder_fraction=Σ_residue I(score>threshold)/L, with threshold sensitivity.
```

```text
logit(DomainDisorder_ds)=α_d+β Efficacy_s+γᵀ covariates_ds+phylogenetic_effect_s+ε_ds.
```

### Variables, units and conventions

- Efficacy: published corrected codon-bias index, dimensionless; not census size.
- L: homologous-domain residues; disorder fraction: 0–1.
- GC/composition: fractions; phylogeny: branch lengths with documented units.
- β: conditional comparative association, not a causal fitness coefficient.

### Assumptions and boundary conditions

- Homology/alignment quality must be reviewed.
- Disorder predictors may inherit composition/training biases.
- Effective population size proxies and selection efficacy need not coincide.

### Derivation step 1

```text
D_KL(p||q)=sum_c p_c log(p_c/q_c).
```

This is a conceptual codon-divergence component, not a substitute for the complete published CAIS correction. Zero-frequency handling and amino-acid weighting must follow the source implementation.

### Derivation step 2

```text
d_ds=sum_(valid residues) I(score>tau); D_ds=d_ds/L_valid.
```

Disorder fraction is dimensionless. The threshold tau is declared, and gaps/unknown residues are excluded consistently rather than counted as ordered.

### Derivation step 3

```text
d_ds~Binomial(L_valid,p_ds); logit p_ds=alpha_d+beta E_s+gamma^T X_ds+u_s.
```

E is the published efficacy proxy, not census population size. The binomial working model needs overdispersion for correlated residues.

### Derivation step 4

```text
u~Normal(0,sigma_phylo² C_tree); Var(beta_hat) uses phylogenetic covariance.
```

Shared branch history induces covariance among species. Predictor/annotation uncertainty adds further terms rather than increasing the number of independent taxa.

### Inference or simulation procedure

Freeze proteome/domain versions, reproduce CAIS and control GC/amino-acid effects according to the primary study. Compare multiple disorder predictors and homologous-domain matched effects using phylogenetic mixed models. Partition within-domain versus changing-domain-composition explanations, propagate alignment/predictor uncertainty and reserve clades for out-of-sample testing. Include negative-control sequence shuffles preserving composition and assess whether an association reflects biology or predictor construction.

### Validity domain and fidelity limits

Predictions cannot establish experimental disorder or adaptive mechanism. Clade sampling and annotation quality vary; selection-efficiency proxies require explicit calibration and cannot infer fitness advantages alone.

## 5. Data specifications and provenance

![B21 proposed data contract: field names, types, units and meanings](figures/data-map.svg)

**Proposed data contract · observations pending.** This visual inventory shows the record fields to acquire or derive. It contains no project measurements. [Open the data blueprint and downloads](data/README.md).

| Field | Type | Unit | Physical / statistical meaning | Quality and missing-data rule |
| --- | --- | --- | --- | --- |
| taxon_key | string | none | Versioned species/proteome identity. | Stable crosswalk and release required. |
| domain_key | string | none | Homologous domain family/interval. | Paralog and boundary uncertainty saved. |
| coding_sequence | sequence key | codons | Source coding-sequence reference. | Translation and frame consistency checked. |
| cais_value | nullable float | dimensionless | Published corrected efficacy index. | Exact method/intermediates retained. |
| disorder_scores | nullable float[] | 0–1 | Per-residue predictor outputs. | Predictor version and invalid masks required. |
| valid_length | integer | residues | Eligible domain positions. | Gaps/unknowns excluded consistently. |
| tree_covariance | matrix | declared branch units | Species shared-ancestry structure. | Taxon order and PSD check required. |
| association_interval | float[3] | logit per index | Conditional comparative effect. | Include clade/predictor uncertainty. |

[Machine-readable record schema](data/schema.json) · [Empty acquisition CSV](data/acquisition.csv) · [Field dictionary CSV](data/dictionary.csv)

The CSV above contains column headers only. Its schema defines future records and does not establish that original-team data or a particular archive product have been acquired. Frame, timing, calibration, covariance, selection and provenance details must accompany populated records.

### Protein domains in vertebrate species with more effective selection have greater intrinsic disorder

[Product, archive or reference](https://pmc.ncbi.nlm.nih.gov/articles/PMC11379457/)

**Fields:** Published domain/proteome analysis, CAIS definition and linked data.

**Access:** Open primary article; freeze associated data/code releases.

**Role:** Reproduction and hypothesis benchmark.

### UniProt proteome documentation

[Product, archive or reference](https://www.uniprot.org/help/proteome)

**Fields:** Proteome identities, sequences and annotation metadata.

**Access:** Public UniProt; record release/version, completeness and license.

**Role:** Independent or expanded comparative sequence inputs.

## 6. Uncertainty, sensitivity and identifiability

GC composition, amino-acid makeup and domain annotation can drive both efficacy proxies and predictor outputs. Reproduce correction steps, then compare domain-matched and composition-adjusted effects. Label alignment gaps and paralogs explicitly. Composition-preserving shuffled controls test predictor sensitivity, while not proving that real sequence-order effects are artifactual.

Phylogenetic sampling and predictor training overlap reduce effective independence. Vary plausible trees, use clade-level holdouts and compare predictor ensembles. Domain boundaries and threshold choices induce correlated fraction errors. Profile efficacy/composition coefficients and report weakly identified combinations; a stable association cannot establish causal fitness benefit or experimentally verified protein disorder.

## 7. Engineering trade study

| Alternative | Benefit | Cost / limitation | Decision rule |
| --- | --- | --- | --- |
| Whole-proteome fractions | Simple broad species summary. | Confounded by domain mixture and length. | Use as descriptive baseline. |
| Matched-domain phylogenetic model | Controls homology and relatedness. | Incomplete orthologs reduce sample support. | Preferred inferential design. |
| Multiple predictor/threshold ensemble | Exposes prediction-method dependence. | Agreement is not experimental structure truth. | Use as uncertainty and robustness layer. |

## 8. Verification and validation cases

| Case ID | Stimulus / condition | Expected result / criterion | Method | Evidence artifact |
| --- | --- | --- | --- | --- |
| B21-V1 | Identical codon distributions | Conceptual KL divergence equals zero. | Condition/fixture: p=q with valid positive support. Verification procedure: Exact frequency-table test.. | Exact frequency-table test. |
| B21-V2 | Fraction fixture | D=0.25. | Condition/fixture: Five disordered valid residues out of twenty. Verification procedure: Independent summary arithmetic.. | Independent summary arithmetic. |
| B21-V3 | Zero phylogenetic covariance | Model reduces to the corresponding nonphylogenetic working model. | Condition/fixture: Set sigma_phylo=0 in synthetic data. Verification procedure: Likelihood comparison.. | Likelihood comparison. |
| B21-V4 | Clade holdout | Report calibrated predictions and coefficient stability across predictors. | Condition/fixture: Reserve complete clades and homologous domain groups. Verification procedure: Blocked comparative evaluation.. | Blocked comparative evaluation. |

**Execution status:** these cases are specified, not claimed as executed. Close a case only with the versioned inputs, output, uncertainty, reviewer and pass/fail rationale.

### Additional scientific validation gates

- Hold out entire clades/domains; avoid splitting homologous records as independent samples.
- Run composition-preserving negative controls and alignment-quality sensitivity.
- Report effect intervals, out-of-clade calibration and agreement across predictors; reserve experimental structure evidence for separate validation.

## 9. Implementation and reproducible work packages

1. Freeze sequence/domain/tree manifests and taxon/translation crosswalks.
2. Implement the exact published CAIS workflow with benchmark intermediates.
3. Run supported disorder predictors with original-coordinate masks.
4. Build matched-domain counts and composition/length covariates.
5. Fit phylogenetic/overdispersed models and clade/predictor sensitivity artifacts.
6. Release association evidence with annotation, prediction and causal limitations.

### Investigation sequence

1. Stage 1: reproduce published index/domain analyses and audit sequence/alignment coverage.
2. Stage 2: compare phylogenetic, composition and predictor alternatives with uncertainty-aware domain matching.
3. Stage 3: evaluate held-out clades and release a reproducible association atlas with predictor limitations.

### Resources and interfaces to expertise

- Evolutionary geneticist, protein-bioinformatics specialist and statistical reviewer.
- Versioned proteomes/domains, phylogenies, predictors and published CAIS code.

## 10. Failure modes and interpretation controls

| Failure mode | Effect on result | Detection / evidence | Design response |
| --- | --- | --- | --- |
| Conceptual KL labeled CAIS | Invalid efficacy measurement. | Compare source intermediate calculations. | Faithful published implementation. |
| Predictions called measured structure | Unsupported biological claim. | Endpoint/citation audit. | Retain predicted-disorder language. |
| Residues treated independent species | Overconfident association. | Effective sample and covariance review. | Phylogenetic/domain blocking. |

- Shared ancestry and annotation bias.
- Composition-driven predictor artifacts.
- Conflating disorder, robustness and organismal adaptation.

## 11. Required engineering outputs

- Reproduction notebook and comparative-data manifest.
- Phylogenetic association/negative-control results.
- Domain/clade atlas with uncertainty and annotation gaps.

### Scientific result figures to produce during execution

Show domain-matched disorder contrasts on a phylogeny and effect intervals across predictors, clades and negative controls.

## 12. Cited technical and scientific resources

- [Protein domains in vertebrate species with more effective selection have greater intrinsic disorder](https://pmc.ncbi.nlm.nih.gov/articles/PMC11379457/) — Primary comparative study defines the association being tested; predicted disorder is not experimental confirmation of structure.
- [UniProt proteome documentation](https://www.uniprot.org/help/proteome) — Official sequence/proteome definitions and release metadata support versioned comparative inputs.

Framework and evidence rules: [engineering documentation standard](../../../engineering/ENGINEERING_STANDARD.md), [model assurance](../../../engineering/MODEL_ASSURANCE.md), [uncertainty procedure](../../../engineering/UNCERTAINTY_AND_DECISION_RULES.md), [data management](../../../engineering/DATA_MANAGEMENT.md). NASA-inspired names are creative identifiers; requirements and results are not NASA certification.
