# Cycle 359: MCA rank-11 K'=43 descending-support ladder payment (2026-08-15)

Cycle 358 left a support-five all-fallback wall at `K'=43`.  This cycle
retained that ceiling and recursively partitioned the still-unused
support-four, support-three, and support-two completion maxima.

## Cycle pins

```text
our start:       291986739177a8511ba46d969e93056d8cc321a3
our end:         cycle commit containing this record
canonical prize: 6ac775504aa7dd6489ae5175235084e270abf6d2
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   #1170 at 6e8e563dde5956320b78f8486cbe2bd958615d32
```

## Descending-support ladder

For source support `c`, let `M_c` be the maximum completion count.  The
universal ceiling gives `0<=M_c<=q`.  At stage `c`, either

```text
M_c=q-s for a unique 0<=s<=9-c,
```

or `M_c<=q-(10-c)` and the ladder descends.  Applying this split at source
supports `5,4,3,2` gives

```text
5+6+7+8+1=27
```

disjoint exhaustive leaves.  Terminal leaves use the direct source deletion
ceiling and every valid cross-support carrier; fallback ceilings persist at
all later stages.  The all-fallback leaf simultaneously has ceilings
`q-5,q-6,q-7,q-8`.

## K'=43 payment

Intersect all 27 leaf caps with the prior supportwise caps and weight by the
full deficits `C(11-d,2)`.  The largest premium is no longer a fallback.  It
is the explicit source-five defect-two leaf:

```text
39510045591272162389536743615445318852720199164.
```

Keeping every chart, kernel, and shadow term gives

```text
demand   =914483065418315732688791860860514116132015913976937462285372733
capacity =910026236077284983829442075178352287542838076252997808763061227
gap      =  4456829341030748859349785682161828589177837723939653522311506.
```

Both the record coefficient and floor-record cross are positive.  Replaying
the same 27 leaves at `K'=44` fails by capacity excess

```text
1729575114830772639212937201922834766923716849296098844264209.
```

The active `K'=44` leaf is again source-five defect two.  Extending only the
fallback ladder cannot improve it; the next proof must sharpen that explicit
branch, lower its rank-nine chart, or extract another shared resource.

```text
result:                PROVED K'=43 component-row closure
newly closed row:      43
closed prefix:         10..43
remaining rank nine:  44..15528
new nodes:             2 PROVED
new premise:           none
critical status delta: none; exact evidence frontier advanced one row
upstream delta:         K'=42 exported in #1170; this K'=43 result pending export
delta-star movement:   none
compute:               exact local arithmetic; four guarded verifier passes
next route action:     attack the explicit c=5,s=2 leaf at the K'=44 wall
```
