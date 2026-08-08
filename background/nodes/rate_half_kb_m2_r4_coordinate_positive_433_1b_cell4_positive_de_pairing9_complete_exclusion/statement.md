# Statement

## Claim `(KBP1B4-DE+-P9-1)`

On the guarded deployed positive `433-1b -> O0a` role-cell-4 branch, every
case with

```text
xi in {0,1},  pairing = 9 = ((0,4),(1,2),(3,5))
```

is empty for all four source signs and four target lanes. The exact compiler
treats 16 `xi=0` rows; identical-positive-copy transport supplies 16 `xi=1`
rows, for 32 excluded raw cases.

The exact ledger has 288 candidate base roots, 544 guarded source points,
1,472 `(u,f)` rows, 1,280 nonzero missing-relation terminals, and 192
nonzero colored-pair terminals. There is no target boundary, colored
solution, witness, or unresolved branch.

The theorem does not independently recompute `xi=2`; that matching-9 label is
already supplied by the proved matching-4/9 quotient composition. It does
not close another matching orbit, cell 4, K3, MCA, or either Prize problem.

## Falsifier

A missing source/target lane, an unlifted exceptional root, or a live target
satisfying the omitted product/squared-sum equations and all three matching
equations.
