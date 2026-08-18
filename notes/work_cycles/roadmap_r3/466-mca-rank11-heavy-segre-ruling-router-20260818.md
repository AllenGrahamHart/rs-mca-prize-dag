# Cycle 466: rank-eleven heavy Segre ruling router

## Starting pins

```text
our SHA: 713a1defb
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
upstream factor-synchronization tip: #1173 at 2788d5ec3
upstream split-pencil tip: #1170 at d296510e80
```

## Result: PROVED macroscopic ruling synchronization

Apply the general margin/interleaving split to the shortened rank-four
heavy Segre bucket at `T=12`. Uniformly over every shortened dimension,

```text
high margin <= 9319299072,
low margin  >=  646108914,
low pair types <= 58361.
```

For a fixed low pair, the selected explanation correction traces a matrix
pencil `A+gamma B` and must hit the rank-one Segre cone. A nonzero quadratic
determinant permits at most two slopes. Consequently at least

```text
646108914-2*58361=645992192
```

records have pair pencils lying entirely in left or right Segre rulings.
The dimension-two low-pair cap is

```text
241*981115=236448715,
```

so at least three ruling planes occur. Removing at most `1039475`
zero-correction records leaves `644952717` nonzero aligned records. One
orientation carries at least `322476359` records through at least two
planes. Left rulings synchronize the original factor; right rulings weld a
residual factor across original factor slices.

## Burn-down

```text
critical target attacked: rate_half_band_crossing_location
DAG delta: +1 background PROVED node, +3 edges
critical status delta: none
route delta: one <=11-exception record -> macroscopic left/right ruling synchronization
new assumptions: none
next action: prove a two-ruling common-core/owner dichotomy and retain the first-owned mass
```

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_heavy_plane_low_margin_segre_ruling_router/verify.py
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_heavy_plane_low_margin_segre_ruling_router/verify.py --tamper-selftest
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_heavy_plane_low_margin_segre_ruling_router/verify_audit.py
```
