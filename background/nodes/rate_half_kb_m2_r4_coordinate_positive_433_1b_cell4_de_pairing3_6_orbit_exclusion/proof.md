# Proof

The pairing-3 parent proves `(0,3)`, `(1,3)`, and `(2,3)` empty for every
source-sign row and target lane.

The parallel-DE quotient parent proves the exact involution on labels. For
`xi=0,1`, exchange of the identical positive records exchanges the missing
role and fixes the canonical residual matching index. Hence

```text
(0,3) <-> (1,3).
```

For `xi>=2`, the missing role is fixed and the matching permutation contains
the transposition `3 <-> 6`. Hence

```text
(2,3) <-> (2,6).
```

The union consists of four labels in two quotient orbits. The involution
preserves source signs and target lane, so each label represents 16 raw
cases and the block contains 64.

Before this composition, the first-pair theorem paid nine labels in six
orbits, leaving 96 labels in 54 orbits. The two disjoint orbits above contain
four of those labels. Subtraction gives

```text
96 - 4 = 92 live labels,
54 - 2 = 52 live orbits.
```

No action sends `(0,3)` or `(1,3)` to pairing 6, so no further label is
deducted. QED.
