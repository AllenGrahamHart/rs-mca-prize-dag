# proof: e22_minimal_scale_overlap_counts

Fix dyadic scales `M_i<M_j`.

The proved node `e22_overlap_nested_fiber_residual_identity` says that, for a
support with canonical minimal scale `M_i`, raw scale-`M_j` admissibility is
equivalent to

```text
|B_i| + M_i * r_{i,j}(S_i) < M_j,
```

where `r_{i,j}(S_i)` counts selected `M_i`-fibers whose `M_j`-parent is not
completely selected.

The proved node `e22_overlap_residual_profile_formula` gives the exact count
of minimal-scale-`M_i` canonical support data satisfying this inequality,
with the same duplicate or multiplicity convention as
`dyadic_profile_evaluation`.

Therefore this value is precisely the overlap term `O_{i,j}` in
`e22_dyadic_chain_mobius_accounting`. Since the argument is uniform in the
pair, all cross-scale overlap counts are known.
