# Cycle 157: rate-half `A=1` double-heavy center overlap (2026-08-11)

Cycle 156's cubic Pade identity meets the extremal split biform at the fixed
heavy row. Let

```text
J=gcd(Lambda,g_*S_B^2),       j=deg J<=3.
```

Exact cancellation gives

```text
G(t,x_*)=[g_*(t)S_B(t)^2/J(t)]T_j(t),
deg T_j<=j.
```

Thus all but at most three roots of this degree-`e-2` row are prescribed.
In the center-disjoint case it is a possibly zero scalar multiple of
`g_*S_B^2`. Since the coefficient polynomials of `G` have `X`-degree at
most `n`, this heavy-row value augments the existing coefficient-MDS gate
with only `j+1<=4` scalar unknowns.

```text
result:                  PROVED heavy-row center-overlap factorization
DAG delta:               +1 PROVED leaf
critical status delta:   none
compute:                 integer degree/tamper checks only
new assumptions:         separated correction locus from Cycle 156
```

This is the missing adapter from the cubic Hankel residual to the split-
biform boundary. It does not prove the augmented matrix full rank; that
rank/nullity decision is now the separated double-root terminal.
