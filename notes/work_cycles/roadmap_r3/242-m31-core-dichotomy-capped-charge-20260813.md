# Cycle 242: M31 core-dichotomy capped charge (2026-08-13)

Fix absorption cutoff `b_abs=65450`.  For any line selected by the recursive
bank, an actual total core

```text
g>=e+10-b_abs
```

synchronizes every explanation above that cutoff.  The exact weighted prefix
through `b_abs` plus one absolute line cap is at most `5161307`, so this
high-core branch pays the original family immediately.

In the complementary branch every peeled line has core at most
`G_e=e+9-b_abs`.  Adding this individual ceiling to the lower-aware convex
envelope keeps the residual threshold positive long enough for distinct-core
packing.  Supports `e=130222,130223` close after 14 threshold-18 lines:

```text
14*9736-C(14,2)*5 = 135849 > e.
```

Supports `e=130224,130225` close after 70 threshold-16 lines:

```text
70*2041-C(70,2)*5 = 130795 > e.
```

At adjacent `e=130226`, the first threshold is 14 and has zero forced core.
After 14,763 zero-lower-bound peels, the capped joint charge is `3199542`
and the next threshold is one.  The compiler cannot force another actual
line.  This is a route wall, not an unsafe certificate.

```text
start:                   bba3e159f
canonical prize:         fdfb20a42
upstream frontier:       #1163-#1166; #1165 @ 4f9ed736
result:                  NARROWED; four PROVED support payments
DAG delta:               +1 PROVED node, +4 edges
critical status delta:   none; replacement target remains TARGET
Mersenne residual:       130226<=e<=1044241
delta-star movement:     none
compute:                 exact arithmetic under RAMguard; no Modal
next route action:       replace the threshold-14 zero-core wall at
                         e=130226, or bridge toward the high-support interval
export target:           extend przchojecki/rs-mca PR #1165
```
