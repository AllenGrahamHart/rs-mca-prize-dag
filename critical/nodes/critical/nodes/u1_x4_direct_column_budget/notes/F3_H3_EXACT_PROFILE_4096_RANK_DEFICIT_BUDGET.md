# F3 h=3 exact-profile H3-ACT(4096) rank-deficit budget

Status: PROVED OFFICIAL-ROW ARITHMETIC INTERFACE, NOT `RC-RANK`.

This packet records the rank-deficit tolerance for the constructive
`H3-ACT(4096)` exact-profile floor from
`F3_H3_EXACT_PROFILE_4096_BUDGET_FLOOR.md`.

## Deficit Form

For one repaired conic image, let

```text
degree_dim = L+1 = A + 6n(B-1)
C_exact(A,D) = DA + 6D(D-1).
```

If a future theorem proves

```text
rank >= degree_dim - Delta,
```

then the exact-profile one-image rank inequality

```text
rank > C_exact(A,D)
```

holds as soon as

```text
Delta <= degree_dim - C_exact(A,D) - 1.
```

## Official Rows

For the original `H3-ACT(16)` exact-profile boxes, the minimum allowed deficit
was

```text
Delta <= 1847.
```

For the constructive `H3-ACT(4096)` floor boxes

```text
Z_4096_floor = 2112..1370944,
```

the replay verifies the improved uniform tolerance

```text
minimum rank room       = 2900
minimum allowed deficit = 2899.
```

The tight row is again the first official row:

```text
s=13: Z_4096_floor=2112, degree_dim=9145225,
      C_exact=9142325, room=2900, allowed_deficit=2899.
```

## Role

The conservative `H3-ACT(4096)` retune does two useful things at once:

```text
Z budget:        33..21421  ->  2112..1370944
rank tolerance:  Delta<=1847 -> Delta<=2899
```

The bridge and rank theorems are still open.  This packet only gives the
correct arithmetic interface for proving the exact-profile route at the weaker
official-row activation target.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_exact_profile_4096_rank_deficit_budget.py
```

Expected digest:

```text
H3_EXACT_PROFILE_4096_RANK_DEFICIT_BUDGET_PASS
```
