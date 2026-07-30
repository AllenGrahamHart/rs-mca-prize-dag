# KoalaBear m2 r2 dihedral outer-factor reduction

- **status:** PROVED
- **scope:** the residual actual KoalaBear `(m,r,delta)=(2,2,4)` row
- **dependencies:** `rate_half_kb_m2_r2_full_v4_source_genus_drop` and the
  exact six-pole source profile
- **consumer:** `rate_half_band_closure`

Let `Gamma` be the actual source normalization and let `C` be the
normalization of its bidegree-`(2,2)` outer image. Then

```text
g(C)=0.
```

For source genus zero this follows from the full-V4 quotient directly. For
source genus one, the first deck lift is a fixed-point-free two-torsion
translation. The second endpoint involution cannot also be a translation,
because then it would commute with the source involution rather than
conjugate it to its product with the first lift. It is therefore a
four-fixed-point elliptic reflection, as is its product with the first
lift; V4 Riemann-Hurwitz again gives a rational quotient.

The two degree-two projections `Y,Z:C->P1` have distinct deck involutions.
They generate a finite dihedral group `D_n`, because the common function

```text
F(Y)=F(Z)
```

has finite deck group. Consequently the outer degree-30 map has a geometric
Dickson/Chebyshev right factor

```text
F=G composed q_n,       deg(q_n)=n,       n|30.
```

The six distinct poles of `F`, all of order five, reduce the factor degree
to

```text
n in {2,3,5,6}.                                     (KBMD-1)
```

For `n=2,3,6`, every selected pole fiber of `q_n` is unramified and `G` has
respectively three, two, or one pole of order five. For `n=5`, `G` has one
generic order-five pole and one simple pole at the totally ramified value
of `q_5`. Degrees `10,15,30` are impossible because a tame dihedral quotient
has ramification indices only `1,2,n`: without index five, an unramified
pole fiber already contains more than six points.

The full-V4 cover `Gamma->C=P1` has exact branch data:

```text
g(Gamma)=0: three branch values, inertia a,c,ac;
g(Gamma)=1: four branch values, inertia c,c,ac,ac.
```

No one of the four factor degrees is deleted. This proves no source/active
coefficient realization, carrier/data/slope owner, payment, `u=2` close,
adjacent certificate, or Prize row.

## Falsifier

An elliptic outer `(2,2)` component, a non-dihedral pair of degree-two
projections, a factor degree outside `(KBMD-1)`, or a full-V4 branch passport
outside the two printed rows.
