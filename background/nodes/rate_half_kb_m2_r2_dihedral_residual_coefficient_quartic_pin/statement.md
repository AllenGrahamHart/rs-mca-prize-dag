# KoalaBear m2 r2 residual coefficient-quartic pin

- **status:** PROVED
- **scope:** the surviving `n=3,6` full-V4 dihedral profiles
- **dependency:**
  `rate_half_kb_m2_r2_dihedral_residual_star_graph_rigidity`
- **consumer:** `rate_half_band_closure`

Let `v` be the deck involution of the `Z` projection on the rational outer
component `C`, and let `Y` be its other degree-two projection. The map

```text
p -> (Y(p),Y(vp))
```

is birational onto a symmetric bidegree-`(2,2)` sibling correspondence
`K`. After geometric coordinate changes normalize the endpoint quadratic
to `h(t)=t^2`. In elementary symmetric coordinates

```text
sigma=y_0+y_1,       pi=y_0*y_1,
```

write the affine equation of `K` as

```text
k(sigma,pi)
 = A*pi^2+B*sigma*pi+C*(sigma^2-2*pi)+D*pi+E*sigma+F.
```

If `S=t+s` and `P=t*s` are the unordered-pair coordinates of the two roots
of the source quadratic `H(T,X)`, then its residual birational coefficient
image has the exact equation

```text
Q(S,P)=k(S^2-2P,P^2)=0.                            (KBMQ-1)
```

Explicitly,

```text
Q=A P^4+B S^2 P^2-2B P^3+C S^4-4C S^2 P
  +(2C+D)P^2+E S^2-2E P+F.
```

Actual existence forces this polynomial to have degree four and to be the
irreducible rational plane quartic already supplied by the residual source
branch. Thus both residual profiles are reduced to the singularity and
source-cover realization of one canonical quartic pullback.

This theorem does not construct or delete either profile, move an owner or
payment, or close an `m=2`, endpoint, KoalaBear, or Prize row.

## Falsifier

A non-birational sibling map, a nonsymmetric or non-`(2,2)` sibling image,
a source coefficient pair not satisfying `(KBMQ-1)`, or an additional
degree-four component of the pullback polynomial.
