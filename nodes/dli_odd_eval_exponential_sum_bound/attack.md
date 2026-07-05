# ATTACK - dli_odd_eval_exponential_sum_bound

Status: conditional.

The standard transfer from geometric nontriviality and conductor control to
Weyl cancellation is isolated in `dli_deligne_weyl_transfer`, and the standard
Artin-Schreier/conductor criterion is isolated in
`dli_artin_schreier_conductor_criterion`. The active DLI analytic leaf is now
`dli_odd_phase_reduced_pole_budget`.

Prove noncollapse and conductor bounds for `P_lambda(sigma(y))` on the
square-root section, uniformly over central profiles and nonzero frequencies.
Likely routes:

- Weil/Deligne bounds after proving the phase is nonconstant on every
  relevant component;
- monodromy for the odd-evaluation map;
- collision-energy bounds strong enough to imply the required Weyl estimates.

The deterministic conversion from Weyl sums to Dirichlet peak-mass control is
already proved in `dli_et_peak_mass_reduction`.
