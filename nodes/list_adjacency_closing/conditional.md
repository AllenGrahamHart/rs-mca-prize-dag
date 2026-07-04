# list_adjacency_closing conditional proof

- **status:** CONDITIONAL
- **closure:** proof from predicate nodes

## Predicate nodes

- `list_crossing_localization`
- `worst_word_planted`
- `list_planted_arithmetic`
- `rate_half_band_closure`
- `list_corridor_ledger`

Convention/evidence guards:

- `rules_m_reading`
- `rate_half_coverage_gap`

## Claim

Conditional on the predicate nodes, for each admissible row and each constant
interleaving arity `m`, there is an adjacent agreement-index `delta` satisfying

```text
sup_U |Lambda(U, delta - 1)| > eps*|F| >= sup_U |Lambda(U, delta)|.
```

## Proof

`rules_m_reading` fixes the quantifier convention: the list challenge is a
family of determinations indexed by constant `m`.

For a fixed admissible row and fixed constant `m`, `list_crossing_localization`
proves that the worst-word list-size function is integer-valued and monotone in
the agreement-index convention. Therefore once the relevant window is bracketed
there is a unique adjacent crossing of `eps*|F|`.

The unsafe side is constructive. Conditional on `worst_word_planted`, the
supremum at the crossing radii is attained by the planted sunflower family or
the classified E15 challenger class. Conditional on
`list_planted_arithmetic`, both classes are priced by exact combinatorial
formulas, so the lower side of the crossing can be exhibited explicitly.

The safe side is supplied by the corridor predicates. `list_corridor_ledger`
closes the clean-rate corridor from the list-side arithmetic columns, while
`rate_half_band_closure` supplies the missing rate-`1/2` band identified by
`rate_half_coverage_gap`. Together they cover every admissible row class in the
current split.

Thus, for each row and constant `m`, the exact planted/challenger arithmetic
exhibits the last unsafe index, the safe ledger controls the next index, and
monotonicity turns those two inequalities into the adjacent crossing displayed
above.

If any predicate fails, the parent does not claim more than bracket-grade
information for the corresponding row or band.
