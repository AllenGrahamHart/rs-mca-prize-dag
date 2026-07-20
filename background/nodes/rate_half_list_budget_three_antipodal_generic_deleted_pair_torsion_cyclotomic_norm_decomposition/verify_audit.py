#!/usr/bin/env python3
"""Independent finite-field inverse-pair audit for the torsion norm node."""

from __future__ import annotations

from math import factorial


PRIME = 257


def primitive_root(prime: int) -> int:
    factors = (2,)
    return next(
        value
        for value in range(2, prime)
        if all(pow(value, (prime - 1) // factor, prime) != 1 for factor in factors)
    )


def generalized_binomial(value: int, count: int) -> int:
    numerator = 1
    for index in range(count):
        numerator = numerator * (value - index) % PRIME
    return numerator * pow(factorial(count), -1, PRIME) % PRIME


def jacobi_value(degree: int, value: int) -> int:
    alpha = -pow(4, -1, PRIME) % PRIME
    beta = -pow(2, -1, PRIME) % PRIME
    left = (value - 1) * pow(2, -1, PRIME) % PRIME
    right = (value + 1) * pow(2, -1, PRIME) % PRIME
    return sum(
        generalized_binomial((degree + alpha) % PRIME, index)
        * generalized_binomial((degree + beta) % PRIME, degree - index)
        * pow(left, degree - index, PRIME)
        * pow(right, index, PRIME)
        for index in range(degree + 1)
    ) % PRIME


def lifted_value(degree: int, z: int) -> int:
    trace = (z + pow(z, -1, PRIME)) * pow(2, -1, PRIME) % PRIME
    return pow(z, degree, PRIME) * jacobi_value(degree, trace) % PRIME


def chebyshev_t(degree: int, value: int) -> int:
    if degree == 0:
        return 1
    previous, current = 1, value
    for _ in range(1, degree):
        previous, current = current, (2 * value * current - previous) % PRIME
    return current


def chebyshev_u(degree: int, value: int) -> int:
    if degree == 0:
        return 1
    previous, current = 1, 2 * value % PRIME
    for _ in range(1, degree):
        previous, current = current, (2 * value * current - previous) % PRIME
    return current


def product(values: list[int]) -> int:
    result = 1
    for value in values:
        result = result * value % PRIME
    return result


def audit() -> int:
    generator = primitive_root(PRIME)
    eighth_root = pow(generator, (PRIME - 1) // 8, PRIME)
    theta = (eighth_root + pow(eighth_root, -1, PRIME)) % PRIME
    assert theta * theta % PRIME == 2
    checked = 0
    for m in (1, 2, 4, 8, 16):
        for value in (3, 7, 11):
            trace_product = 1
            trace_degree = 1
            while trace_degree <= m:
                trace_product = (
                    trace_product * chebyshev_t(trace_degree, value) % PRIME
                )
                trace_degree *= 2
            assert chebyshev_u(2 * m - 1, value) == 2 * m * trace_product % PRIME
            t_m = chebyshev_t(m, value)
            assert chebyshev_t(2 * m, value) == (
                (theta * t_m - 1) * (theta * t_m + 1)
            ) % PRIME

        minus_root = pow(generator, (PRIME - 1) // (8 * m), PRIME)
        minus_z = [pow(minus_root, exponent, PRIME) for exponent in range(1, 8 * m, 2)]
        minus_w = [
            (z + pow(z, -1, PRIME)) * pow(2, -1, PRIME) % PRIME
            for z in minus_z[: 2 * m]
        ]
        minus_norm = product([lifted_value(m, z) for z in minus_z])
        minus_values = product([jacobi_value(m, w) for w in minus_w])
        assert minus_norm == minus_values * minus_values % PRIME

        plus_root = pow(generator, (PRIME - 1) // (4 * m), PRIME)
        plus_z = [
            pow(plus_root, exponent, PRIME)
            for exponent in range(1, 4 * m)
            if exponent != 2 * m
        ]
        plus_w = [
            (z + pow(z, -1, PRIME)) * pow(2, -1, PRIME) % PRIME
            for z in plus_z[: 2 * m - 1]
        ]
        plus_norm = product([lifted_value(m, z) for z in plus_z])
        plus_values = product([jacobi_value(m, w) for w in plus_w])
        assert plus_norm == plus_values * plus_values % PRIME

        tower = 1
        order = 4
        while order <= 4 * m:
            root = pow(generator, (PRIME - 1) // order, PRIME)
            tower = tower * product(
                [lifted_value(m, pow(root, exponent, PRIME)) for exponent in range(1, order, 2)]
            ) % PRIME
            order *= 2
        assert tower == plus_norm
        checked += 1
    return checked


def main() -> None:
    checked = audit()
    print(
        "RATE_HALF_DELETED_PAIR_TORSION_CYCLOTOMIC_NORM_AUDIT_PASS "
        f"prime={PRIME} dyadic_orders={checked} inverse_pairs=1 "
        "trace_tower=1 quadratic_split=1"
    )


if __name__ == "__main__":
    main()
