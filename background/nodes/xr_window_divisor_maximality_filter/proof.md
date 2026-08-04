# Proof

Fix a maximal codeword pair with full joint core `W` of size `k+e`.
A raw `(k+d)`-set producing this pair is exactly a subset
`Z subset W` of size `k+d`: interpolation on `Z` recovers the unique
pair because `|Z|>=k`, and every raw set recovering the pair must lie
inside its full agreement set. Hence this fiber has size
`binom(k+e,k+d)`. Distinct maximal pairs have disjoint fibers by unique
interpolation. Summing the fibers proves `(F)`.

If a predicate `Pi` depends only on the reconstructed maximal pair, it is
constant on each fiber. Retaining exactly the fibers whose pair satisfies
`Pi` proves `(PF)` by the same count.

For inversion, substitute `(PF)` into the right side of `(INV)`. The
coefficient of a fixed `MAX_e^Pi`, with `e=d+g`, is

```text
sum_(j=0)^g (-1)^j
 binom(k+d+j,k+d) binom(k+d+g,k+d+j)
=binom(k+d+g,k+d) sum_(j=0)^g (-1)^j binom(g,j).
```

It is one when `g=0` and zero otherwise. This proves `(INV)`.

For the truncated sum, the same calculation gives coefficient one at
`g=0`, zero for `1<=g<=L`, and, for `g>L`,

```text
binom(k+d+g,k+d)(-1)^L binom(g-1,L).                 (1)
```

Every maximal count is nonnegative. Hence an even `L` adds only
nonnegative surplus to `MAX_d^Pi`, while an odd `L` adds only nonpositive
surplus. This proves `(BON)`.

For `e=d` the fiber size is one. For `e>d` it is larger than one and
the corresponding locator is not a maximal depth-`d` core. The
selected condition is an additional predicate on the unique maximal
pair and is absent from the linear window equations. This proves the
necessity of both filters.

Finally, two copies of the same full-rank `d`-row matrix have stacked
rank `d`, not `2d`; full single-word rank alone cannot establish joint
transversality.
