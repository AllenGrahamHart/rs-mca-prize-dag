# e22_minimal_scale_overlap_counts

- **status:** PROVED
- **closure:** proof

## Statement

For each dyadic pair of quotient scales `M_i < M_j`, compute exactly the
number of support classes whose selected minimal admissible scale is `M_i`
and which are also counted by the raw quotient staircase summand at scale
`M_j`.

This is proved from:

- `e22_overlap_nested_fiber_residual_identity`, which proves that raw
  `M_j`-admissibility is equivalent to the fine-tail residual inequality
  `|B_i| + M_i*r_{i,j}(S_i) < M_j`; and
- `e22_overlap_residual_profile_formula`, which computes the exact
  residual-profile counts with the same duplicate subtraction or multiplicity
  convention as `dyadic_profile_evaluation`.

## Falsifier

A smaller-minimal-scale class contributing to a larger raw scale with an
unaccounted or wrongly weighted overlap.
