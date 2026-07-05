# conditional: sov_hminus1_coefficient_distribution

## Predicate nodes

- `sov_hminus1_fiber_fourier_duality`
- `sov_hminus1_character_sum_bound`

## Claim

Conditional on the anchored-core character-sum bound, the coefficient
`[X^{h-1}]L` has fibers below the active-core budget after forced-root
higher-coefficient conditioning.

## Proof

Fix an official-shape row, `h in (20,A]`, and a forced-root
higher-coefficient conditioning cell `Omega` of anchored-core locators. Let

```text
c(L) = [X^{h-1}]L.
```

The proved node `sov_hminus1_fiber_fourier_duality` gives, for every field
value `a`, the bound

```text
|{L in Omega : c(L)=a}|
  <= |Omega|/|F| + |F|^{-1} sum_{xi != 0} |S(xi)|.
```

The predicate `sov_hminus1_character_sum_bound` says that the nontrivial sums
`S(xi)` for the actual conditioned anchored-core family are small enough that
the right-hand side is below the active-core budget.

Therefore every `[X^{h-1}]L` fiber in every forced-root conditioning cell is
below the active-core budget. This is the required coefficient-distribution
statement.
