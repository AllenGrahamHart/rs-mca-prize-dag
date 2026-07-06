# ATTACK - e22_overlap_residual_profile_formula

This is now an assembly node.

The proved node `e22_overlap_nested_fiber_residual_identity` reduces a
cross-scale overlap `O_{i,j}` to a residual-profile count:

```text
|B_i| + M_i * r_{i,j}(S_i) < M_j.
```

Known:

- `e22_residual_profile_generating_function` enumerates selected
  `M_i`-fiber subsets and allowable fine tails satisfying the residual budget
  before lower-scale filtering.

Remaining task:

- prove `e22_residual_minimality_multiplicity_filter`: impose the
  minimal-scale conditions for all smaller dyadic moduli and include the
  exact duplicate/multiplicity convention from `dyadic_profile_evaluation`.

Do not close this node from the raw residual generating function alone.
