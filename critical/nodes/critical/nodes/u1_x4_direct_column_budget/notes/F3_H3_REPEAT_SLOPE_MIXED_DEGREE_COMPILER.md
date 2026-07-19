# F3 h=3 repeat slope mixed degree compiler

Status: PROVED ARITHMETIC COMPILER, NOT `H3-SLOPE-RATIO-HIT`.

This packet records the bounded-degree interfaces for lambda-distinct
slope-hit pairs where exactly one edge lies in the `lambda=1` scale branch.

## Generic Source, Scale Target

For a mixed pair one may orient the source as the generic edge.  Set

```text
a = lambda - 1,      N(z)=1+z+z^2,
```

and let `x` be the scale parameter of the `mu=1` target.  The six membership
maps are

```text
U_a(z), V_a(z), W_a(z),
1+x, 1+omega x, 1+omega^2 x.
```

Their degree budget in variables `(a,z,x)` is

```text
maps    = 6,
S_a     = 3,
S_z     = 6,
S_x     = 3,
S_total = 10.
```

The generic source hit factors specialize the target invariant to `x^3`.
Each factor has degree profile

```text
deg_a=3, deg_z=6, deg_x=3, total=9,
```

so the product is bounded by

```text
deg_a <= 9, deg_z <= 18, deg_x <= 9, total <= 27.
```

## Scale Source, Generic Target

The slope numerator compiler also supports the reverse orientation.  Let

```text
b = mu - 1,      M(y)=1+y+y^2.
```

The six membership maps are

```text
1+x, 1+omega x, 1+omega^2 x,
U_b(y), V_b(y), W_b(y).
```

Their degree budget in variables `(x,b,y)` is

```text
maps    = 6,
S_x     = 3,
S_b     = 3,
S_y     = 6,
S_total = 10.
```

The three scale-source hit factors have degree profile

```text
deg_x=3, deg_b=3, deg_y=6, total=9,
```

and product bound

```text
deg_x <= 9, deg_b <= 9, deg_y <= 18, total <= 27.
```

Here the primitive-cube coefficients are field constants, not additional
variables.

## Role in h=3

The generic-generic slope-miss packet covers pairs with no `lambda=1` edge.
This packet covers the mixed branch.  Since lambda-distinct pairs cannot have
two `lambda=1` edges, these two packets account for all branches of
`H3-SLOPE-RATIO-HIT`.

For a future proof it is enough to use the generic-source, scale-target
orientation on mixed pairs.  The scale-source budget is recorded so that the
existing oriented numerator compiler remains fully documented.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_slope_mixed_degree_compiler.py
```

Expected digest:

```text
H3_REPEAT_SLOPE_MIXED_DEGREE_COMPILER_PASS
```
