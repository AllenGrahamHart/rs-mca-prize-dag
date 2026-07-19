# m720_h3_large_gate_replay

- **status:** PROVED
- **closure:** proof

## Statement

The M720 gate arithmetic reproduces the two large h=3 banked calibration facts:

```text
full_census(128,3,17921) = 18 anchored cores
full_census(256,3,65537) = 129 anchored cores
```

## Falsifier

An exact replay of either large h=3 row returning a different anchored-core
count, or a corrected banked calibration table.
