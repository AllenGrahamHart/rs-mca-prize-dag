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

## Upstream K3 export

The same theorem, recast in upstream's column-far fixed-union terminology,
was exported as draft PR
[`#1106`](https://github.com/przchojecki/rs-mca/pull/1106), commit
`98149fc6`. At the deployed KoalaBear MCA adjacent candidate it uses

```text
R=1048576,   r=981104,   h=67472,
B*=274980728111395087.
```

The exact `(GRK)` floors are at most `B*` for every `0<=d<=9`; the boundary
values are

```text
d=9:    55413538236037195,
d=10:  861057176799343503 > B*.
```

This removes direction-rank-defect conditions from the column-far
fixed-union charts through nullity nine. It does not count charts, pay the
sparse branch, move an endpoint, or close K3.
