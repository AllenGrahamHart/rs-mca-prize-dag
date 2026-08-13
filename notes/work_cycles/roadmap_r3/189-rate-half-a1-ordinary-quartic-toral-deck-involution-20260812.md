# Cycle 189: rate-half quartic toral deck involution (2026-08-12)

Shape C's `(4,6)` companion has `18e-14` row-slope incidences against
capacity `18e`, hence defect fourteen. At least `2^39-13` slopes have six
distinct rows and force `4123168604063` distinct ordered pair coincidences.
The divided quartic resultant has bidegree at most `(20,20)`.

A degree-six cover has at most five off-diagonal orbit components. The
Corvaja--Zannier bound makes five non-toral components far too small, so one
component is a translated subtorus. Retaining the component subdegree and
image-map degree shows that its primitive character has exponents
`(+/-1,+/-1)` and subdegree one. It is the graph of a deck involution,
necessarily `X -> -X` or `X -> k/X` with `k in mu_(2^41)`.

Thus the companion descends to a `(4,3)` quotient in `X^2` or `X+k/X`.
Shape C remains open; the next attack must rule out those two quotient arms.

```text
start:                   19f3c442d
result:                  NARROWED, new PROVED supporting node
DAG delta:               +1 PROVED node, +2 req edges, +1 ev edge
critical status delta:   none
upstream terminal delta: candidate Lane-T PR #1161 extension
delta-star movement:     none
compute:                 exact local replay only; no Modal spend
next route action:       attack antipodal/reciprocal cubic quotient arms
```
