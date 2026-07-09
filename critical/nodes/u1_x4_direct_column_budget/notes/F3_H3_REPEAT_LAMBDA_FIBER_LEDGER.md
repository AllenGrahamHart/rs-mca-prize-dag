# F3 h=3 repeat lambda-fiber ledger

Status: PROVED LEDGER PLUS FINITE GUARDRAILS.

This packet makes the `H3-NO-SAME-LAMBDA` target from the pair-intersection
compiler explicit.

## Ledger

For each active coordinate edge `E`, write

```text
lambda(E) = sum(E) - 2.
```

Let

```text
K_lambda = #{active coordinate edges E : lambda(E)=lambda}.
```

By the pair-intersection compiler, two distinct active edges with the same
`lambda` are automatically disjoint.  Therefore the number of same-`lambda`
disjoint pairs is exactly

```text
sum_lambda binom(K_lambda,2).
```

Thus

```text
H3-NO-SAME-LAMBDA
```

is equivalent to

```text
max_lambda K_lambda <= 1.
```

## Guardrails

Boundary-style witness rows:

```text
p=337   n=16  active_edges=1 lambda_values=1 max_K_lambda=1 same_lambda_pairs=0
p=2017  n=32  active_edges=1 lambda_values=1 max_K_lambda=1 same_lambda_pairs=0
p=4801  n=64  active_edges=1 lambda_values=1 max_K_lambda=1 same_lambda_pairs=0
p=7937  n=64  active_edges=2 lambda_values=2 max_K_lambda=1 same_lambda_pairs=0
p=65537 n=256 active_edges=8 lambda_values=8 max_K_lambda=1 same_lambda_pairs=0
p=91393 n=256 active_edges=2 lambda_values=2 max_K_lambda=1 same_lambda_pairs=0
```

The non-boundary contrast row has exactly one same-`lambda` collision:

```text
p=97 n=32 active_edges=15 lambda_values=14 max_K_lambda=2 same_lambda_pairs=1
```

## Role in h=3

The same-`lambda` part of the disjoint-edge theorem is now the injectivity
target

```text
H3-LAMBDA-INJECTIVE:
  the map E -> lambda(E) is injective on active boundary-style edges.
```

Together with `H3-NO-QUADRATIC-MISS`, this proves `H3-NO-DISJOINT-EDGES`.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_lambda_fiber_ledger.py
```

Expected digest:

```text
H3_REPEAT_LAMBDA_FIBER_LEDGER_PASS
```
