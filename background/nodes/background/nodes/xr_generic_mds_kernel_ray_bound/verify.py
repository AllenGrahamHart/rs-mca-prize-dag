#!/usr/bin/env python3
"""Audit GRK on finite MDS rows and at all six XR candidate rows."""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import comb


def add(left: tuple[int, ...], right: tuple[int, ...], prime: int) -> tuple[int, ...]:
    return tuple((a + b) % prime for a, b in zip(left, right, strict=True))


def scale(value: int, vector: tuple[int, ...], prime: int) -> tuple[int, ...]:
    return tuple(value * coordinate % prime for coordinate in vector)


def sparse_syndromes(
    prime: int, redundancy: int, coordinates: tuple[int, ...]
) -> tuple[set[tuple[int, ...]], tuple[set[tuple[int, ...]], ...]]:
    columns = tuple(
        tuple(pow(x, exponent, prime) for exponent in range(redundancy))
        for x in coordinates
    )
    column_spans = tuple(
        {scale(value, column, prime) for value in range(prime)} for column in columns
    )
    return set().union(*column_spans), column_spans


def exhaustive_radius_one(
    prime: int, redundancy: int, coordinates: tuple[int, ...], d: int, h: int
) -> tuple[int, int]:
    if redundancy - h != 1:
        raise AssertionError("this replay enumerates radius-one witnesses")
    sparse, spans = sparse_syndromes(prime, redundancy, coordinates)
    vectors = tuple(product(range(prime), repeat=redundancy))
    maximum = 0
    generic_pairs = 0
    for y0 in vectors:
        for y1 in vectors:
            if any(y0 in span and y1 in span for span in spans):
                continue
            generic_pairs += 1
            hits = sum(
                add(y0, scale(gamma, y1, prime), prime) in sparse
                for gamma in range(prime)
            )
            maximum = max(maximum, hits)

    n_union = redundancy + d
    bound = Fraction(
        comb(n_union, d) * redundancy,
        comb(d + h, d),
    )
    if maximum > bound:
        raise AssertionError((prime, redundancy, d, h, maximum, bound))

    # Removing genericity lets one sparse line contribute every field slope.
    column = tuple(pow(coordinates[0], exponent, prime) for exponent in range(redundancy))
    tangent_hits = sum(
        add(column, scale(gamma, column, prime), prime) in sparse
        for gamma in range(prime)
    )
    if tangent_hits != prime or tangent_hits <= bound:
        raise AssertionError(("genericity mutation", tangent_hits, bound))
    return maximum, generic_pairs


def official_thresholds() -> tuple[tuple[str, int], ...]:
    rows = (
        ("rowc-r1_4", 1024, 4, 256),
        ("rowc-r1_8", 1024, 8, 256),
        ("rowc-r1_16", 1024, 16, 512),
        ("prize-r1_4", 1 << 41, 4, 256),
        ("prize-r1_8", 1 << 41, 8, 256),
        ("prize-r1_16", 1 << 41, 16, 512),
    )
    thresholds: list[tuple[str, int]] = []
    for name, n, rate_denominator, scale_denominator in rows:
        k = n // rate_denominator
        redundancy = n - k
        h = n // scale_denominator + 1
        budget = 8 * n**3
        d = 0
        while True:
            bound = Fraction(
                comb(redundancy + d, d) * redundancy,
                comb(d + h, d),
            )
            if bound > budget:
                break
            d += 1
        max_paid = d - 1
        if max_paid < 3:
            raise AssertionError((name, max_paid))
        mutation = comb(redundancy + max_paid, max_paid) * redundancy
        if mutation <= budget:
            raise AssertionError((name, "normalization mutation"))
        thresholds.append((name, max_paid))
    return tuple(thresholds)


def main() -> None:
    d1 = exhaustive_radius_one(11, 2, (1, 2, 3), d=1, h=1)
    d2 = exhaustive_radius_one(7, 3, (1, 2, 3, 4, 5), d=2, h=2)
    thresholds = official_thresholds()
    print(
        "XR_GENERIC_MDS_KERNEL_RAY_BOUND_PASS "
        f"finite_max={d1[0]},{d2[0]} "
        + " ".join(f"{name}:d<={depth}" for name, depth in thresholds)
    )


if __name__ == "__main__":
    main()

