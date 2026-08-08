# Statement

## Claim `(KBP1B4-DE-P6P-1)`

On the guarded deployed positive `433-1b -> O0a` role-cell-4 branch, every
outside case with

```text
xi in {0,1},  pairing = 6 = ((0,3),(1,2),(4,5))
```

is empty for all four source-sign rows and all four target-sign lanes. Thus

```text
2 positive-DE omissions * 1 matching
* 4 source signs * 4 target lanes = 32 raw cases
```

are excluded.

The exact computation treats `xi=0`; deleting the other identical positive
`DE` copy gives the same ordered residual products, squared sums, matching,
and guards for `xi=1`. Every root of the necessary norm and every numerator
or denominator root introduced by rational inversion is lifted through the
original source equations. Across 16 computed rows this gives 160 candidate
base-field roots, 176 guarded source points, 48 candidates satisfying the
omitted squared-sum equation, and 96 nonzero colored-pair terminals. There
are no target boundaries, witnesses, or unresolved branches.

The negative-DE slice `(xi,pairing)=(2,6)` is supplied by the separate
parallel-DE matching quotient. This node does not itself reprove that slice,
close cell 4, K3, MCA, or either Prize problem.

## Falsifier

A missing sign row, an unlifted norm or inversion-exception root, a finite
quadratic root omitted from replay, or a target surviving the colored pair.
