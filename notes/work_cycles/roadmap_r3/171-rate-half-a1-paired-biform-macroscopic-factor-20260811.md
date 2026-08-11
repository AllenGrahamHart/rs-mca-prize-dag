# Cycle 171: rate-half `A=1` paired-biform macroscopic factor (2026-08-11)

Factor the extremal paired biform over `F(X)`. Its `R` classified rows each
have all `M=e-2` roots among the same `T=3e` supported slopes. Counting the
zeros of every factor in the row and parameter directions closes with
equality:

```text
3e n_j>=(3p-3+d_A)m_j,
```

and every factor itself splits completely on every classified row. Exact
degree on the at least `e+6+d_A` clean parameter fibers also makes every
factor split over `U_0` there. Since the complete domain degree is only

```text
N=(3(e-2)-1)/2,
```

parity and integer rounding force one factor of parameter degree at least

```text
ceil(e/3)   for d_A=0,
ceil(3e/7)  for d_A=1.
```

```text
result:                  PROVED factor saturation and macroscopic component
DAG delta:               +1 PROVED leaf, 1 req edge
critical status delta:   none
compute:                 small partition audit only; no Modal spend
new assumptions:         none
```

This rules out every bounded-degree factor mechanism, including the type of
low-degree common factor used by the Layer-A saturation counterexample. The
remaining route must confront one macroscopic two-directionally split
factor with the Hankel and multiplicative-domain structure.
