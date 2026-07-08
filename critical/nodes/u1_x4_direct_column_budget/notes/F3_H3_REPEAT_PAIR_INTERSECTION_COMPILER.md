# F3 h=3 repeat pair-intersection compiler

Status: PROVED ALGEBRAIC COMPILER PLUS FINITE GUARDRAILS.

This packet sharpens the `H3-NO-DISJOINT-EDGES` target from the
star-obstruction taxonomy.

## Pair Difference

Let two active edges have cubic data

```text
P_E(T)=T^3-(lambda+2)T^2+(2lambda+1)T-m,
P_F(T)=T^3-(mu+2)T^2+(2mu+1)T-n.
```

Subtracting gives

```text
P_E(T)-P_F(T)
  = -(lambda-mu)T^2 + 2(lambda-mu)T - (m-n).
```

Therefore common roots of two active edge cubics must lie in the quadratic
difference locus.

If `lambda=mu`, then the difference is the constant `-(m-n)`.  Thus two
distinct active edges with the same `lambda` are automatically disjoint.

If `lambda != mu`, then every common coordinate is a root of

```text
Q_{E,F}(T)=-(lambda-mu)T^2+2(lambda-mu)T-(m-n).
```

Checking this quadratic on the three roots of one edge recovers the exact
intersection.

## Disjoint-Pair Cases

The disjoint-edge obstruction now splits into two algebraic cases:

```text
SAME-LAMBDA:
  two distinct active edges have the same lambda;

QUADRATIC-MISS:
  lambda != mu and Q_{E,F} misses the roots of the first edge.
```

Proving `H3-NO-DISJOINT-EDGES` is equivalent to ruling out both cases in the
boundary-style regime.

## Guardrails

Boundary-style witness rows:

```text
p=337   n=16  pairs=0  disjoint=0
p=2017  n=32  pairs=0  disjoint=0
p=4801  n=64  pairs=0  disjoint=0
p=7937  n=64  pairs=1  disjoint=0
p=65537 n=256 pairs=28 disjoint=0
p=91393 n=256 pairs=1  disjoint=0
```

The non-boundary contrast row has both obstruction mechanisms:

```text
p=97 n=32 pairs=105 disjoint=83 same_lambda=1 quadratic_miss=82
```

## Role in h=3

The first half of the star theorem is now:

```text
H3-NO-SAME-LAMBDA:
  no two distinct active boundary-style edges have the same lambda;

H3-NO-QUADRATIC-MISS:
  for lambda != mu, the quadratic difference Q_{E,F} hits the active roots.
```

Together these prove `H3-NO-DISJOINT-EDGES`.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_pair_intersection_compiler.py
```

Expected digest:

```text
H3_REPEAT_PAIR_INTERSECTION_COMPILER_PASS
```
