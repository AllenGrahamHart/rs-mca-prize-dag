# Cycle 179: rate-half `A=1` collision barycentric split-jet gate (2026-08-12)

The global collision jets are now computable directly from the classified
row-root data and the unique scalar-weld vector. The correction parameter
is outside every supported root set, and explicit full-set Lagrange value
and derivative weights give

```text
G(t,x_*)   =sum_x b_x lambda_x P_x(t),
G_X(t,x_*) =sum_x d_x lambda_x P_x(t).
```

At the correction, the first row has exact order two. Its zeroth, first,
and second Hasse coefficients are `0,0,nonzero`; the zeroth and first
coefficients of the derivative row select `[4]`, `[1,3]`, or `[2,2]`.

```text
result:                  PROVED unsupported-parameter barycentric jet gate
DAG delta:               +1 PROVED leaf, 3 req edges, 1 evidence edge
critical status delta:   none
compute:                 small exact interpolation replay; no Modal spend
new assumptions:         none
```

The next attack is an exact rank/nonvanishing theorem for these four
functionals on the unique connected weld vector, using the factor-degree
trichotomy rather than another local contact classification.
