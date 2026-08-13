# Cycle 241: M31 lower-aware joint-core charge (2026-08-13)

The parent joint charge maximized over core sizes using only their common
upper budget.  Every peeled line also carries a certified total-core lower
bound.  Sorting these lower bounds and filling the largest coordinates first
to `m-1` gives a majorization-maximal vector for the increasing convex line
cap

```text
f(g)=(N-g)/(m-g).
```

This yields a smaller rigorous charge at the first two residual rows.  Both
`e=130220` and `e=130221` force 38 lines.  Their inside-core lower bounds have
runs `15811*5,2041*33`, so

```text
5*15811+33*2041-C(38,2)*5 = 142893 > e.
```

At adjacent `e=130222`, the same exact compiler reaches 288 removed lines.
Its envelope allocation is `67453*5,1037,0*282`, with charge `4910044`.
The resulting target `11867171` lies below base `12148280`, so no next line
is forced.  A rank-by-rank subset-core audit removes this artificial
concentration but still forces no second positive core.  This is a route
wall, not an unsafe certificate.

```text
start:                   c42df589a
canonical prize:         fdfb20a42
upstream frontier:       #1163-#1166; #1165 @ 8e627a27
result:                  NARROWED; two PROVED support payments
DAG delta:               +1 PROVED node, +4 edges
critical status delta:   none; replacement target remains TARGET
Mersenne residual:       130222<=e<=1044241
delta-star movement:     none
compute:                 exact arithmetic under RAMguard; no Modal
next route action:       add structure beyond first-order pairwise core
                         intersections at e=130222, or bridge toward the
                         high-support interval
export target:           extend przchojecki/rs-mca PR #1165
```
