# F3 h=3 repeat slope equality factorization

Status: PROVED ALGEBRAIC COMPILER, NOT A SLOPE THEOREM.

This packet factors the generic-generic and mixed slope-hit numerators into
coordinate-equality products.  It sharpens the two open slope gates without
closing either one.

## Generic-Gg Branch

Let

```text
a = lambda - 1,      b = mu - 1,
N(z)=1+z+z^2,        M(y)=1+y+y^2.
```

Write the three generic coordinate increments as

```text
R_a(z) in {a z(1+z), a(1+z), -a z}.
```

The corresponding H-coordinates are `1+R_a(z)/N(z)`.  For a lambda-distinct
generic source and target, the three slope-hit numerators satisfy

```text
Q_i = +/- product_j (R_i(a,z) M(y) - R_j(b,y) N(z)).
```

Thus each `Q_i` vanishes exactly when source coordinate `i` equals one of the
three target coordinates, after clearing denominators.

The replayed total degrees are unchanged from the degree compiler:

```text
Q0: 15,
Q1: 13,
Q2: 13.
```

## Mixed Generic/Scale Branch

For the `lambda=1` scale target, write the target coordinates as

```text
1+x, 1+omega x, 1+omega^2 x.
```

The mixed slope-hit numerators satisfy

```text
Q_i = +/- (R_i(a,z)^3 - x^3 N(z)^3).
```

Equivalently,

```text
Q_i = +/- product_{c^3=1} (R_i(a,z) - c x N(z)).
```

Again, vanishing is exactly coordinate overlap between the generic edge and the
scale edge.  Each mixed factor has total degree `9`; the product bound remains
`27`.

The reverse orientation has the same interpretation.  If the scale source
coordinate is `1+c x` with `c^3=1` and the generic target increments are
`R_j(b,y)`, then

```text
Q_{c^2} = +/- product_j (c x M(y) - R_j(b,y)).
```

The square map permutes the three cube-root labels, so this is the same
coordinate-overlap condition with labels relabelled.  The reverse-orientation
product bound is also `27`.

## Role in h=3

This does not prove

```text
H3-SLOPE-GG-HIT
H3-SLOPE-MIXED-HIT.
```

It replaces the opaque slope-miss targets by exact coordinate-intersection
targets:

```text
H3-SLOPE-GG-HIT:
  every admissible lambda-distinct generic/generic active pair intersects;

H3-SLOPE-MIXED-HIT:
  every admissible generic/scale active pair intersects.
```

The mixed branch is therefore not paid by the scale count alone.  The scale
count controls how many scale edges exist; this factorization shows that a
mixed proof still needs a mechanism forcing overlap with every admissible
generic edge, or a separate residue argument that can tolerate all remaining
mixed misses.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_slope_equality_factorization.py
```

Expected digest:

```text
H3_REPEAT_SLOPE_EQUALITY_FACTORIZATION_PASS
```
