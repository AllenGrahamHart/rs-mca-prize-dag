# ATTACK - e22_minimal_scale_pricing_compatibility

Use the selected representative from `e22_dyadic_minimal_scale_selector`:

```text
(R, M_min(R), B_{M_min}(R), selected M_min-fibers).
```

The selected-scale predicate is now proved in
`e22_minimal_scale_tail_criterion`, and the raw-to-selected triangular
accounting is proved in `e22_dyadic_chain_mobius_accounting`. The residual
filter has been reduced to `e22_lower_scale_intersection_formula_payload`:
reconcile the proved minimal-scale partition cells with the exact dyadic
quotient staircase column from `dyadic_profile_evaluation`.

Acceptable closures:

- prove that the column's summand at scale `M` counts exactly supports
  satisfying the tail-minimality criterion at `M`;
- or prove an explicit duplicate multiplicity factor and show the consumer
  divides by that factor;
- or refine the column by subtracting non-minimal scale overlap contributions and
  rerun the exact integer comparison.

The selector theorem does not itself prove pricing compatibility.
