# W3 two-class minimal-ledger reduction

- **status:** PROVED
- **dependency:** `ww_paid_residual_partition_adapter`
- **consumer:** `ww_row_envelope_clause` (evidence only)

Fix a planted-sunflower receiver `U` at agreement `k+sigma`. Let

```text
L(U) = {f : deg(f)<k and agr(f,U)>=k+sigma},
P(U) = the set of distinct printed planted polynomials,
R(U) = L(U) \ P(U).
```

Every printed plant agrees on its `(k-1)`-point core and its own
`(sigma+1)`-point petal, so `P(U)` is a subset of `L(U)`. Therefore

```text
|L(U)| = p(U) + N_nonplant(U),
p(U)=|P(U)|,  N_nonplant(U)=|R(U)|.
```

For `B*=floor(q/2^128)`, the exact safe-side condition is

```text
N_nonplant(U) <= B* - p(U),
```

with `p(U)<=B*`; if `p(U)>B*`, the cell is already unsafe. Under distinct
scalar labels, `p(U)` equals the petal count
`floor((n-k+1)/(sigma+1))`; with repeated labels, deduplication gives the
exact smaller value.

Any tangent, quotient, staircase, moment-trade, or other subdivision of
`R(U)` is an optional proof refinement. It is not a prerequisite for the
consumer-exact two-class inequality.
