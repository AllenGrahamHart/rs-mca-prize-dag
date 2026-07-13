# Attack surface

The proved strip rungs force every post-strip cross-slope core to have size at
most `k`; therefore a high-core collision has core exactly `k`. In error-set
notation, with

```text
R=n-k,       h=A-k,       r=n-A=R-h,
```

two colliding rays have error-set union of size exactly `R`.

The pair-moment identity is an instrument only. Dense pencils can make
`sum_W C(mult(W),2)` much larger than the number of distinct slopes, so a
moment bound is not an honest replacement for the target.

The proved `xr_highcore_component_union_atlas` removes the chart-overlap
ambiguity. It partitions the high-core slopes into canonical collision
components `C`, chooses one witness ray per slope, and assigns the component
the union chart `U_C` of size `R+d_C`. The exact aggregate ledger is

```text
#high-core slopes = sum_C |Z_C|,
|Z_C| <= floor(C(R+d_C,d_C) R / C(d_C+h,d_C)).
```

Thus slopes, collision cores, and charts are deduplicated before payment.
The denominator is the exact information-set occupancy forced by the
agreement reserve. The tangent-strip hypothesis prevents `h` persistent
zeros and is load-bearing.

The complementary proved `xr_direction_distance_ray_bound` pays any fixed
chart with

```text
(|U|-r)^2 > |U| (|U|-d_U(y_1))
```

by at most `|U|^2` slopes. Failure gives an explicit low-weight lift of the
received direction and hence a sparse-direction/near-pencil normal form. This
is a real dichotomy, but both sides are still per-chart.

Independently of the chart atlas, the proved
`xr_all_lineray_affine_core_bound` applies the nonuniform set-pair inequality
to any one-per-slope selector. If one selector has affine span dimension
`sigma`, then

```text
#high-core slopes <= C(sigma+r,sigma).
```

The exact candidate threshold is `sigma<=3`; all six `sigma=4` bounds exceed
`8n^3`. Consequently every counterexample to P-A must have rank at least four
for every selector. Applying the theorem to the complete pair family remains
a stronger pair-count branch, but is not required for this slope corollary.

At selector rank `s>=4`, the proved
`xr_highcore_collision_line_basis_ledger` assigns each collision line `ell`
its number `b_ell` of independent `(s-1)`-minors in the size-`k` common core.
It proves

```text
sum_ell b_ell <= C(n,s-1),
#points on ell <= floor((n-k)/(A-k)).
```

A basis-poor line is not an exception: if it has `b_ell=b`, then the entire
selector lies in one union chart of excess at most `b+s-2`, where GRK applies.
Choosing a minimum-basis line self-localizes the line ledger to that smaller
chart. If every core restriction is uniform, the ledger pays through selector
ranks `13,9,7,60,40,30` on the six rows.

The proved `xr_affine_core_cogirth_ray_bound` uses the rank-`s-1` kernel slice
inside the selector. Its coordinate matroid has enough information sets by a
deletion-contraction cogirth bound, giving

```text
#slopes C(h+s-1,s-1) <= C(N,s-1)(N-s+1).
```

On the full domain this pays selector ranks through `4,4,3,11,11,10` on the
six rows. On the self-localized charts left by the line ledger, it also pays
the RowC `1/16` rank-four residue. Thus selector rank four is completely
closed on every P-A row; at the prize rows the minimum open selector ranks are
`12,12,11`.

The P9 diagnostics show that the residual is not automatically low-rank:
every `n=16,k=8` conservative far high-core family had no selector of rank at
most three; its canonical selector had rank `9=k+1` and its giant collision
component had `d_C=k`. Therefore the remaining task is the explicit
component-excess ledger

```text
sum_C floor(C(R+d_C,d_C) R / C(d_C+h,d_C)) <= 8n^3,
```

or a sharper sum using DDR on the high-direction components and its certified
sparse-direction normal form on the complement. A proof must control the
number of canonical components and their union excesses; the raw number of
possible subsets `U` no longer appears. Any rank-based continuation must use a
rank--weight or rank--collision tradeoff specific to the retained RS family.
The line-basis and cogirth theorems supply that tradeoff. The next local attack
is their higher-rank iteration, not another bare rank bound.
