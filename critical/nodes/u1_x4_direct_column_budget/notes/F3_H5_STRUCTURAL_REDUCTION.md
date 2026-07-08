# F3 h=5 structural reduction

Status: PROVED CLASSIFICATION REDUCTION, NOT AN h=5 ZERO THEOREM.

This note tightens the h=5 residual in T4.  The h=5 blocker is not an unknown
classification problem: the existing DAG already reduces every finite-row h=5
survivor to the p-specific x83 norm-gate branch.

## Inputs

The replay checks these DAG inputs:

```text
x24_char0_dyadic_descent: PROVED
x83_uniform_square_shift_obstruction_gate: PROVED
a_universal_trade_variety: PROVED
```

The relevant consequences are:

- `x24_char0_dyadic_descent`: over `mu_n(C)`, dyadic trades are exactly full
  fibers when `h` is a power of two, and there are no such trades when `h` is
  not a power of two.
- `x83_uniform_square_shift_obstruction_gate`: every finite-row minimal
  h-trade is either a char-zero paid trade or a p-specific norm-gate event.
- `a_universal_trade_variety`: the square-shift obstructions define a universal
  variety `W_h`; the row dependence enters through torsion/root-of-unity
  specialization and the row prime.

Since `h=5` is not a power of two, the char-zero branch is empty.  Therefore:

```text
Every finite-row h=5 minimal trade is a p-specific x83 norm-gate event.
```

## Consequence for F3/T4

The remaining h=5 task is now exactly one of:

1. prove a norm-gate incompatibility theorem excluding the h=5 x83
   p-specific branch for all `p = 1 mod n`, `p >= n^2`; or
2. produce a maintainable certificate family that verifies that branch is empty
   for every official row.

The current row certificates already prove selected zero instances.  They do
not cover the whole official row family and should not be promoted to a uniform
h=5 theorem.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_structural_reduction.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py
```

Expected digests:

```text
H5_STRUCTURAL_REDUCTION_PASS
H5_CERTIFICATE_COVERAGE_AUDIT_PASS
```
