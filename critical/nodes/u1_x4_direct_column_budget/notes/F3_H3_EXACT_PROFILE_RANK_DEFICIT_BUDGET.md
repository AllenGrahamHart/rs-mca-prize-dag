# F3 h=3 exact-profile rank-deficit budget

Status: PROVED OFFICIAL-ROW ARITHMETIC INTERFACE, NOT `RC-RANK`.

The exact-profile route does not need full degree-space rank for each repaired
same-fiber conic chart.  It only needs the rank to beat the exact log-jet
condition count

```text
C_exact(A,D) = DA + 6D(D-1).
```

This packet records the amount of rank deficit the official exact-profile
boxes can tolerate.

## Deficit Form

For one repaired image, let

```text
degree_dim = L+1 = A + 6n(B-1).
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

The right side is the `allowed_deficit` printed by the compiler.

## Official Rows

For every official row `n=2^s`, `13 <= s <= 41`, using the exact-profile
bridge-budget boxes, the replay verifies:

```text
minimum rank room       = 1848,
minimum allowed deficit = 1847.
```

The first row is the tightest:

```text
s=13: degree_dim=1623378, C_exact=1621530,
      room=1848, allowed_deficit=1847.
```

The final row has much larger slack:

```text
s=41: room=1077314196, allowed_deficit=1077314195.
```

## Role

This is the correct way to use the conic-chart degree-space guardrail.  Since
same-fiber conic charts are not automatically degree-space full in every box,
the next `RC-RANK` theorem may instead prove a bounded-deficit statement.  Any
uniform deficit bound at most `1847` would already be enough for all official
exact-profile boxes, after the bridge assigns one exact-profile capacity unit
per repaired image.
The companion conic-chart large-gap pilot records bounded exact-rank evidence
on the known same-fiber chart: at `A=5,B=4` and `H=20,24,32`, the deficits are
`27,1,0`, while the first official exact-profile row has
`H/A = 8192/1362 = 4096/681`.

This is only arithmetic.  It does not prove the bounded-deficit theorem and it
does not assign activated shapes to repaired images.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_exact_profile_rank_deficit_budget.py
```

Expected digest:

```text
H3_EXACT_PROFILE_RANK_DEFICIT_BUDGET_PASS
```
