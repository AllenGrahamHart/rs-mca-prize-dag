# Proof

The proved four-basis common-locus theorem covers every source-sign row by
six exact tower charts: two quadratic `b` charts times three linear `c`
charts.  On each chart, run the pinned common-`f` pairing-11 eliminator for
the four target lanes and `xi in {0,2}`.  This gives

```text
4 source signs * 6 charts * 4 target lanes * 2 roles = 192 rows.
```

Every row is complete and excluded.  An external FLINT computation rebuilds
the roots of all 73 distinct univariate profiles as
`gcd(P(x),x^p-x)`, finding 364 field roots in total; the maximum profile
degree is 1396.  Those roots give an exact candidate cover in every row.

An independent streaming replay then checks all source relations, guards,
quadratic lifts, common-`f` intersections, missing-product quartics, and
colored pairing cuts.  Its terminal census is

```text
source routes                         2496
missing-free regularized points        384
missing-impossible points              192
target-product boundaries              192
ordinary checked routes               1728
complete (u,f) lifts                   1152
nonzero colored cuts                   1152
colored solutions                         0
```

The apparent free branches are already paid exact boundaries.  There are
192 `b`-leading and 384 `c`-leading rows; substitution puts each on the
corresponding unit-ideal boundary in its tower chart.  The 384
missing-free rows are exactly the regularized base points, and the proved
base certificate gives a unit ideal for pairing `11`, both required roles,
and every target lane.  Thus no ordinary or boundary branch remains.

Finally, the universal orbit compiler sends direct labels `(0,11)` and
`(2,11)` to

```text
[(0,11),(1,11)] and [(2,11),(2,14)].
```

Both active orbits are empty. QED.
