# L1 Mersenne HNF m=8 order-one cubic three-two-one generic fully-proportional structural-consistency compiler

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_q_quotient_router`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the `E_G*a_2*rho_1!=0` generic coefficient chart of the fully
  proportional official `h=7` cubic `3+2+1` residue

Retain (FCR1)--(FCR8), (FBC1)--(FBC6), and (FQR1)--(FQR10). To distinguish
the inherited structural variable from the quotient remainder, put

```text
x=(b+15)/4,               A=-(b+3)/2,
ell=(b^2+6b+105+8q)/16,

D_c=D_*/(3600b),          Q_c=Q_*/(72D_*),
G_c=-F_*/(600bE_G),       H_c=ell-G_c,
Y_c=(ell-2G_c)/A-x,
V_c=G_c+xY_c+Y_c^2,
R_c=-qP/(2880b).                                      (FSC1)
```

For a rational function over the official base field, let `Num` denote its
numerator after clearing fixed numerical units and cancelling common factors.
Define

```text
Z_D=Num(D_c-Y_cV_c),

Z_Q=Num(Q_c-A G_c-x ell+20+8q/3+D_c),

Z_R=Num(R_c-G_c(ell-G_c)+xQ_c+(A+x)D_c
        +15+23q/4+q^2/8).                            (FSC2)
```

On the inherited `b*(b+3)*D_*E_G!=0` saturation, the original structural
definitions of `G_2,H,Y,V,D,Q_0,R_0,W_0` are jointly equivalent to

```text
G_2=G_c, H=H_c, Y=Y_c, V=V_c,
D=D_c, Q_0=Q_c, R_0=R_c,
Z_D=Z_Q=Z_R=0.                                      (FSC3)
```

The cleared bivariate degree bounds are

```text
deg(Z_D)<=18,       deg(Z_Q)<=10,       deg(Z_R)<=15. (FSC4)
```

On the generic quotient chart `rho_1!=0`, let `m_i=deg_q Z_i` and define

```text
Zhat_i(b)=rho_1(b)^m_i Z_i(b,-rho_0(b)/rho_1(b)),
                       i in {D,Q,R}.                (FSC5)
```

These are univariate polynomials. The complete generic coefficient and
structural endpoint is exactly

```text
U(b)=Zhat_D(b)=Zhat_Q(b)=Zhat_R(b)=0,
q=-rho_0/rho_1,                                    (FSC6)
```

together with every printed denominator and inherited saturation. The
selected role-discriminant weld, `P_4`, and arithmetic-lift filters remain.
This is an exact structural compiler, not a gcd, unit, emptiness, norm,
Frobenius-converse, cyclotomic, exact-fiber, or inner-lift verdict.
