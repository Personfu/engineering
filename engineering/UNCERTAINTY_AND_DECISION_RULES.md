# Uncertainty and engineering decision rules

Every project must connect uncertainty to its particular engineering decision. The annexes identify domain-specific contributors; this document defines the common calculation and reporting procedure. Measurement uncertainty, stochastic variability, numerical error, and model discrepancy remain separate until a defensible combination is established.

## Measurement model and covariance

For an output vector derived from inputs, write

$$
\mathbf y=f(\mathbf x,\boldsymbol\theta)+\boldsymbol\delta,
\qquad \mathbf J=\partial f/\partial(\mathbf x,\boldsymbol\theta).
$$

The discrepancy term represents missing physics, unresolved population effects or instrumentation behavior; it is not automatically independent white noise. A first-order propagated covariance is

$$
\boldsymbol\Sigma_y\approx \mathbf J\boldsymbol\Sigma_{x,\theta}\mathbf J^T+\boldsymbol\Sigma_\delta.
$$

Use this approximation only where the linearization is adequate and cross-covariance with discrepancy is negligible or explicitly modeled. Calibration offsets shared across channels, common reference stars, common water-flow calibration, repeated participants and common geodetic frames create off-diagonal covariance. Counting them as independent observations understates uncertainty.

For independent inputs and a scalar quantity, the familiar sum of squared sensitivity-weighted terms is a special case. The [NIST Technical Note 1297](https://www.nist.gov/pml/nist-technical-note-1297) provides primary guidance for expressing measurement uncertainty, including combined and expanded uncertainty. Type A versus Type B describes how an uncertainty component is evaluated; it is not a label for random versus systematic error.

## Worked thermal-power accounting example

For single-phase coolant with negligible kinetic/potential changes,

$$
Q_f=\dot m c_p\Delta T,\qquad
u^2(Q_f)=\mathbf g^T\boldsymbol\Sigma\mathbf g,
\qquad \mathbf g=(c_p\Delta T,\dot m\Delta T,\dot m c_p).
$$

The covariance is expressed in the order $(\dot m,c_p,\Delta T)$. If the temperature difference uses two sensors, its variance is

$$
u^2(\Delta T)=u^2(T_o)+u^2(T_i)-2\operatorname{cov}(T_o,T_i).
$$

As a **synthetic arithmetic example**, take $\dot m=0.020$ kg/s, $c_p=4180$ J/(kg K), and $\Delta T=5.0$ K. Then $Q_f=418$ W. If independent standard uncertainties are $0.001$ kg/s, 20 J/(kg K), and 0.2 K, the relative standard uncertainty is approximately 6.42%, or 26.84 W. These illustrative numbers are not a measured engine result or a selected hardware specification. A common thermometer offset may cancel in a difference; differential drift may not. Storage and external losses must also be measured before a complete energy balance can be closed.

## Identifiability before optimization

Compute parameter sensitivities under the actual sampling and noise model. If two columns of the sensitivity matrix are nearly collinear, more precise observations of the same observable can leave the same ambiguity. Examples include wall convection versus unmeasured heat loss, spectral abundance versus grain-size effects, particle energy versus incident angle, and latent ecology detection probability versus true abundance.

Inspect singular values or a documented posterior geometry; rescale parameters so units alone do not dominate a condition number. If a parameter is weakly constrained, report a bound, prior sensitivity or alternative model rather than a falsely precise best fit. A sensor-placement trade should ask which new observable separates competing states.

## Nonlinear propagation and numerical error

Use joint Monte Carlo draws, profile likelihood, a justified bootstrap, or posterior sampling when transformations are nonlinear, distributions are bounded, censoring matters or linear uncertainty is inadequate. Retain covariance, bounds, discrete model alternatives and missing-data patterns in the draws. Save random seed, sample count, convergence diagnostics, effective sample size and numerical tolerances. Resample the independent physical unit: a flight, site, star, observing epoch, team or family of simulations, rather than correlated rows.

Refine mesh, time step, precision or quadrature separately from parameter sampling. Show a convergence sequence and comparison with an analytic or independent reference where available. A difference between two resolutions is not automatically a rigorous error bound. If numerical error is not negligible compared with measurement uncertainty or the decision margin, refine or qualify the intended use.

## Decision margins and acceptance

For a scalar upper limit $L$, define a margin using the appropriate decision convention, for example

$$
M=L-(\widehat y+k u_y).
$$

The coverage factor and one-sided/two-sided interpretation must match the distribution, effective degrees of freedom, consequence and controlling requirement. $k=2$ is not automatically exactly 95% coverage. If $M<0$, the available evidence does not establish the selected upper-bound criterion; fitting a favorable mean does not close the requirement.

For comparisons, report the effect size, uncertainty and independent validation units, not only a p-value. For multiple trials, model choices or targets, report the selection procedure and confirmatory versus exploratory status. Freeze acceptance gates before confirmatory data are analyzed; any subsequent change requires a visible rationale and reclassification of the evidence.

## Required uncertainty record

| Item | Information to retain |
|---|---|
| Measurand / decision | Output definition, units, limit and application boundary |
| Inputs | Nominal value or missing/TBD state, distribution, units, source and validity range |
| Dependence | Covariance basis, repeated-unit grouping, shared calibration and uncertain model choice |
| Sensitivity | Derivative/sampling method, parameter scaling and unidentifiable combinations |
| Numerics | Algorithm, tolerances, refinement evidence and independent comparator |
| Discrepancy | Residual structure, out-of-domain flags and model-promotion criteria |
| Output | Estimate, standard/interval uncertainty, coverage interpretation and decision consequence |

The procedure supports the model-credibility discipline described in [NASA-STD-7009B](https://standards.nasa.gov/standard/nasa/nasa-std-7009); project-specific values and evidence remain the responsibility of each design record.
