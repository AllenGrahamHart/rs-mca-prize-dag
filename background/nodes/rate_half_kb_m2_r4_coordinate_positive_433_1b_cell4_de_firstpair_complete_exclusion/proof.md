# Proof

Enumerate perfect matchings recursively by pairing the first unused position
with each later unused position in increasing order. For six positions the
first three matchings are exactly

```text
M_0=((0,1),(2,3),(4,5)),
M_1=((0,1),(2,4),(3,5)),
M_2=((0,1),(2,5),(3,4)).                 (KBP1B4-DE-FIRST-2)
```

For `xi=0`, deleting the first positive `DE` record leaves

```text
DE, -DE, DF, sigma_o EF, BF, sigma_c CF.
```

The `xi=1` list is value-for-value identical by the proved exchange of the
two parallel positive copies. For `xi=2`, deleting the negative copy leaves

```text
DE, DE, DF, sigma_o EF, BF, sigma_c CF.   (KBP1B4-DE-FIRST-3)
```

Every matching in `(KBP1B4-DE-FIRST-2)` therefore imposes the same first
paired-product equation as matching zero. For `xi=0,1` this is the
opposite-record cut `P(m,-m)=0`. For `xi=2`, if `m` denotes the omitted
value, then `DE=-m` and the cut is `P(-m,-m)=0`.

The `xi=0` four-basis norm theorem excludes the first cut in all four source
signs. Exact parallel-edge transport supplies `xi=1`. The `xi=2` four-basis
norm theorem excludes the second cut in all four source signs. These cuts
are necessary consequences of the complete outside system and contain no
target-lane sign. Once a first-pair cut is impossible, the other two pairs
cannot restore a solution.

Thus all `3*3` missing/matching slices are empty in every source-sign and
target-lane row, giving `3*3*4*4=144` excluded raw cases. QED.
