# Statement

## Claim `(KBP1B47-COMPLETE-1)`

The complete deployed positive `433-1b -> O0a` route is empty in the
duplicate-common-role orbit of source cells `[4,7]`.

Cell 4 is empty by `(KBP1B4-COMPLETE-1)`. For cell 7, exchange common target
roles `B,C` and, in a lane `(sigma_c,sigma_o)`, set

```text
A'=A, B'=C, C'=B,
D'=sigma_c D, E'=sigma_c E, F'=sigma_c F.        (KBP1B47-T-1)
```

The induced source-root action is

```text
(epsilon_1,epsilon_2) -> (epsilon_1,-epsilon_2). (KBP1B47-T-2)
```

This bijection sends common source role cell 4 to cell 7, preserves every
complete common Vieta row, fixes both target-lane invariants and all target
guards, and swaps only the two colored outside records
`bf <-> sigma_c cf`.  It therefore permutes bijectively all

```text
7 missing records * 15 matchings * 4 source signs * 4 target lanes
= 1680
```

principal cell-7 systems onto the proved-empty cell-4 systems. The exact
global rank-drop theorem independently excludes every deployed rank-drop
packet, including cell 7. Hence cell 7 is empty on both rank strata.

This use of the `B,C` exchange is valid only because the entire source cell 4
has now been closed.  It was not a valid shortcut for closing an individual
within-cell matching.  The theorem does not close another role-cell orbit,
all of `433-1b -> O0a`, positive coordinate parity, K3, LIST, MCA, or either
Prize problem.

## Falsifier

A common Vieta row, source sign, lane invariant, outside record, squared-sum
row, target guard, missing-record/matching case, or rank stratum not preserved
or covered by `(KBP1B47-T-1)--(KBP1B47-T-2)`.
