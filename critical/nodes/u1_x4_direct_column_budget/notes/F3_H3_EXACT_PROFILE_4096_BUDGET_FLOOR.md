# F3 h=3 exact-profile H3-ACT(4096) budget floor

Status: PROVED OFFICIAL-ROW ARITHMETIC RETARGETING LEDGER, NOT A BRIDGE
THEOREM, NOT A MAXIMALITY CLAIM.

This packet retunes the exact-profile bridge arithmetic after
`F3_H3_OFFICIAL_ACCIDENT_SLACK.md`.  It does not search for the largest
possible budget.  Instead it records explicit passing witnesses showing that
the current exact-profile budget table can be multiplied by `64` if the target
is weakened from `H3-ACT(16)` to official-row `H3-ACT(4096)`.

## Statement

The current exact-profile bridge-budget table proves, conditionally on the
rank and bridge theorems, budgets

```text
Z_exact = 33..21421
```

for the stronger target `H3-ACT(16)`.

For every official row `n=2^s`, `13 <= s <= 41`, the replay verifies explicit
exact-profile Stepanov boxes with

```text
Z_4096_floor = 64 * Z_exact.
```

Thus

```text
Z_4096_floor = 2112..1370944.
```

Each pinned witness satisfies the exact-profile inequalities and gives a
compiled activation bound

```text
bound <= 4096 n.
```

The largest row-wise ratio in the replay is `576927` ppm of the `4096 n`
activation target, so this is a conservative constructive retune rather than
a tight frontier.

## Role

This gives a proof-facing replacement target:

```text
F3-RANK-AVOID-EXACT
  + H3-BRIDGE-RANKCAP-EXACT(Z_4096_floor)
  => official-row H3-ACT(4096)
  => T3 < n^3 on all official rows.
```

The bridge theorem is still open: activated non-toral shape pairs must still be
assigned to repaired rank-effective images within the stated budget.  This
packet only proves that the arithmetic compiler can tolerate a budget `64`
times larger than the current `H3-ACT(16)` exact-profile table.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_exact_profile_4096_budget_floor.py
```

Expected digest:

```text
H3_EXACT_PROFILE_4096_BUDGET_FLOOR_PASS
```
