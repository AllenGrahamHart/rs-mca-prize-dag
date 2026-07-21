# Proof

Let

```text
G_i=B+w_iV,       Phi(W)=product_i(W-w_i),
lambda_i=1/Phi'(w_i).
```

The canonical factorization is `Q=product_i G_i`.  Partial fractions give

```text
sum_i lambda_i/G_i=-V^3/Q,
sum_i lambda_i w_i/G_i=BV^2/Q.                       (1)
```

Indeed, substitute `T=-B/V` into
`1/Phi(T)=sum_i lambda_i/(T-w_i)` for the first identity; the second follows
from `w_i=(G_i-B)/V` and `sum_i lambda_i=0`.  Therefore

```text
sum_i lambda_i G_i'/G_i
 =V^2(BV'-B'V)/Q.                                    (2)
```

On the other hand,

```text
G_i=product_(a in A_i)(1-az)
```

turns the left side of `(2)` into

```text
-sum_(j>=1)(sum_i lambda_i p_(i,j))z^(j-1).          (3)
```

Since `Q=(1-z^N)/E`, equations `(2)--(3)` show that one period of the
weighted cell moments is the coefficient vector of

```text
K=-EV^2(BV'-B'V).                                    (4)
```

There is no alias in that period.  Both `B` and `V` have degree at most
`r=2H-3`; their leading Wronskian terms cancel, so

```text
deg(BV'-B'V)<=2r-2,
deg K<=4+2r+(2r-2)=N-2.                              (5)
```

The negation difference multiplies the `j`th moment by
`1-(-1)^j`.  Since the coefficient of `z^(j-1)` has the opposite parity,
its moment polynomial is consequently `K(z)+K(-z)`.

Now use `V=z^HC`.  Direct differentiation gives

```text
BV'-B'V=z^(H-1)Theta.                                (6)
```

The apparent top term of `Theta` cancels: if the leading terms of `B,C` are
`bz^(2H-3),cz^(H-3)`, its scalar is

```text
H+(H-3)-(2H-3)=0.
```

Thus `deg Theta<=3H-7`.  Substituting `(6)` and
`E=(1-z^2)Q_-` into `(4)`, and using that `3H-1` is even, gives exactly

```text
K(z)+K(-z)=-z^(3H-1)(1-z^2)J(z).                    (7)
```

This proves `(BSP2)--(BSP3)`, including evenness of `J`.

For `x in mu_N`, finite Fourier inversion and `uhat_0=0` give

```text
Nxu(x)=sum_(j=1)^(N-1)uhat_j x^(-(j-1)).             (8)
```

Evaluate `(BSP3)` at `z=x^(-1)` in `(8)` to obtain `(BSP4)`.

The zero set of `u` contains `x=+/-1`.  Away from those two points,
`(BSP4)` says that it is exactly the inverse of the subgroup-root set of
`J`.  Hence

```text
#zeros(u)<=2+deg J<=5H-9,
```

and `N=8H-8` gives `|supp u|>=3H+1`.

Equality requires equality at every step: `J` has degree `5H-11`, all its
roots are distinct elements of `mu_N`, and neither `+1` nor `-1` is among
them.  Since `z^N-1` is squarefree, these conditions are equivalent to
`(BSP5)`.  Conversely `(BSP5)` gives exactly `5H-9` zeros in `(BSP4)` and
hence support `3H+1`. QED.
