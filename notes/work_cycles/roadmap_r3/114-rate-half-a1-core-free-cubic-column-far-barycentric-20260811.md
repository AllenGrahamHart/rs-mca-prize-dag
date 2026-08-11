# Cycle 114: core-free cubic column-far barycentric gate (2026-08-11)

## Cycle pins

```text
our start:       0abdefa3a
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
compute:         local tiny verifier only
critical open:   28
```

## Strictness correction and true boundary

Column-farness gives, for every supported pair,

```text
|S_alpha union S_beta|>=rho+1,
|S_beta\S_alpha|>=c_alpha+1.
```

Thus Cycle 113's `c_alpha`-point equality branch cannot occur. On the true
minimum-union boundary, the difference has `c_alpha+1` points and the
first-jet radical has the unique barycentric form

```text
mu_xR_alpha(x)=kappa/P'(x),       kappa!=0.
```

This yields the exact field-valued error formula `(CBG6)` and proves that no
new difference point is a root of `R_alpha` there.

## Burn-down

```text
result:                  FENCED weak support route; EXPOSED barycentric boundary
DAG delta:               +1 PROVED leaf, +2 req edges, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next compare the barycentric values with the heavy-row cube/Forney formulas.
For larger unions derive the second coefficient-jet equation; do not pursue
the now-impossible `c_alpha`-source equality branch.
