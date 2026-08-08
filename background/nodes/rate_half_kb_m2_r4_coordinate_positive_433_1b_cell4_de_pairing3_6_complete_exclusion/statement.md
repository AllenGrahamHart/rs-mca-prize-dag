# Statement

## Claim `(KBP1B4-DE-P36C-1)`

In the deployed positive `433-1b -> O0a` cell-4 outside atlas, every labeled
slice

```text
xi in {0,1,2},  pairing in {3,6}
```

is empty. These are the six labels

```text
(0,3), (1,3), (2,3), (0,6), (1,6), (2,6),
```

forming three parallel-DE quotient orbits. Across four source signs and four
target lanes, the block contains `6*4*4=96` raw cases.

Together with the nine first-pair labels at pairings `0,1,2`, the live
cell-4 ledger is

```text
paid labels:  15 / 105,
live labels:  90,
paid orbits:   9 / 60,
live orbits:  51.
```

No label outside pairings `0,1,2,3,6` and `xi in {0,1,2}` is claimed.

## Falsifier

A parent scope that omits one displayed label, overlap with the first-pair
block, or quotient arithmetic different from `60-9=51` live orbits.
