#!/usr/bin/env python3
"""Exact checks for the antipodal-selector prefix transport."""

from __future__ import annotations

import itertools
from collections import Counter


CHECKS = 0


def check(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def elementary_prefix(points: tuple[int, ...], depth: int, p: int) -> tuple[int, ...]:
    coefficients = [1] + [0] * depth
    for point in points:
        for degree in range(depth, 0, -1):
            coefficients[degree] = (
                coefficients[degree] + point * coefficients[degree - 1]
            ) % p
    return tuple(coefficients[1:])


def power_prefix(points: tuple[int, ...], depth: int, p: int) -> tuple[int, ...]:
    return tuple(sum(pow(point, degree, p) for point in points) % p
                 for degree in range(1, depth + 1))


def verify_case(p: int, theta: int, m: int, r: int) -> None:
    check(pow(theta, 2 * m, p) == 1, "root order upper")
    check(pow(theta, m, p) == p - 1, "root order antipode")
    check(p > 2 * r, "Newton characteristic gate")
    half = tuple(pow(theta, index, p) for index in range(m))
    domain = tuple(pow(theta, index, p) for index in range(2 * m))
    check(len(set(domain)) == 2 * m, "root order exact")

    cube_fibers: Counter[tuple[int, ...]] = Counter()
    selector_fibers: Counter[tuple[int, ...]] = Counter()
    selector_images: dict[tuple[int, ...], tuple[int, ...]] = {}
    for bits in itertools.product((0, 1), repeat=m):
        odd = tuple(
            sum(bit * pow(point, 2 * degree - 1, p)
                for bit, point in zip(bits, half)) % p
            for degree in range(1, r + 1)
        )
        selector = tuple(
            point if bit else (-point) % p
            for bit, point in zip(bits, half)
        )
        prefix = power_prefix(selector, 2 * r, p)
        expected = []
        for degree in range(1, 2 * r + 1):
            constant = sum(pow(point, degree, p) for point in half) % p
            if degree % 2:
                expected.append((2 * odd[(degree - 1) // 2] - constant) % p)
            else:
                expected.append(constant)
        check(prefix == tuple(expected), "selector affine prefix")
        cube_fibers[odd] += 1
        selector_fibers[prefix] += 1
        selector_images[odd] = prefix

    check(len(selector_images) == len(cube_fibers), "fiber-key injection")
    for odd, size in cube_fibers.items():
        check(selector_fibers[selector_images[odd]] == size, "fiber equality")

    ambient: Counter[tuple[int, ...]] = Counter()
    power_to_elementary: dict[tuple[int, ...], tuple[int, ...]] = {}
    elementary_to_power: dict[tuple[int, ...], tuple[int, ...]] = {}
    for subset in itertools.combinations(domain, m):
        powers = power_prefix(subset, 2 * r, p)
        elementary = elementary_prefix(subset, 2 * r, p)
        ambient[powers] += 1
        previous = power_to_elementary.setdefault(powers, elementary)
        check(previous == elementary, "Newton forward partition")
        previous_power = elementary_to_power.setdefault(elementary, powers)
        check(previous_power == powers, "Newton reverse partition")

    ambient_maximum = max(ambient.values())
    check(max(cube_fibers.values()) <= ambient_maximum, "ambient fiber bound")
    for prefix, size in selector_fibers.items():
        check(size <= ambient[prefix], "transversal subset injection")


def main() -> None:
    cases = (
        (17, 2, 4, 1),
        (13, 2, 6, 2),
        (17, 3, 8, 3),
    )
    for case in cases:
        verify_case(*case)
    print(
        "F2_ANTIPODAL_SELECTOR_PREFIX_TRANSPORT_PASS "
        f"checks={CHECKS} cases={len(cases)}"
    )


if __name__ == "__main__":
    main()
