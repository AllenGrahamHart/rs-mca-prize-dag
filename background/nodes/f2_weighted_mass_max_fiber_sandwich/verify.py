#!/usr/bin/env python3
"""Fail-closed finite checks for the max-fiber/mass sandwich."""

from __future__ import annotations

import itertools
from collections import Counter
from fractions import Fraction


CHECKS = 0


def check(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def syndrome(
    rows: list[list[int]], vector: tuple[int, ...], prime: int
) -> tuple[int, ...]:
    return tuple(
        sum(entry * value for entry, value in zip(row, vector)) % prime
        for row in rows
    )


def verify_case(prime: int, width: int, rows: list[list[int]]) -> None:
    fibers: Counter[tuple[int, ...]] = Counter()
    for bits in itertools.product((0, 1), repeat=width):
        fibers[syndrome(rows, bits, prime)] += 1

    maximum = max(fibers.values())
    collisions = sum(size * size for size in fibers.values())

    mass = Fraction(0)
    for word in itertools.product((-1, 0, 1), repeat=width):
        if not any(syndrome(rows, word, prime)):
            weight = sum(value != 0 for value in word)
            mass += Fraction(1, 1 << weight)

    check((1 << width) * mass == collisions, "collision identity")
    check(Fraction(maximum * maximum, 1 << width) <= mass, "lower sandwich")
    check(mass <= maximum, "upper sandwich")
    check(collisions <= maximum * (1 << width), "pointwise domination")


def main() -> None:
    cases = (
        (3, 4, []),
        (3, 5, [[1, 0, 1, 2, 1], [0, 1, 1, 1, 2]]),
        (
            5,
            6,
            [
                [1, 2, 3, 4, 0, 1],
                [2, 4, 1, 3, 0, 2],
                [0, 1, 0, 1, 0, 1],
            ],
        ),
        (7, 6, [[1, 1, 1, 1, 1, 1], [0, 1, 2, 3, 4, 5]]),
    )
    for case in cases:
        verify_case(*case)

    print(
        "F2_WEIGHTED_MASS_MAX_FIBER_SANDWICH_PASS "
        f"checks={CHECKS} cases={len(cases)}"
    )


if __name__ == "__main__":
    main()
