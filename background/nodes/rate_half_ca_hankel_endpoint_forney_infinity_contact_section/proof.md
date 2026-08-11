# Proof

The coefficient bound follows directly from `(FIC2)`: each coefficient of
`q^vee` has parameter degree at most `m`, while every syndrome moment is
affine in `z`.

The numerator is nonzero. Indeed, put `a=q_rho!=0` in `F(z)`. If `N=0`,
its coefficients successively give

```text
a y_0=0,
a y_1+q_(rho-1)y_0=0,
...,
a y_(rho-1)+...+q_1y_0=0,
```

so `y_0=...=y_(rho-1)=0`. The row-zero kernel recurrence then gives
`y_rho=0`, and the remaining `rho+1` rows inductively give
`y_(rho+1)=...=y_(2rho+1)=0`. This would make the full Hankel pencil zero,
contrary to its generic rank `rho`.

Now use all available moments and put

```text
Y(z;u)=sum_(i=0)^(2rho+1)y_i(z)u^i.                  (1)
```

For `rho<=k<=2rho+1`, the coefficient of `u^k` in `q^vee Y` is

```text
sum_(j=0)^rho q_j(z)y_(k-rho+j)(z),                  (2)
```

which is row `k-rho` of `M(z)q(z)=0`. The coefficients below `u^rho` are
exactly `N`. Hence

```text
q^vee(z;u)Y(z;u)=N(z;u)+u^(2rho+2)R(z;u)             (3)
```

for some polynomial `R`.

On the domain-infinity chart of `C`, `q^vee=0` and

```text
u^(rho-1)P(z;u^(-1))=N(z;u).
```

Equation `(3)` proves divisibility by `u^(2rho+2)` in the coordinate ring of
the reduced curve. No component of `C` is the domain-infinity divisor, so
`u` is a nonzerodivisor at every generic component point and the local
quotients glue. Homogenizing `P` as a section of `O_C(rho-1,m+1)` therefore
gives a section of

```text
O_C(rho-1-(2rho+2),m+1)=O_C(-rho-3,m+1).             (4)
```

It is nonzero on `C`: a biform of `X`-degree at most `rho-1` cannot be
divisible by the full bidegree-`(rho,m)` equation `Q`, and `P` itself is
nonzero. Finally

```text
deg_C O_C(-rho-3,m+1)
 =(-rho-3)m+(m+1)rho=rho-3m=m-1.                     (5)
```

This proves `(FIC3)--(FIC4)`. QED.
