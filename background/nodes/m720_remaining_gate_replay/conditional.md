# discharged conditional: m720_remaining_gate_replay

## Predicate nodes

- `m720_h5_n32_gate_replay`
- `m720_h3_large_gate_replay`

## Claim

The two large h=3 rows are now proved by `m720_h3_large_gate_replay`, so this
conditional has been discharged.

## Proof

The proved predicate `m720_h5_n32_gate_replay` supplies the locally bounded row:

```text
full_census(32,5,97) = 96 unordered trades
```

The proved predicate `m720_h3_large_gate_replay` supplies the two large h=3
rows:

```text
full_census(128,3,17921) = 18 anchored cores
full_census(256,3,65537) = 129 anchored cores
```

Together these are exactly the rows still needed beyond
`m720_small_gate_replay` for the M720 h=3,4,5 ground-truth table.
