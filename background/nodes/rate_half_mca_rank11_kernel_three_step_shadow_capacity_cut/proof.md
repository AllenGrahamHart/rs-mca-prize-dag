# Proof

The predecessor closes through `K'=18101`, so only the 58 rows
`18102<=K'<=18159` require replay.  Normalize the nine corank counts by the
residual-record floor.

On every new row, the exact optimizer has two hierarchy components.  The
first is

```text
1 --H_(3,2)-- 3.
```

The second has spanning tree

```text
2 --H_(4,2)-- 4 --H_(6,2)-- 6 --H_(8,2)-- 8,
|
H_(5,3)
|
5 --H_(7,2)-- 7 --H_(9,2)-- 9.
```

The corank-one individual cap fixes the first component.  The
full-containment equality fixes the second.  Every displayed hierarchy edge
then determines its child count exactly.  All nine counts are positive, all
other individual caps are slack, and the rank-preserving nine-shadow
resource is slack.

The primary verifier checks all 28 hierarchy inequalities.  Seventeen bind;
the additional ten tight rows are cycle-consistency identities, while the
remaining eleven are strict.  It solves the nine complementary-slackness
equations for the containment multiplier, corank-one cap multiplier, and
seven spanning-tree multipliers by exact Gaussian elimination.  Every dual
multiplier is nonnegative and the dual objective equals the primal count.

At `K'=18158`, exact integer replay gives the displayed positive
demand-capacity gap.  At `K'=18159`, the sign reverses by the displayed wall
excess.  The independent audit derives the same dual multipliers by a
backward recurrence on the hierarchy tree rather than Gaussian elimination.
