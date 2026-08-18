# Cycle 468: heavy-ruling partial-relative composition

## Starting pins

```text
our SHA: d06a895ec
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
upstream factor-synchronization tip: #1173 at 2788d5ec3
upstream split-pencil tip: #1170 at d296510e80
```

## Result: PROVED exact local trichotomy

Apply support-collapsed homogeneous interpolation directly to the exact
shortened supports from the degree-24 order-32 seed. If `c` is the canceled
common-support size, the residual parameters satisfy

```text
K'=K-c>=3,       m'=m-c,       m'-K'=67472.
```

Below the residual two-cover threshold, a nonzero solution with

```text
deg Q<=67472,       deg A',deg B'<=m'
```

gives either a pure-locator certificate or a nontrivial scalar-locator
rational certificate. Denominator roots are retained. The scalar-zero
rational case would make all 32 explanations globally affine and is
excluded by the 24 anchor records plus the certified off-line record.

Multiplication by the common locator lifts the certificate exactly to the
original heavy-ruling supports. In the complementary branch,

```text
chi=chi'+2c
   >=3(m-c)-(K-c)+3+2c
    =3m-K+3
    =2299571.
```

Thus the macroscopic ruling route reaches the exact partial-relative
interfaces while retaining slope degree `24..31`, first-owned slope labels,
and the selected support labels.

## Burn-down

```text
critical target attacked: rate_half_band_crossing_location
DAG delta: +1 background PROVED node, +2 edges
critical status delta: none
route delta: actual degree-24 packet -> pure locator / rational profile / chi>=2299571
new assumptions: none
next action: pay one output using the retained ruling and anchor structure
```

## Nonclaims

- no pure-locator, rational-profile, or high-complexity payment;
- no local-core synchronization or whole-line owner;
- no adjacent-row safety or MCA closure.

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_heavy_plane_ruling_degree24_partial_relative_router/verify.py
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_heavy_plane_ruling_degree24_partial_relative_router/verify.py --tamper-selftest
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_heavy_plane_ruling_degree24_partial_relative_router/verify_audit.py
```
