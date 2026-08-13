# Cycle 240: M31 joint-core charge peeling (2026-08-13)

The recursive line-peeling theorem charged every removed line independently
by the worst-case `Q=N-m+1`.  The same core geometry gives a much smaller
joint charge.  For `r` distinct parameterized lines with actual total-core
sizes `g_i`, pairwise inside-core intersections and the outside zero bound
give

```text
sum_i g_i <= min(r(m-1),e+C(r+1,2)(K-1)).
```

The individual line cap

```text
f(g)=(N-g)/(m-g)
```

is increasing and convex.  Moving core mass to endpoints shows that the
maximum total charge has as many cores `m-1` as the joint budget permits,
at most one remainder, and every other core zero.  This exact rational
envelope replaces `rQ` in the unsafe residual target.

The joint-charge recursion pays all

```text
130199<=e<=130219.
```

All 21 supports terminate by inside-core packing, with line-count census
`4:2, 5:10, 6:3, 7:2, 8:1, 10:1, 13:2`.  At the endpoint,

```text
18393+12*9736-C(13,2)*5 = 134835 > 130219.
```

At adjacent `e=130220`, the first threshold is 20 and the next 42 are 16.
Their core-packing lower bound is only `97018`.  When `r=43`, the joint
core allowance admits a second endpoint core, the charge rises to `1962895`,
and the next threshold falls to 13, whose forced-core lower bound is zero.
Later thresholds cannot increase.  This is a method wall, not an unsafe
certificate.

```text
start:                   eeee3a5a3
canonical prize:         fdfb20a42
upstream frontier:       #1163-#1166; #1165 @ bc6f8286
result:                  NARROWED; one PROVED interval payment
DAG delta:               +1 PROVED node, +4 edges
critical status delta:   none; replacement target remains TARGET
Mersenne residual:       130220<=e<=1044241
delta-star movement:     none
compute:                 subsecond constant-memory C replay under RAMguard;
                         no Modal
next route action:       add structure for the zero-core line population at
                         e=130220 or bridge toward the high-support interval
export target:           extend przchojecki/rs-mca PR #1165
```
