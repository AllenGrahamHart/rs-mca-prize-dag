# Cycle 467: heavy ruling degree-24 order-32 seed

## Starting pins

```text
our SHA: 23774adb2
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
upstream factor-synchronization tip: #1173 at 2788d5ec3
upstream split-pencil tip: #1170 at d296510e80
```

## Result: PROVED branch-local actual packet

Fix the ruling orientation carrying at least `322476359` nonzero
first-owned records. Removing all possible singleton pair types leaves

```text
322476359-58361=322417998
```

records on heavy pair types. Their common pair core has size below `K-2`:
otherwise exact cancellation to residual dimension two would cap the heavy
mass at `241*981115=236448715`, and even restoring every singleton would
give only `236507076` records. One heavy pair therefore owns at least

```text
ceil(322417998/58361)=5525
```

records. All pair components lie in the same four-dimensional correction
space, so this anchor and at most four further heavy types recover the
complete heavy-core intersection. Take two records from every further type
and fill the remaining places in an order-32 packet from the anchor. The
packet has at least 24 explanations on the anchor affine line, at least one
off that line, and common selected support of size below `K-2`.

Exact cancellation of that support preserves actual support-wise MCA
badness and leaves dimension at least three. Coefficientwise interpolation
in the slope, and hence the residual slope-error polynomial, has degree
between 24 and 31. This is an actual packet from the macroscopic ruling
bucket, not a formal low-degree witness.

## Burn-down

```text
critical target attacked: rate_half_band_crossing_location
DAG delta: +1 background PROVED node, +3 edges
critical status delta: none
route delta: macroscopic ruling orientation -> actual degree-24 order-32 packet
new assumptions: none
next action: compose the packet with the exact partial-relative harvest
```

## Nonclaims

- no whole-line chronology owner;
- no payment of the pure-locator, rational, spread, exception, or
  high-complexity outputs;
- no synchronization of local seed cores;
- no MCA closure.

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_heavy_plane_ruling_degree24_order32_seed/verify.py
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_heavy_plane_ruling_degree24_order32_seed/verify.py --tamper-selftest
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_heavy_plane_ruling_degree24_order32_seed/verify_audit.py
```
