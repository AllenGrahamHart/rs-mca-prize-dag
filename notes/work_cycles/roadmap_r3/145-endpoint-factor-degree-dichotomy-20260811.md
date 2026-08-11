# Cycle 145: endpoint kernel-biform factor-degree dichotomy (2026-08-11)

The Round 34 factor argument was reconstructed as a first-class proved node.
For irreducible factors of parameter/domain degrees `(m_j,d_j)`, exact
incidence counting gives

```text
T*rho-O <= sum_j min(T*d_j,N*m_j),
sum_j d_j<=rho.
```

There is exactly one small factor, and it has parameter degree at least
`ceil((3m+1)/4)`. At the official `m=2^37`, that degree is at least
`103079215105`. Both specialization guards were checked explicitly:
neither a fixed parameter nor a fixed domain point can annihilate a factor
identically.

```text
result:                  PROVED factor-degree dichotomy
DAG delta:               +1 PROVED
critical status delta:   none
delta-star movement:     none
new assumptions:         none
compute requests:        none
next route-deciding:     attack Rout or the dominant component through
                         multiplicative-domain evaluation hyperplanes
```
