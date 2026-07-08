# F3 h=3 repeat slope-miss degree compiler

Status: PROVED ARITHMETIC COMPILER, NOT `H3-SLOPE-RATIO-HIT`.

This packet records degree budgets for the generic lambda-distinct slope-miss
target.

## Generic Source And Target

Let

```text
a = lambda - 1,      b = mu - 1,
N(z)=1+z+z^2,        M(y)=1+y+y^2.
```

The generic source and target active edges contribute six membership maps:

```text
U_a(z), V_a(z), W_a(z),
U_b(y), V_b(y), W_b(y).
```

Their denominator-clearing degree budget is

```text
maps    = 6,
S_a     = 3,
S_b     = 3,
S_z     = 6,
S_y     = 6,
S_total = 14.
```

## Slope-Hit Numerators

For the generic source, the slope numerator compiler gives three factors

```text
Q_0, Q_1, Q_2.
```

After clearing the target reciprocal-product denominator `M(y)^3`, their
degrees in `(a,b,z,y)` are:

```text
Q_0: deg_a=3, deg_b=3, deg_z=6, deg_y=6, total=15,
Q_1: deg_a=3, deg_b=3, deg_z=6, deg_y=6, total=13,
Q_2: deg_a=3, deg_b=3, deg_z=6, deg_y=6, total=13.
```

Thus the generic slope-miss condition is the complement of

```text
Q_0 Q_1 Q_2 = 0,
```

where the product has degree bounded by

```text
deg_a <= 9, deg_b <= 9, deg_z <= 18, deg_y <= 18, total <= 41.
```

## Role in h=3

This packet gives a concrete bounded-degree incidence target for the generic
part of `H3-SLOPE-RATIO-HIT`.  It does not prove the numerator product always
vanishes.  The scale-source branch remains separate, as in the slope numerator
compiler.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_slope_miss_degree_compiler.py
```

Expected digest:

```text
H3_REPEAT_SLOPE_MISS_DEGREE_COMPILER_PASS
```
