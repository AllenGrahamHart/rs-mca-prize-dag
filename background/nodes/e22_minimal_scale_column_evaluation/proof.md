# proof: e22_minimal_scale_column_evaluation

The proved node `e22_dyadic_chain_mobius_accounting` gives, for every dyadic
scale `M_j`, the triangular identity

```text
A_j = N_j + sum_{i<j} O_{i,j},
```

where `A_j` is the raw scale-`M_j` count, `N_j` is the selected
minimal-scale cell at `M_j`, and `O_{i,j}` are the overlaps from smaller
minimal scales that are also counted at `M_j`.

The proved node `e22_minimal_scale_overlap_counts` supplies the exact formula
for every `O_{i,j}` using the same multiplicity convention as
`dyadic_profile_evaluation`. Substituting those formulas into the triangular
identity recovers each selected cell `N_j` from the raw dyadic column.

The cells `N_j` are disjoint by `e22_minimal_scale_partition`, so summing them
gives exactly the selected minimal-scale support classes, with the declared
multiplicity and without unaccounted larger-scale duplicates.
