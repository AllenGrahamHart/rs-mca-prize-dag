# L1 Mersenne HNF m=8 order-one cubic three-two-one generic doubly-singular quadratic-quotient router

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_double_linear_d_router`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the generic `Delta!=0`, doubly singular
  `C_1=M_1=C_0=M_0=0` arm of the official `h=7` cubic color profile
  `3+2+1`

Retain (GLD1)--(GLD10) and (GDL1)--(GDL5). Put

```text
a_d=4x-21,       alpha=a_d/3,       beta=4R_0/q.    (DQR1)
```

The inherited `q!=0` saturation makes `P_4=0` equivalent to the quadratic
quotient relation

```text
d^2=alpha d+beta.                                   (DQR2)
```

Define the denominator-cleared conic remainder

```text
N_1=q^2(40a_d^3+480a_d^2+(2520+462q)a_d+6480+3402q)
       +2880qR_0(a_d+6),

N_0=qR_0(480a_d^2+5760a_d+30240+5544q)
       +17280R_0^2+q^2(3240+3402q+315q^2).          (DQR3)
```

Then

```text
9q^2 Conic =N_1d+N_0-3qQ_C(d)P_4,                 (DQR4)

Q_C(d)=120(d^2+alpha d+alpha^2+beta)
        +480(d+alpha)+840+154q.
```

For one of the 21 alternative official role packets, write

```text
Phi(X,Y)=c_2X^2+c_1XY+c_0Y^2,
S_0=(Y-A)V-Q_0.                                     (DQR5)
```

Irreducibility gives `c_0!=0`. Define

```text
U_1=9q(c_1R+2c_0S_0)+c_0q^2a_d,
U_0=27(c_2R^2+c_1RS_0+c_0S_0^2)+12c_0qR_0.         (DQR6)
```

On `E_6=0`, the homogeneous transported role equation obeys

```text
27Phi(R,S_0+qd/3)+c_0qP_4=U_1d+U_0.                (DQR7)
```

Consequently the complete doubly singular generic core is exactly

```text
C_1=M_1=C_0=M_0=0,
P_4=0,
N_1d+N_0=0,
U_1d+U_0=0,                                        (DQR8)
```

with `Delta*W!=0` and every inherited saturation. Put

```text
Xi=N_1U_0-U_1N_0.                                  (DQR9)
```

There are three exact disjoint charts.

1. If `N_1!=0`, reconstruct `d=-N_0/N_1` and retain `Xi=0`.
2. If `N_1=0` and `U_1!=0`, retain `N_0=0` and reconstruct
   `d=-U_0/U_1`.
3. If `N_1=U_1=0`, retain `N_0=U_0=0` and `P_4=0`; this is the only
   quotient-proportional chart which still retains `d`.

On the rational charts, substitute into `P_4` and all generic and inherited
nonzero factors. Thus every other doubly singular packet is a parameter-only
system in `(x,Y,q)`. No unit, emptiness, norm, Frobenius-converse,
cyclotomic, exact-fiber, or inner-lift verdict is claimed.
