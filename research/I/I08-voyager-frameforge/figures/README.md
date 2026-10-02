# I08 · Figure gallery

[VOYAGER FRAMEFORGE](../README.md) · [Data blueprint](../data/README.md) · [Data diagnostic gallery](../../../../data/figures/README.md)

## Engineering architecture

![Engineering architecture](architecture.svg)

State provenance and gravity inputs remain independent; model-domain checks precede correctness and performance comparisons.

[SVG](architecture.svg) · [Editable Mermaid source](architecture.mmd)

## Data blueprint

![Proposed data contract](data-map.svg)

**Proposed contract · observations pending.** Every field, type, unit and meaning comes from the controlled dictionary. [Open SVG](data-map.svg) · [Download dictionary](../data/dictionary.csv)

## Mission profile

![Engineering mission profile](mission-profile.svg)

The scientific question, hypothesis, model boundary and document metadata are drawn from controlled sources. Proposed work remains distinguished from acquired evidence. [Open SVG](mission-profile.svg)

## Data diagnostic

![I08 data diagnostic](../../../../data/figures/14_orbit_conservation_and_refinement.svg)

Synthetic two-body conservation and refinement diagnostics from immutable model outputs. Panel A scales relative specific-energy error to parts per million and reports angular-momentum conservation for the stored 400-step-per-period run. Panel B compares three recorded maximum-energy errors with a second-order reference anchored to the coarsest run. This is an integration check, not trajectory prediction validation.

[SVG](../../../../data/figures/14_orbit_conservation_and_refinement.svg) · [PNG](../../../../data/figures/14_orbit_conservation_and_refinement.png) · [Figure provenance](../../../../data/figures/14_orbit_conservation_and_refinement.provenance.json)

## Original numerical view

![I08 included numerical demonstration](../../../../models/figures/07_two_body_convergence.svg)

[Model formulation, data, assumptions and executed numerical checks](../../../../models/README.md)

## Planned scientific result

A provenance diagram beside state-residual plots and a radial gravity-model disagreement map, with convergence boundaries and reference conventions labeled.

This final scientific result remains an execution deliverable; the design diagrams do not establish an empirical finding.
