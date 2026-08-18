# Cycle 456: rank-eleven chronology-safe subspace cover

## Starting pins

```text
our branch: codex/full-prize-resolution-v12-20260807
our SHA: d4455c0cc
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
upstream rich-flat tip: PR #1173 at 2788d5ec3
```

The canonical tree and upstream open-PR frontier were inspected before this
cycle. K'=87 and PR #1171--#1173 are already represented locally; the local
O0b chart route is ahead of the canonical tree.

## Result: PROVED chronology-aware cover obstruction

At the full-span rank-eleven row, the nontransverse first-match ledger has
residual allowance

```text
L=B_*-E_transverse=65167969673715470.
```

If its represented row spaces are partitioned into correction subspaces of
dimensions `d_alpha<=9`, ordinary affine-span and the proved sub-square
interleaving collapse give the exact additive cost

```text
sum_alpha (n-A) floor(C(n-K+d_alpha,d_alpha)/
                      C(A-K+d_alpha,d_alpha)).
```

Unsafety forces this sum to exceed `L`. The first possible unsafe uniform
cover sizes for dimensions one through nine are

```text
4420641497, 262093370, 16384884, 1027929, 64502,
4048, 254, 16, 2.
```

Thus two five-dimensional blocks are paid. The abstract two-block example
that fences a bare rich-atlas-to-factor inference cannot model an unsafe
line once every represented slope is actually assigned to those blocks. An
unsafe `2 x 5` factor presentation must use at least `64502` distinct factor
slices.

## Burn-down

```text
critical target attacked: rate_half_band_crossing_location
DAG delta: +1 background PROVED node, +1 evidence edge
critical status delta: none
route delta: bare two-block rich-atlas obstruction removed at actual-owner scope
new assumptions: none
next action: force a low-cost chronology-aware cover from the anchored
             row-space partition, or exploit the >=64502 used-slice horn
```

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_chronology_safe_subspace_cover_payment/verify.py
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_chronology_safe_subspace_cover_payment/verify_audit.py
```
