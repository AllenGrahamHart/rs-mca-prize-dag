# ATTACK - e22_residual_minimality_multiplicity_filter

This is now an assembly node.

Inputs:

- `e22_residual_profile_generating_function` counts all canonical scale-`M_i`
  data that pass the raw `M_j` residual budget;
- `e22_minimal_scale_partition` gives the lower-scale failure conditions that
  make `M_i` the selected minimal scale;
- `e22_lower_scale_filter_inclusion_exclusion` gives the formal
  inclusion-exclusion filter for those smaller-scale events;
- `dyadic_profile_evaluation` fixes the quotient-column multiplicity
  convention.

Needed output:

- prove `e22_lower_scale_intersection_formula_payload`: compute the exact
  weighted intersections of smaller-scale admissibility events inside the raw
  residual-profile universe.

Do not replace this with an unfiltered residual-budget count: that would still
include supports whose true selected scale is smaller than `M_i`.
