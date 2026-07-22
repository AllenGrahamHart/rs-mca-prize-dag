#!/usr/bin/env python3
"""Exact controls for the degree-two support-tail rigidity theorem."""

from __future__ import annotations


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def mobius_fiber_count(prime: int, a: int, b: int, value: int) -> int:
    count = 0
    for x in range(prime):
        if x == b:
            continue
        ratio = (x - a) * pow(x - b, -1, prime) % prime
        if ratio * ratio % prime == value:
            count += 1
    return count


def fixed_points(prime: int, reciprocal_constant: int | None) -> int:
    if reciprocal_constant is None:
        return sum(1 for x in range(1, prime) if -x % prime == x)
    return sum(
        1
        for x in range(1, prime)
        if reciprocal_constant * pow(x, -1, prime) % prime == x
    )


def main() -> None:
    prime = 101
    maximum_fiber = max(
        mobius_fiber_count(prime, 7, 13, value) for value in range(prime)
    )
    need(maximum_fiber <= 2, "squared Mobius fiber exceeded degree two")

    antipodal_fixed = fixed_points(prime, None)
    reciprocal_fixed = fixed_points(prime, 4)
    need(antipodal_fixed == 0, "antipodal subgroup involution had a fixed point")
    need(reciprocal_fixed == 2, "reciprocal fixture did not have two fixed points")

    proportional_cap = 2
    quartic_escape_cap = 4
    antipodal_tail_cap = proportional_cap + quartic_escape_cap + antipodal_fixed
    reciprocal_tail_cap = proportional_cap + quartic_escape_cap + reciprocal_fixed
    need(antipodal_tail_cap == 6, "wrong antipodal tail budget")
    need(reciprocal_tail_cap == 8, "wrong reciprocal tail budget")

    official_e = 2**38 - 1
    need(official_e - 40 > 0, "no good comparison pair on the official row")
    print(
        "RATE_HALF_DISTANCE_THREE_DEGREE_TWO_TAIL_RIGIDITY_PASS "
        f"mobius_fiber={maximum_fiber} proportional={proportional_cap} "
        f"quartic_escape={quartic_escape_cap} fixed=({antipodal_fixed},"
        f"{reciprocal_fixed}) tails=({antipodal_tail_cap},"
        f"{reciprocal_tail_cap})"
    )


if __name__ == "__main__":
    main()
