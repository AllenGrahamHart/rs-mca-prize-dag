# m720_ground_truth_replay

- **status:** PROVED
- **closure:** proof

## Statement

The M720 gate arithmetic reproduces the banked h=3,4,5 calibration facts used
by the bounded-band scanner:

```text
full_census(16,3,17)      = 352 trades
full_census(16,3,97)      = 16 trades
full_census(128,3,17921)  = 18 anchored cores
full_census(256,3,65537)  = 129 anchored cores
full_census(16,4,17)      = 120 non-toral + 6 toral
full_census(32,5,97)      = 96 trades
```

## Falsifier

Any replay of the gate arithmetic returning a different count, or a corrected
banked calibration table.
