# L1 Mersenne HNF m=8 order-one cubic three-two-one exceptional-E J-zero structural-consistency compiler

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_j0_affine_router`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the `E_G=X_*=J_*=L_*=F_b=0` chart of the fully proportional
  official `h=7` cubic `3+2+1` residue

Retain (FCR1)--(FCR8), (FBC1)--(FBC6), and (FJ01)--(FJ09). Put

```text
x=(b+15)/4,                    A=-(b+3)/2,
ell=(b^2+6b+105+8q)/16,

D_j=D_*/(3600b),               Q_j=q^2/3,
G_j=(Q_j-x ell+20+8q/3+D_j)/A,
H_j=ell-G_j,
Y_j=(ell-2G_j)/A-x,
V_j=G_j+xY_j+Y_j^2,
R_j=-qP/(2880b).                                  (FJS1)
```

For a rational function over the official base field, let `Num` denote its
numerator after clearing fixed numerical units and cancelling common
factors. Define

```text
Z_D^j=Num(D_j-Y_jV_j),

Z_R^j=Num(R_j-G_j(ell-G_j)+xQ_j+(A+x)D_j
           +15+23q/4+q^2/8).                     (FJS2)
```

On the inherited `b*(b+3)*D_*!=0` saturation, the original structural
definitions of `G_2,H,Y,V,D,Q_0,R_0,W_0` are jointly equivalent to

```text
G_2=G_j, H=H_j, Y=Y_j, V=V_j,
D=D_j, Q_0=Q_j, R_0=R_j,
Z_D^j=Z_R^j=0.                                    (FJS3)
```

Uncancelled numerator representatives in (FJS2) satisfy

```text
deg(Z_D^j)<=12,       deg_q(Z_D^j)<=6,
deg(Z_R^j)<=8,        deg_q(Z_R^j)<=4.             (FJS4)
```

Use the proved reconstruction `q=5bM/T` from (FJ06). If `m_i` is the
`q`-degree in (FJS4), define

```text
Zhat_i^j(b)=T(b)^m_i Z_i^j(b,5bM(b)/T(b)),
                         i in {D,R}.               (FJS5)
```

These are univariate polynomials with

```text
deg Zhat_D^j<=24,       deg Zhat_R^j<=16.          (FJS6)
```

Consequently the complete coefficient-and-structural endpoint on this chart
is exactly

```text
Bhat=Ehat=Fhat=Xhat=Zhat_D^j=Zhat_R^j=0,
q=5bM/T,                                            (FJS7)
```

together with every printed denominator and inherited saturation. The
selected role-discriminant weld, `P_4`, and arithmetic-lift filters remain.
This is an exact structural compiler, not a common-gcd, ambient-root,
emptiness, role, lift, or critical-node verdict.
