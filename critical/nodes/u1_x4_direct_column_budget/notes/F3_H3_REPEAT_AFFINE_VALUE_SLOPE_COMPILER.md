# F3 h=3 repeat affine value-slope compiler

Status: PROVED ALGEBRAIC NORMAL FORM PLUS FINITE GUARDRAILS.

This packet rewrites the active edge cubics in a form that unifies the
`lambda`-injectivity and `rho`-hit targets.

## Affine Form

The active edge cubic is

```text
P_E(T)=T^3-(lambda+2)T^2+(2lambda+1)T-m.
```

Equivalently,

```text
P_E(T)=A_lambda(T)-m,
```

where

```text
A_lambda(T)=T(T-1)^2 + lambda*T(2-T).
```

Thus an active edge over `lambda` with product `m` is exactly a 3-point
subgroup level fiber

```text
{T in H : A_lambda(T)=m}.
```

The same-`lambda` target becomes:

```text
for each lambda, at most one H-value m gives a 3-point active H-fiber.
```

This is the value-fiber form of `H3-LAMBDA-INJECTIVE`.

## Slope Form

For two active edges with data `(lambda,m)` and `(mu,n)`, `lambda != mu`, the
rho value is

```text
rho = (m-n)/(lambda-mu).
```

Because `A_lambda(T)` is affine in `lambda`, a common coordinate `t` satisfies

```text
rho = t(2-t).
```

Therefore `H3-RHO-HIT` is the slope-hit statement

```text
rho in {t(2-t): t in E}
```

for every lambda-distinct active edge pair.

## Guardrails

Boundary-style witness rows have no rho misses:

```text
p=7937  n=64  lambda_distinct_pairs=1  rho_hit=1  rho_miss=0
p=65537 n=256 lambda_distinct_pairs=28 rho_hit=28 rho_miss=0
p=91393 n=256 lambda_distinct_pairs=1  rho_hit=1  rho_miss=0
```

Rows with only one active edge have no lambda-distinct pairs.  The non-boundary
contrast row remains bad:

```text
p=97 n=32 lambda_distinct_pairs=104 rho_hit=22 rho_miss=82
```

## Role in h=3

The disjoint-edge half of the star theorem can now be attacked through the
single polynomial family `A_lambda`:

```text
H3-VALUE-INJECTIVE:
  fixed lambda has at most one active 3-point H-level fiber;

H3-SLOPE-HIT:
  secant slopes between active fibers are hit by T(2-T) on the source edge.
```

These are just renamed algebraic forms of `H3-LAMBDA-INJECTIVE` and
`H3-RHO-HIT`.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_affine_value_slope_compiler.py
```

Expected digest:

```text
H3_REPEAT_AFFINE_VALUE_SLOPE_COMPILER_PASS
```
