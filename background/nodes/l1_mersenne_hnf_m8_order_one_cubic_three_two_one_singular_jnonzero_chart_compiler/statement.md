# L1 Mersenne HNF m=8 order-one cubic three-two-one singular-J-nonzero chart compiler

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_coefficient_matrix_router`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the determinant-singular `Delta=0`, `J!=0` arm of the official
  `h=7` cubic color profile `3+2+1`

Retain (SQC1)--(SQC7) and (CMR1)--(CMR4). On this arm, `H!=0`, and

```text
x=0  if and only if  G_2=0.                          (SJC1)
```

This gives the following exact disjoint charts.

## The x=0 chart

Here

```text
G_2=0,       Y=L_2/6=(q+30)/12,
A=6,         V=Y^2,       D=Y^3,
H=6Y,        J=-6dY^3.                               (SJC2)
```

Put

```text
P_W^+=q^3+126q^2+(4356+504d+72d^2)q+31320,

A_+(q)=q^3+90q^2+3132q+57240,
B_+(q)=8q^3+864q^2+30528q+250560,
P_L^+=A_+(q)d-B_+(q).                                (SJC3)
```

On `Y!=0`, the three coefficient equations are exactly

```text
P_W^+=0,
P_L^+=0,
K_6+Y^6+L_3Y^3=0.                                   (SJC4)
```

The conic and one official quadratic role equation remain. If `A_+(q)!=0`,
the first two equations reconstruct `d=B_+(q)/A_+(q)`. If `A_+(q)=0`, they
instead require `B_+(q)=0`; this exceptional chart is retained.

## The x!=0 chart

Here `G_2!=0`. Define

```text
N=G_2^2+xD,
Z=N+6DG_2,
P=3x(6G_2+AxU-20-D)-8qx-3G_2H.                     (SJC5)
```

Then `N*Z!=0`, and the singular determinant and sixth-coefficient equations
give the exact reconstruction

```text
d=P/(qx),
q^2xN-PZ=0.                                         (SJC6)
```

For a displayed expression below, a vertical bar means substitute
`d=P/(qx)`. Define the denominator-cleared polynomials

```text
W_hat=(qx)^2 W|_(d=P/(qx)),
E_hat=(qx)^4 (DG_2H-xK_6)|_(d=P/(qx)),
C_hat=(qx)^4 Conic(q,d)|_(d=P/(qx)),
Phi_hat=(qx)^8 Phi(R_D,S_D)|_(d=P/(qx)).             (SJC7)
```

Fixed numerical denominators may be cleared because every official
characteristic exceeds five. The complete `x!=0` singular-`J!=0`
coefficient core is exactly the five-equation system

```text
q^2xN-PZ=0,       W_hat=0,       E_hat=0,
C_hat=0,          Phi_hat=0                              (SJC8)
```

in `(x,Y,q)`, with `d` reconstructed by (SJC6), saturated by the inherited
nonzero factors and by `qxG_2NZP(q^2x-P)`. Thus this chart has three rather
than four variables. No unit, emptiness, norm, Frobenius-converse,
cyclotomic, exact-fiber, or inner-lift verdict is claimed.
