# I10 · Figure gallery

[GEMINI POINTLOCK](../README.md) · [Data blueprint](../data/README.md) · [Data diagnostic gallery](../../../../data/figures/README.md)

## Engineering architecture

![Engineering architecture](architecture.svg)

Opposite wheel/body torque and momentum limits close the control loop; electrical consumption and wheel kinetic energy remain separate measured/model interfaces.

[SVG](architecture.svg) · [Editable Mermaid source](architecture.mmd)

## Data blueprint

![Proposed data contract](data-map.svg)

**Proposed contract · observations pending.** Every field, type, unit and meaning comes from the controlled dictionary. [Open SVG](data-map.svg) · [Download dictionary](../data/dictionary.csv)

## Mission profile

![Engineering mission profile](mission-profile.svg)

The scientific question, hypothesis, model boundary and document metadata are drawn from controlled sources. Proposed work remains distinguished from acquired evidence. [Open SVG](mission-profile.svg)

## Data diagnostic

![I10 data diagnostic](../../../../data/figures/13_attitude_phase_and_authority.svg)

Synthetic one-axis PD attitude response and actuator authority. The phase portrait is colored by elapsed model time. Requested torque is reconstructed from the recorded states and sidecar gains; the applied torque is clipped to ±8 mN·m. The right panel focuses on the first 40 seconds, while the phase portrait uses the full 120-second record.

[SVG](../../../../data/figures/13_attitude_phase_and_authority.svg) · [PNG](../../../../data/figures/13_attitude_phase_and_authority.png) · [Figure provenance](../../../../data/figures/13_attitude_phase_and_authority.provenance.json)

## Original numerical view

![I10 included numerical demonstration](../../../../models/figures/06_one_axis_attitude.svg)

[Model formulation, data, assumptions and executed numerical checks](../../../../models/README.md)

## Planned scientific result

Angle command and calibrated response above wheel momentum, torque saturation, and uncertainty; polar error plots cover the full tested one-axis range.

This final scientific result remains an execution deliverable; the design diagrams do not establish an empirical finding.
