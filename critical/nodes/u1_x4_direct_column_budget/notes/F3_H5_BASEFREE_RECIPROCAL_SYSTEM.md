# F3 h=5 base-free reciprocal system

Status: SYMBOLIC COMPILER / NORM-GATE INTERFACE, NOT AN h=5 CLOSURE.

`F3_H5_RECIPROCAL_COMPATIBILITY_COMPILER.md` uses the `E4` row as a convenient
base chart.  This packet records the base-free version: all reciprocal rows,
including the central `l5` row, must be pairwise compatible with one shared
support product `delta`.

## Setup

For `j=1..4`, write the reciprocal h=5 rows as

```text
P_j = D_j delta * bar_l(10-j).
```

The central coefficient gives a fifth row

```text
l5 = delta * bar_l5.
```

Let the five slots be

```text
(P_1, D_1 bar_l9),
(P_2, D_2 bar_l8),
(P_3, D_3 bar_l7),
(P_4, D_4 bar_l6),
(l5,  bar_l5).
```

The existence of one `delta` implies every `2 x 2` minor vanishes:

```text
Cij = slot_j_den * slot_i_num - slot_i_den * slot_j_num = 0.
```

## Replayed Profiles

The compiler verifies all ten pairwise equations:

```text
C12: terms=40, total=10, top_total=9, bar_total=1
C13: terms=35, total=10, top_total=9, bar_total=1
C14: terms=32, total=10, top_total=9, bar_total=1
C15: terms=23, total=10, top_total=9, bar_total=1
C23: terms=31, total=9,  top_total=8, bar_total=1
C24: terms=28, total=9,  top_total=8, bar_total=1
C25: terms=19, total=9,  top_total=8, bar_total=1
C34: terms=23, total=8,  top_total=7, bar_total=1
C35: terms=14, total=8,  top_total=7, bar_total=1
C45: terms=11, total=7,  top_total=6, bar_total=1
```

Thus the base-free h=5 norm-gate target is a rank-one compatibility system:
ten explicit equations, all linear in the conjugate variables and with maximum
total degree `10`.

This still only gives a necessary algebraic surface.  On a chart where one
slot denominator is nonzero, the corresponding four equations recover the
single `delta`; if all available denominators vanish, a future proof must handle
that degenerate reciprocal cell separately.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_basefree_reciprocal_system.py
```

Expected digest:

```text
H5_BASEFREE_RECIPROCAL_SYSTEM_PASS
```
