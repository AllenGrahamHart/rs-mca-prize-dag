# F3 h=8 rank-one chart propagation

Status: PROVED ABSTRACT IDENTITIES FOR THE H8 RECIPROCAL CHARTS.

This packet records the rank-one algebra behind the h=8 chart-local reciprocal
targets.  It is independent of the large h=8 locator polynomials.

## Setup

For eight reciprocal slots `(A_i,B_i)`, the base-free equations are the minors

```text
Cij = B_j A_i - B_i A_j.
```

The unit rows are

```text
N_i = A_i bar_A_i - B_i bar_B_i.
```

## Minor Propagation

On chart `B_i != 0`, the seven incident minors `Cij` imply every nonincident
minor after saturating by `B_i`, because

```text
B_i*C_jk + B_k*C_ij - B_j*C_ik = 0.
```

For eight slots this gives:

```text
charts=8
incident_minors_per_chart=7
nonincident_minors_per_chart=21
minor_syzygies=168
total_pairwise_minors=28
```

## Unit Propagation

On chart `B_i*bar_B_i != 0`, one unit row `N_i` plus the incident minors and
their conjugates imply every other unit row after saturation:

```text
B_i bar_B_i N_j - B_j bar_B_j N_i in <C_ij, conjugate(C_ij)>.
```

For eight slots this gives:

```text
unit_targets_per_chart=7
unit_syzygies=56
```

## Role In h=8

This justifies the local systems in
`F3_H8_ODD_CHART_RECOVERY_COMPILER.md`: on one odd chart, seven incident
rank-one minors plus the matching Hermitian unit row recover the full
base-free reciprocal and unit-norm surface after chart saturation.

It does not prove any h=8 local system empty.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_rank_one_chart_propagation.py
```

Expected digest:

```text
H8_RANK_ONE_CHART_PROPAGATION_PASS
```
