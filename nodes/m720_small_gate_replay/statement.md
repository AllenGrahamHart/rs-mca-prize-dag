# m720_small_gate_replay

- **status:** PROVED
- **closure:** proof

## Statement

The M720 `full_census` arithmetic reproduces the locally cheap n=16 gate
facts:

```text
full_census(16,3,17) = 352 trades
full_census(16,3,97) = 16 trades
full_census(16,4,17) = 120 non-toral + 6 toral
```

## Falsifier

A local exact replay of any n=16 gate row returning a different count.
