# conditional: e22_minimal_scale_column_evaluation

## Predicate nodes

- `e22_dyadic_chain_mobius_accounting`
- `e22_minimal_scale_overlap_counts`

## Claim

Conditional on exact cross-scale overlap counts, the dyadic quotient staircase
pricing column evaluates to the sum over selected minimal-scale partition
cells with the declared multiplicity.

## Proof

The proved predicate `e22_dyadic_chain_mobius_accounting` gives, for every
scale `M_j`, the triangular identity

```text
A_j = N_j + sum_{i<j} O_{i,j},
```

where `A_j` is the raw scale-`M_j` count, `N_j` is the selected minimal-scale
cell at `M_j`, and `O_{i,j}` are the overlaps from smaller minimal scales
that are also counted at `M_j`.

The predicate `e22_minimal_scale_overlap_counts` supplies the exact formulas
for every `O_{i,j}` using the same multiplicity convention as
`dyadic_profile_evaluation`. Substituting those formulas into the triangular
identity recovers each `N_j` from the raw dyadic column. Summing the disjoint
`N_j` cells gives exactly the selected minimal-scale support classes, with the
declared multiplicity and without unaccounted larger-scale duplicates.

This proves the column evaluation.
