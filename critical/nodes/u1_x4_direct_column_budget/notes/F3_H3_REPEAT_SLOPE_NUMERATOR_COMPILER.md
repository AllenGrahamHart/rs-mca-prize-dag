# F3 h=3 repeat slope numerator compiler

Status: PROVED ALGEBRAIC COMPILER PLUS FINITE GUARDRAILS.

This packet turns the ratio form of `H3-SLOPE-HIT` into a denominator-cleared
product condition.

## Generic Source

For a generic source edge, set

```text
a=lambda-1,
N=1+z+z^2,
A=-a^3 z^2(1+z)^2,
B=N^3.
```

Then

```text
R^-1 = A/B.
```

For a lambda-distinct target with invariant `S^-1`, put

```text
Delta = lambda-mu,
rho_num = Delta*B + A - S^-1*B.
```

The three source slope values have numerator-denominator form

```text
sigma_i = S_i/N^2.
```

Explicitly:

```text
S_0 = N^2 - a^2 z^2(1+z)^2,
S_1 = N^2 - a^2(1+z)^2,
S_2 = N^2 - a^2 z^2.
```

Therefore

```text
rho = sigma_i
```

is equivalent, away from the registered non-poles, to

```text
Q_i := rho_num - S_i*Delta*N = 0.
```

Thus the generic source slope-hit target is:

```text
Q_0 Q_1 Q_2 = 0.
```

## Scale Source

For the `lambda=1` source branch, with scale parameter `x`,

```text
R^-1=x^3
```

and the source slope values are

```text
1-x^2, 1-(omega x)^2, 1-(omega^2 x)^2.
```

The compiler treats this as the separate scale-source numerator product.

## Guardrails

Boundary-style rows:

```text
p=337   n=16  checked_pairs=0  numerator_nonzero=0
p=2017  n=32  checked_pairs=0  numerator_nonzero=0
p=4801  n=64  checked_pairs=0  numerator_nonzero=0
p=7937  n=64  checked_pairs=1  numerator_zero=1  numerator_nonzero=0
p=65537 n=256 checked_pairs=28 numerator_zero=28 numerator_nonzero=0
p=91393 n=256 checked_pairs=1  numerator_zero=1  numerator_nonzero=0
```

The contrast row has many nonzero products:

```text
p=97 n=32 checked_pairs=104 numerator_zero=22 numerator_nonzero=82
```

## Role in h=3

`H3-SLOPE-RATIO-HIT` can now be stated as a concrete numerator vanishing
problem.  For generic sources this is the factored equation

```text
Q_0 Q_1 Q_2 = 0.
```

This is the natural input for a future algebraic counting argument: the target
is not merely that a field value belongs to a set, but that one of three
explicit rational factors vanishes.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_slope_numerator_compiler.py
```

Expected digest:

```text
H3_REPEAT_SLOPE_NUMERATOR_COMPILER_PASS
```
