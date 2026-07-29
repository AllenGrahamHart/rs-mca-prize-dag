# L1 Mersenne HNF m=8 order-one cubic three-double linear remainder reduction

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_m8_order_one_cubic_three_double_symmetric_compiler`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the h=7 cubic color profile `2+2+2`

Use the dimensionless variables

```text
q=dr,       a=dU,       b=d^2s_2,       x=a-3.       (TLR1)
```

Put

```text
G=1+q(10d^4+62d^3+163d^2+237d+213)/60
    +q^2(13d^2+55d+76)/72+q^3/48,

H=x^2-8-q/6,
K=48-12x^2+q(-d^2-3d+5)/4-q^2/24,
D_b=b^2+3Hb+3K.                                    (TLR2)
```

Then the fourth HNF coefficient is exactly

```text
D_b=0.                                               (TLR3)
```

Define

```text
B_5=12x^3+6
    +q(d^2+5d+11+(1-d^2-3d)x-(d+2)x^2)/2
    +q^2(d+5-x)/12,
A_5=-x(x^2+q/6).                                    (TLR4)
```

Modulo (TLR3), the fifth HNF coefficient is the affine-linear equation

```text
M_5=(q-d)(A_5b+B_5)+6dG=0.                          (TLR5)
```

For the sixth coefficient, put

```text
k=6x-3+q/2,
t_0=12x-16-q(d+2)/6,
t_1=2-x,
P_0=-x^3+3x^2+30+(x-1)q/2,
m=x^2-9,
N=18-6x,

C_3=4/27,
C_2=(4x^2-2x-15)/3,
C_1=-2xt_0+t_1P_0+km/3+(2kN-k^2)/9,
C_0=t_0^2+t_0P_0+k^2N/9+k^3/27,

A_6=C_1+4H^2/3-4K/9-3HC_2,
B_6=C_0+4HK/3-3KC_2-G.                              (TLR6)
```

Modulo (TLR3), the sixth HNF coefficient is the second affine-linear
equation

```text
M_6=A_6b+B_6=0.                                     (TLR7)
```

Together with the residual conic

```text
35q^2+14q(11d^2+27d+27)
 +120(d^4+4d^3+7d^2+6d+3)=0,                       (TLR8)
```

equations (TLR3), (TLR5), and (TLR7) are an exact p-free necessary core.
Since `q-d=d(r-1)` is saturated, the fifth-equation slope has precisely
the two exceptional loci

```text
x=0                  or                  q=-6x^2.    (TLR9)
```

Off (TLR9), (TLR5) determines `b`; the generic branch therefore reduces to
three variables before any color or official-row sharding. No branch is
declared empty here.
