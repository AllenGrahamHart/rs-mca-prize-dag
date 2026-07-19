# ATTACK - e22_lower_scale_intersection_formula_payload

Closed by the dyadic-tree tail polynomial in `proof.md`.

The raw residual universe is proved by
`e22_residual_profile_generating_function`, the minimal-scale inclusion-
exclusion consumer is proved by `e22_lower_scale_filter_inclusion_exclusion`,
and weighted-bijection soundness is proved by
`e22_weighted_intersection_certificate_soundness`.

Delivered output:

- exact finite coefficient formulas for every lower-scale admissibility
  intersection;
- coverage of every subset `S` of smaller dyadic scales;
- a bijection from formula atoms to residual profiles in that
  intersection;
- multiplicity agreement with `dyadic_profile_evaluation`.

The formula does not treat lower-scale tail events as independent. It records
the recovered tail counters for all constrained scales in one dyadic occupancy
tree, so intersections are coefficient slices of a shared support object.
