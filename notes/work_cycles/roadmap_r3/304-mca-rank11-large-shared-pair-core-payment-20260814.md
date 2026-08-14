# Cycle 304: MCA rank-11 large shared pair-core payment (2026-08-14)

Cycle 303 proved that the local dense-pair terminal need not coalesce: twelve
distinct deficiency-one owners can each carry `238825` exact records. A
first-match audit of Grande Finale v4 showed why that construction does not
reach the primitive S/A/E residual. Its mixed-owner supports share a common
set of size `K-9`, so the correct next operation is shortening, not owner
identification.

The new proved node
`rate_half_mca_rank11_large_shared_pair_core_payment` closes a uniform
version of that branch. Split the post-near rank-eleven family at the proved
support-local cutoff `theta=388`. The high-margin family costs at most

```text
274790124064526354.
```

Assume every distinct minimizing pair used below the cutoff shares one
componentwise pair core `J` of size at least `K-4922`. If `d=K-|J|`,
shortening pair differences on `J` gives a two-fold interleaving of a GRS
code with

```text
N_d=1048576+d,
A_d=d+67085,
1<=d<=4922.
```

The ordinary MDS Johnson denominator simplifies to the linear expression

```text
D(d)=4501445801-914405d.
```

It is positive through `d=4922`, where it equals `744391`, and becomes
`-170014` at `d=4923`. The endpoint ordinary-list bound is exactly `94943`.
Its square is below the sextic field size, so the proved interleaving
collapse gives the same bound for ordered minimizing pairs. The exact
fixed-pair ratio cap then gives

```text
low records <=94943*981105=93149052015.
```

Adding the high family and disjoint near charge yields

```text
134944+274790124064526354+93149052015
 =274790217213713313
 =B_*-190510897681774.
```

This pays the complete shared-core branch and absorbs the Cycle-303
twelve-owner construction, whose shortened dimension is only nine. An
unsafe rank-eleven family must now have low-margin minimizing pair-core
intersection below `K-4922`. That is a materially sharper cross-pair/spread
target; no S/A/E owner is assumed or constructed.

Focused verification:

```text
RATE_HALF_MCA_RANK11_LARGE_SHARED_PAIR_CORE_PAYMENT_PASS
  dimensions=4922 pair_types=94943 low=93149052015
  slack=190510897681774 controls=8/8
RATE_HALF_MCA_RANK11_LARGE_SHARED_PAIR_CORE_PAYMENT_AUDIT_PASS
  list=94943 total=274790217213713313
  slack=190510897681774 controls=4/4
DAG_MANIFEST_PASS nodes=2442 edges=7255 bytes=5553161 mutations=3/3
RUN_ALL_VERIFIERS total=2 failures=0
```

No Modal computation was used; the complete dimension interval replay takes
well below one second under RAMguard.

```text
start:                   67d4398e8
DAG delta:               +1 PROVED branch-payment node, +2 requirement
                         edges, +1 evidence edge
critical status delta:   none
upstream terminal delta: common pair core >=K-4922 paid; smaller-core
                         cross-pair/spread residual remains
delta-star movement:     none
compute:                 exact local arithmetic only; no Modal spend
next route action:       derive a small-core diversity/spread compiler for
                         the theta<=387 minimizing pairs, preserving actual
                         line, support, slope, and first-owner chronology
```
