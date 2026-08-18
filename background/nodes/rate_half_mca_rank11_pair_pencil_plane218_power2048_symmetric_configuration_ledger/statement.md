# The degree-2048 endpoint is a symmetric configuration

- **status:** PROVED
- **scope:** the `e=2048` branch of the 218-plane pure-power router

Assume the endpoint residual direction pencil is projectively equivalent to
`(X^2048,1)`. Then `K'=2049`, and the 218 selected scalar points and
their 218 full affine lines form a symmetric configuration `218_15`:

1. every full line contains 15 selected points;
2. every selected point lies on exactly 15 full lines;
3. no two full lines are parallel, and all 218 directions lie in
   `mu_1024`; and
4. each point has exactly seven uncovered partners, while each line has
   exactly seven other lines whose intersection is not selected.

Both leave graphs are therefore 7-regular on 218 vertices and have 763
edges. If `M` is the point-line incidence matrix and `L_P,L_B` are the point
and line leave adjacency matrices, then

```text
M M^T =14I+J-L_P,        M^T M=14I+J-L_B.           (SC-1)
```

The matrix `M` is nonsingular over the reals, and the two leave graphs are
cospectral.

If `d_eta=2048-z_eta` is the missing-root count of a full direction, then

```text
sum_eta d_eta<=72.                                  (SC-2)
```

Consequently at least 146 direction fibers are completely saturated. Some
selected point lies on at least 11 saturated lines, and some selected point
has total incident defect at most four. The latter point receives at least

```text
15*2048-4=30716
```

full residual-core coordinates from its 15 disjoint quotient fibers.

This ledger does not exclude the symmetric configuration, prove that the
actual endpoint is pure-power, or pay the quotient-periodic branch.

## Falsifier

A point or line degree other than 15; a leave degree other than seven;
parallel full lines; a defect sum above 72; fewer than 146 saturated
fibers; failure of either matrix identity; or singularity of `M` over the
reals.
