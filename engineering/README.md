# Engineering practice

**The rules that make a model, dataset and claim reviewable.**

These shared procedures connect the 117 [research records](../research/README.md) to usable evidence. Start with the documentation standard, then follow the data, interface and assurance procedures applicable to the investigation.

| Guide | Use it to |
| --- | --- |
| [Documentation standard](ENGINEERING_STANDARD.md) | Define the design basis, required sections, review gates and evidence states |
| [Data management](DATA_MANAGEMENT.md) | Preserve selection, units, calibration, missingness, rights and transformation history |
| [Interface control](INTERFACE_CONTROL.md) | Freeze record shapes, frames, clocks, dimensional conventions and handoffs |
| [Model assurance](MODEL_ASSURANCE.md) | Match numerical verification and empirical validation to the intended decision |
| [Uncertainty and decision rules](UNCERTAINTY_AND_DECISION_RULES.md) | Propagate covariance, expose nonidentifiability and evaluate decision margins |
| [Execution roadmap](EXECUTION_ROADMAP.md) | Carry every A–I work package through review, implementation, verification and release |

## Follow the evidence

`Question → requirements → model → data contract → verification → validation → supported claim`

Each arrow requires a controlled artifact. A schema pass establishes structure; an analytical test checks declared mathematics; empirical validation needs independent evidence. Numerical targets in the project records remain proposed unless a controlling source identifies them otherwise.

[Research atlas](../research/README.md) · [Data gallery](../data/README.md) · [Evidence room](../evidence/README.md) · [Repository home](../README.md)
