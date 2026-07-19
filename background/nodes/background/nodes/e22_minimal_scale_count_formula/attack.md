# ATTACK - e22_minimal_scale_count_formula

Use the predicate from `e22_minimal_scale_tail_criterion`:

```text
|B_M(R)| < M
and
|B_{M'}(R)| >= M' for every smaller admissible M' < M.
```

The dyadic classes satisfying this predicate are partitioned by
`e22_minimal_scale_partition`, and the triangular accounting step is proved in
`e22_dyadic_chain_mobius_accounting`. The residual-profile filter has been
reduced to `e22_lower_scale_intersection_formula_payload`: the exact
lower-scale admissibility intersections that make
`e22_minimal_scale_column_evaluation` effective. It should specify one of:

- a refined binomial/divisor formula that counts exactly the tail-minimal
  support classes;
- an explicit duplicate factor converting the raw dyadic scale sum into the
  selected-class count;
- or a subtraction formula for non-minimal scale contributions, followed by
  the exact integer pricing comparison.

The live E22 cross-scale pricing leaf is now
`e22_lower_scale_intersection_formula_payload`.
