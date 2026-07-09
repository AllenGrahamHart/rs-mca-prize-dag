# F3 h=5 rank-one minor propagation

Status: PROVED ABSTRACT SYZYGY, NOT AN h=5 CLOSURE.

This packet records the algebraic reason the h=5 reciprocal target can be
localized to four incident minors on any nonzero denominator chart.

## Abstract Identity

For rank-one slots `(A_i,B_i)`, write

```text
C_ij = B_j A_i - B_i A_j.
```

For any three distinct slots `i,j,k`, the compiler verifies

```text
B_i C_jk + B_k C_ij - B_j C_ik = 0.
```

Therefore, on chart `B_i != 0`, the two incident minors `C_ij=C_ik=0` force
the nonincident minor `C_jk=0`.

## h=5 Consequence

The h=5 base-free reciprocal system has five slots and ten pairwise minors.  On
one chart, only four minors are incident to the chart denominator and the
remaining six are nonincident.  The identity above proves that those six
nonincident minors are saturated consequences of the four incident minors.

The compiler verifies all chart-to-minor instances:

```text
charts                         = 5
incident minors per chart       = 4
nonincident minors per chart    = 6
ordered chart syzygies verified = 30
total pairwise minors           = 10
```

Together with `F3_H5_RANK_ONE_UNIT_PROPAGATION.md`, this makes the chart-local
residual exact: four incident rank-one minors plus the chart unit condition
are equivalent, after saturating by the chart denominator, to the global
rank-one/unit system.

This does not prove that any chart-local h=5 system is empty.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_rank_one_minor_propagation.py
```

Expected digest:

```text
H5_RANK_ONE_MINOR_PROPAGATION_PASS
```
