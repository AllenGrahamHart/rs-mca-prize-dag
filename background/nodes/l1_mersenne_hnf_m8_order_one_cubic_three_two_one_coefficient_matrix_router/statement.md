# L1 Mersenne HNF m=8 order-one cubic three-two-one coefficient-matrix router

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_scaled_quadratic_core_compiler`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the official h=7 cubic color profile `3+2+1`

Retain (SQC1)--(SQC7), and define

```text
H=G_2+AU,
W=Y(A+x)V+L_4,
J=(q-d)G_2-6dD,
Delta=G_2J+x(q-d)D.                                  (CMR1)
```

The fourth and fifth equations in (SQC5) are the two-by-two linear system

```text
D G_2 H-xK_6=DW,
(q-d)D^2H+JK_6=0,                                   (CMR2)
```

whose determinant is `D Delta`. Since `D!=0`, the coefficient core has the
following exact split.

On `Delta!=0`, equations (CMR2) are equivalent to

```text
Delta H-WJ=0,
Delta K_6+(q-d)D^2W=0.                              (CMR3)
```

On `Delta=0`, consistency forces `WJ=0`, and there are exactly two
subbranches:

```text
J=0:       x=H=W=0;

J!=0:      W=0,
           (q-d)D^2H+JK_6=0.                       (CMR4)
```

Every branch retains `E_6=0`, the conic, one quadratic role equation
`Phi(R_D,S_D)=0`, and all inherited saturations.

There is also a useful exact `x=0` chart. Put `L=L_2`. Then

```text
G_2=L/2-3Y,
H=L/2+3Y,
V=Y^2-3Y+L/2,
M=6G_2-L_3-D.                                       (CMR5)
```

The three coefficient equations become

```text
C_0=96Y^3-144Y^2+(720+24q)Y
     +q^2+4q(d^2+7d+8)-660=0,

F_6=DM-K_6=0,
F_5=(q-d)DH+JM=0.                                   (CMR6)
```

Thus `x=0` leaves a cubic equation in `Y`. In its determinant-singular
`J=0` subbranch, `H=W=0` further gives

```text
Y=-L/6,
V=(q+30)(q+102)/144,

F_J=d(q^2+132q+2916)+144q=0,
F_W=q^3+126q^2+(5364-504d-72d^2)q+87480=0.          (CMR7)
```

Together with the conic, (CMR7) is an explicit three-equation endpoint in
only `(q,d)`. No unit, emptiness, norm, or lift verdict is claimed.
