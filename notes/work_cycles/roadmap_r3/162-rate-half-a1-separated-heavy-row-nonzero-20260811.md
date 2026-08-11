# Cycle 162: rate-half `A=1` separated heavy row is always nonzero (2026-08-11)

A re-audit of the complete exact resultant removes the center-overlap
restriction from Cycles 160--161. The factorization

```text
Res_X(Q,G)=c E_4 product_(delta off line)
                    ell_delta^(n-a_delta)
```

shows that a center correction root, like any root not off-line supported,
has exact order two. A zero heavy row would force the component `X-x_*` and
therefore order at least three from `Q(t,x_*)=a_Qg_*S_B^3`, a contradiction.
Off-line supported correction roots are still excluded by the exact
actual/padding fiber dichotomy.

```text
result:                  PROVED nonzero heavy row for all j=0,1,2,3
DAG delta:               +1 PROVED leaf, 4 req edges
critical status delta:   none
compute:                 local valuation replay only; no Modal spend
new assumptions:         none beyond the separated squarefree locus
```

The zero-row obstruction is fully removed on the separated double-root arm.
The remaining wall is divisibility of a nonzero barycentric remainder by
`H`, not possible collapse to zero.
