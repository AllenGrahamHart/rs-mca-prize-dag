# L1 Mersenne HNF m=8 order-one cubic three-two-one scaled quadratic-core compiler

- **status:** PROVED
- **dependencies:** `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_common_quadratic_compiler`, `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_official_frobenius_role_split`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the official h=7 cubic color profile `3+2+1`

Put

```text
x=dg_1,       Y=dy,       q=dr,       A=6-2x,       U=x+Y.            (SQC1)
```

Define the scaled HNF coefficients

```text
L_2=15+q/2,
L_3=20+q(d+8)/3,
L_4=15+q(d^2+7d+23)/4+q^2/8,
K_6=1+q(10d^4+62d^3+163d^2+237d+213)/60
       +q^2(13d^2+55d+76)/72+q^3/48.                (SQC2)
```

The triangular variables from (TQC3) and (TQC6), scaled by powers of `d`,
are

```text
G_2=(L_2-x^2-A(2x+Y))/2,
V=G_2+xY+Y^2,
S=L_3+2YV-2xG_2-A(V+xU+G_2),
R=A(3Y^2+2xY+G_2),
D=YV.                                                  (SQC3)
```

Here `S=d^3B`, while `R` is `d^3` times the role numerator in (TRW1), so
their ratio is unchanged. On the inherited saturation

```text
d(q-d)K_6!=0,                                         (SQC4)
```

the three remaining coefficient equations (TQC5) are exactly

```text
E_6=D((Y-A)V-S)-K_6=0,

E_4=D(G_2^2+AU G_2-Y(A+x)V-L_4)-xK_6=0,

E_5=(q-d)(Y^2V^2(G_2+AU)+G_2K_6)-6dK_6D=0.          (SQC5)
```

In particular, `E_6=0` and `K_6!=0` force `D=YV!=0`. Put

```text
R_D=DR,
S_D=Y(Y-A)V^2-K_6.                                   (SQC6)
```

Then `E_6=0` gives `(R_D,S_D)=D(R,S)`. For any one of the 21 homogeneous
quadratic official role packets `Phi` from (FRS1)--(FRS4), its role equation
is therefore exactly

```text
Phi(R_D,S_D)=0.                                      (SQC7)
```

Consequently each official `3+2+1` branch is the conic together with
`E_4=E_5=E_6=0` and one explicit quadratic equation (SQC7), all in
`(x,Y,q,d)`. Rational numerical denominators in (SQC2)--(SQC3) may be
cleared once because every official characteristic exceeds five. This is
an exact triangular compiler, not a unit verdict.
