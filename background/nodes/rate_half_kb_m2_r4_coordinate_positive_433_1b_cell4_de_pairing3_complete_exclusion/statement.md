# Statement

## Claim `(KBP1B4-DE-P3-1)`

On the guarded deployed positive `433-1b -> O0a` role-cell-4 branch, every
outside case with

```text
xi in {0,1,2},  pairing = 3 = ((0,2),(1,3),(4,5))
```

is empty for all four source-sign rows and all four target-sign lanes. Thus

```text
3 parallel-DE omissions * 1 matching
* 4 source signs * 4 target lanes = 48 raw cases
```

are excluded.

The exact computation treats `xi=0` and `xi=2` separately and transports
`xi=1` from the identical positive `DE` copy. Every root of the necessary
norm and every numerator or denominator root introduced by rational
inversion is lifted through the original source equations. Across the 32
computed rows this gives 312 candidate base-field roots, 272 guarded source
points, 64 candidates satisfying the omitted squared-sum equation, 96
nonzero colored-pair terminals, and 16 `f=0` target boundaries. There are no
witnesses and no unresolved branches.

This pays three of the `7*15=105` cell-4 missing/matching slices. It does not
by itself pay matching 6, close cell 4 or orbit `[4,7]`, close
`433-1b -> O0a`, or prove K3, LIST, MCA, or either Prize problem.

## Falsifier

A missing source or target sign row, an unlifted elimination-exception root,
a guarded finite row omitted from the direct replay, or a live target with
all three matching equations and the missing product/squared-sum equations.
