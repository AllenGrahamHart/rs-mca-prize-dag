# F3 h=8 antipodal x83 quotient reduction

Status: PROVED SYMBOLIC QUOTIENT REDUCTION + FINITE-FIELD REPLAY.

This packet separates the paid antipodal h=8 n=64 branch from the primitive
non-antipodal residual.  It proves that, on antipodal 16-supports, the h=8 x83
forced-root obstruction is exactly the h=4 quotient obstruction under the
substitution `Y=X^2`.

## Statement

Let `zeta` be a primitive `64`th root and put `eta=zeta^2`, a primitive `32`nd
root.  If `R <= mu_64` is antipodal, then it is the full preimage of an
8-support `A <= mu_32`:

```text
R = { +/- zeta^e : eta^e in A }.
```

Let

```text
L_R(X) = product_{r in R} (X-r),
M_A(Y) = product_{a in A} (Y-a).
```

Then

```text
L_R(X) = M_A(X^2).
```

Let `S_R(X)` be the forced monic degree-8 square root candidate recovered from
the top nine coefficients of `L_R`, and let `N_A(Y)` be the forced monic
degree-4 square root candidate recovered from the top five coefficients of
`M_A`.  The recursion is compatible with `Y=X^2`:

```text
S_R(X) = N_A(X^2).
```

Consequently the h=8 obstruction vector is just the h=4 quotient obstruction
with zeros inserted in odd degrees:

```text
obs_8(R) = (0, obs_4(A)_1, 0, obs_4(A)_2, 0, obs_4(A)_3, 0),
lambda_8(R) = lambda_4(A).
```

Therefore an antipodal support is x83 full-zero if and only if its quotient
support is full-zero for the degree-4 forced-root test.  When `lambda` is a
nonzero square, the canonical h=8 split is the antipodal lift of the canonical
h=4 quotient split.

## Role in T4

The h=8 n=64 support-first residual can now be stated without ambiguity:

```text
antipodal x83 full-zero supports are paid by the h=4 quotient ledger;
the primitive h=8 residual is non-antipodal x83 full-zero support.
```

This does not certify the non-antipodal branch.  It only proves that the
already-paid antipodal branch cannot hide a separate primitive h=8 obstruction.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_antipodal_x83_quotient.py
```

Expected digest:

```text
H8_ANTIPODAL_X83_QUOTIENT_PASS
```
