# L1 Mersenne HNF m=8 order-one cubic three-two-one exceptional-E structural-consistency compiler

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_quadratic_router`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the `E_G=0`, `a_2*S_1*J_*!=0` chart of the fully
  proportional official `h=7` cubic `3+2+1` residue

Retain (FBC1)--(FBC6) and (FEQ1)--(FEQ9). Write `V_E` for the coefficient
filter `V(b)` in (FEQ4), to distinguish it from the structural variable
`V_e`. Put

```text
x=(b+15)/4,                  A=-(b+3)/2,
ell=(b^2+6b+105+8q)/16,

D_e=D_*/(3600b),             Q_e=Q_*/(72D_*),
G_e=-D_*^2L_*/(720bJ_*),     H_e=ell-G_e,
Y_e=(ell-2G_e)/A-x,
V_e=G_e+xY_e+Y_e^2,          R_e=-qP/(2880b).     (FES1)
```

For a rational function over the official base field, let `Num` denote its
numerator after clearing fixed numerical units and cancelling common factors.
Define

```text
Z_D^e=Num(D_e-Y_eV_e),

Z_Q^e=Num(Q_e-A G_e-x ell+20+8q/3+D_e),

Z_R^e=Num(R_e-G_e(ell-G_e)+xQ_e+(A+x)D_e
          +15+23q/4+q^2/8).                       (FES2)
```

On the inherited `b*(b+3)*D_*J_*!=0` saturation, the original structural
definitions of `G_2,H,Y,V,D,Q_0,R_0,W_0` are jointly equivalent to

```text
G_2=G_e, H=H_e, Y=Y_e, V=V_e,
D=D_e, Q_0=Q_e, R_0=R_e,
Z_D^e=Z_Q^e=Z_R^e=0.                              (FES3)
```

The cleared bivariate total-degree bounds are

```text
deg(Z_D^e)<=27,      deg(Z_Q^e)<=13,
deg(Z_R^e)<=21.                                      (FES4)
```

On `S_1!=0`, let `m_i=deg_q Z_i^e` and define

```text
Zhat_i^e(b)=S_1(b)^m_i Z_i^e(b,-S_0(b)/S_1(b)),
                          i in {D,Q,R}.             (FES5)
```

These are univariate polynomials. The complete exceptional coefficient and
structural endpoint on this chart is exactly

```text
V_E(b)=X_E(b)=Zhat_D^e(b)=Zhat_Q^e(b)=Zhat_R^e(b)=0,
q=-S_0/S_1.                                        (FES6)
```

Every printed denominator and inherited saturation remains. The
`S_1=0`, `a_2=0`, and `J_*=0` charts, the selected role-discriminant
weld, `P_4`, and arithmetic-lift filters also remain. This is an exact
structural compiler, not a gcd, unit, root, emptiness, norm,
Frobenius-converse, cyclotomic, exact-fiber, or inner-lift verdict.
