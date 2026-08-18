# Cycle 517: projective-image degree router

## Result: PROVED conic-composition dichotomy

The residual scalar-space gcd has at most 310 official-domain roots by the
exact 218-fold occupancy deficit. After dividing that gcd, the primitive
three-dimensional scalar space defines a basepoint-free projective map. If
its polynomial degree is `d`, its image-curve degree is `c`, and its map
degree is `e`, pullback degree gives

```text
d=ec,       c>=2.
```

One projective evaluation normal has at most `e` full-coordinate
preimages. The endpoint therefore splits exactly as follows.

```text
c=2:
  W_hom=span{A^2,AB,B^2} after a base-field projective change,
  1021<=deg(A/B)<=2490,
  at least 398..422 distinct full normals row-wise;

c>=3:
  e<=floor((K'-1)/3),
  at least 597..633 distinct full normals row-wise.
```

Every one of the at least 41,746 represented directions in the conic branch
is now a binary quadratic in the same pair `A,B` with at least 2,041
official-domain roots after the common-gcd charge.

## Burn-down

```text
starting local pin:       21686a0cb
canonical prize pin:      0dd5b3244
upstream PR #1170 pin:    dab75a23
DAG delta:                +1 PROVED image-degree node, +5 edges
critical status delta:    none
compute spend:            none
closed interface:         abstract image-degree-two scalar systems
next action:              conic split-fiber classification and c>=3 normal incidence
```

## Nonclaims

- the rational map `A/B` is not classified as quotient-periodic;
- the image-degree-at-least-three branch is not excluded;
- no endpoint family, rank-eleven row, or prize problem is paid.
