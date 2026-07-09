# F3 h=3 repeat same-lambda product parameter

Status: PROVED ALGEBRAIC COMPILER, NOT `H3-VALUE-GEN-INJECTIVE`.

This packet combines the fixed-lambda cubic form with the same-lambda
`J`-invariant.

## Fixed First Two Symmetric Coefficients

For `lambda != 1`, write `a=lambda-1`, `N(z)=1+z+z^2`, and

```text
U(z) = 1 + a z(1+z)/N(z),
V(z) = 1 + a(1+z)/N(z),
W(z) = 1 - a z/N(z).
```

The compiler verifies

```text
U+V+W = a+3,
UV+UW+VW = 2a+3.
```

Thus, for fixed `lambda`, the generic active edge has cubic

```text
T^3 - (a+3)T^2 + (2a+3)T - m(z),
```

where the only free coefficient is the product

```text
m(z) = U(z)V(z)W(z).
```

## Product And J

With

```text
J(z) = (1+z+z^2)^3 / (z^2(1+z)^2),
```

the product parameter is

```text
m(z) = a + 1 - a^3/J(z).
```

Equivalently, this is the original-coordinate version of the reciprocal
identity

```text
m = lambda + 1/R,
R = -J(z)/a^3.
```

The compiler also verifies the derivative profile

```text
m'(z) numerator   = a^3 z(z-1)(z+1)(z+2)(2z+1)
m'(z) denominator = (z^2+z+1)^4.
```

On the generic active-edge domain, `a`, `z`, `z+1`, and `z^2+z+1` are nonzero,
and the factors `(z-1)(z+2)(2z+1)` are the duplicate-coordinate locus.  Hence
`m(z)` has no active critical points after the standard generic exclusions.

## Role

The generic same-lambda gate can now be stated in the edge-cubic language:

```text
For fixed lambda, among admissible ratio orbits z with
U(z),V(z),W(z) in H and distinct, there is at most one product m(z).
```

This is equivalent to uniqueness of the active cubic

```text
T^3 - (lambda+2)T^2 + (2lambda+1)T - m.
```

The packet does not prove that uniqueness.  It records that the product
parameter is a separable coordinate on the distinct generic quotient domain,
so the remaining obstruction is arithmetic, not a parametrization singularity.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_same_lambda_product_parameter.py
```

Expected digest:

```text
H3_REPEAT_SAME_LAMBDA_PRODUCT_PARAMETER_PASS
```
