#!/usr/bin/env python3
"""Exact finite-field checks for the mismatch trace-resolvent formulas."""

from __future__ import annotations

from itertools import combinations
from random import Random


PRIME = 1009


def elementary(roots: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    e1 = sum(roots)
    e2 = sum(roots[i] * roots[j] for i, j in combinations(range(4), 2))
    e3 = sum(
        roots[i] * roots[j] * roots[k]
        for i, j, k in combinations(range(4), 3)
    )
    e4 = roots[0] * roots[1] * roots[2] * roots[3]
    return tuple(value % PRIME for value in (e1, e2, e3, e4))


def invariants_from_roots(roots: tuple[int, int, int, int]) -> tuple[int, int]:
    e1, e2, e3, e4 = elementary(roots)
    invariant_i = (12 * e4 - 3 * e1 * e3 + e2 * e2) % PRIME
    invariant_j = (
        72 * e2 * e4
        + 9 * e1 * e2 * e3
        - 27 * e3 * e3
        - 27 * e1 * e1 * e4
        - 2 * e2 * e2 * e2
    ) % PRIME
    return invariant_i, invariant_j


def poly_mul(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % PRIME
    return out


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] % PRIME == 0:
        poly.pop()
    return [value % PRIME for value in poly]


def poly_divmod(
    numerator: list[int], denominator: list[int]
) -> tuple[list[int], list[int]]:
    numerator = trim(numerator[:])
    denominator = trim(denominator[:])
    if denominator == [0]:
        raise ZeroDivisionError
    quotient = [0] * max(1, len(numerator) - len(denominator) + 1)
    inv = pow(denominator[-1], -1, PRIME)
    while len(numerator) >= len(denominator) and numerator != [0]:
        shift = len(numerator) - len(denominator)
        scale = numerator[-1] * inv % PRIME
        quotient[shift] = scale
        for j, value in enumerate(denominator):
            numerator[shift + j] = (
                numerator[shift + j] - scale * value
            ) % PRIME
        numerator = trim(numerator)
    return trim(quotient), numerator


def poly_gcd(left: list[int], right: list[int]) -> list[int]:
    left, right = trim(left), trim(right)
    while right != [0]:
        _, remainder = poly_divmod(left, right)
        left, right = right, remainder
    inv = pow(left[-1], -1, PRIME)
    return [(value * inv) % PRIME for value in left]


def resolvent_direct(roots: tuple[int, int, int, int]) -> list[int]:
    out = [1]
    for i, j in combinations(range(4), 2):
        a, b = roots[i], roots[j]
        out = poly_mul(out, [-(a + b) ** 2 % PRIME, a * b % PRIME])
    return out


def resolvent_formula(roots: tuple[int, int, int, int]) -> list[int]:
    e1, e2, e3, e4 = elementary(roots)
    r6 = e4**3
    r5 = -e4**2 * (e1 * e3 + 8 * e4)
    r4 = e4 * (
        e1**2 * e2 * e4
        + 6 * e1 * e3 * e4
        - 2 * e2**2 * e4
        + e2 * e3**2
        + 24 * e4**2
    )
    r3 = (
        -e1**4 * e4**2
        - e1**2 * e2 * e4**2
        - e1 * e2**2 * e3 * e4
        - 16 * e1 * e3 * e4**2
        + 8 * e2**2 * e4**2
        - e2 * e3**2 * e4
        - e3**4
        - 32 * e4**3
    )
    r2 = (
        3 * e1**4 * e4**2
        + e1**3 * e2 * e3 * e4
        - 4 * e1**2 * e2 * e4**2
        - e1**2 * e3**2 * e4
        - 2 * e1 * e2**2 * e3 * e4
        + e1 * e2 * e3**3
        + 24 * e1 * e3 * e4**2
        + e2**4 * e4
        - 8 * e2**2 * e4**2
        - 4 * e2 * e3**2 * e4
        + 3 * e3**4
        + 16 * e4**3
    )
    r1 = (
        -3 * e1**4 * e4**2
        + e1**3 * e2 * e3 * e4
        - e1**3 * e3**3
        - e1**2 * e2**3 * e4
        + 4 * e1**2 * e2 * e4**2
        + 2 * e1**2 * e3**2 * e4
        + 4 * e1 * e2**2 * e3 * e4
        + e1 * e2 * e3**3
        - 16 * e1 * e3 * e4**2
        - e2**3 * e3**2
        + 4 * e2 * e3**2 * e4
        - 3 * e3**4
    )
    r0 = (e1**2 * e4 - e1 * e2 * e3 + e3**2) ** 2
    return [value % PRIME for value in (r0, r1, r2, r3, r4, r5, r6)]


def outer_cubic(invariant_i: int, invariant_j: int) -> list[int]:
    # 4 I^3 Z(Z-36)^2 - J^2(Z+12)^3, in ascending order.
    first = poly_mul([0, 1], poly_mul([-36, 1], [-36, 1]))
    second = poly_mul(poly_mul([12, 1], [12, 1]), [12, 1])
    return [
        (
            4 * invariant_i**3 * first[index]
            - invariant_j**2 * second[index]
        )
        % PRIME
        for index in range(4)
    ]


def eval_poly(poly: list[int], value: int) -> int:
    total = 0
    for coefficient in reversed(poly):
        total = (total * value + coefficient) % PRIME
    return total


def c2_original(
    a: int, b: int, invariant_i: int, invariant_j: int
) -> int:
    i2 = (a * a + 14 * a * b + b * b) % PRIME
    j2 = (2 * (a + b) * (a * a - 34 * a * b + b * b)) % PRIME
    return (invariant_i**3 * j2**2 - i2**3 * invariant_j**2) % PRIME


def c1_original(
    a: int,
    b: int,
    d: int,
    u: int,
    invariant_i: int,
    invariant_j: int,
) -> int:
    i1 = (a * a + b * d + 3 * a * (b + d) - 8 * a * u) % PRIME
    j1 = (
        2
        * (a - u)
        * (a * a + b * d + 16 * a * u - 9 * a * (b + d))
    ) % PRIME
    return (invariant_i**3 * j1**2 - i1**3 * invariant_j**2) % PRIME


def c1_components(
    a: int, b: int, d: int, invariant_i: int, invariant_j: int
) -> tuple[int, int, int]:
    product = b * d % PRIME
    total = (b + d) % PRIME
    x = (a * a + product + 3 * a * total) % PRIME
    y = (a * a + product - 9 * a * total) % PRIME
    e0 = a * (y - 16 * product) % PRIME
    f0 = (16 * a * a - y) % PRIME
    j_even = 4 * (e0 * e0 + product * f0 * f0) % PRIME
    j_odd = 8 * e0 * f0 % PRIME
    i_even = (x**3 + 192 * a * a * x * product) % PRIME
    i_odd = (-24 * a * x * x - 512 * a**3 * product) % PRIME
    k0 = (invariant_i**3 * j_even - invariant_j**2 * i_even) % PRIME
    k1 = (invariant_i**3 * j_odd - invariant_j**2 * i_odd) % PRIME
    norm = (k0 * k0 - product * k1 * k1) % PRIME
    return k0, k1, norm


def square_root(value: int) -> int:
    for candidate in range(PRIME):
        if candidate * candidate % PRIME == value % PRIME:
            return candidate
    raise AssertionError("expected a square")


def centered(
    values: tuple[int, int, int, int]
) -> tuple[int, int, int, int]:
    mean = sum(values) * pow(4, -1, PRIME) % PRIME
    return tuple((value - mean) % PRIME for value in values)


def main() -> None:
    rng = Random(20260720)
    coefficient_checks = 0
    c2_checks = 0
    c1_checks = 0

    for _ in range(80):
        roots = tuple(rng.sample(range(1, PRIME), 4))
        assert resolvent_direct(roots) == resolvent_formula(roots)
        for i, j in combinations(range(4), 2):
            a, b = roots[i], roots[j]
            z = (a + b) ** 2 * pow(a * b % PRIME, -1, PRIME) % PRIME
            assert eval_poly(resolvent_formula(roots), z) == 0
        coefficient_checks += 1

        outer = centered(tuple(rng.sample(range(1, PRIME), 4)))
        if len(set(outer)) < 4:
            continue
        invariant_i, invariant_j = invariants_from_roots(outer)
        cubic = outer_cubic(invariant_i, invariant_j)
        assert len(trim(cubic)) == 4
        for i, j in combinations(range(4), 2):
            a, b = roots[i], roots[j]
            z = (a + b) ** 2 * pow(a * b % PRIME, -1, PRIME) % PRIME
            old = c2_original(a, b, invariant_i, invariant_j)
            assert old == (a * b) ** 3 * eval_poly(cubic, z) % PRIME
            c2_checks += 1

    omega = (1, 4, 9, 16)
    c2_source = (1, -1 % PRIME, 2, -2 % PRIME)
    c2_i, c2_j = invariants_from_roots(c2_source)
    assert len(
        poly_gcd(resolvent_formula(omega), outer_cubic(c2_i, c2_j))
    ) > 1

    negative_outer = centered((3, 5, 7, 29))
    while True:
        neg_i, neg_j = invariants_from_roots(negative_outer)
        if len(
            poly_gcd(resolvent_formula(omega), outer_cubic(neg_i, neg_j))
        ) == 1:
            break
        negative_outer = tuple(
            (value + index + 1) % PRIME
            for index, value in enumerate(negative_outer)
        )
        negative_outer = centered(negative_outer)

    for a_index in range(4):
        a = omega[a_index]
        remaining = [
            omega[index] for index in range(4) if index != a_index
        ]
        for b, d in combinations(remaining, 2):
            u = square_root(b * d % PRIME)
            for invariant_i, invariant_j in (
                (c2_i, c2_j),
                (neg_i, neg_j),
            ):
                k0, k1, norm = c1_components(
                    a, b, d, invariant_i, invariant_j
                )
                plus = c1_original(
                    a, b, d, u, invariant_i, invariant_j
                )
                minus = c1_original(
                    a, b, d, -u % PRIME, invariant_i, invariant_j
                )
                assert plus == (k0 + u * k1) % PRIME
                assert minus == (k0 - u * k1) % PRIME
                assert norm == plus * minus % PRIME
                c1_checks += 2

    c1_source = centered((1, -1 % PRIME, 2, 3))
    c1_i, c1_j = invariants_from_roots(c1_source)
    # A=1, {B,D}={4,9}, u=6 reconstructs {+/-1,2,3}.
    _, _, positive_norm = c1_components(1, 4, 9, c1_i, c1_j)
    assert positive_norm == 0

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_MISMATCH_TRACE_RESOLVENT_PASS "
        f"coefficient_checks={coefficient_checks} c2_checks={c2_checks} "
        f"c1_checks={c1_checks} resultant_positive=1 resultant_negative=1"
    )


if __name__ == "__main__":
    main()

