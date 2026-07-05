# ATTACK - e22_minimal_scale_overlap_counts

This is now an assembly node, not the live arithmetic leaf.

Known:

- `e22_minimal_scale_partition` proves disjoint selected cells by minimal
  dyadic scale;
- `e22_dyadic_chain_mobius_accounting` proves that raw scale counts equal the
  selected cell plus smaller-minimal-scale overlaps;
- `e22_overlap_nested_fiber_residual_identity` proves the finite nested-fiber
  identity that converts raw larger-scale admissibility into the residual
  inequality

```text
|B_i| + M_i * r_{i,j}(S_i) < M_j.
```

Remaining task:

- prove `e22_residual_minimality_multiplicity_filter`: apply lower-scale
  nonadmissibility and the duplicate/multiplicity convention used by
  `dyadic_profile_evaluation` to the proved residual-profile generating
  function;
- plug those residual-profile formulas into the triangular subtraction.

Do not close this node from the nested-fiber identity alone; the residual
profile count is the remaining arithmetic input.
