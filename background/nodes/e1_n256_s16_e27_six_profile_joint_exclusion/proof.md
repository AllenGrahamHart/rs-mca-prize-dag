# Proof

The E27 reduction proves that every candidate has one of six magnitude
profiles and a light support in eight three-odd affine orbits. For each
representative, choose the three heavy positions among the 124 remaining
coordinates. Global sign fixes the coefficient at the first heavy position
to `+2`; the remaining two heavy and four light signs give 64 vectors. Hence
each engine examines exactly

```text
8*binom(124,3)*64 = 158,783,488
```

representatives. Translation and odd-unit multiplication preserve the
profile, conductor, cubic moment, and absolute cyclotomic norm, so this is a
complete orbit census.

The folded-chord engine updates signed difference classes directly. The audit
instead multiplies each sparse vector by its conjugate in
`Z[x]/(x^128+1)` and derives the profile from the resulting 128 coefficients.
They agree exactly on every row, histogram, maximum, and exceptional witness:

```text
profile        vectors   M_3>443   full conductor   max M_3   full max
(3,6)            2,344       1,388              328       1020        912
(2,4,1)            752         338               68       1074        678
(1,2,2)            272         128                8        738        480
(3,2,0,1)          666         146                0        648        390
(0,0,3)              4           0                0        162         --
(2,0,1,1)           86           0                0        408        198
total             4,124       2,000              404
```

Every vector with `M_3<=443` has norm below `2^250` by the cubic-Hermite norm
criterion. Of the remaining 2,000, exactly 1,596 have proper conductor and are
excluded by the proper-conductor theorem. For the 404 full-conductor vectors,
FLINT and PARI independently compute the resultant with `x^128+1` and agree
entry by entry. There are 144 distinct norms; their common maximum is the
247-bit integer in the statement, strictly below `2^250`. Therefore none can
vanish modulo a pair-feasible row prime. These cases exhaust all six profiles.
QED.
