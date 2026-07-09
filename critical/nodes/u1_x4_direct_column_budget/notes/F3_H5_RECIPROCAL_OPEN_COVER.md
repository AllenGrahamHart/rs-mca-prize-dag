# F3 h=5 reciprocal open cover

Status: PROVED OFFICIAL-ROW CHART COVER, NOT AN h=5 CLOSURE.

The base-free reciprocal system in
`F3_H5_BASEFREE_RECIPROCAL_SYSTEM.md` records all pairwise compatibility
equations for one shared support product `delta`.  This packet proves that, on
the official rows `n=2^s`, these pairwise equations cover every h=5 x83
survivor by a chart on which `delta` can be recovered.

## Open Cover

The five reciprocal slots are

```text
(P_1, D_1 bar_l9),
(P_2, D_2 bar_l8),
(P_3, D_3 bar_l7),
(P_4, D_4 bar_l6),
(l5,  bar_l5).
```

If any denominator slot is nonzero, the vanishing of all pairwise `2 x 2`
minors recovers a unique value of `delta` on that chart.  Thus the only
uncovered cell is

```text
bar_l5 = bar_l6 = bar_l7 = bar_l8 = bar_l9 = 0.
```

Since conjugation is an automorphism of the row field, this is the same as

```text
l5 = l6 = l7 = l8 = l9 = 0.
```

For an x83 survivor, the triangular low-key equations then give

```text
l1 = l2 = l3 = l4 = 0,
```

because every high part `P_j(l5,...,l9)` vanishes at the origin.  Therefore the
support locator would have the form

```text
L_R(X) = X^10 + l0.
```

All ten support roots would have the same tenth power.  But on the official
rows `H=mu_{2^s}`, the map

```text
x -> x^10
```

has kernel size

```text
gcd(10,2^s)=2.
```

Every fiber has size at most `2`, so it cannot contain a 10-support.  Hence the
all-zero denominator cell is empty on all official h=5 rows.

## Consequence

Every official-row h=5 x83 survivor lies on at least one of the five reciprocal
charts.  On that chart, the base-free pairwise equations recover the shared
`delta`; the h=5 norm-gate residual can therefore be attacked through the
rank-one compatibility system without a hidden all-zero high-coefficient cell.

This does not prove the rank-one compatibility system has no support solutions.
It only removes the chart-coverage caveat from the reciprocal formulation.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_reciprocal_open_cover.py
```

Expected digest:

```text
H5_RECIPROCAL_OPEN_COVER_PASS
```
