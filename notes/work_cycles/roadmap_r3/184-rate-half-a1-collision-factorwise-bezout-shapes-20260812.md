# Cycle 184: rate-half `A=1` collision factorwise Bezout shapes (2026-08-12)

```text
our start:              51dcd6dde
canonical prize:        9569b0d5d
upstream main:          93fba1be3
relevant upstream PRs:  #1160, #1161, #1162, #1163
critical orbit:         167 PROVED / 37 CONDITIONAL / 27 UNPROVED
crosswalk:              PASS, 103 rows (pins remain due for next wave)
```

The corrected `d_A=1` collision has one large odd factor and ordinary-even
companions. Factoring the projective Bezout count componentwise turns the
global four-core into an exact per-factor ledger. The classified grid uses
`(3p-2)m_j` transverse intersections on a factor `(m_j,n_j)`, leaving

```text
c_j=e n_j+(3e-2-(3p-2))m_j.
```

The `e-7` padded-heavy first copies and the collision contact lengths exhaust
these capacities. The Pade contact module gives total length four, and a
two-by-two norm calculation in the local quadratic algebra gives

```text
ell_j=2 ord_tau Q_j(t,x_*).
```

Writing `r_j,b_j,t_j` for padding, correction, and remaining heavy-row
degrees yields

```text
sum(r_j,b_j,t_j)=(e-7,2,3).
```

An ordinary factor must then be exactly `(m,n)=(2,3)` or `(4,6)`. Therefore
the whole biform has only four shapes: irreducible; one quadratic companion;
one quartic companion; or two quadratic companions. The large factor has
degree `e-2`, `e-4`, or `e-6`.

```text
result:                  NARROWED, new PROVED supporting node
DAG delta:               +1 PROVED node, +6 req edges, +1 ev edge
critical status delta:   none
upstream terminal delta: bankable extension for Lane-T PR #1161
delta-star movement:     none
compute:                 exact local replay only; no Modal spend
next route action:       attack the (2,3)/(4,6) companions, then shape A
```
