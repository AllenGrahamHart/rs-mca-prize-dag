# ATTACK - e22_lower_scale_intersection_profile_counts

Closed assembly node. The former E22 residual-filter leaf
`e22_lower_scale_intersection_formula_payload` is proved.

Inputs:

- `e22_residual_profile_generating_function` gives the raw residual universe;
- `e22_lower_scale_filter_inclusion_exclusion` gives the formal minimality
  filter once all lower-scale intersection counts are known;
- `dyadic_profile_evaluation` fixes the pricing multiplicity convention.

Delivered output:

- for each subset of smaller dyadic scales, the exact count of raw
  residual profiles also admissible at those scales;
- the count is weighted by the same multiplicity convention used in the
  quotient staircase column;
- the formulas are packaged so inclusion-exclusion yields the minimal-scale
  overlap term `O_{i,j}`.

Do not approximate these intersections by treating lower-scale tail events as
independent; the tails are recovered from the same support.
