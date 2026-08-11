# Cycle 164: rate-half `A=1` separated center-overlap cap two (2026-08-11)

The external heavy row lies outside `U=S_alpha union S_beta`. If `alpha` or
`beta` were a correction root, `Q(gamma,x_*)=0` would make `x_*` a padded
root there, forcing the same center into `g_*` and `S_B`, contrary to the
separated hypothesis. Thus only `theta` can be a correction center.

The exact center-line rank-loss sum allows at most one padded-heavy center.
Since supported and correction factors are disjoint,

```text
deg gcd(S_B,Lambda)<=1,
deg gcd(g_*,Lambda)<=1,
j=deg gcd(Lambda,g_*S_B^2)<=2.
```

```text
result:                  PROVED center-overlap cap j<=2
DAG delta:               +1 PROVED leaf, 7 req edges
critical status delta:   none
compute:                 seven-case exact replay only; no Modal spend
new assumptions:         none beyond the separated extremal profile
```

The four-scalar `j=3` case is gone. Every separated survivor now has a
nonzero correction-coprime `T_j` with at most three coefficients.
