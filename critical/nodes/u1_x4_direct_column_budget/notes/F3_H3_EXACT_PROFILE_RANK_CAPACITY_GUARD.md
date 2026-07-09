# F3 h=3 exact-profile rank-capacity guard

Status: PROVED OFFICIAL-ROW ARITHMETIC GUARD, NOT `RC-RANK` AND NOT THE
BRIDGE THEOREM.

The exact reduced-condition profile changes the rank-capacity unit from

```text
13D(A+D)
```

to

```text
C_exact(A,D) = DA + 6D(D-1).
```

This packet records what that does, and does not, buy on the official
exact-profile bridge-budget rows.

## Result

For every official row `n=2^s`, `13 <= s <= 41`, using the exact-profile box
from `F3_H3_EXACT_PROFILE_BRIDGE_BUDGET.md`, the compiler verifies:

```text
floor((A B^3 - 1) / C_exact) = Z_exact,
floor(((A + 6n(B-1)) - 1) / C_exact) = 1,
floor((A(3B-2) - 1) / C_exact) = 0.
```

The three lines mean:

1. the printed `Z_exact=33..21421` is exactly the strict rank capacity allowed
   by the full coefficient box;
2. even a degree-space-full repaired image has one unit of exact-profile
   capacity, so duplicate curve images cannot be paid twice by a one-image
   rank theorem;
3. the constant-ratio collapsed model still has zero capacity in every
   official exact-profile row.

The last point is important because the old toy `D=1` rank sample is no longer
a good collapsed-control warning after switching to the exact profile.  The
official rows have large `D`, and there the collapsed model remains rank-bad.

## Consequence For The Bridge

The larger exact-profile budget should be read as:

```text
H3-BRIDGE-RANKCAP-EXACT(Z_exact):
  assign activated non-toral h=3 shape pairs to distinct rank-effective
  repaired curve images whose consumed exact-profile capacity is at most
  Z_exact(s).
```

This is still conditional on the finite-row `RC-RANK`/minor nonvanishing
theorem.  The guard only prevents a mistaken interpretation where the larger
`Z_exact` is spent on repeated copies of the same curve image or on the
constant-ratio collapsed cells.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_exact_profile_rank_capacity_guard.py
```

Expected digest:

```text
H3_EXACT_PROFILE_RANK_CAPACITY_GUARD_PASS
```
