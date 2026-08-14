# Cycle 323: MCA rank-11 rank-nine fixed-chart local-cap fence (2026-08-14)

The fixed target from cycle 322 is not locally payable from its printed
rank-nine chart hypotheses. The new PROVED node
`rate_half_mca_rank11_rank9_fixed_chart_local_cap_fence` gives an explicit
official-row realization.

Choose a nonzero RS word `u` with exactly `K-1` evaluation roots `J`, and a
ten-dimensional correction space whose evaluation on `B subset J`,
`|B|=9`, has kernel `F u`. After deleting `J`, the coordinate and support
weights are

```text
N=n-(K-1)=1048577,
L=m-(K-1)=67473.
```

Place weight `L-1=67472` on each of eight affine owner points and place the
remaining `508801` coordinates at distinct unit owner points. The eight
heavy-to-unit pencils have

```text
8*508801=4070408
```

distinct directions. Each line contains exactly one heavy and one unit
owner point, so its lifted agreement support has size `m`. The heavy fibre
plus `J` has size `m-1>K-1`; the RS root bound therefore proves full
same-support pair noncontainment. Two heavy-fibre coordinates adjoined to
`B` give a rank-ten eleven-subset on a fixed-owner component. All error
differences lie in `span(r_1,u)`.

The strict comparison is

```text
4070408-2578110=1492298.
```

This construction does not instantiate the 32-anchor/18-dense-root ancestor
packet and is far below global unsafety. Its exact conclusion is narrower:
the selector output, considered in isolation, admits more than its guaranteed
population. A successful continuation must preserve pre-deduplication
component weights, couple charts, or invoke additional ancestor identities.

Focused verification:

```text
RATE_HALF_MCA_RANK11_RANK9_FIXED_CHART_LOCAL_CAP_FENCE_PASS
  slopes=4070408 excess=1492298 controls=6/6
RATE_HALF_MCA_RANK11_RANK9_FIXED_CHART_LOCAL_CAP_FENCE_AUDIT_PASS
  intervals=8 slopes=4070408 toy=15/15
```

No Modal computation was used. Both replayers use constant memory.

```text
DAG delta:             +1 PROVED local-cap fence, +1 requirement edge,
                       +1 evidence edge
critical status delta: none
rank-eleven delta:     chart-local rank-nine payment fenced
delta-star movement:   none
compute:               exact arithmetic and a 15-line toy only
next route action:     retain weighted component incidence through a
                       chronology-compatible owner assignment
```
