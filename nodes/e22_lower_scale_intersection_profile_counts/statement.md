# e22_lower_scale_intersection_profile_counts

- **status:** PROVED
- **closure:** proof

## Statement

For every dyadic pair `M_i<M_j` and every subset `S` of smaller dyadic scales
`M'<M_i`, compute the exact `dyadic_profile_evaluation`-weighted count of
residual-profile data that:

- satisfy the raw `M_j` residual budget from
  `e22_residual_profile_generating_function`; and
- are admissible at every scale in `S`.

These intersection counts are the inputs to
`e22_lower_scale_filter_inclusion_exclusion`.

This node is proved from:

- `e22_weighted_intersection_certificate_soundness`, the proved
  weighted-bijection rule for formula certificates; and
- `e22_lower_scale_intersection_formula_payload`, the exact formula
  package for all lower-scale intersections.

## Falsifier

A lower-scale admissibility intersection inside the residual-profile universe
whose exact size or pricing multiplicity differs from the claimed formula, or
a defect in the weighted-intersection certificate soundness rule.
