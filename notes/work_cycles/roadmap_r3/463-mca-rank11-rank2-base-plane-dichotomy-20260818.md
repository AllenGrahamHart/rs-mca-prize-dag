# Cycle 463: rank-eleven rank-two base/plane dichotomy

## Starting pins

```text
our SHA: 76c569082
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
upstream rich-flat tip: PR #1173 at 2788d5ec3
```

## Result: PROVED residual class collapse

After the rank-two triple is cancelled, the residual base is a three-space
on at most `1116045` anchor-good coordinates, and every residual class has
at least `37733` common roots.

Let `q` be the number of zero evaluation columns of the entire three-space.
If `q>=10001`, the complete `388650911452`-slope bucket has another common
core and shortens reversibly.

If `q<=10000`, no dimension-three class can occur. Every class is a plane,
and at least `37733-q` of its roots are nonzero evaluation columns in one
projective clone class. Distinct planes use disjoint clone classes, so

```text
number of planes
 <= max_(0<=q<=10000) floor((1116045-q)/(37733-q))
 =39.
```

One plane therefore has mass at least

```text
ceil(388650911452/39)=9965407986.
```

This exceeds `R_3=3977322801`, forcing its correction span to have dimension
exactly four. It retains at least 27,733 nonbase clone coordinates.

## Burn-down

```text
critical target attacked: rate_half_band_crossing_location
DAG delta: +1 background PROVED node, +4 edges
critical status delta: none
route delta: shortened 2 x 3 -> common-base recursion / heavy rank-4 plane
new assumptions: none beyond the parent factor branch
next action: classify the heavy 2 x 2 plane or terminate common-base iteration
```

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_rank_two_residual_base_plane_dichotomy/verify.py
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_rank_two_residual_base_plane_dichotomy/verify.py --tamper-selftest
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_rank_two_residual_base_plane_dichotomy/verify_audit.py
```
