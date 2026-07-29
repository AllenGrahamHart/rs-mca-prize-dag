# Proof - L1 Mersenne HNF m=8 order-one cubic three-two-one generic fully-proportional coefficient router

The change of variables gives

```text
x=(b+15)/4,       a=4x-21=b-6,
kappa=12q+366-176x=12q-44b-294.                    (1)
```

Use `R_0=-qP/(2880b)` in (GDL1). The equation `M_1=0` becomes

```text
360D=kappa a-3186-258q+11P/(20b).                  (2)
```

Expanding the right side of (2) and multiplying by `10b` gives

```text
3600bD
 =3q(40b^2-253b+1155)-20b(11b^2+81b+414)
 =D_*.                                               (3)
```

Likewise `M_0=3(B_0+4kappa R_0)`, so `M_0=0` is equivalent to

```text
360DQ_0
 =360+1098q+191q^2-10q^3+kappa qP/(720b).          (4)
```

Multiplying (4) by `720b` and using (3) gives
`Q_*=72D_*Q_0`. Conversely, (3)--(4) recover `M_1=M_0=0`.
The inherited `bD!=0` saturation makes `D_*!=0`, proving (FCR2).

Next use the definitions in (SQC1)--(SQC3). Since

```text
2G_2=L_2-x^2-A(2x+Y),       H=G_2+A(x+Y),
```

eliminating `Y` gives

```text
H+G_2=L_2-x^2-Ax=(b^2+6b+105+8q)/16=ell.           (5)
```

Moreover `R=A(3Y^2+2xY+G_2)` and the inherited role saturation has
`R!=0`; hence `A=-(b+3)/2!=0`. This proves (FCR3).

Put `T=G_2+6D`. From (GLD4), (GDL1), and `C_0=0`, direct cancellation of
the `DH` terms gives the exact identity

```text
C_1+C_0/q
 =T(qa+12R_0/q)-3q^2G_2-54DQ_0.                   (6)
```

Since `qa+12R_0/q=K_*/(240b)`, multiplying (6) by `240b` gives the first
line of (FCR5). On the other hand, substitute `H=ell-G_2` and
`R_0=-qP/(2880b)` directly into `C_0/q`. Multiplication by `240b` gives

```text
240b C_0/q=J_GG_2+D L_G,                            (7)
```

which is the second line of (FCR5). Equation (7) recovers `C_0=0`; then
(6) recovers `C_1=0`, so the reduction is reversible.

If `E_G!=0`, solve the first line of (FCR5) for `G_2`. Substitution into
the second line gives exactly `Theta_G=0`. Equation (5), followed by
`H=G_2+A(x+Y)`, gives the reconstructions in (FCR6).

If `E_G=0`, then `K_*=720bq^2`. Because `6bD!=0`, the equation `F_G=0`
is equivalent to `Q_0=q^2/3`. Combining this with (FCR2) gives the second
equation in (FCR7). The two `J_G` charts now follow directly from the
second line of (FCR5), using `D!=0` when `J_G=0`. All divisions use the
printed chart guards and inherited saturations. QED.
