# F3 h=3 repeat loose shared-core degree split

Status: PROVED ARITHMETIC COMPILER, NOT `LOOSE-A-RANK/NV` OR
`LOOSE-B-RANK/NV`.

This packet splits the two clean special loose branches into their common
six-map core and their branch-private two-map tails.

## Shared Core

The branch-geometry compiler proves the exact slope-map identifications

```text
branch_A.C_1  = branch_B.C_1,
branch_A.C_a  = branch_B.C_a,
branch_A.C_b  = branch_B.C_1b,
branch_A.C_1a = branch_B.C_1a,
branch_A.C_1b = branch_B.C_b,
branch_A.L_b  = branch_B.L_b.
```

For the denominator-cleared maps `1+c_i(a)X`, this shared six-map target has

```text
maps=6,  sum_a_degrees=10,  sum_total_degrees=14,  max_total_degree=5.
```

Thus any future loose-branch argument that only uses the shared core can be
proved once and reused for both clean branches.

## Private Tails

The only private maps on each clean branch are still

```text
C_ab, L_ab.
```

Their degree budgets are:

```text
branch A private: maps=2, sum_a_degrees=7, sum_total_degrees=8,  max_total=5;
branch B private: maps=2, sum_a_degrees=9, sum_total_degrees=10, max_total=7.
```

Consequently the full clean branch totals remain:

```text
branch A: 14 + 8  = 22,
branch B: 14 + 10 = 24.
```

## Role in h=3

This does not close either loose branch.  It refines the current residual:

```text
shared six-map one-parameter target, S_total=14;
branch A private tail, S_total=8;
branch B private tail, S_total=10.
```

So a future proof can either attack the existing eight-map branch targets
directly, or prove a common shared-core theorem and then handle the two
private tails separately.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_shared_core_degree.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_SHARED_CORE_DEGREE_PASS
```
