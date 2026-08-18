# Cycle 462: rank-eleven rank-two shortening and transversality

## Starting pins

```text
our SHA: 5e6815c60
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
upstream rich-flat tip: PR #1173 at 2788d5ec3
upstream support-local theorem: PR #1166
```

## Result: PROVED low-exception line terminal

The genuine rank-two evaluation triple has a three-dimensional residual
kernel. Dividing its degree-three locator transports the retained
`388650911452` first-owned slopes to

```text
(n',K',m')=(2097149,1048573,1116045)
```

and preserves at least 37,733 common residual roots per class. The complete
correction bucket has dimension at most six. Dimension at most four is
impossible because

```text
63397365764 < 388650911452,
```

so the correction rank is five or six.

Recomputing the exact support-local transversality bound gives

```text
rank 5, theta  9: 408591854341
rank 5, theta 10: 367732668907 < retained mass
rank 6, theta 294: 388738149260
rank 6, theta 295: 387420392821 < retained mass.
```

Thus rank five emits a direction approximation with at most 9 support
exceptions; rank six emits one with at most 294.

## Burn-down

```text
critical target attacked: rate_half_band_crossing_location
DAG delta: +1 background PROVED node, +5 edges
critical status delta: none
route delta: genuine rank-two triple -> shortened rank-5/6 low-exception record
new assumptions: none beyond the parent factor branch
next action: enter direction-mismatch recursion or exact split-pencil census
```

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_rank_two_triple_shortening_transversality/verify.py
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_rank_two_triple_shortening_transversality/verify.py --tamper-selftest
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_rank_two_triple_shortening_transversality/verify_audit.py
```
