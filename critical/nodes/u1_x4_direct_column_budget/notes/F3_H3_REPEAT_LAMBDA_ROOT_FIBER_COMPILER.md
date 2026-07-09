# F3 h=3 repeat lambda-root fiber compiler

Status: PROVED ALGEBRAIC COMPILER PLUS FINITE GUARDRAILS.

This packet turns the reciprocal-product normal form into an exact fiber
statement on the reciprocal subgroup image

```text
S = {1/(u-1) : u in H, u != 1}.
```

## Root-To-Product Map

The reciprocal-product compiler gives the edge polynomial

```text
X^3 + (lambda-1)R X - R.
```

If `r` is a root, then

```text
r^3 + (lambda-1)Rr - R = 0.
```

Solving for `R` gives the rational map

```text
Phi_lambda(r) = r^3 / (1 - (lambda-1)r).
```

The denominator-zero case is a pole and cannot be a finite active edge root.

## Exact Fiber Form

For `lambda in H`, active edges with that lambda are exactly the 3-point
fibers of

```text
Phi_lambda : S -> F_p
```

whose fiber sum is zero.  The zero-sum condition is automatic for a 3-point
fiber because it is the root set of the monic cubic above.

Therefore the same-lambda target becomes:

```text
H3-LAMBDA-ROOT-FIBER-UNIQUE:
  for every lambda in H, Phi_lambda has at most one 3-point fiber on S.
```

This is the reciprocal-fiber version of `H3-VALUE-INJECTIVE`.

## Guardrails

Boundary-style witness rows:

```text
p=337   n=16  active_edges=1 lambda_values=1 max_lambda_fibers=1 same_lambda_pairs=0
p=2017  n=32  active_edges=1 lambda_values=1 max_lambda_fibers=1 same_lambda_pairs=0
p=4801  n=64  active_edges=1 lambda_values=1 max_lambda_fibers=1 same_lambda_pairs=0
p=7937  n=64  active_edges=2 lambda_values=2 max_lambda_fibers=1 same_lambda_pairs=0
p=65537 n=256 active_edges=8 lambda_values=8 max_lambda_fibers=1 same_lambda_pairs=0
p=91393 n=256 active_edges=2 lambda_values=2 max_lambda_fibers=1 same_lambda_pairs=0
```

The non-boundary contrast row has one repeated-lambda pair:

```text
p=97 n=32 active_edges=15 lambda_values=14 max_lambda_fibers=2 same_lambda_pairs=1
```

## Role in h=3

The disjoint same-lambda obstruction is now a fiber uniqueness theorem for the
explicit rational map `Phi_lambda` on `S`.  This is a sharper target than the
earlier ledger statement `sum_lambda binom(K_lambda,2)=0`.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_lambda_root_fiber_compiler.py
```

Expected digest:

```text
H3_REPEAT_LAMBDA_ROOT_FIBER_COMPILER_PASS
```
