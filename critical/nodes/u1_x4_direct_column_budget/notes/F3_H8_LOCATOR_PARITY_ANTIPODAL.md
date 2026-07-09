# F3 h=8 locator parity criterion for antipodal supports

Status: PROVED SYMBOLIC CRITERION + FINITE-FIELD REPLAY.

This packet gives the h=8 n=64 support certifier a coefficient-level test for
the paid antipodal branch.  It is deliberately small: it does not certify the
primitive non-antipodal x83 residual, but it makes the branch split intrinsic to
the support locator rather than dependent on set-enumerator bookkeeping.

## Statement

Let `F` have odd characteristic and contain a primitive `64`th root `zeta`.
For a 16-support `R <= mu_64`, let

```text
L_R(X) = product_{r in R} (X-r).
```

Then the following are equivalent:

```text
R is antipodal, i.e. r in R => -r in R;
L_R(X) is an even polynomial;
all odd-degree coefficients of L_R vanish.
```

If these conditions hold and `eta = zeta^2`, then `R` is the full preimage of
the quotient 8-support

```text
A = { r^2 : r in R } <= mu_32
```

and

```text
L_R(X) = M_A(X^2),  M_A(Y) = product_{a in A} (Y-a).
```

Consequently every primitive h=8 n=64 support has a locator with at least one
nonzero odd coefficient.  The x83 support certifier can therefore route:

```text
odd locator coefficients all zero  => paid h=4 quotient branch;
some odd locator coefficient nonzero => primitive non-antipodal branch.
```

## Proof

If `R` is antipodal, pair each root as `{r,-r}`.  Each pair contributes
`(X-r)(X+r)=X^2-r^2`, so `L_R` is a polynomial in `X^2`.

Conversely, if `L_R` is even and `r` is a root, then

```text
0 = L_R(r) = L_R(-r).
```

The support is a set of distinct roots and the characteristic is not two, so
`-r` is the unique antipodal partner of `r` and also lies in `R`.  Hence `R` is
antipodal.  The coefficient formulation is just the definition of an even
polynomial.

For an antipodal support the paired factorization gives

```text
L_R(X) = product_{a in A} (X^2-a) = M_A(X^2).
```

## Role in T4

Combined with `F3_H8_ANTIPODAL_X83_QUOTIENT.md`, this gives a purely
coefficient-level paid-branch detector:

```text
even locator -> h=4 quotient obstruction ledger;
not even     -> remaining non-antipodal x83 support target.
```

Combined with `F3_H8_NONANTIPODAL_APERIODIC.md`, the second branch is also
rotation-aperiodic.  Thus the remaining h=8 obstruction is exactly an
aperiodic support whose locator has a nonzero odd coefficient and whose x83
forced-root obstructions all vanish.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_locator_parity_antipodal.py
```

Expected digest:

```text
H8_LOCATOR_PARITY_ANTIPODAL_PASS
```
