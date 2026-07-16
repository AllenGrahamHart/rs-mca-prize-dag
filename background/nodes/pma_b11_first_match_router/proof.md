# Proof - PMA B11 first-match router

The five predicates are exhaustive by first splitting on `d>ell+E`, then on
the Johnson gate, then on `G_2<=V_2`, and finally on `G_R<=V_R`. The strict
complements printed in every later cell make them pairwise disjoint.

For `d<=ell+E`, upstream Theorem B11 bounds the union of the three conditions

```text
lambda>=lambda_J,       G_2<=V_2,       G_R<=V_R
```

by the displayed Johnson, two-petal-anchor, and background-petal-anchor
summands. The first-match cells `J`, `A2`, and `AR` form a subset of that
union, so the same bound applies. Corollary B10 supplies the replacement of
the Johnson summand by `1` under the printed unique-decoding inequality.

The complement within `d<=ell+E` is exactly `RES`; the other complement is
exactly `GROW`. This proves both the partition and the bound.

Source pin: Przemek upstream `c35a6da3`,
`experimental/notes/l1/l1_full_list_quotient_proof_program.md`, Theorem B11
and Corollary B10.
