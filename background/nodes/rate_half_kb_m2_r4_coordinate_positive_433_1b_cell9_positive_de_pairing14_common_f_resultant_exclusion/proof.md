# Proof

The proved source theorem covers each of the four source-sign rows by six
exact tower charts. On each chart, run the pinned positive pairing-14
common-`f` eliminator for four target lanes and `xi=0`. This is

```text
4 source signs * 6 charts * 4 target lanes = 96 rows.
```

The pairing is `((0,5),(1,4),(2,3))`. The first two equations share `f`:

```text
P_b(f) = Pair(-de,b*f),
P_c(f) = Pair(de,sigma_c*c*f).
```

Both cuts are quadratic in `f`. Their division-free quadratic resultant is
normed through the four-dimensional tower, with all inversion guards
retained. All 96 rows are complete and excluded.

An external FLINT computation reconstructs the roots of all 57 distinct
univariate profiles as `gcd(P(x),x^p-x)`. It finds 244 field roots in total;
the maximum profile degree is 1,372. These roots give an exact candidate
cover in every row.

A separate streaming replay intersects both scalar quadratic root sets. For
each common `f`, it solves the omitted product/squared-sum equation as an
even quartic in `u=e*f`, reconstructs `e`, `d`, and `v=d*f`, and evaluates
the final cut `Pair(v,sigma_o*u)`. Its terminal census is

```text
target roots                          1008
candidate roots                       1600
source routes                         1152
missing-free regularized points        192
missing-impossible points               96
target-product boundaries               96
ordinary checked routes                768
common-f quartic lifts                 384
nonzero colored cuts                   384
colored solutions                        0
```

The 96 `b`-leading and 192 `c`-leading exits lie on the corresponding
proved unit-ideal tower boundaries. The 192 missing-free rows are exactly
the regularized base points, where the proved all-role certificate gives a
unit ideal for pairing `14`, direct role `xi=0`, and every target lane. No
ordinary or boundary branch remains.

Finally, the universal orbit compiler maps the direct label to the orbit
printed in the statement. It is empty. QED.
