# F3 h=3 repeat same-lambda J ramification

Status: PROVED ALGEBRAIC COMPILER, NOT `H3-VALUE-GEN-INJECTIVE`.

This packet records the ramification profile of the same-lambda quotient
invariant

```text
J(z) = (1+z+z^2)^3 / (z^2(1+z)^2).
```

It complements the J-invariant packet, which proves that `J(z)=J(y)` is
exactly the `S_3` orbit relation away from the recorded poles.

## Derivative

The compiler verifies

```text
J'(z) numerator   = (z-1)(z+2)(2z+1)(z^2+z+1)^2
J'(z) denominator = z^3(z+1)^3.
```

The generic same-lambda ratio domain already excludes

```text
z = 0,
z = -1,
z^2+z+1 = 0.
```

Therefore, on the generic domain and away from characteristics `2` and `3`,
the only derivative-zero orbit is

```text
{1, -2, -1/2}.
```

These three points are one `S_3` orbit, and the common critical value is

```text
J(1) = J(-2) = J(-1/2) = 27/4.
```

## Meaning

The quotient map has the expected finite stabilizer ramification at the
exceptional orbit `{1,-2,-1/2}`.  Apart from the already-excluded
`z^2+z+1=0` orbit, there is no additional structural ramification in the
generic ratio domain.

Thus the remaining `H3-VALUE-GEN-INJECTIVE` obstruction is not a hidden
singularity of `J`; it is the arithmetic question of whether two distinct
admissible `S_3` ratio orbits can both satisfy the six `H`-membership
conditions for the same `lambda`.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_same_lambda_j_ramification.py
```

Expected digest:

```text
H3_REPEAT_SAME_LAMBDA_J_RAMIFICATION_PASS
```
