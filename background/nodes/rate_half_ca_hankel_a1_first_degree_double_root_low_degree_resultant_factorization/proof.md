# Proof

We first record the norm calculation for a line-bundle section. Let `C` have
bidegree `(d,e)` and let the domain projection to the parameter line be
finite flat of degree `d`. Let

```text
L=O_C(a,-e-1),       div(W)=D_+-D_-,                 (1)
```

where `D_+,D_-` are effective and disjoint. Let `S_+,S_-` be homogeneous
binary forms cutting out their parameter pushforwards. If `q_d(U,V)` is the
leading homogeneous `X` coefficient of `Q`, comparison with the standard
affine frame of `L` gives

```text
Norm(W)=c S_+/(S_- q_d^a)                            (2)
```

for one `c in F^x`.

Indeed, the divisor of the norm is the pushforward of `D_+-D_-` minus `a`
times the parameter divisor cut out by `q_d`, plus the parameter-infinity
term contributed by `-(e+1)`. The degree identity

```text
deg(D_+)-deg(D_-)=ae-(e+1)d                          (3)
```

makes the infinity coefficient in `(2)` exact. This divisor argument works
for the finite reduced total-quotient algebra and does not require `C` to be
irreducible.

The resultant cube gate says, for the locator numerator `P`,

```text
Res_X(Q,P)/(q_d^b H^d)=Norm(W)^3,       b=deg P.      (4)
```

In every branch here,

```text
b=3a.                                                 (5)
```

To check `(5)`, in the core-free cubic case the heavy factor has degree
`rho-6`, so `deg G_L=3rho+6` and

```text
deg P_3=3rho+9=3(rho+3).                             (6)
```

In the core-one quadratic case, `G` has degree `N-1`, the heavy factor again
has degree `rho-6`, and hence `deg G_L=3rho+5`; therefore

```text
deg P_2=3rho+6=3(rho+2).                             (7)
```

Substitute `(2),(5)` into `(4)`. The complete leading-coefficient factor
cancels and gives the uniform identity

```text
S_-^3 Res_X(Q,P)=c^3 H^d S_+^3.                     (8)
```

For a no-ordinary cubic packet, the radical quotient is a section of
`O_C(rho+3,-e-1)` with divisor `A`. Thus `S_-=1`, `S_+=S_A`, and `(8)` is
`(LRF3)`.

For the ordinary cubic packet its divisor is `A+B-R_0`. The negative point
lies over the supported slope `L_0=0`, so `S_-=L_0`, `S_+=S_AB`, and
`H=L_0H_0`. Equation `(8)` becomes

```text
L_0^3 R_3=c^3 L_0^rho H_0^rho S_AB^3.               (9)
```

Cancel `L_0^3` to obtain `(LRF4)`.

For the quadratic double-root packet, the radical quotient is a section of
`O_C(rho+2,-e-1)` with effective divisor `B` of degree two. Hence
`S_-=1`, `S_+=S_B`, and `d=rho-1`; equation `(8)` is `(LRF7)`.

Finally use `rho=3e-1`. The two resultant degrees are

```text
deg R_3=e deg P_3=3(rho+3)e=(rho+3)(rho+1),
deg R_2=e deg P_2=3(rho+2)e=(rho+2)(rho+1).          (10)
```

Expanding the right sides of `(LRF3),(LRF7)` gives respectively
`rho(rho+4)+3` and `(rho-1)(rho+4)+6`, equal to `(10)`. The ordinary
formula has the same total degree as `(LRF3)`. This proves `(LRF8)` and the
theorem. QED.
