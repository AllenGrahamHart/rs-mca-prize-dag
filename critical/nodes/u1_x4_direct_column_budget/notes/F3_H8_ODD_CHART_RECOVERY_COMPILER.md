# F3 h=8 odd-chart reciprocal recovery

Status: SYMBOLIC COMPILER / X83 INTERFACE, NOT AN h=8 CERTIFICATE.

This packet combines the h=8 parity reduction, base-free reciprocal system, and
unit-norm equations into a four-chart local target for the remaining
non-antipodal x83 branch.

## Odd Open Cover

`F3_H8_X83_PARITY_REDUCTION.md` proves that any non-antipodal x83 full-zero
support has at least one nonzero high odd locator coefficient:

```text
c15, c13, c11, c9.
```

On official rows conjugation is an automorphism, so this gives an open cover by
the four reciprocal denominator charts

```text
D1*bar_c15 != 0,  D3*bar_c13 != 0,  D5*bar_c11 != 0,  D7*bar_c9 != 0.
```

Thus future symbolic attacks do not need all eight reciprocal charts for the
non-antipodal branch; they only need charts `1,3,5,7`.

## Chart Systems

On each odd chart, the seven incident rank-one minors recover the shared
support product `delta`, and the matching Hermitian row imposes
`delta*bar_delta=1`.
`F3_H8_RANK_ONE_CHART_PROPAGATION.md` proves the abstract propagation:
the seven incident minors imply the other twenty-one pairwise minors after
chart saturation, and the matching unit row implies the other seven unit rows
after conjugate saturation.

The compiler verifies:

```text
chart 1: denominator=33554432*bar_c15, minors=C12,C13,C14,C15,C16,C17,C18, unit=N1
chart 3: denominator=4194304*bar_c13,  minors=C13,C23,C34,C35,C36,C37,C38, unit=N3
chart 5: denominator=262144*bar_c11,   minors=C15,C25,C35,C45,C56,C57,C58, unit=N5
chart 7: denominator=32768*bar_c9,     minors=C17,C27,C37,C47,C57,C67,C78, unit=N7
```

The local equation profiles are:

```text
chart 1: 8 equations, 20977 total terms, max degree 30
chart 3: 8 equations, 8992  total terms, max degree 26
chart 5: 8 equations, 3553  total terms, max degree 22
chart 7: 8 equations, 1552  total terms, max degree 18
```

This isolates the h=8 symbolic residual to four explicit local systems.  Chart
`7` is the smallest immediate target; chart `1` is the largest because it
contains `N1`.

The companion `F3_H8_CHART7_GRAPH_REDUCTION.md` sharpens chart `7`: the seven
incident minors solve all non-chart bar variables over `P7`, and `N7` forces
that denominator to be live on the official chart after saturation by
`c9*bar_c9`.

## Role In h=8

This packet does not prove that the local systems are empty.  It replaces the
global non-antipodal x83 target with the sharper necessary form:

```text
non-antipodal x83 survivor
  => one of four odd charts
  => seven incident rank-one minors on that chart
  => matching Hermitian unit row
  => full reciprocal/unit surface after chart propagation.
```

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_odd_chart_recovery_compiler.py
```

Expected digest:

```text
H8_ODD_CHART_RECOVERY_COMPILER_PASS
```
