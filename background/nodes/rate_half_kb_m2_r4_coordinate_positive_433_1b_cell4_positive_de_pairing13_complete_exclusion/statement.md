# Statement

## Claim `(KBP1B4-DE+-P13-1)`

On the guarded deployed positive `433-1b -> O0a` role-cell-4 branch, every
case with

```text
xi in {0,1},  pairing = 13 = ((0,5),(1,3),(2,4))
```

is empty for all four source signs and four target lanes. The exact compiler
treats 16 `xi=0` rows; identical-positive-copy transport supplies 16 `xi=1`
rows, for 32 excluded raw cases.

The exact ledger has 224 candidate base roots, 208 target-norm roots, 320
guarded source points, and 1,088 `(u,f)` rows. Of these, 960 have a nonzero
missing-relation value and all 128 survivors have a nonzero colored-pair
value. There is no target boundary, colored solution, witness, or unresolved
branch.

The theorem does not independently recompute `xi=2`; that matching-13 label is
already supplied by the proved matching-8/13 quotient composition. It does
not close another matching orbit, cell 4, K3, MCA, or either Prize problem.

## Falsifier

A missing source/target lane, an unlifted exceptional root, or a live target
satisfying the omitted product/squared-sum equations and all three matching
equations.
