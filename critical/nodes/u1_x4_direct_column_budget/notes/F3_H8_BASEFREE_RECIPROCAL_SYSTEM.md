# F3 h=8 base-free reciprocal system

Status: SYMBOLIC COMPILER / X83 INTERFACE, NOT AN h=8 CERTIFICATE.

`F3_H8_RECIPROCAL_COMPATIBILITY_COMPILER.md` uses the `E7` row as a convenient
base chart.  This packet records the base-free version: all reciprocal rows,
including the central `c8` row, must be pairwise compatible with one shared
support product `delta`.

## Setup

For `j=1,...,7`, write the reciprocal h=8 rows as

```text
P_j = D_j delta * bar_c(16-j).
```

The central coefficient gives an eighth row

```text
c8 = delta * bar_c8.
```

Let the eight slots be

```text
(P_1, D_1 bar_c15), ..., (P_7, D_7 bar_c9), (c8, bar_c8).
```

The existence of one `delta` implies every `2 x 2` minor vanishes:

```text
Cij = slot_j_den * slot_i_num - slot_i_den * slot_j_num = 0.
```

## Replayed Profiles

The compiler verifies all twenty-eight pairwise equations.  They are all
linear in the reciprocal bar variables, with:

```text
pairwise_equations=28
max_total_degree=16
max_top_total_degree=15
max_bar_total_degree=1
max_terms=255
```

The `E7`-based reciprocal compatibility rows are the seven incident equations
against the `E7`/central chart.  This base-free packet records the full
rank-one surface so future chart-local attacks can choose any nonzero
denominator slot.
The companion `F3_H8_ODD_CHART_RECOVERY_COMPILER.md` uses the parity reduction
to restrict the non-antipodal x83 branch to the four odd charts.

## Role In h=8

This still only gives a necessary algebraic surface.  On a chart where one slot
denominator is nonzero, the incident seven equations recover the single
`delta`; nonincident minors should then follow by rank-one propagation.  A
future h=8 open-cover argument must also handle the all-zero denominator cell.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_basefree_reciprocal_system.py
```

Expected digest:

```text
H8_BASEFREE_RECIPROCAL_SYSTEM_PASS
```
