# Cycle 243: M31 exact-layer slot-core packing (2026-08-13)

Every slot selected by the recursive line bank belongs to an exact layer
`h>b`.  If a slot has `lambda>=2` members and inside common core `u`, then
off-core agreement incidences on its parameterized affine line are disjoint.
Counting incidences in the fixed `e`-coordinate inside support gives

```text
lambda*h <= e+(lambda-1)u,
u >= ceil((lambda*h-e)/(lambda-1)).
```

This lower bound is already an inside-core bound, so it spends none of the
outside zero allowance.  Combining it with the preceding high-core/capped-
core dichotomy makes three distinct selected lines violate pairwise
inside-core packing for every support `130226<=e<=130236`.  The smallest
printed three-line lower bound is

```text
3*43948-C(3,2)*5 = 131829 > 130229.
```

At adjacent `e=130237`, the best useful legal bank forces only size-two
slots.  The exact-layer bound is then 807 and
`max_s(s*807-C(s,2)*5)=65529<e`.  The capped charge reaches threshold one
without contradiction.  This is a method wall, not evidence of unsafety;
the next route decision is exact primitive shift-pair control or a stronger
global coupling between size-two slots.

```text
start:                   2907b9fb3
canonical prize:         fdfb20a42
upstream frontier:       #1163-#1166; #1165 @ 42ff3c97
result:                  NARROWED; eleven PROVED support payments
DAG delta:               +1 PROVED node, +4 edges
critical status delta:   none; replacement target remains TARGET
Mersenne residual:       130237<=e<=1044241
delta-star movement:     none
compute:                 exact arithmetic under RAMguard; no Modal
next route action:       control the size-two primitive shift-pair bank at
                         e=130237, or bridge toward the high-support interval
export target:           extend przchojecki/rs-mca PR #1165
```
