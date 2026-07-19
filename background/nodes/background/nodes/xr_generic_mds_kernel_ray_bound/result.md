# Replay and candidate thresholds

Modal app `ap-z1dXkHXX1RqYhgEgJESrc2` replayed two complete finite MDS
syndrome-line rows and the exact six-candidate arithmetic. It returned

```text
XR_GENERIC_MDS_KERNEL_RAY_BOUND_PASS
finite_max=3,2
rowc-r1_4:d<=3 rowc-r1_8:d<=3 rowc-r1_16:d<=3
prize-r1_4:d<=11 prize-r1_8:d<=10 prize-r1_16:d<=9
```

Thus one fixed generic union chart fits below `8n^3` through excess `d=3`
at every RowC candidate. At the prize rows the paid depths are respectively
`11,10,9`. The next depth fails the same exact rational comparison in each
case. These are per-chart thresholds, not an aggregate payment over all
possible union sets.

The finite replays exhaust every syndrome-line endpoint pair on RS MDS
restrictions `(q,R,N,h)=(11,2,3,1)` and `(7,3,5,2)`. Removing genericity
produces a same-support tangent line with all `q` slopes, exceeding `(GRK)`;
the hypothesis is therefore load-bearing. Peak worker RSS was `58 MB`.

The repository-wide Modal replay passed `119/119` verifiers with no timeout,
hash mismatch, or remote error in app `ap-1neXhjFN7gdFPvtdx9mgcc`.
