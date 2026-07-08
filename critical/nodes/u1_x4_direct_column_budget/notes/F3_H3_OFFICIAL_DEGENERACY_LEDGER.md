# F3 h=3 official degeneracy ledger

Status: PROVED LEDGER FOR OFFICIAL ROWS, NOT `RC-RANK` OR THE BRIDGE THEOREM.

This packet records which h=3 degeneracy cells remain relevant on the official
F3 rows `n=2^s`, `13 <= s <= 41`.

## Inputs

The ledger uses three already-banked facts:

- `F3_H3_CHAR0_CLASSIFICATION.md`: the toral h=3 column in `mu_n` exists
  exactly when `3 | n`, with unordered count `binom(n/3,2)`.
- `F3_H3_RICH_CURVE_DEGENERACY_FILTER.md`: constant-ratio rational-map pairs
  are exactly detectable; ratio in `H` collapses conditions, ratio outside `H`
  makes them incompatible.
- `F3_H3_HYPERBOLA_LINE_DEGENERACY.md`: the hyperbola-line cell is exactly
  `b=a^2/3` after adjoining a primitive cube root.

## Official-Row Consequence

For every official F3 row

```text
n = 2^s,    13 <= s <= 41,
```

one has `3 ∤ n`.  Therefore the toral h=3 branch is empty on the actual
official rows:

```text
toral_bound(2^s) = 0.
```

The h=3 repaired rich-curve/rank theorem still needs to exclude or pay:

```text
constant-ratio cells;
hyperbola-line cells b=a^2/3.
```

But it does not need an official-row toral budget term.  The toral term remains
useful in nonofficial evidence rows such as `n=96`, and in general statements
with `3 | n`; it is simply absent from the official F3 floor rows.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_official_degeneracy_ledger.py
```

Expected digest:

```text
H3_OFFICIAL_DEGENERACY_LEDGER_PASS
```
