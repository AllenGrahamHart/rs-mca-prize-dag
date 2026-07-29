# L1 Mersenne HNF m=8 order-one cubic three-two-one generic fully-proportional coefficient router

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_bivariate_factorization`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the four coefficient-zero equations in the generic fully
  proportional official `h=7` cubic `3+2+1` residue

Retain (FPR1)--(FPR5) and (FBF1)--(FBF6), and put

```text
a=b-6,                 kappa=12q-44b-294,
ell=(b^2+6b+105+8q)/16,

D_*=3q(40b^2-253b+1155)-20b(11b^2+81b+414),

Q_*=720b(360+1098q+191q^2-10q^3)+kappa qP,

K_*=240bqa-P.                                         (FCR1)
```

The equations `M_1=M_0=0` are exactly the reconstructions

```text
D_*=3600bD !=0,
Q_*=72D_*Q_0.                                        (FCR2)
```

In particular, both `D` and `Q_0` are rational functions of `(b,q)`.
The structural definitions also give

```text
H+G_2=ell,                 A=-(b+3)/2 !=0.           (FCR3)
```

Define

```text
E_G=K_*-720bq^2,
F_G=6D(K_*-2160bQ_0),
J_G=2160b(Q_0-D)-P,
L_G=2160b ell-6P.                                    (FCR4)
```

Subject to (FCR2)--(FCR3), the remaining equations `C_1=C_0=0` are
exactly the two affine equations

```text
E_G G_2+F_G=0,
J_G G_2+D L_G=0.                                    (FCR5)
```

Consequently the coefficient-zero locus has the following exact disjoint
router.

1. If `E_G!=0`, then

```text
G_2=-F_G/E_G,
Theta_G:=E_G D L_G-J_G F_G=0,
H=ell-G_2,
Y=(ell-2G_2)/A-x.                                   (FCR6)
```

   Thus all coefficient variables are reconstructed from `(b,q)`, and the
   retained compatibility equation `Theta_G=0` is bivariate after the
   denominators in (FCR2) are cleared.

2. If `E_G=0`, the first line of (FCR5) is equivalent to

```text
Q_0=q^2/3,
Q_*-24D_*q^2=0.                                     (FCR7)
```

   If also `J_G!=0`, reconstruct

```text
G_2=-D L_G/J_G,
H=ell-G_2,
Y=(ell-2G_2)/A-x.                                   (FCR8)
```

   If `J_G=0`, the second line of (FCR5) is equivalent to `L_G=0`; this is
   the only coefficient chart that still retains `G_2`, with `H` and `Y`
   reconstructed from it by (FCR3).

Every chart retains `F_b=0`, the structural definitions, the selected
role-discriminant weld, `P_4=0`, and all generic and arithmetic
saturations. This is an exact coefficient router, not a unit, emptiness,
norm, Frobenius-converse, cyclotomic, exact-fiber, or inner-lift verdict.
