# Cycle 364: MCA rank-11 K'=60..70 cross-support collision payment (2026-08-15)

Cycle 363 closed `K'=54..59` by comparing same-support deletion carriers,
but the active `K'=60` branch left supports `6..9` on fallback.  The same
vanishing-space intersection has a mixed-support form and directly prices
those high-support strata.

## Cycle pins

```text
our start:       b8ce7859cfa0f40b26ba69b5c90148e295af45de
our end:         cycle commit containing this record
canonical prize: 69c14c8bc
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   #1170 at 0d7998d1b66d165a7eafc819371a26bc32572919
```

## Cross-support collision theorem

Let source support `c<=5` have exact nonempty defect `s`, and choose an
attaining carrier `B`.  For a target support `d` with `c+d<=11`, the source
and target deletion-vanishing spaces have dimensions `11-c` and `11-d`.
Their intersection has dimension at least

```text
12-c-d>0.
```

The common-root bound implies that every target deletion carrier has at
most `s+d-1` points outside `B`.  Splitting a target circuit by its exact
outside count gives

```text
C(b,d)+sum_(j=1)^d floor(
  C(b,d-j) C(m-b,j-1) (s+d-j) / j
),
```

for `0<s<q`, with exact containment `C(b,d)` at `s=0`.  No target cap is
inferred from the empty source value `s=q`.

## Eleven-row payment

Refine source supports `2..5` to every exact defect and apply the new charge
to all admissible targets.  Preserve every old cap, the joint support-four
charge, all `120` support-`6..9` terminal/fallback choices, every kernel
corank, and all rank-nine marks.  Grouped Pareto compression leaves between
`351` and `528` maximal vectors in each low-support group and seven in the
high-support group.

The active branch on `K'=60..71` is

```text
s_2=s_3=s_4=s_5=ceil(q/2),       c6F/c7F/c8F/c9F.
```

All rows `K'=60..70` have positive exact component gaps.  The smallest is
at `K'=70`:

```text
854274172985042754802177028749324962520517760595473749602211.
```

At `K'=71`, complete capacity exceeds demand by

```text
824875968499878215752683873455674299360608616555107905777434.
```

Primary and independently coded replays agree on all eleven safe rows, all
group frontiers, exact floor-sensitive payments, and the adjacent wall.

```text
result:                PROVED K'=60..70 component-row closure
newly closed rows:     60..70
closed prefix:         10..70
remaining rank nine:  71..15528
new nodes:             2 PROVED
new premise:           none
critical status delta: none; exact evidence frontier advanced eleven rows
upstream delta:         cycle-363 K'=54..59 packet exported to #1170
delta-star movement:   none
compute:               exact local arithmetic under 1 GiB cap; no Modal spend
next route action:     attack the balanced high-support fallback wall at K'=71
```
