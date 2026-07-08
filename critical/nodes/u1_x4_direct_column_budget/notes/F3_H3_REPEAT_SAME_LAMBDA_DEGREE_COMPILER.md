# F3 h=3 repeat same-lambda degree compiler

Status: PROVED ARITHMETIC COMPILER, NOT `H3-VALUE-INJECTIVE`.

This packet records denominator-clearing degree budgets for the same-lambda
collision target.

## Generic Collision

For `lambda != 1`, write

```text
a = lambda - 1,      N(t)=1+t+t^2.
```

An admissible ratio orbit is represented by

```text
U(t) = 1 + a t(1+t)/N(t),
V(t) = 1 + a(1+t)/N(t),
W(t) = 1 - a t/N(t).
```

A generic same-lambda collision is two distinct admissible `S_3` ratio orbits
`z` and `y` for the same `a`.  Thus the raw membership target has six maps:

```text
U(z), V(z), W(z), U(y), V(y), W(y) in H.
```

The replay verifies the denominator-clearing degree budget:

```text
maps       = 6,
S_a        = 6,
S_z        = 6,
S_y        = 6,
S_total    = 14,
max_total  = 3.
```

The additional exclusions are non-poles, `lambda != 1`, and distinctness of the
two `S_3` ratio orbits.  Those are not hidden inside this arithmetic compiler.

## Lambda Equals One

For `lambda=1`, the scale branch is

```text
{1+x, 1+omega x, 1+omega^2 x} subset H,
```

modulo `x -> omega x`, where `omega` is a primitive cube root if it exists in
the row field.  A same-lambda collision is two distinct scale orbits `x,y`.
Over `F(omega)`, the six membership maps are affine linear, so

```text
maps       = 6,
S_x        = 3,
S_y        = 3,
S_total    = 6,
max_total  = 1.
```

If the row field has no primitive cube root of unity, this branch is empty.
The separate scale-count compiler also gives the trivial count bound
`K_1 <= floor((n-1)/3)`, so scale collision pairs are already bounded by
`binom(floor((n-1)/3),2)` in count/payment routes.

## Role in h=3

This packet turns `H3-VALUE-INJECTIVE` into two explicit collision-incidence
targets with degree budgets:

```text
generic:        three variables (a,z,y), six maps, S_total=14;
lambda = 1:     two scale variables (x,y), six affine maps, S_total=6.
```

It does not prove that either collision target is empty in the boundary-style
regime.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_same_lambda_degree_compiler.py
```

Expected digest:

```text
H3_REPEAT_SAME_LAMBDA_DEGREE_COMPILER_PASS
```
