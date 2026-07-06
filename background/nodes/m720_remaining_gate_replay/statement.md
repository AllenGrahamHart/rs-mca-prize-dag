# m720_remaining_gate_replay

- **status:** PROVED
- **closure:** proof

## Statement

The M720 gate arithmetic reproduces the remaining banked calibration facts by
combining the local h=5 n=32 replay with the h=3 large replay:

```text
full_census(128,3,17921) = 18 anchored cores
full_census(256,3,65537) = 129 anchored cores
full_census(32,5,97) = 96 trades
```

## Falsifier

Any remaining gate replay returning a different count, or a corrected banked
calibration table.
