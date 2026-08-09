# Proof

The proved source theorem covers each of the four source-sign rows by six
exact tower charts. On each chart, run the pinned positive pairing-9
nested-quadratic eliminator for four target lanes and `xi=0`. This is

```text
4 source signs * 6 charts * 4 target lanes = 96 rows.
```

In every row the two paired cuts have degree two, the `(u,f)` eliminant has
degree eight, and its division-free pseudo-remainder has degree one. All 96
rows are complete and excluded.

An external FLINT computation reconstructs the roots of all 53 distinct
univariate profiles as `gcd(P(x),x^p-x)`. It finds 208 field roots in total;
the maximum profile degree is 10,674. These roots give an exact candidate
cover in every row.

A separate streaming replay checks the source relations, guards, both
paired quadratics, every Cartesian `(u,f)` pair, the missing-record relation,
and the final colored pair. Its terminal census is

```text
source routes                         1728
missing-free regularized points        192
missing-impossible points               96
target-product boundaries               96
ordinary checked routes               1344
nonzero missing-relation pairs        2752
zero missing-relation (u,f) pairs      384
nonzero colored cuts                   384
colored solutions                        0
```

The 96 `b`-leading and 192 `c`-leading exits lie on the corresponding
proved unit-ideal tower boundaries. The 192 missing-free rows are exactly
the regularized base points, where the proved all-role certificate gives a
unit ideal for pairing `9`, direct role `xi=0`, and every target lane. No
ordinary or boundary branch remains.

Finally, the universal orbit compiler maps the direct label to the orbit
printed in the statement. It is empty. QED.
