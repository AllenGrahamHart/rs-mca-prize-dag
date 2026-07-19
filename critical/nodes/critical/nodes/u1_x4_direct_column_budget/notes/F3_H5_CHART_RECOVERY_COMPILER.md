# F3 h=5 chart-local reciprocal recovery

Status: SYMBOLIC COMPILER / NORM-GATE INTERFACE, NOT AN h=5 CLOSURE.

This packet refines the h=5 reciprocal norm-gate target after the base-free
rank-one system, the official open cover, and the unit-norm equations have been
compiled.

## Chart Recovery

The five reciprocal slots are

```text
(P_1, D_1 bar_l9),
(P_2, D_2 bar_l8),
(P_3, D_3 bar_l7),
(P_4, D_4 bar_l6),
(l5,  bar_l5).
```

On chart `i`, where the denominator of slot `i` is nonzero, the four incident
`2 x 2` minors recover the shared support product:

```text
delta = slot_i_num / slot_i_den.
```

For charts `1..4`, the condition `delta conjugate(delta)=1` is exactly the
corresponding Hermitian row `N_i`.

For the central chart `bar_l5 != 0`, however,

```text
delta = l5 / bar_l5
```

has unit norm identically, because conjugation swaps `l5` and `bar_l5`.  Thus
the central chart needs no additional high-degree Hermitian equation beyond the
four incident rank-one minors.

The compiler also verifies the saturated syzygies behind this statement.  For
each `j=1..4`,

```text
l5 * N_j in < Cj5, conjugate(Cj5) >.
```

On official rows the central chart has `bar_l5 != 0`, hence also `l5 != 0`, so
the four Hermitian rows follow from the incident central minors and their
conjugates.

The abstract propagation identity is recorded in
`F3_H5_RANK_ONE_UNIT_PROPAGATION.md`.  It proves that on any nonzero
denominator chart, one unit row plus the rank-one minors and their conjugates
forces the unit rows for all other slots.

The companion `F3_H5_RANK_ONE_MINOR_PROPAGATION.md` proves the corresponding
rank-one minor statement: on chart `B_i != 0`, the four incident minors force
the six nonincident minors after saturation by `B_i`.

The companion open-cover packet proves that official rows have at least one of
these five charts: the all-zero denominator cell would force
`L_R(X)=X^10+l0`, impossible for a 10-support in `mu_{2^s}`.

## Replayed Chart Table

The compiler verifies:

```text
chart 1: denominator=16384*bar_l9, minors=C12,C13,C14,C15, unit=N1
chart 2: denominator=16384*bar_l8, minors=C12,C23,C24,C25, unit=N2
chart 3: denominator=256*bar_l7,   minors=C13,C23,C34,C35, unit=N3
chart 4: denominator=512*bar_l6,   minors=C14,C24,C34,C45, unit=N4
chart 5: denominator=bar_l5,       minors=C15,C25,C35,C45, unit=TAUTOLOGY
```

The largest nontrivial unit equation is still `N1`, with `485` terms and total
degree `18`; the central chart has unit degree `0`.  Four central syzygies
verify that the global unit rows are saturated consequences of the central
rank-one equations.

The compiler also profiles the local equation systems:

```text
chart 1: 5 equations, 615 total terms, max degree 18
chart 2: 5 equations, 443 total terms, max degree 16
chart 3: 5 equations, 273 total terms, max degree 14
chart 4: 5 equations, 195 total terms, max degree 12
chart 5: 4 equations,  67 total terms, max degree 10
```

Thus the central chart is the smallest immediate symbolic target: it has only
the four incident rank-one minors and no Hermitian equation.
`F3_H5_CENTRAL_CHART_GRAPH.md` records the sharper graph form: after
saturating by `l5*bar_l5`, those four equations solve
`bar_l9,bar_l8,bar_l7,bar_l6` explicitly.

## Consequence

The h=5 symbolic residual can now be attacked chart by chart:

```text
official open cover
+ four incident rank-one minors on the selected chart
+ one unit equation on charts 1..4, or no unit equation on the central chart
=> no official h=5 x83 survivor.
```

This is a smaller local target than carrying all ten pairwise equations and all
four Hermitian equations at once.  It still does not prove that the h=5 branch
is empty.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_chart_recovery_compiler.py
```

Expected digest:

```text
H5_CHART_RECOVERY_COMPILER_PASS
```
