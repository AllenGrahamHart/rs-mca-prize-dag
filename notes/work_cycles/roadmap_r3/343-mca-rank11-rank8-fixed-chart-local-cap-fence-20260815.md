# Cycle 343: MCA rank-11 rank-eight fixed-chart local-cap fence (2026-08-15)

This cycle tests whether the remaining lower rank-eight interval can be paid
from the current fixed-chart output alone.  An exact algebraic construction
shows that it cannot, even after retaining the weighted component-extension
multiplicity.

## Eight-petal construction

At residual shortening `K'=11`, choose a nine-set `B`, its locator `u_0`,
and the ten-space

```text
V'=span{1,X,...,X^7,u_0,Xu_0}.
```

Then `rank(ev_B)=8`, while every two-coordinate extension outside `B` has
rank ten.  Partition the remaining coordinates into eight petals of size
`67473` and a remainder of size `508794`.  Eight owners
`(t_e u_0,1)` and a greedy choice of the received first-column values on
the remainder give

```text
8*508794=4070352
```

globally distinct slopes.  Each exact support is one petal, `B`, and one
remainder coordinate.  It has size `67483`, is not contained in any
received pair core, and carries `C(67473,2)` rank-ten affine-owner component
extensions.  Error differences lie in the two-space
`span{u_0,r_1-1}`.

The greedy step excludes at most

```text
64(508794-1)+8*18=32562896<2130706433
```

field values, so the construction exists over the deployed field and can
avoid the eighteen dense slopes.  Locator multiplication through a deleted
common core of size `K-11` lifts it reversibly to the official row.

## Two target fences

The construction exceeds the distinct-record target by

```text
4070352-2578110=1492242.
```

It also exceeds the exact weighted demand in the same `(record,T)` unit:

```text
marked weight:    4070352*C(67473,2)=9265216597693056
weighted demand:                       5869376383979174
excess:                                3395840213713882.
```

The node is deliberately scoped to the target-router output.  The witness
does not have the unsafe-family size or the ten-dimensional normalized-
deviation span, and therefore does not refute any proved ancestor.  It
rules out a chart-local continuation that forgets those ancestors.

```text
RATE_HALF_MCA_RANK11_RANK8_FIXED_CHART_LOCAL_CAP_FENCE_PASS
  slopes=4070352 distinct_excess=1492242
  marked=9265216597693056 weighted_excess=3395840213713882
  controls=10/10
RATE_HALF_MCA_RANK11_RANK8_FIXED_CHART_LOCAL_CAP_FENCE_AUDIT_PASS
  toy_records=8 toy_slopes=8 components=24 rank_checks=45
```

```text
result:                NARROWED
DAG delta:             +1 PROVED route-fence node
critical status delta: none
rank-eight route:      target-local distinct and weighted caps fenced;
                       retain normalized-span/ancestor data or use
                       cross-chart chronology/global incidence coupling
delta-star movement:   none
compute:               exact arithmetic and a 19-coordinate toy audit
                       under the 256 MB guard; no Modal run needed
next route action:     formulate and discharge a chronology/global coupling
                       that uses information absent from the eight-petal
                       model
```
