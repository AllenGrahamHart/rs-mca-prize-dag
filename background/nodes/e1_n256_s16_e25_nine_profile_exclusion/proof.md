# Proof

The E25 reduction proves that every candidate has one of the nine magnitude
profiles in the statement and a light support in exactly 111 affine odd-unit
orbits. For each representative, choose the three heavy positions among the
124 remaining coordinates. Global sign fixes the first heavy coefficient to
`+2`; the remaining two heavy and four light signs give 64 vectors. Hence
each engine examines exactly

```text
111*binom(124,3)*64 = 2,203,120,896
```

representatives. Translation and odd-unit multiplication preserve the
profile, conductor, cubic moment, and absolute cyclotomic norm, so this is a
complete orbit census.

The folded-chord engine updates signed difference classes directly. The audit
instead multiplies each sparse vector by its conjugate in
`Z[x]/(x^128+1)`. They agree exactly on every row and retained vector:

```text
profile       vectors   M_3>13   full conductor   full M_3 range
(5,5)          12,156     12,156            6,944          60..900
(1,6)          11,884     11,628            6,888           0..720
(4,3,1)         5,526      5,526            2,868         120..696
(0,4,1)           416        352               32           0..276
(3,1,2)           632        632              116         120..480
(5,1,0,1)         238        238               56          96..384
(1,2,0,1)         812        748               80           0..240
(0,0,1,1)          16          0                0                --
(0,0,0,0,1)         6          0                0                --
total           31,686     31,280           16,984
```

The cubic-Hermite norm criterion excludes the 406 vectors with `M_3<=13`.
Of the remaining 31,280, exactly 14,296 have proper conductor and are excluded
by the proper-conductor theorem. For the 16,984 full-conductor vectors, FLINT
and PARI independently compute the resultant with `x^128+1` and agree entry
by entry. There are 3,727 distinct norms. Their common maximum is the 249-bit
integer in the statement and is strictly below `2^250`. Therefore none can
vanish modulo a pair-feasible row prime. These cases exhaust all nine
profiles. QED.
