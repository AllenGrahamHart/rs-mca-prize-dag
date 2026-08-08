# Statement

## Claim `(KBP1B4-DE-FIRST-1)`

On the guarded deployed positive `433-1b -> O0a` role-cell-4 branch, every
outside case with

```text
xi in {0,1,2},  pairing in {0,1,2}
```

is empty for all four source-sign rows and all four target-sign lanes. Thus
the complete

```text
3 parallel-DE omissions * 3 first-pair matchings
* 4 source signs * 4 target lanes = 144 raw cases
```

block is excluded.

Canonical matchings `0`, `1`, and `2` of six ordered residual records are

```text
((0,1),(2,3),(4,5)),
((0,1),(2,4),(3,5)),
((0,1),(2,5),(3,4)).
```

They all retain positions `(0,1)` as the first pair. After deleting either
positive `DE` copy, those positions contain `(DE,-DE)`; after deleting the
negative copy they contain `(DE,DE)`. The three matching-zero parent
theorems prove that the corresponding necessary target-free cuts have no
guarded common point. The remaining two pairs therefore never need to be
solved.

This pays nine of the `7*15=105` cell-4 missing/matching slices and leaves
`96`. It does not cover `xi=3,...,6`, `pairing=3,...,14`, close cell `4` or
orbit `[4,7]`, close `433-1b -> O0a`, or prove K3, LIST, MCA, or either
Prize problem.

## Falsifier

A canonical pairing among indices `0,1,2` whose first pair is not `(0,1)`,
a residual record order different from the signed-edge atlas, or a guarded
common point surviving one of the three parent target-free cuts.
