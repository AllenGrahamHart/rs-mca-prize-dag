# Proof

At an active outside row `x`, exact row degree and the external split design
give a nonzero scalar `a_x` with

```text
Q(z;x)=a_x G_x(z).                                   (1)
```

The pair-Lagrange normalization and its internal fibers give

```text
Q(0;x)=A(x),
Q(xi_i;x)=lambda_i B(x)A(x)/D_i(x).                 (2)
```

All factors in the following ratios are nonzero: active outside rows avoid
the roots of `A B`, external slope locators avoid `0` and every `xi_i`, and
the internal scalars are nonzero. Dividing the two equations in `(2)` and
using `(1)` gives

```text
G_x(0)/G_x(xi_i)=D_i(x)/(lambda_i B(x)).             (3)
```

Multiplying rows by `B(x)` and columns by `lambda_i` turns the matrix in
`(CR3G4)` into

```text
(D_i(x))_(x,i).                                      (4)
```

Every `D_i` is quadratic in `x`, so the columns of `(4)` lie in the span of
the three vectors `(1)_x`, `(x)_x`, and `(x^2)_x`. Hence both `(4)` and
`M_inv` have rank at most three.

There are `6e+3>2` distinct active outside rows. Evaluation of a polynomial
of degree at most two on those rows is injective. Therefore the rank of
`(4)` is exactly `dim span{D_i}`. The pair-locator Mobius dichotomy now gives
the exact rank split in `(CR3G4a)`.

Because `G_x H_x=P_Z`,

```text
H_x(xi_i)=P_Z(xi_i)/G_x(xi_i).                      (5)
```

Multiplying the rows of `M_comp` by `G_x(0)` and its columns by
`1/P_Z(xi_i)` turns it into `M_inv`. These scalars are nonzero, so
`rank M_comp=rank M_inv<=3`.

Finally, evaluation at the `e` distinct roots of `I` is an isomorphism from
the `e`-dimensional quotient `F[z]/(I)` to `F^e`. Therefore the matrix rank
in `(CR3G3)` is exactly the dimension of the span of the residue classes
`H_x mod I`, proving `(CR3G2)`.

The kernel of reduction

```text
F[z]_(<=2e) -> F[z]/(I)
```

is `I F[z]_(<=e)` and has dimension `e+1`. Restricting this map to
`W_comp`, then applying `(CR3G2)`, gives

```text
dim W_comp
 <=dim(W_comp intersect I F[z]_(<=e))+3
 <=e+4.
```

Subtracting this from the `6e+3` rows gives nullity at least `5e-1`. This is
`(CR3G5)` and completes the proof. QED.
