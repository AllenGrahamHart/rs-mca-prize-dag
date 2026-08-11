# `A=1` quadratic gap-four minimum-pair rank-two normal form

- **status:** PROVED
- **closure:** exact affine split-pencil coordinate at pair union `rho+3`
- **consumer:** `rate_half_band_crossing_location`

Retain either core-one quadratic `u=4` arm and distinct supported slopes
with

```text
|S_alpha union S_beta|=rho+3.                       (QR21)
```

Choose an orientation `(sigma,tau)` as follows. Either orientation is valid
in the double-root arm. In the two-simple arm, use an endpoint with positive
`r` as `sigma` if one exists; if both endpoint deficits vanish, use either.
Put

```text
X=S_tau\S_sigma,       m=|X|=r_sigma+3,
L_X(T)=product_(x in X)(T-x).                       (QR22)
```

Let `eta_x!=0` be the contracted two-center source weights from the complete
coefficient chain. There are linearly independent homogeneous parameter
forms `A,B` of degree at most `e` such that

```text
eta_x L_X'(x) Qbar(U,V;x)=A(U,V)+xB(U,V)   (x in X). (QR23)
```

Every right side in `(QR23)` has exact degree `e`, is squarefree, and has
all its roots among the `T=3e+3` supported slopes. In particular, distinct
points of `X` give distinct projective row forms: there are no clone classes
on the minimum boundary.

Put

```text
G=gcd(A,B),       g=deg G.                           (QR24)
```

Then `G` is squarefree, contains `tau` but not `sigma`, and the roots outside
`G` of the `m` forms `A+xB` are pairwise disjoint. Consequently

```text
g+m(e-g)<=3e+3,
g>=max(1,ceil((r_sigma e-3)/(r_sigma+2))).           (QR25)
```

Every supported root of `G` has its assigned center on the codeword pencil
through the endpoint centers. Thus

```text
3(g+1)<=rho+3-r_sigma-sum_(delta in Z(G))r_delta.   (QR26)
```

The reverse orientation has its own analogous rank-two coordinate and gcd.

## Scope

The theorem classifies but does not exclude pair union `rho+3`. It does not
identify the two oriented gcds, bound the residual split-pencil roots beyond
`(QR25)`, or close either quadratic packet.
