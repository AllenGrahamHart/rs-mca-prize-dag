# Statement

## Claim `(KBP1B4-DE+-P12-1)`

On the guarded deployed positive `433-1b -> O0a` role-cell-4 branch, every
case with

```text
xi in {0,1},  pairing = 12 = ((0,5),(1,2),(3,4))
```

is empty for all four source signs and four target lanes. The exact compiler
treats 16 `xi=0` rows; identical-positive-copy transport supplies 16 `xi=1`
rows, for 32 excluded raw cases.

The exact ledger has 224 candidate base roots, 320 guarded source points,
1,088 `(u,f)` rows, 960 nonzero missing-relation terminals, and 128
nonzero colored-pair terminals. There is no target boundary, colored
solution, witness, or unresolved branch.

The theorem does not independently recompute `xi=2`; that matching-12 label is
already supplied by the proved matching-5/12 quotient composition. It does
not close another matching orbit, cell 4, K3, MCA, or either Prize problem.

## Falsifier

A missing source/target lane, an unlifted exceptional root, or a live target
satisfying the omitted product/squared-sum equations and all three matching
equations.
