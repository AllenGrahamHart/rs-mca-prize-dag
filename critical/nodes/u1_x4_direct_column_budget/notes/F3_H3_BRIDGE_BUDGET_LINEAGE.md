# F3 h=3 bridge-budget lineage

Status: REPLAYED ACCOUNTING LEDGER, NOT `RC-RANK` AND NOT `H3-ACT`.

This packet prevents a bookkeeping mistake in the h=3 bridge target.  The older
diagonal bridge-budget compiler is still valid, but it is no longer the active
`Z_budget` table.  The current h=3 rank-avoidance interface uses the improved
non-diagonal budget table.

## Budget Lineage

The diagonal compiler `F3_H3_BRIDGE_BUDGET_COMPILER.md` gave:

```text
Z_diag(13) = 11,       Z_diag(41) = 7420.
```

The non-diagonal low/high row compilers prove a strictly larger budget on every
official row:

```text
Z_budget(13) = 16,     Z_budget(41) = 10795.
```

Across all official exponents `13 <= s <= 41`, the replay verifies:

```text
diagonal Z range      = 11..7420
non-diagonal Z range  = 16..10795
total diagonal Z      = 35917
total non-diagonal Z  = 52255
total gain            = 16338
min per-row gain      = 5
max per-row gain      = 3375
```

Thus any current statement of

```text
H3-BRIDGE-RANKCAP(Z_budget(s))
```

should use the non-diagonal `Z_budget` table imported by
`F3_H3_RANK_AVOID_INTERFACE.md` and `F3_H3_FRONTIER_LEDGER.md`, not the older
diagonal `Z_diag` table.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_bridge_budget_lineage.py
```

Expected digest:

```text
H3_BRIDGE_BUDGET_LINEAGE_PASS
```
