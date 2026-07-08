# F3 h=3 repeat same-lambda orbit domain

Status: PROVED ALGEBRAIC DOMAIN COMPILER, NOT `H3-VALUE-INJECTIVE`.

This packet makes the non-diagonal part of the same-lambda collision target
explicit.  It prevents a future count or rank argument from accidentally
counting relabelings of the same active edge as genuine collisions.

## Generic Branch

For `lambda != 1`, a 3-point reciprocal fiber is represented by

```text
{r, zr, -(1+z)r},
```

and the `S_3` ratio orbit of `z` is

```text
z, 1/z, -(1+z), -1/(1+z), -(1+z)/z, -z/(1+z).
```

The generic same-lambda collision domain has two admissible ratios `z,y`
outside the same `S_3` orbit.  Away from the non-poles

```text
z(1+z)(1+z+z^2)y(1+y)(1+y+y^2) != 0,
```

the six diagonal/orbit divisors are

```text
y - z != 0,
yz - 1 != 0,
y + z + 1 != 0,
y(1+z) + 1 != 0,
yz + z + 1 != 0,
y(1+z) + z != 0.
```

Their product has degree profile

```text
deg_z = 6, deg_y = 6, total = 10.
```

The non-pole product has degree profile

```text
deg_z = 4, deg_y = 4, total = 8.
```

## Lambda Equals One

For `lambda=1`, the primitive-cube branch is

```text
{1+x, 1+omega x, 1+omega^2 x}.
```

Two scale representatives define the same orbit exactly when

```text
x^3 = y^3
```

over a field containing a primitive cube root.  Thus the non-diagonal
scale-domain exclusion is

```text
x^3 - y^3 != 0.
```

If the row field has no primitive cube root of unity, the 3-point
`lambda=1` branch is empty.

## Role in h=3

The same-lambda collision target is now:

```text
generic:
  a = lambda - 1 != 0,
  z,y are admissible non-poles,
  U_a(z),V_a(z),W_a(z),U_a(y),V_a(y),W_a(y) in H,
  and all six off-orbit exclusions above hold;

lambda = 1:
  x,y are nonzero primitive-cube scale representatives,
  1+x,1+omega x,1+omega^2 x,
  1+y,1+omega y,1+omega^2 y in H,
  and x^3-y^3 != 0.
```

Proving `H3-VALUE-INJECTIVE` means proving both domains are empty in the
boundary-style regime.  This packet only supplies the exact domain equations
and guardrails.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_same_lambda_orbit_domain.py
```

Expected digest:

```text
H3_REPEAT_SAME_LAMBDA_ORBIT_DOMAIN_PASS
```
