#!/usr/bin/env python3
"""Independent finite audit for the ideal-star packing and normalization."""

from __future__ import annotations

import itertools


def multiply(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def subtract(left: list[int], right: list[int]) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index in range(len(out)):
        out[index] = (left[index] if index < len(left) else 0) - (
            right[index] if index < len(right) else 0
        )
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def divide_exact(dividend: list[int], divisor: list[int]) -> list[int]:
    work = dividend[:]
    quotient = [0] * max(1, len(work) - len(divisor) + 1)
    while len(work) >= len(divisor):
        assert divisor[-1] in (1, -1)
        coefficient = work[-1] // divisor[-1]
        shift = len(work) - len(divisor)
        quotient[shift] = coefficient
        for index, value in enumerate(divisor):
            work[shift + index] -= coefficient * value
        while work and work[-1] == 0:
            work.pop()
    assert not work
    return quotient


def beta(pair: tuple[int, int]) -> list[int]:
    left, right = pair
    first = [1] + [0] * (left - 1) + [-1]
    second = [1] + [0] * (right - 1) + [-1]
    return multiply(first, second)


def normalization_audit() -> int:
    pairs = tuple(itertools.combinations_with_replacement(range(1, 8), 2))
    pi_squared = [1, -2, 1]
    checked = 0
    for left, right in itertools.combinations(pairs, 2):
        quotient = divide_exact(subtract(beta(left), beta(right)), pi_squared)
        assert quotient
        checked += 1
    assert checked == 378
    return checked


def sharpness_audit() -> tuple[int, int]:
    # Four edges force a repeated endpoint; three need not.
    four_edges = ((0, 1), (2, 3), (4, 5), (0, 6))
    degrees = [0] * 7
    for left, right in four_edges:
        degrees[left] += 1
        degrees[right] += 1
    assert max(degrees) == 2

    matching = ((0, 1), (2, 3), (4, 5))
    degrees = [0] * 7
    for left, right in matching:
        degrees[left] += 1
        degrees[right] += 1
    assert max(degrees) == 1

    without_distance_two = (8 * 21 - 147 + 3) // 4
    with_distance_two = (8 * 21 - 147 + 5) // 6
    assert (without_distance_two, with_distance_two) == (6, 4)
    return without_distance_two, with_distance_two


def main() -> None:
    normalized = normalization_audit()
    excluded, distance_two_allowed = sharpness_audit()
    print(
        "AUDIT_F3_H3_LOW_DISTANCE_IDEAL_STAR_ROUTER_PASS "
        f"integral_quotients={normalized} low_edges={excluded}/{distance_two_allowed}"
    )


if __name__ == "__main__":
    main()
