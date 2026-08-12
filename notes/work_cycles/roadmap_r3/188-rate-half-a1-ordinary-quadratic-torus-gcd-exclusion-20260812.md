# Cycle 188: rate-half ordinary-quadratic torus-gcd exclusion (2026-08-12)

The coordinate-corner gap from Cycle 187 is removed by the already audited
Corvaja--Zannier positive-characteristic gcd theorem. On a coincidence
component of bidegree `(d_1,d_2)`, normalization gives
`chi<=2d_1d_2`. The theorem bounds every non-toral `(4,4)` `S_3` component
strictly below its forced `3(2^39-6)` subgroup points, and every non-toral
`(2,2)` cyclic orientation below its forced half-count.

A translated-subtorus survivor is also impossible. The unique `S_3`
component is swap-invariant, reducing its primitive character to `XY=k` or
`X/Y=k`, both incompatible with three distinct rows in one fiber. In the
cyclic case, coordinate degree two reduces the relation to scaling or
inversion; order three and the dyadic subgroup force coordinate invariance,
contradicting the degree-three quotient.

Thus no `(2,3)` companion exists and shapes B/D are empty. Only shapes A/C
remain in this collision arm.

```text
start:                   0d9c83d6b
result:                  NARROWED, new PROVED companion exclusion
DAG delta:               +1 PROVED node, +2 req edges, +1 ev edge
critical status delta:   none
upstream terminal delta: strong Lane-T PR #1161 extension
delta-star movement:     none
compute:                 exact local replay only; no Modal spend
next route action:       attack shape C's (4,6) companion, then shape A
```
