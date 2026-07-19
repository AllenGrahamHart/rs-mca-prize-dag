# ATTACK - e22_minimal_scale_column_evaluation

This node is now an assembly point.

The selected representatives are partitioned by
`e22_minimal_scale_partition`, and the triangular accounting identity is
proved in `e22_dyadic_chain_mobius_accounting`. The residual-profile
minimality and multiplicity filter is now proved, so larger-scale duplicate
contributions are subtracted by exact overlap formulas.

The overlap formulas:

- give the refined formula for minimal-scale `M_i` data
  satisfying `|B_i| + M_i*r_{i,j}(S_i) < M_j`;
- include any duplicate/multiplicity convention used by
  `dyadic_profile_evaluation`;
- keep the comparison in exact integer arithmetic.
