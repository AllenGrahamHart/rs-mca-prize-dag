# Proof

The E26 reduction proves that every remaining six-odd candidate has one of
the four magnitude profiles in the statement and a light support in exactly
1,234 affine odd-unit orbits. Each orbit has one representative in the proved
six-odd atlas. For each representative, choose the three heavy positions
among the 124 remaining coordinates. Global sign fixes the coefficient at the
first heavy position to `+2`; the remaining two heavy and four light signs
give 64 vectors. Hence each engine examines exactly

```text
1234*binom(124,3)*64 = 24,492,353,024
```

representatives. Translation and odd-unit multiplication preserve the
profile, conductor, cubic moment, and absolute cyclotomic norm, so this is a
complete orbit census.

The folded-chord engine updates signed difference classes directly. The audit
instead multiplies each sparse vector by its conjugate in
`Z[x]/(x^128+1)` and derives the profile from the resulting coefficients.
They agree exactly on all 1,234 rows, including every printed primitive
exception:

```text
profile       vectors   M_3>228   full conductor   max M_3   full max
(6,5)          51,562      48,918           32,096       1074       1062
(5,3,1)        23,884      23,232           12,632        942        942
(4,1,2)         1,614       1,590              408        870        690
(6,1,0,1)       1,788         874              272        606        606
total          78,848      74,614           45,408
```

Every vector with `M_3<=228` has norm below `2^250` by the cubic-Hermite norm
criterion. Of the remaining 74,614, exactly 29,206 have proper conductor and
are excluded by the proper-conductor theorem. For the 45,408 full-conductor
vectors, FLINT and PARI independently compute the resultant with
`x^128+1` and agree entry by entry. There are 20,636 distinct norms. Their
common maximum is the integer in the statement, strictly below `2^250`.
Therefore none can vanish modulo a pair-feasible row prime. These cases
exhaust all four profiles. QED.
