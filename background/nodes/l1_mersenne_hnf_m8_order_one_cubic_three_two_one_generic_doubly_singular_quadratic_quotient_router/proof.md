# Proof - L1 Mersenne HNF m=8 order-one cubic three-two-one generic doubly-singular quadratic-quotient router

Because `q!=0`, equation `P_4=0` in (GLD3) is exactly (DQR2). In this
quotient,

```text
d^2=alpha d+beta,
d^3=(alpha^2+beta)d+alpha beta,
d^4=(alpha^3+2alpha beta)d+alpha^2beta+beta^2.       (1)
```

The differences between the left and right sides in (1) are respectively
`1`, `d+alpha`, and
`d^2+alpha d+alpha^2+beta` times
`d^2-alpha d-beta=-P_4/(3q)`.

Expand the conic as

```text
C=120d^4+480d^3+(840+154q)d^2
  +(720+378q)d+360+378q+35q^2.                     (2)
```

Substitution of (1) into (2), followed by multiplication by `9q^2`, gives
the coefficients (DQR3). The preceding difference formulas give the exact
quotient term `-3qQ_C(d)P_4`, proving (DQR4).

Now let `Phi` be one official homogeneous quadratic. From (DQR5) and
`Q_6=Q_0-qd/3`,

```text
S=(Y-A)V-Q_6=S_0+qd/3.                              (3)
```

On `E_6=0`, the scaled-core compiler gives
`(R_D,S_D)=D(R,S)`. Since `D!=0` and `Phi` is homogeneous, its transported
role equation is equivalent to `Phi(R,S)=0`. Expanding (3) gives a quadratic
in `d` with leading coefficient `c_0q^2/9`. Multiplying by 27 and adding
`c_0qP_4` cancels this quadratic term; collecting the remaining terms gives
exactly (DQR6)--(DQR7).

On the doubly singular coefficient locus, the dependency proves that
`P_4=Conic=0` recovers `E_6=0`, while the four vanished coefficient
functions recover the other two coefficient equations. By (DQR4), under
`P_4=0` the conic is equivalent to `N_1d+N_0=0`; by (DQR7), its role
equation is equivalent to `U_1d+U_0=0`. This proves (DQR8).

If `N_1!=0`, the first line reconstructs `d=-N_0/N_1`, and the second is
equivalent to `Xi=0`. If `N_1=0`, the first line gives `N_0=0`; `U_1!=0`
then reconstructs `d=-U_0/U_1`. If both coefficients vanish, their two
equations are exactly `N_0=U_0=0`. Conversely, each chart reconstructs both
linear equations and hence (DQR8). Clearing denominators is reversible under
the printed coefficient and inherited saturations. QED.
