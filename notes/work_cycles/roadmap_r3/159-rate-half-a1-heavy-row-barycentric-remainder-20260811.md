# Cycle 159: rate-half `A=1` heavy-row barycentric remainder (2026-08-11)

The heavy-row adapter from Cycle 157 is now combined with the connected
scalar weld. If `lambda` is the unique surviving weld vector, define

```text
R_lambda(t)=sum_(x in X)
 L_X(x_*)lambda_xP_x(t)/((x_*-x)L_X'(x)).
```

Coefficient-RS interpolation proves that this is exactly `G(t,x_*)`. Hence
the complete augmented heavy-row gate is

```text
H divides R_lambda,
H=g_*S_B^2/gcd(Lambda,g_*S_B^2).
```

Equivalently one explicit polynomial-remainder matrix `B_H` must kill the
already unique vector `lambda`. It has `e-2-j` rows, with `j<=3`; in the
center-disjoint case the test is simply `R_lambda=c g_*S_B^2`, allowing
`c=0`.

```text
result:                  PROVED exact one-polynomial augmented-row gate
DAG delta:               +1 PROVED reduction node, 4 req edges
critical status delta:   none
compute:                 exact F_101 replay only; no Modal spend
new assumptions:         none beyond the separated correction locus
```

The next route-deciding theorem is universal nonvanishing of this remainder
on admissible Hankel/source packets, or an exact classification of its zero
locus. Generic row counts are no longer the target.
