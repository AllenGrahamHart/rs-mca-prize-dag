# Cycle 233: M31 two-boundary-layer case split (2026-08-13)

At the first residual Mersenne support `e=98231`, the division

```text
e-K=3s+q
```

has residue `q=2`.  This extra unit beyond the preceding residue-one close
supports a complete second boundary-layer decomposition.

- At least two top-third anchors synchronize both boundary layers, giving
  `P_(H-2)+(N-m+1)`.
- With one top anchor, two first-boundary members synchronize that layer.
  Charge the top anchor separately and use the sharper outside-core line cap
  `484`; if the layer has at most one member, charge it directly.
- With no top anchor, either two boundary missed sets intersect, in which
  case they synchronize the entire layer onto an outside-core line, or all
  missed sets are pairwise disjoint and the layer has at most
  `floor(e/(s+1))=3` members.

The five exact cases are

```text
16486411, 16434204, 16433721, 16434203, 16433722.
```

Their maximum is below the Mersenne budget by `290804`.  At `e=98232`, the
residue resets to zero, so the theorem stops cleanly without making an
unsafe claim.

```text
start:                   c2c37ceb8
canonical prize:         c8d48cd4b (no newer Fable commit)
upstream frontier:       #1163-#1166; #1165 @ b04c8f1d
result:                  NARROWED; one PROVED two-boundary payment
DAG delta:               +1 PROVED node, +4 edges
critical status delta:   none; replacement target remains TARGET
Mersenne residual:       98232<=e<=1044241
delta-star movement:     none
compute:                 two exact 65k-cap replays under RAMguard;
                         no Modal
next route action:       attack the residue-zero boundary defect and the
                         Koala full-lift chord wall
export target:           extend przchojecki/rs-mca PR #1165
```
