# F3 h=3 repeat reciprocal-product compiler

Status: PROVED ALGEBRAIC COMPILER PLUS FINITE GUARDRAILS.

This packet rewrites the disjoint-edge targets in the reciprocal chart

```text
r(u)=1/(u-1).
```

## Reciprocal Edge Polynomial

For an active edge, let `{r,s,t}` be its reciprocal coordinates.  The shifted
reciprocal form gives

```text
r+s+t=0.
```

Write

```text
Q = rs+rt+st,
R = rst.
```

Then the active edge is the root set of

```text
X^3 + QX - R = 0.
```

The original active-edge parameters satisfy

```text
lambda = 1 + Q/R,
m = uvw = lambda + 1/R.
```

Equivalently,

```text
Q = (lambda-1)R,
X^3 + (lambda-1)R X - R = 0.
```

Thus, for fixed `lambda`, the active edge is controlled by the single
reciprocal product `R`.

## Targets

The same-lambda target becomes:

```text
H3-RECIPROCAL-R-INJECTIVE:
  for each active lambda, at most one reciprocal product R gives a 3-root
  active edge in S={1/(u-1): u in H, u != 1}.
```

The rho target also has a reciprocal product form.  If two edges have
parameters `(lambda,R)` and `(mu,S)`, with `lambda != mu`, then

```text
rho = 1 + (R^-1 - S^-1)/(lambda-mu).
```

For a coordinate root `u=1+1/r`,

```text
u(2-u) = 1 - r^-2.
```

So `H3-SLOPE-HIT` is equivalent to

```text
rho in {1-r^-2 : r is a reciprocal root of the source edge}.
```

## Guardrails

Boundary-style witness rows:

```text
p=337   n=16  same_lambda_pairs=0  rho_miss=0
p=2017  n=32  same_lambda_pairs=0  rho_miss=0
p=4801  n=64  same_lambda_pairs=0  rho_miss=0
p=7937  n=64  same_lambda_pairs=0  rho_hit=1  rho_miss=0
p=65537 n=256 same_lambda_pairs=0  rho_hit=28 rho_miss=0
p=91393 n=256 same_lambda_pairs=0  rho_hit=1  rho_miss=0
```

The non-boundary contrast row hits both disjoint-edge failure modes:

```text
p=97 n=32 same_lambda_pairs=1 rho_hit=22 rho_miss=82
```

No same-lambda pair has the same reciprocal product `R`; if it did, the
reciprocal cubic would be identical and the active edge would be the same.

## Role in h=3

The disjoint-edge branch is now a statement about the one-parameter reciprocal
cubics

```text
X^3 + (lambda-1)R X - R.
```

Together with the reciprocal closure theorem for loose triangles, this is the
current sharp algebraic interface for proving `tau_coord <= 1`.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_reciprocal_product_compiler.py
```

Expected digest:

```text
H3_REPEAT_RECIPROCAL_PRODUCT_COMPILER_PASS
```
