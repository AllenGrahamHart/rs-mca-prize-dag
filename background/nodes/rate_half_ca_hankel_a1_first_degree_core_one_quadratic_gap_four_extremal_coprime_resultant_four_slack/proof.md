# Proof

The paired first-jet theorem gives `gcd(Q,G)=1`, so `(CRS1)` is nonzero.
For biforms of bidegrees `(d,e)` and `(n,m)`, the parameter resultant has
domain degree at most the intersection number

```text
I=dm+en.                                            (1)
```

Fix `x in M`. The two row polynomials have the factorizations

```text
Q(t,x)=c_x q_gamma(t)P_x(t),
G(t,x)=lambda_xP_x(t),                             (2)
```

where `P_x` has `m` distinct roots. Thus the vertical line `X=x` contains
at least `m` intersections of the two curves, counted with multiplicity.
The standard local interpretation of the resultant gives

```text
(X-x)^m divides R_QG(X).                           (3)
```

The classified rows are distinct, so multiplication of `(3)` proves
`(CRS3)`. Its residual degree is at most `I-Rm`. Substitution of

```text
d=3e-2,       n=(3e-7)/2,       m=e-2,
R=(9e-9+2d_A)/2
```

gives exactly `(CRS4)`.

For a zero-excess slope, the two vertical fibers are

```text
Q(delta,X)=chi_delta A_delta B_delta R_delta,
G(delta,X)=zeta_delta A_delta R_delta.             (4)
```

Every root of `R_delta` is outside `U_0`, hence outside `M`. Every such
common point contributes at least its multiplicity in `R_delta` to the
resultant after the factor `L_M^m` is removed. Multiplying over all
zero-excess slopes proves the padded factors in `(CRS6)--(CRS7)`.

Suppose `d_A=0`. The exceptional row is outside `M`. Whenever an off-line
supported slope contains `x_circ`, the row identity

```text
G(t,x_circ)/L_U0'(x_circ)
 =omega_(x_circ)(t)Q(t,x_circ)/Lambda(t)           (5)
```

shows that the off-line root of `Q(t,x_circ)` is also a root of
`G(t,x_circ)`: `Lambda` is nonzero there. The exact extremal slack identity,
`sum a_delta=e`, and `sum r_delta=e-6` give

```text
sum_delta b_delta=e-3.                             (6)
```

Thus `(X-x_circ)^(e-3)` also divides `T_QG`, proving `(CRS6)`.

The mandatory divisor degree is `(e-3)+r_0` when `d_A=0` and `r_0` when
`d_A=1`. Subtracting it from `(CRS4)` gives respectively

```text
(2e-5)-(e-3)-r_0=4+(e-6-r_0)=4+r_bad,
(e-3)-r_0=4+(e-7-r_0)=4+r_bad.                    (7)
```

The quotient `W_QG` is nonzero because `R_QG` is nonzero. This proves
`(CRS8)`. Finally, the first-jet theorem makes every selected
actual-support intersection transverse, so those points have local
intersection multiplicity exactly one and add no hidden charge to
`W_QG`. QED.
