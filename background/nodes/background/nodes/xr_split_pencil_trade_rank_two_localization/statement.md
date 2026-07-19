# XR split-pencil trade rank-two localization

- **status:** see `dag.json` (single source of truth)
- **consumers:** `xr_highcore_collision_count`, `xr_lowcore_spread_heart`
- **dependency:** `xr_split_pencil_dual_trade_core`

Let `Lambda=(lambda_i(x))` be a nonzero dual trade from the preceding node,
with distinct slopes and agreement blocks of common size `m`, pairwise
intersecting in at most four coordinates. Put `r=rank Lambda`.

Then `r!=1`. If `r=2`, let `t` be the number of nonzero block rows and `R`
the number of coordinates used by at least one row. One has

```text
t>=4,
R <= floor(t m/(t-1)) <= floor(4m/3).               (RL1)
```

Thus every rank-two P-A base trade is supported on at most `12,12,9`
coordinates at the three RowC rates, and every rank-two P-B one-loop trade
is supported on at most `13,13,10` coordinates.

Consequently, after active-coordinate charts up to those explicit sizes are
classified or paid, the remaining primitive dual-trade obstruction has
matrix rank at least three. This node proves the localization only; it does
not assert that the current XR ledger already pays every such chart and does
not promote either consumer.
