# `A=1` first-degree double-root marked Hankel determinant gate

- **status:** PROVED
- **closure:** primitive-kernel cofactors turn the cube packets into explicit Hankel determinants
- **consumer:** `rate_half_band_crossing_location`

Put

```text
e=ceil((rho-1)/3),       rho=3e-1.                    (MHD1)
```

All equalities below may be normalized by one nonzero base-field scalar.
The row `nu(x)` is the monomial evaluation row in the coefficient convention
for the residual apolar polynomial.

## Core-free cubic arm

Let `M_0(U,V)` be the core-free residual syndrome Hankel pencil of size
`rho x (rho+1)`, and let `q` be the primitive coefficient vector of
`Q(U,V;X)`. There is a nonzero binary form `D_0` of degree

```text
Delta_0=rho-e=2e-1                                      (MHD2)
```

such that the signed maximal-minor vector of `M_0` is `D_0q`. Hence, for

```text
M_0[x]=stack(M_0,nu(x)),
```

one has

```text
det M_0[x]=D_0 Q(U,V;x).                              (MHD3)
```

Let `L` be the root set of the light-row locator `G_L` in a retained
gap-one cubic double-root packet. Then

```text
(product_(x in L) det M_0[x])
 (det M_0[x_s])^2 det M_0[x_d]
 =D_0^(3(rho+3)) Res_X(Q,P_3).                        (MHD4)
```

Consequently the right side of `(MHD4)` has the exact linear/quadratic-cube
factorization from `(LRF3)--(LRF4)`. Individually, if

```text
g_x=gcd(Q(U,V;x),H),       K_x=Q(U,V;x)/g_x,          (MHD5)
```

then

```text
I_0=0: deg K_s=deg K_d=1;
I_0=1: deg K_s=2, deg K_d=1,                          (MHD6)
```

and `det M_0[x]/(D_0g_x)=K_x`.

## Core-one quadratic arm

Let `d=rho-1` and let `M_1(U,V)` be the core-one residual symmetric middle
Hankel pencil of size `(d+1) x (d+1)` and generic rank `d`. For its
primitive kernel vector `q`,

```text
adj M_1=D_1 q q^T,       deg D_1=e-2.                (MHD7)
```

For every `x` and every `tau in F^x`, the rank-one marked determinant is

```text
det(M_1+tau nu(x)nu(x)^T)=tau D_1 Q(U,V;x)^2.         (MHD8)
```

At the double heavy root `x_*` of the `u=4` quadratic packet, put

```text
g_*=gcd(Q(U,V;x_*),H),       deg g_*=e-6.             (MHD9)
```

If `S_B` is the binary quadratic cutting out the pushforward of the
degree-two divisor `B` in `(QG44)`, then for some `c in F^x`,

```text
Q(U,V;x_*)=c g_* S_B^3,                              (MHD10)
det(M_1+tau nu(x_*)nu(x_*)^T)
 =tau c^2 D_1 g_*^2 S_B^6.                           (MHD11)
```

In characteristic three, `(MHD10)` gives the exact affine test

```text
d/dz (Q(z;x_*)/g_*(z))=0.                            (MHD12)
```

## Scope

These identities are necessary gates, not exclusions. They expose the
remaining non-cube problem as a factorization of explicit Hankel minors or
rank-one updated Hankel determinants. No positivity of a Cauchy--Binet
expansion, irreducibility of `Q`, or base-field sixth root of `c^2` is
asserted.
