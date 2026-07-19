# F3 h=3 repeat loose coordinate-slope distinctness

Status: PROVED ALGEBRAIC COMPILER PLUS FINITE GUARDRAILS.

This packet records the exact reason the coordinate slopes in the normalized
loose target do not collide.

## Statement

For a normalized loose core

```text
s = a r,    t = b r,    X = 1/r,
```

the six reciprocal multipliers are

```text
q in {1, a, b, -(1+a), -(1+b), -(a+b)}.
```

The coordinate slopes are their inverses:

```text
1,
1/a,
1/b,
-1/(1+a),
-1/(1+b),
-1/(a+b).
```

In a genuine loose six-point system the six reciprocal points

```text
r, s, t, -(r+s), -(r+t), -(s+t)
```

are distinct.  Since `r != 0`, this is exactly the statement that the six
multipliers `q` are distinct.  On the non-pole locus, inversion is injective,
so the six coordinate slopes are distinct.

Thus the coordinate slopes are distinct under the full normalized loose-system
hypotheses: non-poles plus six-point distinctness.  Non-poles alone are not
enough; for example `a=1` would collide the slopes `1` and `1/a`.

## Collision Table

The compiler verifies the complete table of multiplier collisions.  For
example:

```text
1 = a           iff 1 - a = 0,
1 = -(a+b)     iff 1 + a + b = 0,
a = -(1+a)     iff 1 + 2a = 0,
a = -(a+b)     iff 2a + b = 0,
-(1+a)=-(a+b)  iff b - 1 = 0.
```

Every coordinate-slope collision is one of these reciprocal-multiplier
collisions.  The special collision `1+a+b=0` is the contained zero-sum triangle
case; the others are ordinary failures of six-point distinctness.

## Role in h=3

The loose affine-line target may safely treat the six coordinate slopes as six
separate conditions once the system is known to be a genuine normalized loose
six-point system.  Multiplicity loss can only come from the three lambda slopes
colliding with those six slopes or with each other.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_coordinate_slope_distinctness.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_COORDINATE_SLOPE_DISTINCTNESS_PASS
```
