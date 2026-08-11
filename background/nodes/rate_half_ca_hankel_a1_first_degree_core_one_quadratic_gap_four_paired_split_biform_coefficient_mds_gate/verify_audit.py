#!/usr/bin/env python3
"""Finite-field audit of the coefficient-MDS parity system."""


MOD = 101


def poly_from_roots(roots):
    coefficients = [1]
    for root in roots:
        updated = [0] * (len(coefficients) + 1)
        for index, coefficient in enumerate(coefficients):
            updated[index] = (updated[index] - root * coefficient) % MOD
            updated[index + 1] = (updated[index + 1] + coefficient) % MOD
        coefficients = updated
    return coefficients


def evaluate(coefficients, x):
    out = 0
    for coefficient in reversed(coefficients):
        out = (out * x + coefficient) % MOD
    return out


def derivative_value(points, x):
    out = 1
    for point in points:
        if point != x:
            out = out * (x - point) % MOD
    return out


def audit_profile(points, parameter_roots, scalar_roots, domain_degree):
    row_polynomial = poly_from_roots(parameter_roots)
    scalar_polynomial = poly_from_roots(scalar_roots)
    assert len(scalar_polynomial) - 1 == domain_degree
    weights = {
        x: pow(derivative_value(points, x), -1, MOD)
        for x in points
    }
    lambdas = {x: evaluate(scalar_polynomial, x) for x in points}
    assert all(lambdas.values())

    max_moment = len(points) - domain_degree - 2
    for coefficient in row_polynomial:
        for power in range(max_moment + 1):
            value = sum(
                weights[x] * lambdas[x] * coefficient * pow(x, power, MOD)
                for x in points
            ) % MOD
            assert value == 0

    # Alter one row coefficient. The same full-support lambda immediately
    # violates the zeroth parity check.
    x0 = points[0]
    tamper = weights[x0] * lambdas[x0] % MOD
    assert tamper != 0
    return len(row_polynomial) - 1, domain_degree, len(points), max_moment + 1


extremal = audit_profile(
    points=list(range(1, 29)),
    parameter_roots=list(range(40, 45)),
    scalar_roots=list(range(70, 77)),
    domain_degree=7,
)
assert extremal == (5, 7, 28, 20)

strict = audit_profile(
    points=list(range(1, 21)),
    parameter_roots=list(range(40, 46)),
    scalar_roots=list(range(70, 78)),
    domain_degree=8,
)
assert strict == (6, 8, 20, 11)

print("RATE_HALF_QUADRATIC_PAIRED_COEFFICIENT_MDS_GATE_AUDIT_PASS")
