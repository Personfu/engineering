# Independent scientific and editorial review

Reviewed on 2026-10-02. This is a proposal-quality review, not comprehensive expert peer review, experimental validation, flight qualification, clinical approval, or NASA certification.

## Scope and evidence

Inspected the summaries, hypotheses, full reduced-model fields, and data-access contracts of all 117 dossiers across Sessions A–I. Examined selected difficult models more closely: Pluto phase equilibrium, neutron-star pairing, radio luminosity conventions, gravitational-wave memory, interferometer thermal noise, shock energy flux, lunar magnetic inversion, carbon-isotope mixing, regeneration-state bookkeeping, ephemeris potential conventions, and reaction-wheel control. Read the complete execution/validation material for selected biological, remediation, aviation-governance, propulsion-surrogate, and spacecraft-console dossiers. Inspected `work/build_portfolio.py` and `work/render_explorer.py` for schema, path, escaping, and rendering assumptions.

An independent run of the assembler's read/validation stage passed: 117 unique IDs, 117 unique mission names, required model fields, at least two scientific resource pointers per dossier, and exact original-title equality against `work/input_projects.json`. Counts are A=12, B=28, C=30, D=7, E=8, F=2, G=8, H=9, I=13. The combined D03 entry retains autorotation and separation-bubble research as distinct work packages.

Primary-source spot checks confirmed that the July 2026 consumer-CMOS detector citation exists and is appropriately limited to detection feasibility; the EZ CMa paper supports a preferred CIR interpretation with remaining binary uncertainty; and TRINITY supplies population connections rather than a native temporal-variability model. Sources checked: [Takano et al.](https://arxiv.org/abs/2607.02106), [Barclay et al.](https://arxiv.org/abs/2310.15986), and [Zhang et al.](https://arxiv.org/abs/2105.10474). This review did not independently verify every URL, download every archive product, or reproduce every cited paper.

## Findings addressed during review

The assembly owner applied the corrections below to the source dossiers. Corrected formulas and definitions were reread. These findings are retained as a change record rather than unresolved defects.

| Dossier | Issue | Corrected model or wording |
|---|---|---|
| B07 | Summed parent/product analyte mass is not conserved across molecular transformations; it cannot establish mineralization. | Use a stoichiometrically balanced molar reaction network and carbon-atom inventories: `n_C,recovered = sum_i N_C,i*(C_i*V+S_i*m_soil)/MW_i + n_C,gas + n_C,biomass`, after explicit mg-to-g conversion. Report unresolved pools and element-specific closure. |
| B02 | A probability multiplied by unconstrained habitat quality could exceed one. | Specify `h_j in [0,1]`, `lambda>0`, and `d>=0` for `p_ij=exp(-d/lambda)*h_j`. |
| B13 | False-positive subtraction must use the same inverse-detection weighting as detected objects. | Use `N_hat = sum_detected_j P(true_j|independent validation,features_j)/p_detect,j`, propagating both calibrations and their uncertainty. |
| C15 | The photon-count expression omitted collecting area while naming the input a spectral flux. | Add `A_tel` and define `F_lambda` in W m^-2 m^-1, with throughput including pixel-assignment probability. |
| C28 | The throughput definition could include atmosphere twice. | Define `T_sys` as optics, filter, and detector response excluding atmosphere; apply `T_atm` once as a separate factor. |
| E01 | A finite susceptible-site count requires a bounded count distribution. | Use `Binomial(N_target,1-exp(-k*H_UV))`; restrict the Poisson approximation to rare breaks and retain independence/overdispersion caveats. |
| E07 | At-least-one-module availability did not represent the stated two-of-three science-return requirement. | Add `A_>=2=A1*A2+A1*A3+A2*A3-2*A1*A2*A3` for independent module availability, retaining a common-cause fault-tree alternative. |
| H03 | The source-only resolution matrix omitted jointly fitted external-field nuisance terms. | Use covariance-weighted nuisance projection before forming source resolution; retain rank, pseudoinverse, gauge, and source-constraint caveats. |
| H09 | The posterior over competing models omitted its model prior. | Include `p(M)` and require prior-sensitivity reporting. |
| G04 | Darcy permeability and viscosity units were unspecified and could conflate intrinsic permeability with hydraulic conductivity. | Specify intrinsic `k` in m², fluid viscosity in Pa s, pressure in Pa, and Darcy flux in m/s. |
| C29 | Shock-normal terminology said “copolarity.” | Correct to “coplanarity.” |
| I10 | Electrical input including losses was called wheel energy, potentially implying stored kinetic energy. | Define `E_elec` as cumulative electrical energy consumed and `dE_elec/dt=P_elec`; distinguish stored wheel kinetic energy. |
| I12 | The physical velocity scale appeared as an ambiguous “an.” | Write the dimensional scale as `a*n`. |

## Data, interpretation, and scope

No fabricated project measurements or completed-flight claims were identified in the inspected material. Data contracts consistently distinguish archive discovery pointers, public papers, proposed measurements, generated fixtures, and original student-team data that have not been supplied. Target-specific product availability, accessions, calibration files, covariance, licenses, and permissions remain explicit execution prerequisites. A reference pointer is not itself an acquired dataset or a completed analysis.

The models generally expose identifiability and selection limits: faint-source radio power versus AGN existence; stellar-tracer dispersion versus dark-matter dispersion; CMOS deposited versus incident particle energy; LyC proxies versus direct escape measurements; absolute sky residuals versus cosmological claims; and effective grain size versus geological particle diameter. Staged validation usually holds out physical objects, observing periods, sites, or simulation families rather than near-duplicate realizations.

Selected biological projects remain literature/computational or nonclinical assessment specifications. The P66 and microgravity antimicrobial-resistance dossiers contain no pathogen cultivation, selection, manipulation, or enhancement procedures. Aviation-ISAC work uses defensive governance and benign synthetic exercises. The CatSat console uses isolated simulated events; it does not authorize live spacecraft interaction. Rocket-related proposals use externally supplied load envelopes and inert thermal/structural surrogates, without a firing sequence or engine build package.

## Assembly and explorer checks

All current `data` URLs use HTTPS; all required arrays and visual dictionaries match the renderer's actual expectations. IDs and session values match the controlled inventory, so generated dossier/visual paths remain in the expected repository subdirectories. SVG text is escaped; browser text and URL attributes are escaped before insertion. The inline catalog replaces `<` with JSON Unicode escapes, preventing embedded closing-script text while retaining comparison operators after JSON parsing. A constructed closing-script payload round-tripped correctly through this encoding.

No present HTML-escaping, path, or schema blocker was identified in the current controlled catalog. This was a static code/schema review plus a targeted JSON-encoding check, not a live browser accessibility or visual-layout evaluation. Browser interaction and generated-file verification are performed separately by the assembly owner. The conceptual SVGs show analysis dependencies; they must not be described as observed results or calibrated engineering drawings.

## Remaining limitations

No unresolved publication-blocking mathematical or scope defect was found within this review's coverage after the listed corrections. This does not establish that every equation is production-ready or every proposed scientific extension is novel. Specialist reviews, product-level data acquisition, numerical implementation, empirical validation, and mission-specific requirements remain necessary before executing these proposals. Most “full models” in the portfolio are explicitly reduced or schematic models with a path to higher fidelity. Their cited resources and proposed gates support research planning; they do not supply completed experiments or NASA endorsement.
