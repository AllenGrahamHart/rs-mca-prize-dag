# F3 h=3 exact-profile bridge-budget compiler

Status: CONDITIONAL ARITHMETIC COMPILER, NOT `RC-NV` AND NOT THE BRIDGE
THEOREM.

This packet re-runs the non-diagonal bridge-budget arithmetic using the exact
rich-curve reduced-condition profile

```text
conditions = |Z| * (DA + 6D(D-1))
```

instead of the legacy sufficient count

```text
conditions = 13D(A+D)|Z|.
```

The nonvanishing theorem is still open.  The point of this packet is to record
the larger rank-capacity budget available once a future `RC-NV` proof targets
the exact profile.

## Result

For every official row `n=2^s`, `13 <= s <= 41`, the compiler verifies a
passing box with

```text
Z_exact = 33..21421.
```

The previous active non-diagonal table had

```text
Z_legacy = 16..10795.
```

The total official-row budget gain is

```text
51451.
```

The first and last rows are:

```text
s=13: old_Z=16,    exact_Z=33,    bound=127856  <= 16n=131072;
s=41: old_Z=10795, exact_Z=21421, bound=35184073533562 <= 16n.
```

## Maximality Within The Box Search

For a box to beat `16n`, the degree bound forces

```text
D >= ceil(3Z(B-1)/8).
```

The image-rank room condition and `A>=1` imply the necessary condition

```text
D(D-1) < n(B-1).
```

Combining these gives a finite analytic `B` cap for each attempted
`Z+1`.  The compiler verifies that `Z_exact` passes and `Z_exact+1` has no
feasible box under this cap on every official row.

## Role

This strengthens the arithmetic side of the `H3-BRIDGE-RANKCAP` route.  It
does not prove `F3-RANK-AVOID / RC-NV`, and it does not assign activated
non-toral shape pairs to repaired chart images.  It gives those future steps a
larger conditional rank-capacity budget.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_exact_profile_bridge_budget.py
```

Expected digest:

```text
H3_EXACT_PROFILE_BRIDGE_BUDGET_PASS
```
