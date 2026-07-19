# XR split-pencil rank-two support atlas

- **status:** see `dag.json` (single source of truth)
- **consumers:** `xr_highcore_collision_count`, `xr_lowcore_spread_heart`
- **dependency:** `xr_split_pencil_trade_rank_two_localization`

Let `Lambda=(lambda_i(x))` be a rank-two dual trade from the preceding
localization. Retain its `t` nonzero block rows, let `U` be their active
coordinate union, and put `R=|U|`. Assume the agreement blocks containing
the row supports have pairwise intersection at most `kappa<=4`.

Every active row has weight at least five, and the `t` rows are pairwise
nonproportional. If `kappa<=3`, no such rank-two trade exists. If
`kappa=4`, then

```text
4 <= t <= 6,                 6 <= R <= 8.             (SA1)
```

More precisely, put `z_i=R-wt(lambda_i)`. Up to permutation of rows and
coordinates, exactly the following five support profiles are possible:

```text
 t   R    {z_i}             row weights       active-column degrees
 4   6    {1,1,1,1}         {5,5,5,5}         {3,3,3,3,4,4}
 4   7    {1,2,2,2}         {6,5,5,5}         {3,3,3,3,3,3,3}
 4   8    {2,2,2,2}         {6,6,6,6}         {3,3,3,3,3,3,3,3}
 5   6    {1,1,1,1,1}       {5,5,5,5,5}       {4,4,4,4,4,5}
 6   6    {1,1,1,1,1,1}     {5,5,5,5,5,5}     {5,5,5,5,5,5}.
                                                               (SA2)
```

There is also an exact double-code normal form. The two-dimensional row
space is a subcode of the dual cubic-evaluation code on `U`. Writing

```text
lambda_i=a_i f+b_i g
```

for a basis `f,g`, the coefficient vectors `(a_i)_i,(b_i)_i` span a
two-dimensional subcode of the dual degree-less-than-two evaluation code on
the distinct slopes. Consequently the first inclusion is equality whenever
`R=6`, and the second is equality whenever `t=4`.

All five profiles occur over fields of characteristic greater than `17` as
exact dual-product-code trades. Thus `(SA2)` is sharp at the trade normal
form level. It reduces the former official active-coordinate caps
`12/12/9` and `13/13/10` uniformly to eight, and excludes rank two outright
in any pair-cap-three branch. It does not count the resulting coordinate
charts or promote either consumer.
