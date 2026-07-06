# conditional: e22_lower_scale_intersection_profile_counts

This node is conditional on:

- `e22_residual_profile_generating_function`
- `e22_minimal_scale_partition`
- `dyadic_profile_evaluation`
- `e22_weighted_intersection_certificate_soundness`
- `e22_lower_scale_intersection_formula_payload`

All dependencies except the final payload are proved. The live payload must
provide exact coefficient formulas and bijection/weight checks for every
lower-scale admissibility intersection.
