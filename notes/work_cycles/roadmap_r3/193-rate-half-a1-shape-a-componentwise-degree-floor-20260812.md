# Cycle 193: rate-half shape-A componentwise degree floor (2026-08-12)

Every geometric off-diagonal component meets every pure split fiber in its
full degree. Those points are rational and etale, so Frobenius cannot move
the component: every component and its row-pair image are base-field
defined.

Retaining the component subdegree `h` and image-map degree `q` gives image
bidegree `D=(e-2)h/q` and at least

```text
ceil((e+7)nD/(e-2))
```

subgroup points on that image. A toral image would be a scaling or
reciprocal deck graph, impossible because the cover degree
`n=2^38-3` is odd while the row subgroup is dyadic. The exact
Corvaja--Zannier comparison then forces

```text
D>=39768216,
#Z(H^2)>=10931403977394458172,
q<4608h.
```

Thus the low-degree component strategy is completely excluded in this
prime-field branch. The surviving obstruction is genuinely macroscopic and
must be coupled to the scalar weld, source coefficients, or concentrated
excess norm.

```text
start:                   28639101d
result:                  NARROWED, componentwise base-field and degree floor
DAG delta:               +1 PROVED node, +2 req edges, +1 ev edge
critical status delta:   none
upstream terminal delta: candidate Lane-T PR #1161 extension
delta-star movement:     none
compute:                 exact local replay only; no Modal spend
next route action:       attack high-degree components through source/norm data
```
