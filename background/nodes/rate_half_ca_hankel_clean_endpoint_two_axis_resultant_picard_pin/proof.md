# Proof

The bidegree and apolar statements are covariant under a projective change
of the binary domain coordinate. Avoid the finite domain, `x_0`, the roots
of `Q(S;X)`, and the roots of `q_inf` when choosing domain infinity. The
transformed domain locator `G` is still a monic split polynomial of degree
`N`, and all complement identities retain their degrees. In particular
`a(S)!=0` and `deg_z a=m`.

The boundary theorem gives `deg_X B=N`, while interpolation gives
`deg_X A=N-rho`. Take the coefficient of `X^N` in

```text
Q A+H B=G.
```

After making `G` monic, this is exactly `(TAP1)`. Hence `a` is coprime to
`H`, and `beta` is nonzero at every root of `a`.

Take the `X`-resultant of the weld `WB=X-x_0 mod Q`. The root-product formula
gives, up to a nonzero scalar,

```text
Res_X(Q,W)Res_X(Q,B)
 =a^(d+N-1)Q(z;x_0)
 =c a^(d+N-1)A_0S.                                  (1)
```

Let `theta` be a root of `a`. Equation `(TAP1)` gives
`beta(theta)=H(theta)^(-1)!=0`, so `Q` and `B` do not meet at domain
infinity. A finite common root would have to be `x_0` by the weld. The
factorization `Q(z;x_0)=cA_0S`, the coprimality `gcd(a,H)=1`, and the chosen
condition `a(S)!=0` exclude that possibility at `theta`. Therefore
`Res_X(Q,B)` is coprime to `a`.

At `X=x_0`, the original complement assigns the `m-1` distinct supported
factors `A_0` to `W`, while the dual complement assigns the residual factor
`S` to `B`. The product `(1)` has total order `m` there, so these lower
orders are exact. Unique factorization now gives `(TAP3)`.

For the divisor assertion, use the already-proved parameter resultant

```text
Res_z(Q,B)=c q_inf^(T+b)(X-x_0).                    (2)
```

Its `X`-degree is

```text
(T+b)rho+1=b rho+Nm,                                (3)
```

which is the full intersection number of biforms of bidegrees `(rho,m)` and
`(N,b)`. Thus `(2)` accounts for every projective intersection; none is
hidden at domain infinity. Squarefreeness of `q_inf` identifies its `rho`
roots with the reduced divisor `Y_inf`, each carrying intersection order
`T+b`. Equation `(TAP3)` identifies the remaining simple point as `P_*`.
This proves `(TAP4)`.

The divisor of a biform of degree `(N,b)` is the restriction of `O(N,b)`.
Since `Y_inf` is the restriction of `O(0,1)`, `(TAP4)` gives

```text
O_C(N,b)=O_C(P_*+(T+b)Y_inf).
```

Cancel `b+T` copies of the parameter fibre to obtain `(TAP5)`. Its degree is
`Nm-T rho=1` by the endpoint arithmetic. QED.
