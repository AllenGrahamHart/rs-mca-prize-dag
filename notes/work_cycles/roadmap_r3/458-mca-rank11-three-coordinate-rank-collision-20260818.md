# Cycle 458: rank-eleven three-coordinate rank collision

## Starting pins

```text
our SHA: c094083be
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
upstream rich-flat tip: PR #1173 at 2788d5ec3
```

## Result: PROVED rank-two evaluation collision

Every residual class in the weighted-root bucket has at least `37736`
actual zero coordinates. Starting from its forced one-coordinate mass
`303637675671716`, two further exact weighted-incidence steps retain

```text
M_2=10266384562185,
M_3=347110921118.
```

If the three selected coordinate evaluations on the residual five-space
`B` had rank three, their common kernel would have dimension two. The final
subfamily would then lie in `P` times that kernel, a correction space of
dimension at most four. Its exact chronology-safe cap is
`R_4=63397365764`, more than five times below `M_3`. Therefore the three
evaluation columns have rank at most two.

## Burn-down

```text
critical target attacked: rate_half_band_crossing_location
DAG delta: +1 background PROVED node, +1 evidence edge
critical status delta: none
route delta: high-mass dimension-eight bucket -> rank<=2 coordinate triple
new assumptions: none beyond the explicit 2 x 5 branch
next action: split proportional-column clones from genuine projective-line
             triples while retaining the 347110921118 first-owned slopes
```

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_factor_flag_three_coordinate_rank_collision/verify.py
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_factor_flag_three_coordinate_rank_collision/verify_audit.py
```
