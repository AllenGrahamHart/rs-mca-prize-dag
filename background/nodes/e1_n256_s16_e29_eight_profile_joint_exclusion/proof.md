# Proof

The E29 reduction proves that every candidate has one of eight magnitude
profiles and a light support in 11 one-odd or 100 five-odd affine orbits.
For each representative, choose the three heavy positions among the 124
remaining coordinates. Global sign fixes the coefficient at the first heavy
position to `+2`; the remaining two heavy and four light signs give 64
vectors. Hence each engine examines exactly

```text
111*binom(124,3)*64 = 2,203,120,896
```

representatives. Translation and odd-unit multiplication preserve the
profile, conductor, cubic moment, and absolute cyclotomic norm, so this is a
complete orbit census.

The folded-chord engine updates signed difference classes directly. The audit
instead multiplies each sparse vector by its conjugate in
`Z[x]/(x^128+1)` and derives the profile from the resulting 128 coefficients.
They agree exactly on every row, histogram, maximum, and exceptional witness:

```text
profile        vectors   M_3>872   full conductor   max M_3   full max
(5,6)           34,810       3,090              544       1332       1164
(1,7)            5,568         520              128       1008       1008
(4,4,1)         11,468         604              148       1038        984
(0,5,1)            560         112                0       1068        624
(3,2,2)          4,252         486                0       1110        732
(5,2,0,1)        2,134           0                0        684        684
(2,0,3)            148           0                0        648        216
(1,3,0,1)        2,468           0                0        708        456
total            61,408       4,812              820
```

Every vector with `M_3<=872` has norm below `2^250` by the cubic-Hermite norm
criterion. Of the remaining 4,812, exactly 3,992 have proper conductor and are
excluded by the proper-conductor theorem. For the 820 full-conductor vectors,
FLINT and PARI independently compute the resultant with `x^128+1` and agree
entry by entry. There are 242 distinct norms; their common maximum is the
247-bit integer in the statement, strictly below `2^250`. Therefore none can
vanish modulo a pair-feasible row prime. These cases exhaust all eight
profiles. QED.
