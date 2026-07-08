# F3 h=3 repeat slope-ratio compiler

Status: PROVED ALGEBRAIC COMPILER PLUS FINITE GUARDRAILS.

This packet rewrites the lambda-distinct `H3-SLOPE-HIT` target in the same
ratio coordinates used for the same-lambda branch.

## Generic Branch

For `lambda != 1`, set

```text
a = lambda-1,
N(z)=1+z+z^2.
```

The generic lambda-ratio parametrization gives

```text
r = N(z)/(a z(1+z)),
s = zr,
t = -(1+z)r.
```

Therefore the reciprocal product satisfies

```text
R^-1 = -a^3 z^2(1+z)^2/N(z)^3.
```

The source-edge slope values are the three values

```text
u(2-u)=1-r^-2
```

on the reciprocal roots, equivalently the values obtained from the three
ratio-membership coordinates

```text
U_lambda(z), V_lambda(z), W_lambda(z).
```

## Rho Form

For lambda-distinct edges with reciprocal products `R` and `S`,

```text
rho = 1 + (R^-1-S^-1)/(lambda-mu).
```

Thus `H3-SLOPE-HIT` becomes:

```text
rho lies in the three source slope values.
```

This formulation also handles pairs involving the exceptional `lambda=1`
scale branch by using `R^-1=x^3` for the scale parameter
`{1+x,1+omega x,1+omega^2 x}`.

## Guardrails

Boundary-style rows have no rho misses:

```text
p=337   n=16  lambda_distinct_pairs=0  rho_miss=0
p=2017  n=32  lambda_distinct_pairs=0  rho_miss=0
p=4801  n=64  lambda_distinct_pairs=0  rho_miss=0
p=7937  n=64  lambda_distinct_pairs=1  rho_hit=1  rho_miss=0
p=65537 n=256 lambda_distinct_pairs=28 rho_hit=28 rho_miss=0
p=91393 n=256 lambda_distinct_pairs=1  rho_hit=1  rho_miss=0
```

The contrast row has both generic-generic pairs and pairs involving the
`lambda=1` branch, with many misses:

```text
p=97 n=32 lambda_distinct_pairs=104 lambda_one_pairs=14 rho_hit=22 rho_miss=82
```

## Role in h=3

The disjoint-edge branch now has two explicit ratio targets:

```text
H3-LAMBDA-RATIO-ORBIT-UNIQUE:
  fixed lambda has at most one admissible ratio orbit;

H3-SLOPE-RATIO-HIT:
  every lambda-distinct pair has rho in the source slope set.
```

Together these are the current sharp algebraic form of
`H3-NO-DISJOINT-EDGES`.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_slope_ratio_compiler.py
```

Expected digest:

```text
H3_REPEAT_SLOPE_RATIO_COMPILER_PASS
```
