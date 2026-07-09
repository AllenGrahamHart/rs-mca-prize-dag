# F3 h=3 repeat lambda-one scale compiler

Status: PROVED ALGEBRAIC COMPILER PLUS FINITE GUARDRAILS.

This packet isolates the exceptional `lambda=1` branch from the generic
lambda-ratio parametrization.

## Scale Form

When `lambda=1`, the reciprocal root map is

```text
Phi_1(r)=r^3.
```

Thus a 3-point fiber has reciprocal roots

```text
{r, omega r, omega^2 r},
```

where `omega` is a primitive cube root of unity.  Writing `x=1/r`, the
original coordinates are

```text
{1+x, 1+omega x, 1+omega^2 x}.
```

So the `lambda=1` active edges are exactly scale orbits `x modulo <omega>`
such that

```text
1+x, 1+omega x, 1+omega^2 x in H.
```

If the field has no primitive cube root of unity, this branch is empty.

## Guardrails

Boundary-style witness rows have no active `lambda=1` scale edge:

```text
p=337   n=16  active_lambda_one_edges=0 scale_orbits=0
p=2017  n=32  active_lambda_one_edges=0 scale_orbits=0
p=4801  n=64  active_lambda_one_edges=0 scale_orbits=0
p=7937  n=64  active_lambda_one_edges=0 scale_orbits=0
p=65537 n=256 active_lambda_one_edges=0 scale_orbits=0
p=91393 n=256 active_lambda_one_edges=0 scale_orbits=0
```

The contrast row has one such scale orbit:

```text
p=97 n=32 active_lambda_one_edges=1 scale_orbits=1
```

## Role in h=3

The same-lambda target now splits cleanly:

```text
lambda != 1:
  uniqueness of an admissible S_3 ratio orbit;

lambda = 1:
  uniqueness of an admissible primitive-cube scale orbit.
```

This prevents the generic ratio-line theorem from carrying the special
`Phi_1(r)=r^3` branch as a hidden exceptional case.

The scale-count compiler adds the direct bound

```text
K_1 <= floor((n-1)/3)
```

for the number of admissible `lambda=1` scale orbits, hence
`binom(floor((n-1)/3),2)` same-lambda scale collision pairs in count/payment
routes.

The companion `F3_H3_REPEAT_LAMBDA_ONE_SCALE_H2_CAP.md` improves this payment
on large official rows by applying the h=2 affine-coset pair corollary to
`1+x` and `1+omega*x`; this first beats the trivial count at `n=2^19`.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_lambda_one_scale_compiler.py
```

Expected digest:

```text
H3_REPEAT_LAMBDA_ONE_SCALE_COMPILER_PASS
```
