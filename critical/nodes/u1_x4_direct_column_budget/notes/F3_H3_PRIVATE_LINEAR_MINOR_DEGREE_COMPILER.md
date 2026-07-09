# F3 h=3 private-linear minor-degree compiler

Status: PROVED ARITHMETIC COMPILER, NOT `RC-RANK`.

This packet turns the private-linear normal form into explicit bad-locus degree
bounds for the remaining rank-avoidance theorem.  It does not prove that any
rank-good minor is nonzero on the actual F3 parameter image.

## Pre-registration

Question:

```text
In the normal form
  Y, (Y-1)/(Y-lambda), (Y-eta)/(Y-theta),
what degree bounds do the universal rank minors have as polynomials in
(lambda,eta,theta)?
```

Success criterion:

- derive entrywise parameter-degree bounds for the cleared substitution matrix;
- derive the corresponding bound for any rank minor;
- replay the bounds symbolically on small parameter boxes;
- keep nonvanishing and bridge assignments explicitly open.

Failure criterion:

- treat a degree bound as a nonvanishing proof;
- forget the split between `lambda` and the `(eta,theta)` pair;
- use a bound that depends on an unnormalized six-parameter private-linear
  model.

## Matrix Entries

In the private-linear normal form, a cleared column indexed by

```text
0 <= a < A,       0 <= b_1,b_2,b_3 < B
```

is

```text
C_{a,b}(Y) =
  Y^(a+H b_1)
  (Y-1)^(H b_2) (Y-lambda)^(H(B-1-b_2))
  (Y-eta)^(H b_3) (Y-theta)^(H(B-1-b_3)).
```

The coefficient of any power of `Y` in this column is a polynomial in
`lambda,eta,theta` with

```text
deg_lambda <= H(B-1-b_2),
deg_eta    <= H b_3,
deg_theta  <= H(B-1-b_3).
```

Consequently every matrix entry satisfies

```text
deg_lambda <= H(B-1),
deg_eta + deg_theta <= H(B-1),
total parameter degree <= 2H(B-1).
```

## Minor Bounds

For an `r x r` rank minor `Delta_r(lambda,eta,theta)`, multilinearity of the
determinant gives

```text
deg_lambda(Delta_r) <= r H(B-1),
deg_eta+theta(Delta_r) <= r H(B-1),
total degree(Delta_r) <= 2 r H(B-1).
```

Thus a future private-linear rank-avoidance proof can aim to exhibit, for each
official row and rank target

```text
r = 13 D(A+D) * capacity + 1,
```

a nonzero normal-form minor of total degree at most

```text
2 r H(B-1)
```

that remains nonzero modulo the row prime on the repaired F3 parameter image.

## Role

This reduces the private-linear bad-minor locus to an explicit bounded-degree
hypersurface problem in three parameters.  It still does not solve either of
the two hard parts:

- identifying a rank-good minor that is nonzero on the repaired F3 image over
  the actual row field;
- proving the geometric bridge/rank-capacity assignment.

## Replay

Standalone only:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_private_linear_minor_degree_compiler.py
```

Expected digest:

```text
H3_PRIVATE_LINEAR_MINOR_DEGREE_COMPILER_PASS
```
