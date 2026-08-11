# `A=1` quadratic double-root heavy-row center-overlap factorization

- **status:** PROVED
- **closure:** at-most-three-free-root adapter from the cubic residual to the split biform
- **consumer:** `rate_half_band_crossing_location`

Retain the extremal split-biform profile in the separated double-root locus
of `(HQC0)`. Put

```text
D_1=a_D g_*S_B^2,
Lambda=ell_alpha ell_beta ell_theta,
J=gcd(Lambda,g_*S_B^2),       j=deg J.              (HRA1)
```

All gcds are homogeneous and defined up to nonzero scalars. Write

```text
Lambda=J Lambda_0,
g_*S_B^2=J H.                                       (HRA2)
```

Then there is a parameter form `T_j` of degree at most `j<=3` such that

```text
a_QS_B B(t,x_*)-a_D L_U0(x_*)C_0(t)
 =Lambda_0(t)T_j(t),                                (HRA3)

G(t,x_*)=H(t)T_j(t)
          =[g_*(t)S_B(t)^2/J(t)]T_j(t).             (HRA4)
```

Thus all but at most `j` roots of the degree-at-most-`e-2` heavy row are
fixed by the supported and correction factors after the center overlaps
are cancelled. In the center-disjoint subcase `J=1`,

```text
G(t,x_*)=c g_*(t)S_B(t)^2                          (HRA5)
```

for one scalar `c`, which may be zero.

Write the split biform as

```text
G(t,X)=sum_(r=0)^(e-2) g_r(X)t^r,
deg_X g_r<=n.                                       (HRA6)
```

For every classified row set `X_cls` not containing `x_*`, the augmented
coefficient vectors obey

```text
(g_r(x))_(x in X_cls union {x_*})
 in RS[F,X_cls union {x_*},n+1],                   (HRA7)

g_r(x_*)=[t^r](H T_j).                              (HRA8)
```

Equations `(HRA7),(HRA8)` are an exact augmented coefficient-MDS gate with
only `j+1<=4` new scalar unknowns in `T_j`.

## Scope

The theorem does not prove that the augmented MDS system has no solution.
It inherits squarefreeness of `S_B` and `gcd(g_*,S_B)=1`; the nonreduced
and supported/correction-collision loci remain outside the claim. The
scalar in `(HRA5)` is not asserted nonzero.
