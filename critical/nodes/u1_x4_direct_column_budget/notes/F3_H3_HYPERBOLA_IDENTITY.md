# F3 h=3 hyperbola identity

Status: PROVED SYMBOLIC IDENTITY + FINITE-FIELD REPLAY.

This note banks the algebraic identity behind the h=3 rich-curve route.  The
existing Modal script enumerates finite rows and verifies the identity on
observed trades; this local replay proves the coordinate identity itself.

## Statement

Let

```text
F(T) = T^3 + a T^2 + b T + c
G_F(u,v) = (F(u)-F(v))/(u-v)
         = u^2 + uv + v^2 + a(u+v) + b.
```

Assume a primitive cube root `omega` is available, with
`omega^2 + omega + 1 = 0`.  Put

```text
A = u - omega v
B = u - omega^2 v
```

and choose `alpha,beta` by

```text
u + v = alpha A + beta B.
```

Equivalently,

```text
alpha = (1 + omega^2)/(omega^2 - omega),   beta = 1 - alpha.
```

Define

```text
X = A + a beta
Y = B + a alpha
Delta = a^2 alpha beta - b.
```

Then

```text
G_F(u,v) = X Y - Delta.
```

Thus same-fiber pairs of the cubic `F` are points on the multiplicative
hyperbola

```text
X Y = Delta.
```

The toral case `a=b=0` gives `Delta=0`, i.e. the two rational asymptote lines
`u = omega v` and `u = omega^2 v`.

## Role in T1

The rich-curve Stepanov target should be applied after this change of
coordinates.  This replay does not prove `RC-RED` or `RC-NV`; it pins the
algebraic normal form those gates consume.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_hyperbola_identity.py
```

Expected digest:

```text
H3_HYPERBOLA_IDENTITY_PASS
```
