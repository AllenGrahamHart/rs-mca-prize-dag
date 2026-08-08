# Statement

## Claim `(KBP1B4-DE-QUOT-1)`

In the deployed positive `433-1b -> O0a` cell-4 outside atlas, exchange of
the two identical positive `DE` records preserves the common source system,
source signs, target lane, product and squared-sum values, missing equations,
and all guards.

On the fifteen canonical perfect matchings of six residual records, the
induced involution has orbit decomposition

```text
{0}, {1}, {2},
{3,6}, {4,9}, {5,12}, {7,10}, {8,13}, {11,14}.   (KBP1B4-DE-QUOT-2)
```

For missing roles `xi=0,1`, the involution exchanges the two roles and fixes
the residual matching index after canonical deletion. For every
`xi in {2,3,4,5,6}`, it fixes the missing role and acts on matchings by
`(KBP1B4-DE-QUOT-2)`.

Consequently the full `7*15=105` missing/matching ledger has exactly

```text
15 + 5*9 = 60
```

parallel-`DE` exchange orbits. The proved first-pair block occupies six of
these orbits and nine labeled slices, leaving `54` orbit representatives
covering `96` live slices.

This is a symmetry quotient, not an exclusion of any additional slice. It
does not identify target lanes, source role cells `4` and `7`, or another
positive route.

## Falsifier

A different matching permutation, a product or squared-sum row changed by
the exchange, a guard not preserved, or a missing-role orbit outside the
displayed `15+5*9` census.
