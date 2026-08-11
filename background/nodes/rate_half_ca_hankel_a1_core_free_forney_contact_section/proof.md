# Proof

Primitivity excludes a parameter-only factor of `Q`, and `s=0` excludes an
`X`-only factor. Hence every component of `C` has positive degree in both
coordinates.

At least

```text
T-Delta>=rho+2-(rho-e)=e+2                           (1)
```

supported slopes have generic rank and a squarefree, completely split
degree-`rho` locator. A repeated mixed factor of parameter degree at most
`e` would remain repeated at one of these fibres outside its finitely many
degree-loss roots. Thus `C` is reduced.

The coefficient bounds in `(A1F3)` are immediate: the coefficients of
`q^vee` have parameter degree at most `e`, while each syndrome moment is
affine in `z`.

Use every moment available on the half-distance pencil:

```text
Y(z;u)=sum_(i=0)^(2rho-1)y_i(z)u^i.                  (2)
```

For `rho<=k<=2rho-1`, the coefficient of `u^k` in `q^vee Y` is a row of
`M(z)q(z)=0`. The coefficients below `u^rho` are exactly `N_F`, so

```text
q^vee(z;u)Y(z;u)=N_F(z;u)+u^(2rho)R(z;u)             (3)
```

for some polynomial `R`.

The numerator is nonzero. If `N_F=0`, its coefficients successively give
`y_0=...=y_(rho-1)=0`. The `rho` recurrence rows then give
`y_rho=...=y_(2rho-1)=0`, making the full Hankel pencil zero, contrary to
generic rank `rho`.

On the domain-infinity chart of `C`, equation `(3)` and `q^vee=0` show that
`N_F` is divisible by `u^(2rho)` in the reduced coordinate ring. No
component is the infinity divisor, so the local quotients glue. Homogenizing
`P_F` therefore gives a nonzero section of

```text
O_C(rho-1-2rho,e+1)=O_C(-rho-1,e+1).                 (4)
```

It is not identically zero because `P_F` is nonzero and has `X`-degree
strictly below `deg_X Q`. Finally,

```text
deg_C O_C(-rho-1,e+1)
 =(-rho-1)e+(e+1)rho=rho-e=Delta.                    (5)
```

This proves `(A1F4)--(A1F5)`. QED.
