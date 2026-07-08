# F3 h=3 repeat lambda-ratio parametrization

Status: PROVED ALGEBRAIC PARAMETRIZATION PLUS FINITE GUARDRAILS.

This packet parametrizes a 3-point fiber of

```text
Phi_lambda(r)=r^3/(1-(lambda-1)r)
```

by the ratio of two reciprocal roots.

## Generic Lambda

Let `lambda != 1` and set `a=lambda-1`.  If `r` and `s=zr` are distinct roots
in the same `Phi_lambda` fiber, then

```text
r^3/(1-ar) = s^3/(1-as).
```

After cancelling `r-s`, this gives

```text
1+z+z^2 = a r z(1+z).
```

Therefore

```text
r = (1+z+z^2) / ((lambda-1) z(1+z)),
s = zr,
t = -(1+z)r.
```

Thus a generic 3-point lambda fiber is determined by an ordered root ratio
`z`, subject to the three reconstructed reciprocal roots lying in

```text
S={1/(u-1):u in H,u!=1}.
```

## Lambda Equals One

When `lambda=1`, the map is

```text
Phi_1(r)=r^3.
```

The ratio equation becomes

```text
z^2+z+1=0.
```

So the special fiber shape is

```text
{r, zr, z^2 r}
```

for a primitive cube-root ratio `z`.

## Guardrails

Boundary-style witness rows exercise only the generic branch:

```text
p=337   n=16  active_edges=1 lambda_one_edges=0 oriented_ratio_checks=6
p=2017  n=32  active_edges=1 lambda_one_edges=0 oriented_ratio_checks=6
p=4801  n=64  active_edges=1 lambda_one_edges=0 oriented_ratio_checks=6
p=7937  n=64  active_edges=2 lambda_one_edges=0 oriented_ratio_checks=12
p=65537 n=256 active_edges=8 lambda_one_edges=0 oriented_ratio_checks=48
p=91393 n=256 active_edges=2 lambda_one_edges=0 oriented_ratio_checks=12
```

The contrast row exercises the `lambda=1` branch:

```text
p=97 n=32 active_edges=15 lambda_one_edges=1 oriented_ratio_checks=90
```

## Role in h=3

The same-lambda target can now be attacked through explicit ratio parameters.
For `lambda != 1`, each candidate fiber is an explicit three-point expression
in one ratio `z`; for `lambda=1`, the only possible ratios are primitive
third roots.  This is a sharper algebraic form of the
`H3-LAMBDA-ROOT-FIBER-UNIQUE` target.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_lambda_ratio_parametrization.py
```

Expected digest:

```text
H3_REPEAT_LAMBDA_RATIO_PARAMETRIZATION_PASS
```
