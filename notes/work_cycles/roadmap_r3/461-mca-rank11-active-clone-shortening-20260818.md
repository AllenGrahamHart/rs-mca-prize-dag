# Cycle 461: rank-eleven active-clone shortening

## Starting pins

```text
our SHA: cc8ac7554
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
upstream rich-flat tip: PR #1173 at 2788d5ec3
```

## Result: PROVED locator adapter

The active projective clone `D` has one common kernel `B_D` inside the
residual five-space. Base-freeness makes this kernel four-dimensional, and
all of it is divisible by the squarefree locator `L_D`. Therefore

```text
B_D=L_D bar(B)_D,          dim bar(B)_D=4.
```

After cancellation the correction bucket lies in

```text
span(P bar(B)_D) <= F[X]_{<K-|D|}.
```

The elementary polynomial product-space bound
`dim span(VW)>=dim V+dim W-1` gives dimension at least five. Consequently

```text
10001<=|D|<=K-5=1048571,
5<=K-|D|<=1038575.
```

The same-record common-core adapter transports every associated residual
class and preserves at least `388650911452` first-owned slopes, producing a
reversible shortened `2 x 4` factor bucket with parameters

```text
(n',k',m')=(2097152-c,1048576-c,1116048-c).
```

All three row differences and pair noncontainment are preserved.

## Burn-down

```text
critical target attacked: rate_half_band_crossing_location
DAG delta: +1 background PROVED node, +3 edges
critical status delta: none
route delta: active large clone -> exact shortened 2 x 4 bucket
new assumptions: none beyond the parent factor branch
next action: pay/classify the shortened bucket or compile the rank-two horn
```

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_active_clone_locator_shortening_adapter/verify.py
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_active_clone_locator_shortening_adapter/verify.py --tamper-selftest
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_active_clone_locator_shortening_adapter/verify_audit.py
```
