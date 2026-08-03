# Statement

## Claim `(KBP1B3-DE-FIRST-1)`

On the guarded deployed positive `433-1b -> O0a` role-cell-3 branch, every
outside case with

```text
xi in {0,1,2},  pairing in {0,1,2}
```

is empty for all four source-sign pairs and all four target-sign lanes.  Thus
the complete

```text
3 DE missing copies * 3 first-pair matchings
* 4 source signs * 4 target lanes = 144 raw cases
```

block is excluded.

The pairing-zero rows are supplied by `(KBP1B3-XI0P0-1)`,
`(KBP1B3-XI1P0-1)`, and `(KBP1B3-XI2P0-1)`.  For pairings one and two, the
same proved target-free ledgers leave finite common points.  Solving the
missing squared-sum row first gives:

1. for the positive `DE` copy, two common points per source/pairing row have
   no field-valued `d`, while the other two have four roots each; the two
   residual paired equations then have gcd degree zero in `f` in all `128`
   point/lane/`d` rows per pairing; and
2. for the negative `DE` copy, no field-valued `d` root at any retained common
   point.

The second positive parallel copy is identical to the first for pairings one
and two because deleting either leaves the same value-by-value residual list.
The exact computed census has zero witnesses, zero target-boundary solutions,
and zero unresolved rows.

The claim does not cover `xi=3,...,6`, `pairing=3,...,14`, complete cell-3 or
positive-route closure, K3, LIST, MCA, or either Prize result.
