# Proof - L1 Mersenne HNF m=8 order-one cubic three-two-one scaled quadratic-core compiler

The HNF formulas give

```text
d l_1=6,       d^2l_2=L_2,       d^3l_3=L_3,
d^4l_4=L_4,   d^5l_5=-6dK_6/(q-d),   d^6l_6=K_6.    (1)
```

Multiply (TQC6) by the appropriate powers of `d` and use (SQC1). This gives
`d a=A`, `d^2g_2=G_2`, `d^2v=V`, `d^3g_3=-YV`, and `d^3B=S`, exactly as
in (SQC3). The scaled role numerator is `R` there as well.

Scale the last equation of (TQC5) by `d^6`. Substituting `d^3g_3=-YV`
gives

```text
(YV)^2-AYV^2-SYV
 =YV((Y-A)V-S)=K_6,                                  (2)
```

which is `E_6=0`. Since `K_6!=0`, (2) also proves `D=YV!=0`.

Let `C_4,C_5` be the scaled fourth and fifth residuals, right side minus
left side in (TQC5). Before using (2), direct substitution gives

```text
C_4=G_2^2+AU G_2+V(A(x-Y)-2xY)+Sx-L_4,
C_5=V(G_2(A-2Y)-AYU)+SG_2+6dK_6/(q-d).              (3)
```

Using

```text
DS=D(Y-A)V-K_6-E_6                                  (4)
```

in `D C_4` and `D C_5` yields the polynomial identities

```text
E_4=D C_4+xE_6,
E_5=-(q-d)(D C_5+G_2E_6).                           (5)
```

Because `D(q-d)!=0`, equations (5) prove that (SQC5) is equivalent to all
three equations (TQC5).

Finally (2) gives

```text
DS=D(Y-A)V-K_6=Y(Y-A)V^2-K_6=S_D.                  (6)
```

By definition `DR=R_D`. Every official role packet is homogeneous of degree
two, so

```text
Phi(R_D,S_D)=Phi(DR,DS)=D^2 Phi(R,S).               (7)
```

The multiplier `D^2` is nonzero. Thus (7) proves the exact role transport
(SQC7), completing the equivalence. QED.
