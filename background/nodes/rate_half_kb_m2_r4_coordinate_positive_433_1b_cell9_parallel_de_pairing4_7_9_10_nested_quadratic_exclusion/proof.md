# Proof

The proved source theorem covers each of the four source-sign rows by six
exact tower charts. On each chart, run the pinned pairing-4
nested-quadratic eliminator for four target lanes and `xi in {0,2}`. This is

```text
4 source signs * 6 charts * 4 target lanes * 2 roles = 192 rows.
```

In every row the two paired cuts have degree two, the `(u,f)` eliminant has
degree eight, and its division-free pseudo-remainder has degree one. All 192
rows are complete and excluded.

An external FLINT computation reconstructs the roots of all 61 distinct
univariate profiles as `gcd(P(x),x^p-x)`. It finds 308 field roots in total;
the maximum profile degree is 10,944. These roots give an exact candidate
cover in every row.

A separate streaming replay checks the source relations, guards, both
paired quadratics, every Cartesian `(u,f)` pair, the missing-record relation,
and the final colored pair. Its terminal census is

```text
source routes                         4032
missing-free regularized points        384
missing-impossible points              192
target-product boundaries              192
ordinary checked routes               3264
nonzero missing-relation pairs        6080
zero missing-relation (u,f) pairs      960
nonzero colored cuts                   960
colored solutions                        0
```

The 192 `b`-leading and 384 `c`-leading exits lie on the corresponding
proved unit-ideal tower boundaries. The 384 missing-free rows are exactly
the regularized base points, where the proved all-role certificate gives a
unit ideal for pairing `4`, both direct roles, and every target lane. No
ordinary or boundary branch remains.

Finally, the universal orbit compiler maps the direct labels to the two
orbits printed in the statement. Both are empty. QED.
