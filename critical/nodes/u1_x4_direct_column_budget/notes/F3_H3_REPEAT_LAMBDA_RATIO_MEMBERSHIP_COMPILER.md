# F3 h=3 repeat lambda-ratio membership compiler

Status: PROVED ALGEBRAIC COMPILER PLUS FINITE GUARDRAILS.

This packet converts the generic lambda-ratio parametrization into explicit
subgroup-membership functions.

## Generic Branch

Let `lambda != 1`, set `a=lambda-1`, and let `z=s/r` be an ordered root ratio.
Write

```text
N(z)=1+z+z^2.
```

The ratio parametrization gives

```text
r = N(z)/(a z(1+z)),
s = zr,
t = -(1+z)r.
```

The corresponding original coordinates `u=1+1/r`, `v=1+1/s`, `w=1+1/t` are

```text
U_lambda(z) = 1 + a z(1+z)/N(z),
V_lambda(z) = 1 + a(1+z)/N(z),
W_lambda(z) = 1 - a z/N(z).
```

Therefore a generic 3-point lambda fiber is equivalent to

```text
U_lambda(z), V_lambda(z), W_lambda(z) in H
```

with the usual non-pole and distinctness exclusions.

## Lambda Equals One

For `lambda=1`, the ratio is a primitive cube root:

```text
z^2+z+1=0,
```

and the remaining parameter is the scale `r`; the reciprocal roots are

```text
{r,zr,z^2r}.
```

This branch is separate from the generic rational `z` functions.

## Guardrails

Boundary-style witness rows exercise only the generic branch:

```text
p=337   n=16  active_edges=1 generic_checks=6  lambda_one_checks=0
p=2017  n=32  active_edges=1 generic_checks=6  lambda_one_checks=0
p=4801  n=64  active_edges=1 generic_checks=6  lambda_one_checks=0
p=7937  n=64  active_edges=2 generic_checks=12 lambda_one_checks=0
p=65537 n=256 active_edges=8 generic_checks=48 lambda_one_checks=0
p=91393 n=256 active_edges=2 generic_checks=12 lambda_one_checks=0
```

The contrast row exercises the special branch:

```text
p=97 n=32 active_edges=15 generic_checks=84 lambda_one_checks=6
```

## Role in h=3

The generic same-lambda obstruction is now a concrete three-membership problem
for the rational functions `U_lambda,V_lambda,W_lambda` on the ratio line.
This aligns the same-lambda target with the rich-curve/Stepanov machinery,
while isolating the `lambda=1` primitive-cube scale branch.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_lambda_ratio_membership_compiler.py
```

Expected digest:

```text
H3_REPEAT_LAMBDA_RATIO_MEMBERSHIP_COMPILER_PASS
```
