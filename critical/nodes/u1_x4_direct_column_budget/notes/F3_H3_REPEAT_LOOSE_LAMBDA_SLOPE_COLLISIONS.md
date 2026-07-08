# F3 h=3 repeat loose lambda-slope collisions

Status: PROVED ALGEBRAIC COMPILER PLUS FINITE GUARDRAILS.

This packet records the exact collision locus for the three lambda slopes in
the normalized loose target.

## Slopes

The three lambda slopes are

```text
L_a  = 1 + 1/a - 1/(1+a)      = (a^2+a+1)/(a(1+a)),
L_b  = 1 + 1/b - 1/(1+b)      = (b^2+b+1)/(b(1+b)),
L_ab = 1/a + 1/b - 1/(a+b)    = (a^2+ab+b^2)/(ab(a+b)).
```

The six coordinate slopes are

```text
1, 1/a, 1/b, -1/(1+a), -1/(1+b), -1/(a+b).
```

All statements are on the normalized loose-system locus: the denominators are
nonzero, the six reciprocal multipliers are distinct, and `1+a+b != 0`.

## Lambda-Lambda Collisions

The lambda slopes are automatically distinct in a genuine normalized loose
system.  The exact factorizations are

```text
L_a  = L_b   iff -(a-b)(a+b+1) = 0,
L_a  = L_ab  iff a(b-1)(a+b+1) = 0,
L_b  = L_ab  iff b(a-1)(a+b+1) = 0.
```

The factors `a`, `b`, and `a+b+1` are excluded by non-poles or looseness; the
factors `a-b`, `b-1`, and `a-1` are failures of six-point distinctness.

## Lambda-Coordinate Collisions

On the non-pole locus, every lambda-coordinate collision is one of nine
explicit divisors:

```text
L_a  = 1/b         iff a^2 b - a^2 + ab - a + b = 0,
L_a  = -1/(1+b)   iff a^2 b + 2a^2 + ab + 2a + b + 1 = 0,
L_a  = -1/(a+b)   iff a^3 + a^2b + 2a^2 + ab + 2a + b = 0,

L_b  = 1/a         iff ab^2 + ab + a - b^2 - b = 0,
L_b  = -1/(1+a)   iff ab^2 + ab + a + 2b^2 + 2b + 1 = 0,
L_b  = -1/(a+b)   iff ab^2 + ab + a + b^3 + 2b^2 + 2b = 0,

L_ab = 1           iff -a^2b + a^2 - ab^2 + ab + b^2 = 0,
L_ab = -1/(1+a)   iff a^3 + 2a^2b + a^2 + 2ab^2 + ab + b^2 = 0,
L_ab = -1/(1+b)   iff 2a^2b + a^2 + 2ab^2 + ab + b^3 + b^2 = 0.
```

All other lambda-coordinate equalities are impossible under the non-pole
hypotheses.

## Role in h=3

The loose affine-line target now has a precise generic/special split:

```text
generic cell:       nine distinct slopes,
collision divisors: eight or fewer distinct slopes, controlled by the nine
                    explicit lambda-coordinate equations above.
```

There is no additional lambda-lambda collision branch for genuine loose
systems.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_lambda_slope_collisions.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_LAMBDA_SLOPE_COLLISIONS_PASS
```
