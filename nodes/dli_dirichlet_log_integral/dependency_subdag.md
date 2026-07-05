# dependency sub-DAG: dli_dirichlet_log_integral

Promoted subclaims.

```text
dli_circle_log_integral_constant [PROVED]
    -> dli_log_integral_equidistribution

dli_odd_evaluation_discrepancy
    -> dli_log_integral_equidistribution

dli_truncated_log_transfer [PROVED]
    -> dli_odd_evaluation_discrepancy

dli_peak_mass_discrepancy
    -> dli_odd_evaluation_discrepancy

dli_et_peak_mass_reduction [PROVED]
    -> dli_peak_mass_discrepancy

dli_deligne_weyl_transfer [PROVED]
    -> dli_odd_eval_exponential_sum_bound
    -> dli_peak_mass_discrepancy

dli_odd_phase_noncollapse_conductor
    -> dli_odd_eval_exponential_sum_bound
    -> dli_peak_mass_discrepancy

dli_log_integral_equidistribution
    -> dli_dirichlet_log_integral
    -> ejm_joint_moment
    -> pcf_evaluation_flatness
    -> pcf_evaluation_flatness / b2b_primitive_core chain

DLI-DWE collision-energy form
    -> ejm_joint_moment
```

## dli_log_integral_equidistribution

Statement: for every nonzero frequency, the odd low-degree evaluations on the
square-root section have near-circle log-integral geometric mean with total
loss `sum eps_j = o(t)`.

Status: CONDITIONAL; this is an assembly node from the circle constant and
the discrepancy predicate.

## dli_odd_evaluation_discrepancy

Statement: the sequence `P_lambda(sigma(y))` has enough distribution away
from Dirichlet peaks, uniformly over central profiles and nonzero frequencies.

Status: CONDITIONAL; the deterministic transfer is proved, and the remaining
leaf is `dli_peak_mass_discrepancy`.

## dli_peak_mass_discrepancy

Statement: odd evaluations satisfy the truncated-log discrepancy and
peak-mass tail bounds required by the transfer lemma.

Status: open; likely a Weil/exponential-sum or collision-energy estimate.

## dli_et_peak_mass_reduction

Statement: finite-frequency Weyl-sum bounds imply the required peak-mass and
truncated-log discrepancy estimates by Erdos-Turan and dyadic annuli.

Status: PROVED.

## dli_odd_eval_exponential_sum_bound

Statement: the odd evaluations satisfy the Weyl-sum bounds required by the
Erdos-Turan reduction.

Status: CONDITIONAL. The standard Deligne/Weil transfer is split off; the
active analytic leaf is `dli_odd_phase_noncollapse_conductor`.

## dli_odd_phase_noncollapse_conductor

Statement: the actual odd-evaluation phases are geometrically nontrivial on
the square-root components, with conductor budget whose harmonic total is
`o(t)`.

Status: open; this is now the active analytic DLI leaf.

## dli_circle_log_integral_constant

Statement: `int_0^1 log |cos(2 pi x)|^2 dx = -2 log 2`.

Status: PROVED.

## DLI-DWE collision-energy form

Statement: the signed `2m`-fold additive energy of the odd-evaluation map is
at the uniform level with the allowed slack.

Status: equivalent route to EJM; useful if geometric log-integral estimates
are too sharp to prove directly.
