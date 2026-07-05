# ATTACK - dli_peak_mass_discrepancy

Status: conditional.

The deterministic Erdos-Turan/annulus reduction is proved in
`dli_et_peak_mass_reduction`. The remaining analytic target is
`dli_odd_eval_exponential_sum_bound`: prove finite-frequency Weyl-sum bounds
for the odd low-degree evaluations on the square-root section.

Viable forms:

- Weil or Deligne-style exponential-sum bounds for nonzero frequencies;
- collision-energy control strong enough to bound peak neighborhoods at every
  truncation scale;
- a direct monodromy estimate for the relevant odd-evaluation map.

The deterministic transfer to the DLI log-integral inequality is already
handled by `dli_truncated_log_transfer`.
