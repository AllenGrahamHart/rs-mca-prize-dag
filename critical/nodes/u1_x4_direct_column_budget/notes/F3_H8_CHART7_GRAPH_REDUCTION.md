# F3 h=8 chart-7 graph reduction

Status: SYMBOLIC COMPILER / CHART-7 REDUCTION, NOT AN h=8 CLOSURE.

This packet records the explicit graph form of the smallest h=8 odd reciprocal
chart from `F3_H8_ODD_CHART_RECOVERY_COMPILER.md`.

## Chart 7

On the chart

```text
bar_c9 != 0,
```

official conjugation also gives `c9 != 0`.  The matching unit row is

```text
N7: P7 * conjugate(P7) = D7^2 c9 bar_c9.
```

Therefore, on official chart 7, `N7` forces `P7` and `conjugate(P7)` to be
nonzero.  After saturating by `c9*bar_c9*P7*conjugate(P7)`, the seven incident
rank-one minors solve all non-chart bar variables.

For target slots `j=1,...,6`,

```text
Cj7 = D7*bar_c9*P_j - D_j*bar_c(16-j)*P7,
```

so

```text
bar_c(16-j) = D7*bar_c9*P_j / (D_j*P7).
```

The central incident equation is

```text
C78 = bar_c8*P7 - D7*bar_c9*c8,
```

so

```text
bar_c8 = D7*bar_c9*c8 / P7.
```

## Replayed Rows

The compiler verifies:

```text
C17 solves bar_c15: numerator terms=140 graph terms=169 graph degree=16
C27 solves bar_c14: numerator terms=115 graph terms=144 graph degree=15
C37 solves bar_c13: numerator terms=89  graph terms=118 graph degree=14
C47 solves bar_c12: numerator terms=70  graph terms=99  graph degree=13
C57 solves bar_c11: numerator terms=52  graph terms=81  graph degree=12
C67 solves bar_c10: numerator terms=40  graph terms=69  graph degree=11
C78 solves bar_c8:  numerator terms=1   graph terms=30  graph degree=10
```

The chart part has:

```text
P7_terms=29
P7_degree=9
N7_terms=842
N7_degree=18
total_graph_terms=710
```

## Consequence

Chart 7 is not a generic eight-equation system in all reciprocal variables.
It is a rational graph over

```text
c8,...,c15,bar_c9
```

plus the single `N7` unit equation and the official support/root constraints.
The direct global substitution of this graph into `N7` is too large for the
local 60-second policy, so the next proof attempt should preserve the graph
form and attack conjugation/support compatibility lazily.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_chart7_graph_reduction.py
```

Expected digest:

```text
H8_CHART7_GRAPH_REDUCTION_PASS
```
