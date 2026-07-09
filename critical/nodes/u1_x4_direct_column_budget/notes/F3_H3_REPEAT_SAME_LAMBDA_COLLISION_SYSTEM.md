# F3 h=3 repeat same-lambda collision system

Status: PROVED ALGEBRAIC/COMBINATORIAL COMPILER PLUS FINITE GUARDRAILS.

This packet states the fixed-`lambda` failure mode as an explicit collision
system in the ratio and scale coordinates.

## Generic Lambda

For `lambda != 1`, an active edge is an admissible `S_3` ratio orbit.  A
same-lambda failure is therefore:

```text
two distinct admissible S_3-orbits z and y for the same lambda.
```

Equivalently, both triples

```text
U_lambda(z), V_lambda(z), W_lambda(z)
U_lambda(y), V_lambda(y), W_lambda(y)
```

lie in `H`, and the two ratio orbits are distinct.

The compiler checks that distinct same-lambda generic orbits have distinct
reciprocal products and disjoint active coordinate edges.

## Lambda Equals One

For `lambda=1`, the generic ratio coordinate is replaced by the scale orbit

```text
{1+x, 1+omega x, 1+omega^2 x} subset H.
```

A same-lambda failure in this branch is two distinct primitive-cube scale
orbits.

## Guardrails

Boundary-style rows have no same-lambda collision systems:

```text
p=337   n=16  same_lambda_pairs=0
p=2017  n=32  same_lambda_pairs=0
p=4801  n=64  same_lambda_pairs=0
p=7937  n=64  same_lambda_pairs=0
p=65537 n=256 same_lambda_pairs=0
p=91393 n=256 same_lambda_pairs=0
```

The contrast row has exactly one generic same-lambda collision:

```text
p=97 n=32 repeated_generic_lambdas=1 generic_collision_pairs=1 same_lambda_pairs=1
```

## Role in h=3

The `H3-VALUE-INJECTIVE` target is now the absence of this collision system:

```text
no fixed lambda has two admissible generic ratio orbits,
and lambda=1 has at most one admissible scale orbit.
```

Together with the slope numerator target, this is the sharpened
lambda/slope interface for ruling out disjoint active edges.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_same_lambda_collision_system.py
```

Expected digest:

```text
H3_REPEAT_SAME_LAMBDA_COLLISION_SYSTEM_PASS
```
