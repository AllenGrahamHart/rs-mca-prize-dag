# Proof - L1 Mersenne HNF m=8 order-one cubic three-two-one generic fully-proportional coefficient bivariate compiler

From (FCR1)--(FCR2),

```text
D=D_*/(3600b),              Q_0=Q_*/(72D_*).       (1)
```

Also `2160/16=135`, so the definition of `ell` gives `L_G=L_*`.
Substitute (1) into the other expressions in (FCR4):

```text
F_G
 =6D(K_*-2160bQ_0)
 =(D_*K_*-30bQ_*)/(600b)
 =F_*/(600b),

J_G
 =2160b(Q_0-D)-P
 =(150bQ_*-3D_*^2-5PD_*)/(5D_*)
 =J_*/(5D_*).                                      (2)
```

Therefore

```text
Theta_G
 =E_GD L_G-J_GF_G
 =[5E_GD_*^2L_*-6J_*F_*]/(18000bD_*)
 =Theta_*/(18000bD_*).                             (3)
```

The inherited `bD_*!=0` saturation makes all three clearings reversible.
Equations (FBC3)--(FBC5) now follow chart by chart from (FCR6)--(FCR8).
For (FBC4), specifically,

```text
-D L_G/J_G=-D_*^2L_*/(720bJ_*).                   (4)
```

The equation `X_*=0` is exactly the cleared equation
`Q_*-24D_*q^2=0`. On the final chart, `J_G=0` is equivalent to `J_*=0`,
and `D L_G=0` is equivalent to `L_*=0` because `D!=0`.

For the degree ledger, `P,D_*,K_*,E_G,L_*` have total degree at most three,
while `Q_*` has total degree at most five and `q`-degree at most three.
The definitions in (FBC1) then give total degrees six, six, and twelve for
`F_*`, `J_*`, and `Theta_*`; their `q`-degrees are at most three, three,
and six. Finally (FBF3) has `q`-degree two. QED.
