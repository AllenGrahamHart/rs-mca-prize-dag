# F3 h=8 x83 triangular obstruction compiler

Status: PROVED SYMBOLIC COMPILER, NOT AN h=8 CERTIFICATE.

This packet makes the remaining h=8 n=64 x83 support target more algebraic.
It derives the seven low obstruction keys from the same square-shift recurrence
used by the support certifier and proves that they are triangular in the low
locator coefficients.

## Setup

Let

```text
L_R(X) = X^16 + c15 X^15 + ... + c1 X + c0
```

be the locator of a 16-support.  The x83 recurrence forces a monic degree-8
polynomial

```text
S_R(X) = X^8 + s7 X^7 + ... + s0
```

by matching the coefficients of `S_R(X)^2` in degrees `15` down to `8`.
The low obstruction keys are

```text
E_j = [X^j](S_R(X)^2 - L_R(X)),   j=1,...,7.
```

An h=8 x83 full-zero support has all seven keys equal to zero.

## Triangular Form

The compiler verifies the exact shape

```text
D_j E_j = -D_j c_j + P_j(c8,c9,c10,c11,c12,c13,c14,c15),
```

with no dependence on `c0` or on any other low coefficient.  Thus the x83
full-zero equations force `c1,...,c7` as explicit polynomial functions of the
high half `c8,...,c15`.

The row data are:

```text
E1: denominator=33554432 terms=141 total_degree=15
E2: denominator=16777216 terms=116 total_degree=14
E3: denominator=4194304  terms=90  total_degree=13
E4: denominator=2097152  terms=71  total_degree=12
E5: denominator=262144   terms=53  total_degree=11
E6: denominator=131072   terms=41  total_degree=10
E7: denominator=32768    terms=30  total_degree=9
```

The first obstruction tested by the radius-shell certifier is `E7`.  Its
cleared formula is compact enough to print in the replay, and has only `30`
terms.

## Role In h=8

This does not shrink the support universe by itself.  It gives the future
non-antipodal certifier a stronger obstruction-key interface:

```text
x83 full-zero support
  => c1,...,c7 are forced by c8,...,c15,
     and at least one of c9,c11,c13,c15 is nonzero
     by F3_H8_X83_PARITY_REDUCTION.md.
```

Combined with the locator parity criterion, the remaining primitive h=8 branch
is exactly a non-even locator satisfying this triangular graph and the support
root constraints.  This is the algebraic target for a future obstruction-key
join or symbolic nonvanishing argument; it is not a global h=8 certificate.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_x83_triangular_obstruction.py
```

Expected digest:

```text
H8_X83_TRIANGULAR_OBSTRUCTION_PASS
```
