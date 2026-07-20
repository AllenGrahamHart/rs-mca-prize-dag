#!/usr/bin/env python3
"""Exact checks for the c=1 parity Mobius router."""

from __future__ import annotations

from random import Random


PRIME = 1009


def inverse(value: int) -> int:
    return pow(value % PRIME, -1, PRIME)


def square_root(value: int) -> int:
    for candidate in range(PRIME):
        if candidate * candidate % PRIME == value % PRIME:
            return candidate
    raise AssertionError("expected square")


IOTA = square_root(-1)


def cross_ratio(a: int, b: int, c: int, d: int) -> int:
    return (
        (a - c)
        * (b - d)
        * inverse((a - d) * (b - c))
        % PRIME
    )


def role_points(role: str, r_value: int) -> tuple[int, int, int, int]:
    if role == "R":
        return (1, -1 % PRIME, r_value, IOTA * r_value % PRIME)
    if role == "P":
        return (1, -1 % PRIME, IOTA, IOTA * r_value % PRIME)
    raise ValueError(role)


def direct_cross_ratios(role: str, r_value: int) -> list[int]:
    points = role_points(role, r_value)
    return [
        cross_ratio(points[0], points[1], points[2], points[3]),
        cross_ratio(points[0], points[2], points[1], points[3]),
        cross_ratio(points[0], points[3], points[1], points[2]),
    ]


def formula_cross_ratios(role: str, r_value: int) -> list[int]:
    r_value %= PRIME
    if role == "R":
        return [
            (r_value - 1)
            * (r_value - IOTA)
            * inverse((r_value + 1) * (r_value + IOTA))
            % PRIME,
            2
            * (1 + IOTA)
            * r_value
            * inverse((r_value + 1) * (r_value + IOTA))
            % PRIME,
            -2
            * (1 + IOTA)
            * r_value
            * inverse((r_value - 1) * (r_value - IOTA))
            % PRIME,
        ]
    if role == "P":
        return [
            IOTA * (r_value - IOTA) * inverse(r_value + IOTA) % PRIME,
            (1 - IOTA)
            * (r_value - 1)
            * inverse(r_value + IOTA)
            % PRIME,
            (1 + IOTA)
            * (r_value - 1)
            * inverse(r_value - IOTA)
            % PRIME,
        ]
    raise ValueError(role)


def trace_from_cross_ratio(value: int) -> int:
    return (
        4 * (value + 1) ** 2 * inverse((value - 1) ** 2) - 2
    ) % PRIME


def matching_polynomial(value: int, ratio: int) -> int:
    return (
        (value - 1) ** 2 * (1 + ratio) ** 2
        - 4 * ratio * (value + 1) ** 2
    ) % PRIME


def trace_iterate(value: int, levels: int = 39) -> int:
    for _ in range(levels):
        value = (value * value - 2) % PRIME
    return value


def outer_trace(lambda_value: int, mu_value: int) -> int:
    alpha = (lambda_value + mu_value) % PRIME
    gamma = lambda_value * mu_value % PRIME
    return (alpha * alpha - 2 * gamma) * inverse(gamma) % PRIME


def harmonic_factor(role: str, index: int, r_value: int) -> int:
    r_value %= PRIME
    if role == "R":
        return (
            r_value * r_value
            + (0 if index == 0 else (3 if index == 1 else -3))
            * (1 + IOTA)
            * r_value
            + IOTA
        ) % PRIME
    if index == 0:
        return (r_value + 1) % PRIME
    return (
        5 * r_value - 4 + (3 if index == 1 else -3) * IOTA
    ) % PRIME


def main() -> None:
    rng = Random(20260720)
    cross_ratio_checks = 0
    trace_checks = 0
    harmonic_checks = 0

    allowed = [
        value
        for value in range(2, PRIME)
        if pow(value, 4, PRIME) != 1
    ]
    for r_value in rng.sample(allowed, 80):
        for role in ("R", "P"):
            direct = direct_cross_ratios(role, r_value)
            formula = formula_cross_ratios(role, r_value)
            assert direct == formula
            cross_ratio_checks += 3

            for index, value in enumerate(formula):
                trace = trace_from_cross_ratio(value)
                for ratio in rng.sample(range(1, PRIME), 4):
                    lhs = matching_polynomial(value, ratio)
                    rhs = (
                        ratio
                        * (value - 1) ** 2
                        * (
                            ratio
                            + inverse(ratio)
                            - trace
                        )
                    ) % PRIME
                    assert lhs == rhs
                    trace_checks += 1

                harmonic = matching_polynomial(value, -1 % PRIME) == 0
                assert harmonic == (harmonic_factor(role, index, r_value) == 0)
                harmonic_checks += 1

    for _ in range(80):
        lambda_value, mu_value = rng.sample(range(1, PRIME), 2)
        ratio = mu_value * inverse(lambda_value) % PRIME
        assert outer_trace(lambda_value, mu_value) == (
            ratio + inverse(ratio)
        ) % PRIME

    # Exact small-order trace criterion, including both directions.
    generator = next(
        candidate
        for candidate in range(2, PRIME)
        if all(
            pow(candidate, (PRIME - 1) // factor, PRIME) != 1
            for factor in (2, 3, 7)
        )
    )
    ratio = pow(generator, (PRIME - 1) // 8, PRIME)
    trace = (ratio + inverse(ratio)) % PRIME
    assert trace_iterate(trace, levels=3) == 2
    assert trace_iterate(trace, levels=2) != 2

    # R0 forces t=-1, whose required even primary coefficient is nonzero.
    for small_m in range(1, 8):
        numerator = 1
        denominator = 1
        for index in range(small_m):
            numerator = numerator * (4 * index + 1) % PRIME
            denominator = denominator * 4 * (index + 1) % PRIME
        assert numerator * inverse(denominator) % PRIME != 0

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C1_PARITY_MOBIUS_PASS "
        f"cross_ratios={cross_ratio_checks} trace_identities={trace_checks} "
        f"harmonic_factors={harmonic_checks} outer_traces=80"
    )


if __name__ == "__main__":
    main()

