# e22_overlap_residual_profile_formula

- **status:** PROVED
- **closure:** proof

## Statement

For every dyadic pair `M_i<M_j`, compute exactly the number of canonical
minimal-scale-`M_i` E22 support data whose fine-scale tail and incomplete
coarse-parent residual profile satisfy

```text
|B_i| + M_i * r_{i,j}(S_i) < M_j,
```

where `r_{i,j}(S_i)` is the number of selected `M_i`-fibers whose
`M_j`-parent is not completely selected, as in
`e22_overlap_nested_fiber_residual_identity`.

This is proved from:

- `e22_residual_profile_generating_function`, which proves the product
  generating function for all canonical scale-`M_i` data satisfying the raw
  residual budget before lower-scale filtering; and
- `e22_residual_minimality_multiplicity_filter`, which imposes the
  minimal-scale conditions from `e22_minimal_scale_partition` and the
  declared duplicate-subtraction or multiplicity factor used by
  `dyadic_profile_evaluation`.

## Falsifier

A minimal-scale-`M_i` support whose residual profile satisfies the inequality
above but is omitted, or one whose residual profile fails the inequality but
is included in the claimed `O_{i,j}` formula.
