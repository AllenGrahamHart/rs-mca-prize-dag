# F3 h=3 private-linear rank-deficit budget

Status: PROVED OFFICIAL-ROW ARITHMETIC INTERFACE, NOT
`F3-PRIVATE-LINEAR-RANK-AVOID`.

The private-linear alternate route does not need full private-linear
degree-space rank.  It only needs each repaired private-linear image to beat
the one-image condition count

```text
C_private(A,D) = 13 D(A+D).
```

This packet records the uniform rank deficit allowed by the official
`Z_private` boxes.

## Deficit Form

For one repaired private-linear image, let

```text
degree_dim = L_private + 1 = A + 3H(B-1).
```

If a future theorem proves

```text
rank >= degree_dim - Delta,
```

then the one-image private-linear rank inequality

```text
rank > 13D(A+D)
```

holds as soon as

```text
Delta <= degree_dim - 13D(A+D) - 1.
```

The right side is the `allowed_deficit` printed by the replay.

## Official Rows

For every official row `n=2^s`, `13 <= s <= 41`, using the retuned
private-linear `Z_private` boxes, the replay verifies:

```text
minimum rank room       = 26,
minimum allowed deficit = 25.
```

The tight row is not the first official row:

```text
s=16: Z_private=47, degree_dim=24576578,
      13D(A+D)=24576552, room=26, allowed_deficit=25.
```

The final row has much larger slack:

```text
s=41: allowed_deficit=1536224960.
```

## Role

This weakens the private-linear rank theorem interface from exact
degree-space fullness to a bounded-deficit statement:

```text
rank >= A + 3H(B-1) - 25
```

would already be enough for all official private-linear boxes, provided the
separate private-linear bridge assigns activated shapes to distinct
rank-effective repaired images within `Z_private`.

The tolerance is much tighter than the degree-2 exact-profile tolerance
`1847`.  This explains why the private-linear route remains an alternate: it
has a larger bridge budget, but a stricter rank-deficit requirement.

This packet is only arithmetic.  It does not prove the bounded-deficit theorem
and it does not prove the private-linear bridge.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_private_linear_rank_deficit_budget.py
```

Expected digest:

```text
H3_PRIVATE_LINEAR_RANK_DEFICIT_BUDGET_PASS
```
