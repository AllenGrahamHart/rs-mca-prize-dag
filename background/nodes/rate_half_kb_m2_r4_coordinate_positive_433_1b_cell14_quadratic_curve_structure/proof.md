# Proof

Write the five source labels as `x_j`, the target products as `p_j`, and
the signed target sums as `q_j`.  A right-kernel vector has coordinates

```text
(A_0,A_1,A_2,B_0,B_1,B_2,beta_0,beta_1),
```

where the product rows impose `B(x_j)=p_j A(x_j)` and the sum rows impose

```text
q_j A(x_j) + beta_0 x_j + beta_1 x_j^2 = 0.
```

The five product rows have rank five on a principal cofactor chart.  The
`AB` sum row is independent because its final coordinate contains the
guarded factor `x_AB(1-x_AB)`.  Hence these six rows have rank six.  Each
of the other three nontrivial sum rows lies in their span exactly when the
corresponding `7 x 7` determinant vanishes.  This proves the compact
three-determinant replacement for the six pairwise common minors.

The structure launcher constructs those determinants independently for
all `4 x 6=24` source-sign/cofactor charts.  It saturates sequentially by
the selected product cofactor and every printed route guard.  All 24 runs
complete with dimension one and basis size 17.  Within each source-sign
pair, all six charts give byte-identical projected relations:

```text
E_t(t,r) = 0,       degree 4, 6 terms, linear in t;
E_c(c,r,b) = 0,     degree 3, 6 terms, linear in c;
F(r,b) = 0,         degree 7, 17 terms, quadratic in b.
```

Adding the coefficient of `t` to the saturated ideal gives the unit ideal
in all 24 rows.  Adding the coefficient of `c` instead gives a
zero-dimensional closure ideal with basis size four in all 24 rows.  The
exception compiler puts each source-sign closure ideal in lexicographic
form, then saturates it only by the route guards, without using a selected
product cofactor.  All four open exception ideals are unit.  Thus both `t`
and `c` are globally rational on the guarded principal curve.  A fixed
reference cofactor still has a retained zero-dimensional intersection, so
no single product-cofactor chart is falsely declared global.

Normalize `(beta_0,beta_1)=(-1,1)`.  Interpolate
the quadratic `A` from the guarded `AB`, `AC`, and `BC+` sum equations,
then interpolate `B` from three product equations.  Reduction modulo
`F(r,b)` yields an exact kernel on the whole guarded principal locus.  The
independent compiler checks all ten
row pairings for each source-sign pair; every reduced numerator is zero
with denominator one.  This proves the stated global guarded kernel. QED.
