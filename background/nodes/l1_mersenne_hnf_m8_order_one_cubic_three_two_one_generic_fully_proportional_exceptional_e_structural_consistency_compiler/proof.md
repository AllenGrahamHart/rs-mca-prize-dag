# Proof - L1 Mersenne HNF m=8 order-one cubic three-two-one exceptional-E structural-consistency compiler

On `E_G=0,J_*!=0`, (FBC4) gives the first four reconstructions in
(FES1). The exact identity

```text
ell=L_2-x^2-Ax
```

follows directly from the displayed formulas for `ell,L_2,x,A`. Hence
`H_e+G_e=ell` and `H_e=G_e+A(x+Y_e)` recover

```text
2G_e=L_2-x^2-A(2x+Y_e),
```

which is the original definition of `G_2`. Defining `V_e` as in (FES1),
the original `D=YV` equation is exactly `Z_D^e=0` under the printed
denominators.

Since `6-2x=A` and `A(x+Y_e)=ell-2G_e`, the original `Q_0` definition
becomes

```text
Q_0=A G_e+x ell-20-8q/3-D_e,                      (1)
```

which is `Z_Q^e=0`. On `Z_D^e=0`,

```text
W_0=(A+x)D_e+15+23q/4+q^2/8.                     (2)
```

Substitution of (2) and `H_e=ell-G_e` in
`R_0=G_2H-xQ_0-W_0` gives `Z_R^e=0`. Before imposing `Z_D^e=0`, the
original `R_0` residual minus the simplified residual in (FES2) is exactly
`(A+x)(Y_eV_e-D_e)`. Thus the joint use of `Z_D^e,Z_R^e` is reversible,
proving (FES3).

For (FES4), (FBC6) gives the following numerator/denominator total-degree
bounds:

```text
(D_e,Q_e,G_e,Y_e,V_e):
(3/1), (5/3), (9/7), (9/8), (18/16).              (3)
```

Indeed the denominator of `G_e` is `bJ_*`, that of `Y_e` divides
`AbJ_*`, and that of `V_e` divides `A^2b^2J_*^2`. Therefore a common
denominator `A^3b^3J_*^3` of degree 24 for `Z_D^e` gives numerator degree
at most 27. Common denominators `bJ_*D_*` and `b^2J_*^2D_*` of degrees
10 and 17 for `Z_Q^e,Z_R^e` give numerator degrees at most 13 and 21,
respectively. Cancellation can only lower these bounds.

Finally, substitution of `q=-S_0/S_1` in a polynomial of `q`-degree
`m_i` is cleared exactly by `S_1^m_i`. Thus (FES5) is polynomial and
reversible on `S_1!=0`. Combining (FEQ6), (FBC4), and (FES3) proves
(FES6). QED.
