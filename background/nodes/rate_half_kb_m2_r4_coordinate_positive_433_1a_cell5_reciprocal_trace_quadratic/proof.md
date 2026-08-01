# Proof

The exact launcher reconstructs the cell-5 common minors with the deployed
`(p,i)` and saturates their ideal by every printed source-label and chart
guard.  It maps the resulting affine ideal to the block ring

```text
F_p[r,c,b,t], order (r,c) >> (b,t).
```

The saturated affine basis has 12 elements.  After the block remap its basis
has 13 elements and dimension one.  Exact elimination of `r,c` returns one
generator of total degree eight and 19 terms.  Centering its deployed-field
coefficients gives exactly `(KBRT-2)`, proving `(KBRT-1)`.

Coefficient reversal in `b` reproduces the generator identically.  Expanding
`b^2 Q(b+b^{-1},t)` gives `P`, proving `(KBRT-3)` on `b!=0`.  Finally, direct
polynomial arithmetic using `i^2=-1` gives `(KBRT-4)`.  The launcher checks
both reciprocal identities before printing the eliminant, and the local
checker independently replays the trace lift and discriminant factorization.
QED.
