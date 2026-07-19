# proof: m720_remaining_gate_replay

The remaining gate-replay rows are supplied by two proved predicates:

- `m720_h5_n32_gate_replay`;
- `m720_h3_large_gate_replay`.

The first proves:

```text
full_census(32,5,97) = 96 unordered trades.
```

The second proves:

```text
full_census(128,3,17921) = 18 anchored cores
full_census(256,3,65537) = 129 anchored cores
```

These are exactly the rows in this node's statement. Therefore the remaining
M720 gate-replay packet is `PROVED`.
