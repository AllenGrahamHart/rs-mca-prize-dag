# Cycle 305: MCA rank-11 heavy-pair order-32 seed compiler (2026-08-14)

Cycle 304 paid rank-eleven families whose complete low-margin minimizing-pair
family shares `K-4922` pair-core coordinates. This cycle removes that global
premise and compiles every remaining unsafe line into the order-32 interface
used by Grande Finale v4.

At cutoff `theta<=387`, the exact interleaved pair cap is

```text
Q_10(387)
 =floor(C(1048586,10)/C(67095,10))
 =869784434119.
```

Pair types owning exactly one record therefore cost at most that amount.
Call all other pair types heavy. If the heavy cores shared `K-4922`
coordinates, the Cycle-304 shortened endpoint would cap the heavy types at
`94943`, giving

```text
low <=869784434119+94943*981105
    =962933486134,
total <=274791086998147432
      =B_*-189641113247655.
```

Thus an unsafe line has heavy-core intersection below `K-4922`.

The cross-pair coupling is finite. After the reversible rank-eleven gauge,
every minimizing direction `b` and every shifted intercept `a-c_0` lies in
the same ten-dimensional direction code `C'`. Fix one heavy pair. At most ten
further heavy pairs suffice for their component differences to span all
heavy-pair component differences. The intersection of these at most eleven
pair cores is therefore the full heavy-core intersection.

Every selected pair is heavy, so choose two owned slopes from it. The exact
fixed-pair exception sets are disjoint across slopes; consequently the two
supports intersect only inside that pair core. At most `22` actual records
therefore already have common support below `K-4922`. An unsafe line has at
least

```text
B_*+1-134944-274790124064526354
 =190604046733790
```

low-margin records, so distinct records pad the packet to exactly `32`
without increasing its common support.

The new proved node
`rate_half_mca_rank11_heavy_pair_order32_seed_compiler` preserves the actual
received line, slopes, explanations, supports, minimizing pairs, and
first-match chronology. It does not classify or pay the resulting packet.
The surviving theorem is now the same-owner classification/payment of an
order-32 packet whose common support is below `K-4922`.

Focused verification:

```text
RATE_HALF_MCA_RANK11_HEAVY_PAIR_ORDER32_SEED_COMPILER_PASS
  Q=869784434119 total=274791086998147432
  slack=189641113247655 basis=7/10 controls=8/8
RATE_HALF_MCA_RANK11_HEAVY_PAIR_ORDER32_SEED_COMPILER_AUDIT_PASS
  Q=869784434119 total=274791086998147432
  low_min=190604046733790 controls=4/4
DAG_MANIFEST_PASS nodes=2443 edges=7258 bytes=5555632 mutations=3/3
RUN_ALL_VERIFIERS total=2 failures=0
```

No Modal computation was used. This is a natural successor to upstream PR
`#1168`, but the existing Package-A branch remains coordinator-gated and was
not silently modified.

```text
start:                   5842715fa
DAG delta:               +1 PROVED compiler node, +2 requirement edges,
                         +1 evidence edge
critical status delta:   none
upstream terminal delta: vague cross-pair coupling replaced by an actual
                         small-common-support order-32 packet
delta-star movement:     none
compute:                 exact local arithmetic only; no Modal spend
next route action:       compare the packet after common-support factoring
                         with thm:partial-relative and isolate the first
                         unproved same-owner classification clause
```
