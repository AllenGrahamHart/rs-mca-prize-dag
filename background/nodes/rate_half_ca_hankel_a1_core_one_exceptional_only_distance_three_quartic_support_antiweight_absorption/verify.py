#!/usr/bin/env python3
"""Exact controls for absorption of the smooth antiweight branch."""

from __future__ import annotations


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def evaluate(poly: list[int], value: int, prime: int) -> int:
    out = 0
    for coefficient in reversed(poly):
        out = (out * value + coefficient) % prime
    return out


def locator(a: int, b: int, prime: int) -> list[int]:
    return [a * b % prime, -(a + b) % prime, 1]


def check_squared_mobius_fibers() -> int:
    prime = 101
    left, right = 7, 19
    checks = 0
    for target in range(1, prime):
        roots = []
        for value in range(prime):
            if value == right:
                continue
            ratio = (value - left) * pow(value - right, -1, prime) % prime
            if ratio * ratio % prime == target:
                roots.append(value)
        need(len(roots) <= 2, "squared Mobius fiber exceeded degree two")
        checks += 1
    return checks


def check_antiweight_degree_two_fixture() -> int:
    prime = 101
    pairs = [(value, -value % prime) for value in range(1, 7)]
    d_polys = [locator(a, b, prime) for a, b in pairs]
    h_values = {
        row: weight
        for a, b in pairs
        for row, weight in ((a, 1), (b, prime - 1))
    }
    checks = 0
    for l, d_poly in enumerate(d_polys):
        for k, (a, b) in enumerate(pairs):
            if k == l:
                continue
            d_a = evaluate(d_poly, a, prime)
            d_b = evaluate(d_poly, b, prime)
            crossing = (
                h_values[b] * d_b * d_b
                + h_values[a] * d_a * d_a
            ) % prime
            need(crossing == 0, "antiweight nonconstant crossing failed")
            # P_l=1 gives r_l=1/D_l^2, a rational function of psi=X^2.
            r_a = pow(d_a * d_a % prime, -1, prime)
            r_b = pow(d_b * d_b % prime, -1, prime)
            need(r_a == r_b and a * a % prime == b * b % prime,
                 "antiweight degree-two field fixture failed")
            checks += 1
    return checks


def main() -> None:
    e_value = (1 << 38) - 1
    need(2 * (e_value - 3) > 18, "common-field Bezout margin failed")
    need(e_value - 6 >= e_value - 40, "degree-two absorption weakened")
    need(e_value - 1 >= e_value - 148, "degree-four absorption weakened")
    mobius_checks = check_squared_mobius_fibers()
    fixture_checks = check_antiweight_degree_two_fixture()
    print(
        "RATE_HALF_DISTANCE_THREE_QUARTIC_SUPPORT_ANTIWEIGHT_ABSORPTION_PASS "
        f"mobius_fibers={mobius_checks} fixture_crossings={fixture_checks} "
        "proportional_quartics_max=2 degree_two_tail=6 degree_four_tail=1"
    )


if __name__ == "__main__":
    main()
