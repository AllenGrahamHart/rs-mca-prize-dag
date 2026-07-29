# L1 Mersenne HNF m=8 order-one cubic three-two-one generic linear-d router

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_coefficient_matrix_router`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the generic `Delta!=0` arm of the official `h=7` cubic color
  profile `3+2+1`

Retain (SQC1)--(SQC7) and (CMR1)--(CMR3). Put

```text
T=G_2+6D,
Q_0=6G_2+AxU-20-8q/3-D,
W_0=Y(A+x)V+15+23q/4+q^2/8,
R_0=G_2H-xQ_0-W_0.                                  (GLD1)
```

Then

```text
Q_6:=(Y-A)V-S=Q_0-qd/3,
W=W_0+q(d^2+7d)/4,
J=qG_2-dT.                                           (GLD2)
```

Define the two quadratics in `d`

```text
P_4=-3qd^2+q(4x-21)d+12R_0,

P_5=qTd^2-(3DH+q^2G_2+3TQ_0)d
       +3q(DH+G_2Q_0),                              (GLD3)
```

and their linear combination

```text
C_1=qT(4x-21)-9DH-3q^2G_2-9TQ_0,
C_0=9q(DH+G_2Q_0)+12TR_0.                           (GLD4)
```

On `E_6=0`, the fourth and fifth coefficient equations are exactly

```text
P_4=0,       C_1d+C_0=0,                            (GLD5)
```

because

```text
3P_5+TP_4=C_1d+C_0.                                 (GLD6)
```

Thus the generic coefficient core has the following exact split.

## The C_1!=0 chart

Reconstruct

```text
d=-C_0/C_1.                                         (GLD7)
```

After this substitution define

```text
P_4_hat=C_1^2 P_4,
E_6_hat=C_1^4 E_6,
C_hat=C_1^4 Conic(q,d),
Phi_hat=C_1^8 Phi(R_D,S_D).                         (GLD8)
```

The complete chart is exactly

```text
P_4_hat=E_6_hat=C_hat=Phi_hat=0                     (GLD9)
```

in `(x,Y,q)`, with the inherited factors and the cleared forms of
`Delta,W,d,q-d` saturated. In particular, this is an overdetermined
four-equation system in three variables for each of the 21 alternative role
packets.

## The C_1=0 chart

Retain

```text
C_1=C_0=P_4=E_6=Conic=Phi=0                         (GLD10)
```

in `(x,Y,q,d)`, together with `Delta*W!=0` and every inherited saturation.
The replacement equations `C_1=C_0=0` are independent of `d`; no division
by their vanishing coefficient is made.

Fixed numerical denominators may be cleared because every official
characteristic exceeds five. No unit, emptiness, norm, Frobenius-converse,
cyclotomic, exact-fiber, or inner-lift verdict is claimed.
