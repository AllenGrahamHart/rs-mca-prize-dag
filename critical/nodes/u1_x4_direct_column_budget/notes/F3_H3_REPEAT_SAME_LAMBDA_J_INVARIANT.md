# F3 h=3 repeat same-lambda J-invariant

Status: PROVED ALGEBRAIC COMPILER, NOT `H3-VALUE-GEN-INJECTIVE`.

This packet identifies the degree-10 generic off-orbit product as the numerator
of a single complete invariant for `S_3` ratio orbits.

## Reciprocal Product Formula

For `lambda != 1`, set

```text
a = lambda - 1,
N(z)=1+z+z^2.
```

The generic reciprocal roots are

```text
r, zr, -(1+z)r,
where r = N(z)/(a z(1+z)).
```

Their reciprocal product is

```text
R(a,z) = -J(z)/a^3,
J(z) = N(z)^3 / (z^2(1+z)^2).
```

The replay verifies the formula symbolically.  The rational degree profile for
`R(a,z)` is

```text
deg_a=3, deg_z=6, total=7.
```

## Orbit Separation

The six `S_3` ratio transforms are

```text
z,
1/z,
-(1+z),
-1/(1+z),
-(1+z)/z,
-z/(1+z).
```

The compiler proves the exact identity

```text
numerator(J(z)-J(y)) = - product_orbit(z,y),
```

where `product_orbit(z,y)` is the six-factor off-orbit product from the
same-lambda orbit-domain compiler.  Therefore, away from the recorded poles,

```text
J(z)=J(y)  iff  y is in the S_3 orbit of z.
```

The off-orbit numerator has degree profile

```text
deg_z=6, deg_y=6, total=10.
```

## Role in h=3

This does not prove the generic same-lambda injectivity gate.  It sharpens it
to a value-uniqueness statement for the invariant `J`:

```text
H3-VALUE-GEN-INJECTIVE:
  for fixed a != 0, at most one S_3 orbit of z has
  U_a(z), V_a(z), W_a(z) in H.
```

Equivalently, in the reciprocal-product normalization, fixed lambda should
have at most one admissible value of

```text
R = -J(z)/a^3.
```

Thus the degree-10 exclusion in the frontier ledger is not bookkeeping noise;
it is exactly the complete quotient invariant for generic ratio orbits.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_same_lambda_j_invariant.py
```

Expected digest:

```text
H3_REPEAT_SAME_LAMBDA_J_INVARIANT_PASS
```
