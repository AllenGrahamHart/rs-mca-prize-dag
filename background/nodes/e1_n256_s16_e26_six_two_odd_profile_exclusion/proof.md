# Proof

The E26 reduction proves that every two-odd candidate has one of six magnitude
profiles and a light support in 87 affine orbits. For each representative,
choose the three heavy positions among the 124 remaining coordinates. Global
sign fixes the first heavy coefficient to `+2`; the remaining relative signs
give 64 vectors. Hence each engine examines exactly

```text
87*binom(124,3)*64 = 1,726,770,432
```

representatives. Translation and odd-unit multiplication preserve every
tested invariant, so this is a complete orbit census.

The folded-chord and direct-negacyclic engines agree on every row and witness:

```text
profile          vectors   M_3>228   full conductor   max M_3   full max
(2,6)             22,214      14,958            7,508        984        984
(1,4,1)            2,148       1,744              438        840        702
(0,2,2)              120          82                4        630        630
(2,2,0,1)          2,754         798              106        600        420
(1,0,1,1)            140          42                4        450        432
(1,0,0,0,1)            4           0                0          0         --
total              27,380      17,624            8,060
```

The cubic-Hermite criterion excludes every vector with `M_3<=228`. The
proper-conductor theorem excludes 9,564 of the remaining vectors. FLINT and
PARI independently compute all 8,060 full-conductor resultants with
`x^128+1` and agree entry by entry. There are 1,442 distinct norms; their
common maximum is the 249-bit integer in the statement and is strictly below
`2^250`. Therefore no two-odd candidate collides on a pair-feasible row. QED.
