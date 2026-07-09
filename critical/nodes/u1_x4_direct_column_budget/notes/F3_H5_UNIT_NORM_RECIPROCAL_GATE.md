# F3 h=5 unit-norm reciprocal gate

Status: SYMBOLIC COMPILER / NORM-GATE INTERFACE, NOT AN h=5 CLOSURE.

This packet adds another `delta`-free consequence of the h=5 reciprocal
equations.  The support product `delta=l0` is a root of unity on the official
rows, so

```text
delta * conjugate(delta) = 1.
```

## Hermitian Equations

For `j=1..4`, the reciprocal rows are

```text
P_j = D_j delta * bar_l(10-j).
```

Conjugating and multiplying eliminates `delta`:

```text
P_j * conjugate(P_j) = D_j^2 l(10-j) bar_l(10-j).
```

Thus any official-row h=5 x83 survivor must satisfy four Hermitian norm
equations `N_j=0` in the high locator coefficients and their conjugates.

## Replayed Profiles

The compiler verifies:

```text
N1: terms=485, total=18, top_total=9, bar_total=9
N2: terms=325, total=16, top_total=8, bar_total=8
N3: terms=170, total=14, top_total=7, bar_total=7
N4: terms=101, total=12, top_total=6, bar_total=6
```

These equations are higher degree than the rank-one pairwise equations, but
they use the unit-root nature of the support product.  They should be useful
for a symbolic h=5 norm-gate incompatibility proof because they are necessary
on every reciprocal chart and do not require choosing a value of `delta`.

This still does not prove that the h=5 branch is empty.

The companion `F3_H5_CHART_RECOVERY_COMPILER.md` refines the chart use of these
equations.  On charts `1..4`, only the matching `N_j` is needed once the four
incident rank-one minors recover `delta`; on the central chart
`bar_l5 != 0`, `delta=l5/bar_l5` has unit norm identically, so no Hermitian row
is needed there.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_unit_norm_reciprocal_gate.py
```

Expected digest:

```text
H5_UNIT_NORM_RECIPROCAL_GATE_PASS
```
