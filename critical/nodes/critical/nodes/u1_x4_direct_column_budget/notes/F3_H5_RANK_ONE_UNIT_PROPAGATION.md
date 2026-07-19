# F3 h=5 rank-one unit propagation

Status: PROVED ABSTRACT SYZYGY, NOT AN h=5 CLOSURE.

This packet records the algebra behind the chart-local h=5 reciprocal target.
It is independent of the explicit h=5 polynomials.

## Abstract Identity

For rank-one slots `(A_i,B_i)`, write

```text
C_ij = B_j A_i - B_i A_j
N_i  = A_i conjugate(A_i) - B_i conjugate(B_i).
```

The compiler verifies the identity

```text
B_i conjugate(B_i) N_j - B_j conjugate(B_j) N_i
  = -conjugate(B_i) conjugate(A_j) C_ij
    -B_j A_i conjugate(C_ij).
```

Thus, on chart `B_i != 0`, the equations

```text
N_i = 0,  C_ij = 0,  conjugate(C_ij) = 0
```

force `N_j=0`.

## h=5 Consequence

For the h=5 reciprocal slots, this proves that one unit equation per nonzero
denominator chart is enough:

```text
chart i in {1,2,3,4}:  four incident minors + N_i force all N_j;
central chart i=5:     N_5 is tautological, so the central minors force N_1..N_4.
```

The h=5 chart compiler also verifies the central saturated identities directly
after substituting the explicit h=5 slot polynomials.

This still leaves the real h=5 residual: prove that none of the five
chart-local rank-one systems has an official-row support solution.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_rank_one_unit_propagation.py
```

Expected digest:

```text
H5_RANK_ONE_UNIT_PROPAGATION_PASS
```
