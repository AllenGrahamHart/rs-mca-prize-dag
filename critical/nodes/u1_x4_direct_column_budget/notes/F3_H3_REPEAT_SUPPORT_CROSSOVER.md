# F3 h=3 repeat-support crossover compiler

Status: CONDITIONAL CONSTANT COMPILER, NOT A SUPPORT THEOREM.

This packet translates the repeat-boundary support compiler into official-row
constant pressure.  It answers: if the remaining quotient support has a linear
bound, which official rows does the repeat-residue payment cover by itself?

## Input

The support compiler proves

```text
repeat_residue
  <= 1584 n^(5/3) + 4752 R_orb n^(5/3) + 18n^2.
```

Assume a future theorem

```text
R_orb <= C n.
```

Then

```text
repeat_residue
  <= 4752 C n^(8/3) + 1584 n^(5/3) + 18n^2.
```

For `n >= 1`, the lower powers are bounded by `n^(8/3)`, so the proof-safe
sufficient bound is

```text
repeat_residue <= (4752 C + 1602) n^(8/3).
```

Therefore this repeat-residue payment is below the cubic floor whenever

```text
n > (4752 C + 1602)^3.
```

This is conservative but exact.

## Official-Row Interpretation

The replay prints the first official power of two `2^s`, `13 <= s <= 41`, for
which this sufficient inequality applies.  Representative conclusions:

- `C=1/2` covers official rows from `2^36` upward;
- `C=1` covers official rows from `2^38` upward;
- `C=2` covers `2^41`;
- `C=4` does not cover any official row by this sufficient test.

Thus a merely linear support theorem is not enough by itself for all official
rows unless its constant is very small or the lower/mid rows are carried by
another certificate or sharper arithmetic.  This is useful T3 information:
the repeat-residue branch is asymptotically harmless under linear support, but
constants still matter.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_support_crossover.py
```

Expected digest:

```text
H3_REPEAT_SUPPORT_CROSSOVER_PASS
```
