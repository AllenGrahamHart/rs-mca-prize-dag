# m720_mitm_enumerator_soundness

- **status:** PROVED
- **closure:** proof

## Statement

For the parameter range used by `modal_midlarge_h7_20.py`
(`n <= 1024`, `W <= n`, and exponents encoded in 11-bit fields), `mitm_slice`
is an exact anchored MITM enumerator over the window `[0,W)`: it counts exactly
the disjoint pairs

```text
P = {0} union P',   |P| = h,
Q subset {1,...,W-1},   |Q| = h,
P cap Q = empty,
```

with equal elementary signatures `e_1,...,e_{h-1}` and unequal `e_h`, and it
classifies such pairs as toral precisely when both halves are `mu_h` cosets.
When `W = n` and the run is not aborted, the anchored census is complete for
the full row.
