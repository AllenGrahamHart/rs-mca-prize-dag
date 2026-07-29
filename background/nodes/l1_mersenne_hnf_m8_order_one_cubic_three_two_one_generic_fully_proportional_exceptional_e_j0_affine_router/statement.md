# L1 Mersenne HNF m=8 order-one cubic three-two-one exceptional-E J-zero affine router

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_coefficient_bivariate_compiler`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the retained `F_b=E_G=X_*=J_*=L_*=0` chart (FBC5) of the
  fully proportional official `h=7` cubic `3+2+1` residue

Retain (FCR1), (FBC1), and (FBF3). Define

```text
B(b,q)=96q^2+(216-32b)q+3b^2+18b+315,

T(b)=-280b^2+2241b+3465,
M(b)=29b^2+234b+81,
R(b)=5bM(b),

R_J=3D_*+5P-3600bq^2.                              (FJ01)
```

There are exact polynomial identities

```text
L_*=45bB+6E_G,
R_J+5E_G=-75bB+3(Tq-R),
J_*=-D_*R_J+150bX_*.                               (FJ02)
```

Consequently the original `E_G=X_*=J_*=L_*=0` chart, with its inherited
`bD_*!=0` saturation, forces

```text
B=0,                 Tq=R.                         (FJ03)
```

The coefficient `T` is a unit on every official solution. Indeed, if
`T=0`, then (FJ03) and `b!=0` give `M=0`. But

```text
29T+280M=9(14501b+13685).                           (FJ04)
```

Thus a common zero would have `b=-13685/14501`. The denominator is a unit
at every official prime, while

```text
14501^2 M(-13685/14501)=-23972710684,               (FJ05)

-23972710684 mod (8191,131071,524287,2147483647)
  =(3690,44145,312391,1797093080).
```

All four residues are nonzero, so `T!=0` and

```text
q=R(b)/T(b).                                        (FJ06)
```

Define the integer polynomials

```text
Bhat(b)=T^2 B(b,R/T),
Ehat(b)=T^2 E_G(b,R/T),
Fhat(b)=T^2 F_b(b^2,R/T),
Xhat(b)=T^3 X_*(b,R/T).                             (FJ07)
```

Then the complete coefficient chart (FBC5) is equivalent to

```text
Bhat=Ehat=Fhat=Xhat=0,       q=R/T,       T!=0,     (FJ08)
```

together with the inherited saturations. Its degree ledger is

```text
deg Bhat<=6,       deg Ehat<=7,
deg Fhat<=10,      deg Xhat<=11.                    (FJ09)
```

The variable `G_2` remains retained on this chart. Every structural
equation, selected role-discriminant equation, `P_4`, saturation, and
arithmetic-lift filter remains mandatory. This is an exact univariate
coefficient router, not a common-root, ambient-quadratic-field, emptiness,
role, lift, or critical-node verdict.
