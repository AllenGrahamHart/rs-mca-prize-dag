# Pair-pencil affine-line cap and direction router

- **status:** PROVED
- **scope:** the at least 520 scalar polynomials in the coprime-direction
  quotient normal form

Every affine `F`-line in the scalar polynomial space contains at most

```text
floor((n-(K-1))/((m-2)-(K-1)))=15                  (DR1)
```

selected quotient types. Therefore the scalar span has dimension in
`{2,3,4}`; the dimension-one branch is impossible.

The secants of the 520 selected scalar points determine at least

```text
ceil(C(520,2)/(34*C(15,2)+C(10,2)))=38             (DR2)
```

projectively distinct direction polynomials. Every such direction is a
nonzero scalar difference and has at least `134940` distinct roots on the
official domain.

If the scalar span has dimension two, all 38 directions lie in the same
projective polynomial pencil `P(W)`. If its dimension is three or four, the
remaining task is a higher-dimensional secant-direction census.

Root-richness here is not full splitting: roots away from the certified
pair-core intersections are neither required nor counted.

## Falsifier

Sixteen selected types on one affine scalar line; a one-dimensional scalar
survivor; fewer than 38 projective secant directions; or a selected secant
direction with fewer than 134940 official-domain roots.
