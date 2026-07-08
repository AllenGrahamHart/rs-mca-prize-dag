# F3 h=3 repeat lambda-ratio orbit compiler

Status: PROVED COMBINATORIAL/ALGEBRAIC COMPILER PLUS FINITE GUARDRAILS.

This packet quotients the lambda-ratio parametrization by the ordering
symmetry of the three roots.

## Ratio Orbit

For a generic reciprocal fiber

```text
{r, zr, -(1+z)r},
```

the six ordered ratios obtained by choosing an ordered pair of roots are

```text
z,
1/z,
-(1+z),
-1/(1+z),
-(1+z)/z,
-z/(1+z).
```

These are exactly the `S_3` relabelings of a 3-point fiber.

Thus the generic same-lambda target should be stated on ratio orbits:

```text
for fixed lambda != 1, at most one admissible S_3-orbit of ratios z
produces U_lambda(z), V_lambda(z), W_lambda(z) in H.
```

## Lambda Equals One

The `lambda=1` branch is exceptional.  It has

```text
Phi_1(r)=r^3
```

and the only possible ratios satisfy

```text
z^2+z+1=0.
```

So the ordered ratio set has size two, not six.  The scale `r` remains the
active parameter in this branch.

## Guardrails

Boundary-style witness rows exercise only generic six-ratio orbits:

```text
p=337   n=16  active_edges=1 generic_edges=1 lambda_one_edges=0 lambda_ratio_orbits=1
p=2017  n=32  active_edges=1 generic_edges=1 lambda_one_edges=0 lambda_ratio_orbits=1
p=4801  n=64  active_edges=1 generic_edges=1 lambda_one_edges=0 lambda_ratio_orbits=1
p=7937  n=64  active_edges=2 generic_edges=2 lambda_one_edges=0 lambda_ratio_orbits=2
p=65537 n=256 active_edges=8 generic_edges=8 lambda_one_edges=0 lambda_ratio_orbits=8
p=91393 n=256 active_edges=2 generic_edges=2 lambda_one_edges=0 lambda_ratio_orbits=2
```

The contrast row includes one `lambda=1` two-ratio orbit:

```text
p=97 n=32 active_edges=15 generic_edges=14 lambda_one_edges=1 lambda_ratio_orbits=15
```

## Role in h=3

The same-lambda target is now:

```text
H3-LAMBDA-RATIO-ORBIT-UNIQUE:
  each lambda has at most one admissible ratio orbit,
  with lambda=1 handled by the primitive-cube scale branch.
```

This avoids overcounting the six ordered ratios attached to a single active
edge and gives the right quotient object for a future Stepanov/counting
argument.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_lambda_ratio_orbit_compiler.py
```

Expected digest:

```text
H3_REPEAT_LAMBDA_RATIO_ORBIT_COMPILER_PASS
```
