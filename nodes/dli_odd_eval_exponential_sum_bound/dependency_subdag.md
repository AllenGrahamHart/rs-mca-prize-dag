# dependency sub-DAG: dli_odd_eval_exponential_sum_bound

Edges are directed from dependency to consumer.

```text
dli_deligne_weyl_transfer [PROVED]
    -> dli_odd_eval_exponential_sum_bound
    -> dli_peak_mass_discrepancy

dli_odd_phase_reduced_pole_budget
    -> dli_odd_phase_noncollapse_conductor
    -> dli_odd_eval_exponential_sum_bound

dli_artin_schreier_conductor_criterion [PROVED]
    -> dli_odd_phase_noncollapse_conductor
```

## Status

- `dli_deligne_weyl_transfer`: PROVED. This is the standard
  Deligne/Weil-to-Weyl cancellation transfer under nontriviality and conductor
  hypotheses.
- `dli_odd_phase_noncollapse_conductor`: CONDITIONAL. The standard
  Artin-Schreier/conductor criterion is proved.
- `dli_odd_phase_reduced_pole_budget`: TARGET. This is the remaining
  project-specific analytic geometry.
- `dli_odd_eval_exponential_sum_bound`: CONDITIONAL.
