# Proof

First establish the curve properties. Primitivity of the coefficient vector
rules out a parameter-only factor, while the core-free condition `s=0` rules
out an `X`-only factor. Thus every component has positive bidegree.

At least

```text
T-delta>=rho+2-(rho-3e)=3e+2                         (1)
```

supported slopes have generic rank and make `Q_gamma` a squarefree
degree-`rho` locator. If an irreducible factor occurred twice in `Q`, its
leading `X`-coefficient could lose degree at at most its parameter degree,
which is at most `e`. A slope counted by `(1)` outside those roots would
specialize the repeated factor with positive degree, contradicting
squarefreeness. Hence `C` is reduced.

The coefficient bound for `P` follows from `(FIC3)`: each coefficient of
`q^vee` has parameter degree at most `e`, while every syndrome moment is
affine in `z`.

The numerator is nonzero. Put `a=q_rho!=0` in `F(z)`. If `N=0`, its
coefficients successively force `y_0=...=y_(rho-1)=0`. Row zero of the
kernel recurrence then gives `y_rho=0`, and the remaining `rho+1` rows give
`y_(rho+1)=...=y_(2rho+1)=0`. The full Hankel pencil would be zero, contrary
to generic rank `rho`.

Use all available moments and put

```text
Y(z;u)=sum_(i=0)^(2rho+1)y_i(z)u^i.                  (2)
```

For `rho<=k<=2rho+1`, the coefficient of `u^k` in `q^vee Y` is

```text
sum_(j=0)^rho q_j(z)y_(k-rho+j)(z),                  (3)
```

which is row `k-rho` of `M(z)q(z)=0`. The coefficients below `u^rho` are
exactly `N`. Hence

```text
q^vee(z;u)Y(z;u)=N(z;u)+u^(2rho+2)R(z;u)             (4)
```

for some polynomial `R`.

On the domain-infinity chart of `C`, `q^vee=0` and

```text
u^(rho-1)P(z;u^(-1))=N(z;u).
```

Equation `(4)` proves divisibility by `u^(2rho+2)` in the coordinate ring of
the reduced curve. No component is the domain-infinity divisor, so the local
quotients glue. Homogenizing `P` as a section of `O_C(rho-1,e+1)` gives a
section of

```text
O_C(rho-1-(2rho+2),e+1)=O_C(-rho-3,e+1).             (5)
```

It is nonzero on `C`: `P` is nonzero and its `X`-degree is below that of the
full equation `Q`. Finally

```text
deg_C O_C(-rho-3,e+1)
 =(-rho-3)e+(e+1)rho=rho-3e=delta.                   (6)
```

This proves `(FIC4)--(FIC5)`. QED.
