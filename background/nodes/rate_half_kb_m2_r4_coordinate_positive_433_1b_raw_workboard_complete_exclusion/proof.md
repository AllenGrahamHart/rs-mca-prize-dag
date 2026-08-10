# Proof

The common Vieta compiler chooses one singleton among five common roles and
one of the three perfect matchings on the remaining four roles. Hence it
produces exactly `5*3=15` role cells, indexed `0,...,14`.

The nine required closure packets own the displayed cell blocks. Their
sizes are `1,2,2,2,2,2,1,2,1`, so they are disjoint and cover all 15
indices. Singleton packets close cells 0, 11, and 14 directly. The six
two-cell packets either close both cells directly or combine one complete
cell with an exact duplicate-role bijection. Every owner packet is
`PROVED` and recursively carries its algebraic dependencies.

For each cell, the signed-edge atlas and direct-label router give seven
missing records, fifteen residual perfect matchings, four source-sign rows,
and four target lanes. Therefore the principal branch has

```text
15 * 7 * 15 * 4 * 4 = 25200
```

systems, grouped into 1,575 raw labels. Every system belongs to exactly one
owner block. Finally, the global rank-drop theorem excludes the complementary
product-rank branch in every cell. These branches exhaust the guarded raw
workboard, so it is empty. QED.
