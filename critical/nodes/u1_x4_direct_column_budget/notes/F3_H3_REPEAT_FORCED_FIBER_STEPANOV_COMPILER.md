# F3 h=3 repeat forced-fiber Stepanov compiler

Status: CONDITIONAL ARITHMETIC COMPILER, NOT A FORCED-FIBER BOUND.

This packet gives the exact Stepanov bookkeeping for the one-variable fibers
that arise in `F3_H3_REPEAT_SUPPORT_FORCED_POINT_REDUCTION.md`.

## Pre-registration

Question:

```text
If a forced-coordinate cover reduces B_line to fibers N_a, what auxiliary
polynomial compiler applies to N_a?
```

Success criterion:

- compute the degrees of the two forced-fiber membership maps;
- prove a reduced derivative condition bound;
- state the missing rank/nonvanishing theorem explicitly;
- avoid claiming that the h=2 affine-coset theorem already bounds `N_a`.

Failure criterion:

- treat `lambda_a(v)` as affine or Mobius when it is degree `2/1`;
- hide the source condition `v in H`;
- promote finite forced-point evidence to a theorem.

## Forced-Fiber Maps

Fix `a in H \ {1}` and use `X` for the remaining coordinate.  The forced-fiber
maps are

```text
w_a(X) = 1 - (a-1)(X-1)/(a+X-2),
lambda_a(X) = a+X+w_a(X)-2.
```

They share the denominator

```text
Q_a(X)=a+X-2.
```

The degrees are:

```text
w_a(X)      = P_1(X)/Q_a(X),   deg P_1 <= 1, deg Q_a = 1,
lambda_a(X) = P_2(X)/Q_a(X),   deg P_2 = 2, deg Q_a = 1.
```

Thus this is not an h=2 affine-coset intersection.  It is a two-condition
rational-fiber problem with one degree-`2/1` condition.

The inequality in `deg P_1 <= 1` matters: at the observed forced point
`a=2`, one has `w_2(X)=1/X`, so the first numerator degree drops to `0`.  The
compiler below uses the uniform upper bound.

## Auxiliary

For a forced-coordinate family `A0` of size `F`, use

```text
Phi(X,Y_1,Y_2),
deg_X < A,
deg_{Y_i} < B.
```

For fixed `a in A0`, substitute

```text
Psi_a(X)=Phi(X, w_a(X)^n, lambda_a(X)^n).
```

There are

```text
A B^2
```

coefficients.

After clearing denominators, the substituted degree is at most

```text
L_FF(A,B,n) = (A-1) + 3n(B-1).
```

Indeed, a monomial contributes one denominator-cleared block of degree
`n(B-1)` from `w_a`, and one block of maximum degree `2n(B-1)` from
`lambda_a`.

## Log-Jet Reduction

For a monomial

```text
m(X)=X^i w_a(X)^(n b_1) lambda_a(X)^(n b_2),
0 <= i < A, 0 <= b_j < B,
```

put

```text
S_a(X)=X P_1(X) P_2(X) Q_a(X).
```

Then `deg S_a <= 5`.  At admissible points no factor of `S_a` vanishes, and
`w_a(X)^n=lambda_a(X)^n=1`.  The same logarithmic jet recurrence used in the
rich-curve packet gives

```text
S_a(X)^j m^{(j)}(X)=m(X)W_j(X),
deg W_j <= 4j.
```

Therefore the `j`-th multiplicity condition is over-imposed by a polynomial in
`X` of degree `< A+4D`, giving at most

```text
5(A+D)
```

linear conditions per derivative order and per forced coordinate.  This proves

```text
FF-RED(5):
  conditions <= 5D(A+D)F.
```

## Conditional Compiler

The remaining theorem gate is:

```text
FF-RANK / FF-NV:
  the direct-sum forced-fiber substitution image over the forced-coordinate
  family has rank greater than 5D(A+D)F.
```

If

```text
5D(A+D)F < A B^2
```

and `FF-RANK` holds, then

```text
sum_{a in A0} N_a < F ((A-1)+3n(B-1))/D.
```

Combined with the forced-point reduction,

```text
B_line <= 3 sum_{a in A0} N_a.
```

This gives a second precise path to the quotient-support theorem: prove a
small forced-coordinate cover and prove `FF-RANK/FF-NV` for the corresponding
fibers.

## Replay

Standalone arithmetic check:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_forced_fiber_stepanov_compiler.py
```

Expected digest:

```text
H3_REPEAT_FORCED_FIBER_STEPANOV_COMPILER_PASS
```
