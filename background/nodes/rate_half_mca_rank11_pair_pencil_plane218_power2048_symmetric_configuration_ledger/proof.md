# Proof

The parent router proves, in the degree-2048 case,

```text
K'=2049,       r=218,       b=218,       F>=446392,
```

where `r` is the number of represented directions, `b` the number of full
15-point lines, and `F` the number of full coordinates. There is exactly
one full line in each represented direction.

Through a selected point, distinct full lines use disjoint sets of 14 other
selected points. Hence a point lies on at most `floor(217/14)=15` full
lines. The 218 full lines have `218*15` point-line incidences. Since there
are 218 points and every point has degree at most 15, every point has degree
exactly 15. Thus each point is joined by full lines to exactly
`15*14=210` other points, leaving exactly seven uncovered partners.

Dually, every full line meets 15 selected points, and at each such point it
meets 14 other full lines. Linearity of the affine plane makes these 210
other lines distinct. Since all 218 full lines have distinct represented
directions, none are parallel. Exactly seven other line intersections are
therefore not selected. Both leave graphs are 7-regular, and each has
`218*7/2=763` edges.

For the point-line incidence matrix `M`, diagonal entries of `M M^T` are
15. An off-diagonal entry is one precisely when the point pair is covered
by a full line, and zero precisely on a point-leave edge. Hence

```text
M M^T=15I+(J-I-L_P)=14I+J-L_P.
```

The line version is identical and gives the second identity in (SC-1).
Because `L_P` is a symmetric 7-regular adjacency matrix, its eigenvalues
on the orthogonal complement of the all-ones vector are at most seven.
There `14I+J-L_P` has eigenvalues at least seven; on the all-ones vector
its eigenvalue is `14+218-7=225`. Thus `M M^T` is positive definite and
`M` is nonsingular. The two Gram matrices have the same spectrum, and the
regular decompositions in (SC-1) then show that `L_P` and `L_B` are
cospectral.

A represented pure-power direction polynomial has exactly 2048 roots in
the smooth domain, and `z_eta` of them are full. Therefore

```text
sum_eta d_eta=218*2048-F<=446464-446392=72.
```

Every defective direction has positive integral defect, so at most 72 of
the 218 directions are defective and at least 146 are saturated. Saturated
line-point incidences number at least `146*15=2190`, which exceeds
`10*218`; some point lies on at least 11 saturated lines.

Finally sum the line defects over their 15 incident points. The total
point-incident defect is at most `15*72=1080`. Since
`1080<5*218`, some point has incident defect at most four. Its 15 directions
are distinct quotient fibers and therefore disjoint; they contribute at
least `15*2048-4=30716` full coordinates to that point's residual core.
QED.
