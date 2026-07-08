# F3 h=5 x83 triangular norm-gate compiler

Status: SYMBOLIC COMPILER / NORM-DIVISOR LEDGER, NOT AN h=5 CLOSURE.

This packet makes the h=5 norm-gate blocker more algebraic.  It derives the
h=5 x83 low obstruction keys from the square-shift recurrence and proves that
they are triangular in the low locator coefficients.  It does not prove that
the keys are nonzero for every official support.

## Setup

Let

```text
L_R(X) = X^10 + l9 X^9 + ... + l1 X + l0
```

be the locator of a 10-support.  The x83 recurrence forces a monic degree-5
polynomial

```text
S_R(X) = X^5 + s4 X^4 + ... + s0
```

from the top coefficients `l5,...,l9` by matching the degrees `9` down to `5`
in `S_R(X)^2`.  The low obstruction keys are

```text
E_j = [X^j](S_R(X)^2 - L_R(X)),  j=1,2,3,4.
```

An h=5 x83 full-zero support has `E_1=...=E_4=0` modulo the row prime.

## Triangular Form

The compiler verifies the exact triangular shape

```text
D_j E_j = -D_j l_j + P_j(l5,l6,l7,l8,l9),  j=1,2,3,4.
```

The denominators and conservative conjugate bounds are:

```text
E1: denominator=16384, terms=23, conjugate_bound=1,104,676,577,280
E2: denominator=16384, terms=19, conjugate_bound=195,853,455,360
E3: denominator=256,   terms=14, conjugate_bound=546,954,240
E4: denominator=512,   terms=11, conjugate_bound=187,415,040
```

The first obstruction is especially compact:

```text
512 E4 =
-512*l4 + 256*l5*l9 + 256*l6*l8 - 192*l6*l9^2
+ 128*l7^2 - 384*l7*l8*l9 + 160*l7*l9^3
- 64*l8^3 + 240*l8^2*l9^2 - 140*l8*l9^4 + 21*l9^6.
```

Thus the first x83 obstruction already forces `l4` as an explicit polynomial in
the top five locator coefficients modulo any odd row prime.  The remaining
three keys then successively force `l3,l2,l1`.

## Norm-Divisor Consequence

For a 10-root locator, every conjugate satisfies

```text
|l_i| <= binom(10,i).
```

The compiler uses this bound term-by-term on each cleared key.  If a primitive
h=5 finite-row support is not a char-zero paid support, then at least one
cleared low key is a nonzero cyclotomic integer.  If that support activates
modulo a row prime `p`, then `p` divides the norm of that nonzero key.

Using the largest low-key bound, one fixed nonzero h=5 key can activate at most
the following number of row primes `p >= n^2`:

```text
n=2^13: <= 6,302
n=2^16: <= 40,966
n=2^20: <= 524,376
n=2^24: <= 6,991,688
n=2^32: <= 1,342,404,147
n=2^41: <= 536,437,794,038
```

This is not strong enough by itself to close h=5, because it is a per-support
bound.  Its role is to replace the vague "p-specific norm-gate event" with an
explicit triangular obstruction system plus exact norm-divisor constants.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_x83_triangular_norm_gate.py
```

Expected digest:

```text
H5_X83_TRIANGULAR_NORM_GATE_PASS
```
