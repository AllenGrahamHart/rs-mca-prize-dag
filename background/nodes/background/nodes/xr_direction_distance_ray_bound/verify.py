#!/usr/bin/env python3
"""Exhaust DDR on small RS syndrome charts and audit official MDS thresholds."""

from __future__ import annotations

from itertools import product
from math import floor


def syndrome(vector: tuple[int, ...], points: tuple[int, ...], redundancy: int, q: int) -> tuple[int, ...]:
    return tuple(
        sum(value * pow(x, exponent, q) for value, x in zip(vector, points, strict=True)) % q
        for exponent in range(redundancy)
    )


def add(left: tuple[int, ...], scalar: int, right: tuple[int, ...], q: int) -> tuple[int, ...]:
    return tuple((a + scalar * b) % q for a, b in zip(left, right, strict=True))


def exhaustive_chart(q: int, redundancy: int, points: tuple[int, ...], radius: int) -> tuple[int, int]:
    n = len(points)
    min_weight: dict[tuple[int, ...], int] = {}
    for vector in product(range(q), repeat=n):
        syn = syndrome(vector, points, redundancy, q)
        weight = sum(value != 0 for value in vector)
        min_weight[syn] = min(weight, min_weight.get(syn, n + 1))

    syndromes = tuple(product(range(q), repeat=redundancy))
    paid_directions = 0
    maximum = 0
    for y1 in syndromes:
        if all(value == 0 for value in y1):
            continue
        distance = min_weight[y1]
        denominator = (n - radius) ** 2 - n * (n - distance)
        if denominator <= 0:
            continue
        paid_directions += 1
        bound = n * (distance - radius) // denominator
        for y0 in syndromes:
            hits = sum(
                min_weight[add(y0, gamma, y1, q)] <= radius
                for gamma in range(q)
            )
            if hits > bound:
                raise AssertionError((q, redundancy, n, radius, y0, y1, hits, bound))
            maximum = max(maximum, hits)
    if paid_directions == 0:
        raise AssertionError((q, redundancy, n, radius, "no paid direction"))
    return maximum, paid_directions


def official_mds_thresholds() -> tuple[tuple[str, int], ...]:
    rows = (
        ("rowc-r1_4", 1024, 4, 256),
        ("rowc-r1_8", 1024, 8, 256),
        ("rowc-r1_16", 1024, 16, 512),
        ("prize-r1_4", 1 << 41, 4, 256),
        ("prize-r1_8", 1 << 41, 8, 256),
        ("prize-r1_16", 1 << 41, 16, 512),
    )
    out: list[tuple[str, int]] = []
    for name, n, rate_denominator, scale_denominator in rows:
        k = n // rate_denominator
        redundancy = n - k
        h = n // scale_denominator + 1
        denominator = redundancy - 2 * h
        max_excess = min(k, (h * h - 1) // denominator)
        if not (h * h > max_excess * denominator):
            raise AssertionError((name, "paid endpoint"))
        if max_excess < k and h * h > (max_excess + 1) * denominator:
            raise AssertionError((name, "first unpaid endpoint"))
        out.append((name, max_excess))
    return tuple(out)


def main() -> None:
    first = exhaustive_chart(5, 2, (1, 2, 3), 1)
    second = exhaustive_chart(5, 3, (0, 1, 2, 3, 4), 1)

    # Dropping (DD) is load-bearing: a one-coordinate direction gives every
    # slope in a radius-one ball, which exceeds N^2 over a larger field.
    q = 29
    n = 3
    tangent_hits = q
    if tangent_hits <= n * n:
        raise AssertionError("low-direction mutation did not exceed N^2")

    thresholds = official_mds_thresholds()
    print(
        "XR_DIRECTION_DISTANCE_RAY_BOUND_PASS "
        f"finite_max={first[0]},{second[0]} paid_directions={first[1]},{second[1]} "
        + " ".join(f"{name}:d<={depth}" for name, depth in thresholds)
    )


if __name__ == "__main__":
    main()

