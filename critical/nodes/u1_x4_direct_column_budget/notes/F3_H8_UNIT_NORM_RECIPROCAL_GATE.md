# F3 h=8 unit-norm reciprocal gate

Status: SYMBOLIC COMPILER / X83 INTERFACE, NOT AN h=8 CERTIFICATE.

This packet adds the unit-root constraint for the support product to the h=8
reciprocal equations.  It is the h=8 analogue of
`F3_H5_UNIT_NORM_RECIPROCAL_GATE.md`.

For an official-row support in roots of unity,

```text
delta * conjugate(delta) = 1.
```

## Hermitian Equations

The reciprocal compatibility compiler gives, for `j=1,...,7`,

```text
P_j = D_j delta * bar_c(16-j).
```

Conjugating and multiplying eliminates `delta`:

```text
P_j * conjugate(P_j) = D_j^2 c(16-j) bar_c(16-j).
```

Thus any official-row h=8 x83 survivor must satisfy seven Hermitian norm
equations `N_j=0` in the high locator coefficients and their conjugates.

## Replayed Profiles

The compiler verifies:

```text
N1: terms=19601 total=30 top_total=15 bar_total=15
N2: terms=13226 total=28 top_total=14 bar_total=14
N3: terms=7922  total=26 top_total=13 bar_total=13
N4: terms=4901  total=24 top_total=12 bar_total=12
N5: terms=2705  total=22 top_total=11 bar_total=11
N6: terms=1601  total=20 top_total=10 bar_total=10
N7: terms=842   total=18 top_total=9  bar_total=9
```

The equations are much larger than the linear reciprocal compatibility rows,
but they use the official-row unit-root property of the support product.  They
give the h=8 x83 branch a second `delta`-free surface that is independent of
the chosen base reciprocal row.

## Role In h=8

This still does not prove the h=8 non-antipodal x83 branch empty.  The current
necessary surface is now:

```text
non-antipodal x83 survivor
  => triangular low-key graph
  => at least one high odd locator coefficient nonzero
  => seven reciprocal compatibility equations
  => seven Hermitian unit-norm equations.
```

The next symbolic attack should use these equations chart-wise, rather than
expanding global fixed-point numerators.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_unit_norm_reciprocal_gate.py
```

Expected digest:

```text
H8_UNIT_NORM_RECIPROCAL_GATE_PASS
```
