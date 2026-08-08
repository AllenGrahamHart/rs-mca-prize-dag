# Statement

## Claim `(KBP1B4-DE-P11-1)`

On the guarded deployed positive `433-1b -> O0a` role-cell-4 branch, every
outside case with

```text
xi in {0,1,2},  pairing = 11 = ((0,4),(1,5),(2,3))
```

is empty for all four source-sign rows and all four target-sign lanes. Thus

```text
3 parallel-DE omissions * 1 matching
* 4 source signs * 4 target lanes = 48 raw cases.
```

The exact computation treats `xi=0,2` and transports `xi=1` from the
identical positive `DE` copy. Every root of the necessary norm and every
numerator or denominator root introduced by rational inversion is lifted
through the original source equations. Across the 32 computed rows this
gives 304 candidate base-field roots, 192 guarded source points, 64
nonboundary quartic candidates, 64 nonzero colored-pair terminals, and 16
`f=0` target boundaries. There are no witnesses and no unresolved branches.

This pays three of the `7*15=105` cell-4 missing/matching slices. It does not
by itself pay the positive-`DE` cases at matching 14, close cell 4, close
`433-1b -> O0a`, or prove K3, LIST, MCA, or either Prize problem.

## Falsifier

A missing sign/lane row, an unlifted elimination-exception root, a guarded
finite row omitted from direct replay, an incomplete common-root or quartic
root set, or a live target satisfying all three matching equations.
