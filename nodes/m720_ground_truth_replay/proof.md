# proof: m720_ground_truth_replay

The full h=3,4,5 calibration table is the union of two proved replay packets:

- `m720_small_gate_replay` proves the n=16 rows:

```text
full_census(16,3,17) = 352 trades
full_census(16,3,97) = 16 trades
full_census(16,4,17) = 120 non-toral + 6 toral
```

- `m720_remaining_gate_replay` proves the remaining rows:

```text
full_census(128,3,17921) = 18 anchored cores
full_census(256,3,65537) = 129 anchored cores
full_census(32,5,97) = 96 trades
```

Together these six exact rows are precisely the M720 h=3,4,5 ground-truth
table. Hence this node is `PROVED`.
