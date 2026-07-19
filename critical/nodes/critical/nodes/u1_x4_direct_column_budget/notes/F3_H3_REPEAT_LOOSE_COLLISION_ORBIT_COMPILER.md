# F3 h=3 repeat loose collision-orbit compiler

Status: PROVED ALGEBRAIC COMPILER.

This packet quotients the lambda-coordinate collision divisors by the same
`S_3` action used for normalized loose systems.

## Orbit Action

For a normalized ratio pair `(a,b)`, relabeling the three loose core vertices
gives

```text
(a,b),
(b,a),
(1/a,b/a),
(b/a,1/a),
(1/b,a/b),
(a/b,1/b).
```

Pulling back the nine lambda-coordinate collision divisors under this action
preserves the registered divisor list, up to a nonzero scalar and cleared
non-pole denominators.

## Result

The nine divisors split into two `S_3` branch types.

### Orbit A, size 3

Representative:

```text
L_a = 1/b
```

with divisor

```text
a^2 b - a^2 + ab - a + b = 0.
```

Orbit members:

```text
L_a = 1/b,    L_b = 1/a,    L_ab = 1.
```

### Orbit B, size 6

Representative:

```text
L_a = -1/(1+b)
```

with divisor

```text
a^2 b + 2a^2 + ab + 2a + b + 1 = 0.
```

Orbit members:

```text
L_a  = -1/(1+b),    L_a  = -1/(a+b),
L_b  = -1/(1+a),    L_b  = -1/(a+b),
L_ab = -1/(1+a),    L_ab = -1/(1+b).
```

## Role in h=3

The loose affine-line target now has one generic branch and two special
collision branch types after quotienting by normalized `S_3` orbits:

```text
generic:         nine distinct slopes,
collision A:     representative L_a = 1/b,
collision B:     representative L_a = -1/(1+b).
```

This reduces future special-case arguments from nine raw divisors to two
normalized divisor families.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_collision_orbit_compiler.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_COLLISION_ORBIT_COMPILER_PASS
```
