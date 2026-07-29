# L1 Mersenne HNF m=8 order-one cubic three-two-one generic fully-proportional parameter reduction

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_doubly_singular_quadratic_quotient_router`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the generic `Delta!=0`, fully proportional
  `N_1=U_1=N_0=U_0=0` arm of one official `h=7` cubic `3+2+1` role packet

Retain (DQR1)--(DQR9). Put

```text
b=a_d+6=4x-15,

P=40b(b^2-6b+27)+42q(11b+15),
Q=480b^2+12960+5544q,
T_c=3240+3402q+315q^2.                              (FPR1)
```

The conic proportionality equations `N_1=N_0=0` force

```text
b!=0,
2880bR_0+qP=0,
F_N:=6P^2-bPQ+2880b^2T_c=0.                        (FPR2)
```

Equivalently, `R_0=-qP/(2880b)` and `F_N=0`.

For the selected role packet write

```text
Phi(X,Y)=c_2X^2+c_1XY+c_0Y^2,
delta_Phi=c_1^2-4c_2c_0.                           (FPR3)
```

Irreducibility gives `c_0*delta_Phi!=0`. The role proportionality equations
`U_1=U_0=0` are exactly

```text
18c_0S_0+9c_1R+c_0qa_d=0,

c_0^2(q^2a_d^2+144qR_0)=81delta_Phi R^2.           (FPR4)
```

The parenthesized expression on the left of the second line is the
discriminant of `P_4` as a quadratic in `d`. Thus the complete fully
proportional core is exactly

```text
C_1=M_1=C_0=M_0=0,
2880bR_0+qP=0,
F_N=0,
18c_0S_0+9c_1R+c_0qa_d=0,
c_0^2 disc_d(P_4)=81delta_Phi R^2,
P_4=0,                                               (FPR5)
```

together with `b*Delta*W!=0` and every inherited saturation. In particular,
`R_0` and `S_0` are rationally reconstructed from `(x,Y,q)` and the selected
role packet, while `d` is only a root of the printed quadratic `P_4`.

This is an exact parameter reduction, not a square-class contradiction:
the coefficient variables live in the ambient quadratic field, where a
prime-field nonsquare may become a square. No unit, emptiness, norm,
Frobenius-converse, cyclotomic, exact-fiber, or inner-lift verdict is claimed.
