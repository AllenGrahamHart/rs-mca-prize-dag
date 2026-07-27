# Proof

The E28 reduction proves that every candidate has one of eight profiles and a
light support in six zero-odd or 148 four-odd affine orbits. For each
representative, choose the three heavy positions among the 124 remaining
coordinates. Global sign fixes the coefficient at the first heavy position to
`+2`; the remaining two heavy and four light signs give 64 vectors. Hence each
engine examines exactly

```text
154*binom(124,3)*64 = 3,056,582,144
```

representatives. Translation and odd-unit multiplication preserve every
quantity used below, so this is a complete orbit census.

The folded-chord engine updates signed difference classes directly. The audit
instead multiplies each sparse vector by its conjugate in
`Z[x]/(x^128+1)`. They agree exactly on every row, histogram, maximum, and
exceptional witness:

```text
profile        vectors   M_3>658   full conductor   max M_3   full max
(4,6)           28,458       9,936            3,838       1200       1200
(0,7)            3,008         656              192        768        720
(3,4,1)         12,458       1,500              330       1020       1020
(2,2,2)          1,182         392               10        924        906
(4,2,0,1)        1,984         152                2        804        696
(1,0,3)             30           2                0        666       none
(0,3,0,1)        1,360           0                0        480        240
(3,0,1,1)          236           0                0        618        396
total            48,716      12,638            4,372
```

Every vector with `M_3<=658` has norm below `2^250` by the cubic-Hermite norm
criterion. Of the remaining 12,638, exactly 8,266 have proper conductor and
are excluded by the proper-conductor theorem. For the 4,372 full-conductor
vectors, FLINT and PARI independently compute the resultant with `x^128+1`
and agree entry by entry. There are 1,723 distinct norms; their common maximum
is the 248-bit integer in the statement, strictly below `2^250`. Therefore no
exception can vanish modulo a pair-feasible row prime. These cases exhaust all
eight profiles. QED.
