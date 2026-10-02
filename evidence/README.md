# Evidence room

**Inspect what was checked, how it was checked, and where the claim stops.**

Start with the [detailed mission-profile verification](MISSION_PROFILE_VERIFICATION.md), [visual assembly verification](VISUAL_REVISION_VERIFICATION.md) and [release verification record](RELEASE_VERIFICATION.md). They distinguish executed documentation/software checks from the 434 specified project cases and pending empirical validation. Earlier revision records remain available here as dated evidence.

| Evidence | Open |
| --- | --- |
| Release scope and executed checks | [Release verification](RELEASE_VERIFICATION.md) |
| Complete project inventory and traceability | [Coverage audit](coverage_audit.json) |
| Independent engineering review | [Revision-2 review](INDEPENDENT_ENGINEERING_REVIEW.md) · [Earlier content review](INDEPENDENT_CONTENT_REVIEW.md) |
| Documentation and schema execution logs | [Portfolio results](portfolio_test_results.txt) · [Contract results](data_contract_test_results.txt) |
| Reduced-model verification and limits | [Numerical QA](NUMERICAL_QA_REVISION_2.md) · [Executed numerical results](numerical_test_results_revision_2.txt) |
| Scientific asset integrity and reproducibility | [Model verification](../models/verification.json) · [Recorded two-run regeneration](numerical_regeneration_verification.json) |
| Engineering diagram source/output integrity | [Architecture manifest](architecture_manifest.json) |
| Original document artwork and field-map integrity | [Visual design manifest](../assets/visual_design_manifest.json) |
| Equation rendering syntax | [Math render audit](math_render_audit.json) |
| Preserved ASTRA FORGE contribution | [Incoming review](INCOMING_REFERENCE_REVIEW.md) · [Asset integrity](incoming_asset_integrity.json) · [Reference test results](reference_library_test_results.txt) |

## Recheck the assembly

From the repository root:

```sh
python evidence/verify_portfolio.py
python evidence/verify_data_contracts.py
```

Use [model instructions](../models/README.md) for numerical checks and the [archive guide](../archive/README.md) for the supplementary kernels. A passing software or structural check does not establish measured model accuracy, qualified hardware or a successful project experiment. New execution evidence should retain input hashes, environment, methods, outputs and limits.

[Data gallery](../data/README.md) · [Engineering practice](../engineering/README.md) · [Research atlas](../research/README.md) · [Repository home](../README.md)
