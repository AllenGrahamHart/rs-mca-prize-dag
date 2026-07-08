# F3 h=3 repeat quadratic-rho compiler

Status: PROVED ALGEBRAIC COMPILER PLUS FINITE GUARDRAILS.

This packet normalizes the `H3-NO-QUADRATIC-MISS` target from the
pair-intersection compiler.

## Rho Normal Form

For two active edge cubics with data `(lambda,m)` and `(mu,n)`, assume
`lambda != mu`.  The pair-intersection compiler gives the quadratic condition

```text
-(lambda-mu)T^2 + 2(lambda-mu)T - (m-n) = 0.
```

Dividing by `lambda-mu`, this becomes

```text
T^2 - 2T + rho = 0,
rho = (m-n)/(lambda-mu).
```

Equivalently,

```text
T(2-T) = rho.
```

Therefore the intersection of the two active edges is exactly

```text
{t in E : t(2-t)=rho}.
```

Thus `H3-NO-QUADRATIC-MISS` is the assertion that this set is nonempty for
every lambda-distinct active edge pair in the boundary-style regime.

## Guardrails

Boundary-style witness rows:

```text
p=337   n=16  lambda_distinct_pairs=0  rho_miss=0
p=2017  n=32  lambda_distinct_pairs=0  rho_miss=0
p=4801  n=64  lambda_distinct_pairs=0  rho_miss=0
p=7937  n=64  lambda_distinct_pairs=1  rho_hit=1 rho_miss=0
p=65537 n=256 lambda_distinct_pairs=28 rho_hit=28 rho_miss=0
p=91393 n=256 lambda_distinct_pairs=1  rho_hit=1 rho_miss=0
```

The non-boundary contrast row has many misses:

```text
p=97 n=32 lambda_distinct_pairs=104 rho_hit=22 rho_miss=82
```

## Role in h=3

The quadratic half of the disjoint-edge theorem is now:

```text
H3-RHO-HIT:
  for every lambda-distinct active boundary-style edge pair,
  rho=(m-n)/(lambda-mu) lies in {t(2-t): t in E}.
```

Together with `H3-LAMBDA-INJECTIVE`, this proves `H3-NO-DISJOINT-EDGES`.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_quadratic_rho_compiler.py
```

Expected digest:

```text
H3_REPEAT_QUADRATIC_RHO_COMPILER_PASS
```
