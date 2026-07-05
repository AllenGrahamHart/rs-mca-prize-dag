# m720_h5_n32_gate_replay

- **status:** PROVED
- **closure:** verifier

## Statement

The M720 `full_census` arithmetic reproduces the locally bounded h=5 row:

```text
full_census(32,5,97) = 96 unordered trades
```

The exact replay also classifies all 96 as non-toral and finds 30 anchored
cores.

## Falsifier

A complete local replay of `full_census(32,5,97)` returning any count other
than 96 unordered trades.
