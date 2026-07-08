# F3 h=3 repeat forced-cover crossover

Status: CONDITIONAL CONSTANT COMPILER, NOT A FORCED-COVER THEOREM.

This packet translates the elementary forced-fiber degree bound into official
row pressure for the remaining forced-coordinate cover problem.

## Input

If a forced-coordinate set `A0` covers every active normalized triple, then
`F3_H3_REPEAT_FORCED_FIBER_DEGREE_BOUND.md` proves

```text
B_line <= 6 |A0| n.
```

Combining this with the repeat-boundary support compiler gives

```text
repeat_residue <= (72 |A0| + 18)n^2.
```

Therefore, for a fixed cover size `F`, the repeat residue is below the cubic
floor whenever

```text
n > 72F + 18.
```

More generally, a cover size `F(n)=O(n^eta)` with `eta<1` pays the repeat
residue subcubically.

## Official-Row Interpretation

The replay prints exact sufficient coverage for several cover profiles.  The
main takeaways are:

- constant-size forced covers are extremely strong: even `F=64` covers every
  official row `2^13..2^41`;
- `F=128` starts at `2^14`;
- `F=1024` starts at `2^17`;
- `F <= ceil(sqrt(n))` covers every official row;
- `F <= ceil(n^(2/3))` starts at `2^19`;
- a linear cover fraction `F <= ceil(n/128)` starts at `2^13`, while
  `ceil(n/256)` also covers all official rows with wider margin.

Thus the forced-coordinate route does not need a constant cover to be useful.
Any substantially sublinear cover is enough asymptotically, and even some
small linear fractions beat the cubic floor in the official range.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_forced_cover_crossover.py
```

Expected digest:

```text
H3_REPEAT_FORCED_COVER_CROSSOVER_PASS
```
