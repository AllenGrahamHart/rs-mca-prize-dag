# Statement

## Claim `(KBP1B4-PDE-P14-1)`

On the guarded deployed positive `433-1b -> O0a` role-cell-4 branch, every
outside case with

```text
xi in {0,1},  pairing = 14 = ((0,5),(1,4),(2,3))
```

is empty for all four source-sign rows and all four target-sign lanes. Thus

```text
2 positive-DE omissions * 1 matching
* 4 source signs * 4 target lanes = 32 raw cases.
```

The exact computation treats `xi=0` and transports `xi=1` from the identical
positive `DE` copy. Every root of the necessary norm and every numerator or
denominator root introduced by rational inversion is lifted through the
original source equations. Across the 16 computed rows this gives 152
candidate base-field roots, 80 guarded source points, 128 nonboundary
quartic candidates, and 128 nonzero colored-pair terminals. There are no
target boundaries, witnesses, or unresolved branches.

This pays the two retained positive labels in the pairing-11/14 block. It
does not by itself close cell 4, close `433-1b -> O0a`, or prove K3, LIST,
MCA, or either Prize problem.

## Falsifier

A missing sign/lane row, an unlifted elimination-exception root, a guarded
finite row omitted from direct replay, an incomplete common-root or quartic
root set, or a live target satisfying all three matching equations.
