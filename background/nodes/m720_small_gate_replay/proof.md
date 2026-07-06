# proof: m720_small_gate_replay

The standalone verifier in this folder copies the `full_census` definitions
from `nodes/midlarge_h7_20/notes/modal_midlarge_h7_20.py`:

- `sig_general` computes the elementary-signature tuple
  `e_1, ..., e_{h-1}` and top coefficient `e_h`;
- two h-subsets form a trade when they are disjoint, have the same lower
  signature, and have unequal `e_h`;
- toral trades are exactly pairs whose halves are both single `mu_h` cosets.

It runs only the n=16 calibration rows, which are small enough for the WSL
laptop:

```text
full_census(16,3,17) -> 352 unordered trades
full_census(16,3,97) -> 16 unordered trades
full_census(16,4,17) -> 126 unordered trades = 120 non-toral + 6 toral
```

These are precisely the n=16 rows in the M720 ground-truth gate.
