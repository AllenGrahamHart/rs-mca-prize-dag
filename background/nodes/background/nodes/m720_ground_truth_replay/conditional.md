# discharged conditional: m720_ground_truth_replay

## Predicate nodes

- `m720_small_gate_replay`
- `m720_remaining_gate_replay`

## Claim

The remaining larger calibration rows are now proved by
`m720_remaining_gate_replay`, so this conditional has been discharged.

## Proof

The proved small-gate predicate replays the locally cheap n=16 rows:

```text
full_census(16,3,17) = 352
full_census(16,3,97) = 16
full_census(16,4,17) = 120 non-toral + 6 toral
```

using the same elementary-signature definitions as the M720 Modal helper.

The proved remaining predicate supplies the h=5 n=32 row and the two large h=3
rows:

```text
full_census(128,3,17921) = 18 anchored cores
full_census(256,3,65537) = 129 anchored cores
full_census(32,5,97) = 96 trades
```

Together these two predicates are exactly the banked h=3,4,5 calibration table
required by this node.
