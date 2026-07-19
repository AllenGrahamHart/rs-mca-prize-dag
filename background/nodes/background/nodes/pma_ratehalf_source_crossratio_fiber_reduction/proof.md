# Proof - PMA rate-half source cross-ratio fiber reduction

## 1. Affine invariance

Divide the core locator by the three-petal product:

```text
L_C=P_0+LQ_0,       deg P_0<3ell,
deg Q_0=N-3ell=K_0-1.                               (1)
```

The CRT label polynomial changes under (XR1) as
`E_c'=alpha E_c+beta`. Linearity and (1) give

```text
P_*'=alpha P_*+beta P_0,
Y'=alpha Y+beta Q_0.                                (2)
```

Map a contributor `H` to

```text
H'=alpha H+beta Q_0.
```

Its degree remains at most `K_0-1`, and on the core

```text
Y'-H'=alpha(Y-H).
```

Thus all agreement sets and list multiplicities are preserved. Choosing
`alpha=(c_2-c_1)^(-1)` and `beta=-alpha c_1` proves (XR2).

If a source quotient word `Y` lies in `RS(C,K_0)`, then its polynomial
representative has degree at most `K_0-1`. In

```text
L_CE_c=P_*+LY,
```

the right side has degree at most `N`. If `E_c` were nonconstant, the left
side would have degree `N+deg E_c>N`, a contradiction. Hence `E_c` is
constant and the three labels are equal. Conversely, a constant label gives
`Y` equal to a scalar multiple of `Q_0`, which lies in `RS(C,K_0)`. This proves
the claimed one-dimensional intersection and two-dimensional quotient.

## 2. CRT idempotent factors

For the label vector `(0,1,0)`, the CRT polynomial `E_2` vanishes modulo
`L_1` and `L_3`, so `L_1L_3|E_2`. The identity

```text
L_CE_2=P_2+LY_2
```

has both the left side and `LY_2` divisible by `L_1L_3`; therefore
`L_1L_3|P_2`. Since `deg P_2<3ell`, this gives
`P_2=L_1L_3R_2` with `deg R_2<ell`. Injectivity of the source-numerator map
makes `R_2` nonzero. The same argument for `(0,0,1)` gives (XR3).

The core is disjoint from all petals, so `L_1L_2` has no core root. Hence the
core zeros of `P_3` are exactly those of `R_3`, proving (XR4).

## 3. Weighted cross-ratio fiber

At a point lying in exactly two of the three agreement sets, pairwise overlap
contributes one to

```text
u_12+u_13+u_23-tau.
```

At a point lying in all three, the three pair intersections minus one triple
intersection contribute two. Thus this aligned gcd bonus is exactly

```text
sum_(x in C) max(0,r_x-1).
```

The predecessor bounds it below by `2(K_0-1)+3a`. Every point of `B_3` has
weight at most two, so deleting `B_3` loses at most `2(ell-1)`. Substituting
`K_0-1=ell+b-2` proves (XR5).

At a remaining overlap point, at least two `H_i` take one common value `h(x)`
and agree with the source word. The equation

```text
P_2(x)+lambda P_3(x)+L(x)h(x)=0
```

has nonzero coefficient `P_3(x)`, and solving it gives (XR6). Triple points
are counted twice, consistently with their overlap weight. If the certificate
is absent, no cell has three contributors, and the predecessor's `8n` sum
applies.
