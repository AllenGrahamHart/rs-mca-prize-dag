#!/usr/bin/env python3
"""Finite replay of the all-LineRay affine-core charge and XR thresholds."""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import comb


Vector = tuple[int, ...]


def add(left: Vector, right: Vector, prime: int) -> Vector:
    return tuple((a + b) % prime for a, b in zip(left, right, strict=True))


def sub(left: Vector, right: Vector, prime: int) -> Vector:
    return tuple((a - b) % prime for a, b in zip(left, right, strict=True))


def scale(value: int, vector: Vector, prime: int) -> Vector:
    return tuple(value * coordinate % prime for coordinate in vector)


def rank(rows: list[list[int]], prime: int) -> int:
    if not rows:
        return 0
    matrix = [row[:] for row in rows]
    columns = len(matrix[0])
    pivot = 0
    for column in range(columns):
        choice = next(
            (row for row in range(pivot, len(matrix)) if matrix[row][column] % prime),
            None,
        )
        if choice is None:
            continue
        matrix[pivot], matrix[choice] = matrix[choice], matrix[pivot]
        inverse = pow(matrix[pivot][column], prime - 2, prime)
        matrix[pivot] = [value * inverse % prime for value in matrix[pivot]]
        for row in range(len(matrix)):
            if row == pivot:
                continue
            factor = matrix[row][column] % prime
            if factor:
                matrix[row] = [
                    (a - factor * b) % prime
                    for a, b in zip(matrix[row], matrix[pivot], strict=True)
                ]
        pivot += 1
        if pivot == len(matrix):
            break
    return pivot


def parity(vector: Vector, prime: int) -> Vector:
    return tuple((vector[index] - vector[0]) % prime for index in range(1, 4))


def in_support_image(target: Vector, support: tuple[int, ...], prime: int) -> bool:
    columns = []
    for coordinate in support:
        basis = tuple(1 if index == coordinate else 0 for index in range(4))
        columns.append(parity(basis, prime))
    base = rank([list(column) for column in columns], prime)
    return rank([list(column) for column in columns] + [list(target)], prime) == base


def affine_rank(errors: list[Vector], prime: int) -> int:
    origin = errors[0]
    return rank([list(sub(error, origin, prime)) for error in errors[1:]], prime)


def complete_small_replay() -> tuple[int, int, int, int]:
    prime, radius = 3, 2
    vectors = tuple(product(range(prime), repeat=4))
    syndromes = tuple(product(range(prime), repeat=3))
    checked = 0
    maximum_pairs = 0
    checked_selectors = 0
    maximum_slopes = 0
    for y0 in syndromes:
        for y1 in syndromes:
            if not any(y1):
                continue
            pairs = []
            for gamma in range(prime):
                target = add(y0, scale(gamma, y1, prime), prime)
                for error in vectors:
                    support = tuple(index for index, value in enumerate(error) if value)
                    if len(support) > radius or parity(error, prime) != target:
                        continue
                    if in_support_image(y0, support, prime) and in_support_image(
                        y1, support, prime
                    ):
                        continue
                    pairs.append((gamma, error))
            if not pairs:
                continue
            errors = [error for _, error in pairs]
            dimension = affine_rank(errors, prime)
            charge = sum(
                Fraction(1, comb(dimension + sum(bool(x) for x in error), dimension))
                for error in errors
            )
            if charge > 1 or len(pairs) > comb(dimension + radius, dimension):
                raise AssertionError((y0, y1, len(pairs), dimension, charge))
            by_slope: dict[int, list[Vector]] = {}
            for gamma, error in pairs:
                by_slope.setdefault(gamma, []).append(error)
            selector_ranks = []
            for selector in product(
                *(by_slope[gamma] for gamma in sorted(by_slope))
            ):
                selector_ranks.append(affine_rank(list(selector), prime))
                checked_selectors += 1
            minimum_selector_rank = min(selector_ranks)
            if len(by_slope) > comb(
                minimum_selector_rank + radius, minimum_selector_rank
            ):
                raise AssertionError(
                    (y0, y1, len(by_slope), minimum_selector_rank)
                )
            checked += 1
            maximum_pairs = max(maximum_pairs, len(pairs))
            maximum_slopes = max(maximum_slopes, len(by_slope))

    # Without transversality, one coordinate supports an arbitrarily long line.
    tangent_prime = 7
    tangent_errors = [((1 + gamma) % tangent_prime, 0) for gamma in range(tangent_prime)]
    tangent_dimension = affine_rank(tangent_errors, tangent_prime)
    if len(tangent_errors) <= comb(tangent_dimension + 1, tangent_dimension):
        raise AssertionError("transversality mutation was not detected")
    return checked, maximum_pairs, checked_selectors, maximum_slopes


def official_thresholds() -> tuple[tuple[str, int], ...]:
    rows = (
        ("rowc-r1_4", 1024, 4, 256),
        ("rowc-r1_8", 1024, 8, 256),
        ("rowc-r1_16", 1024, 16, 512),
        ("prize-r1_4", 1 << 41, 4, 256),
        ("prize-r1_8", 1 << 41, 8, 256),
        ("prize-r1_16", 1 << 41, 16, 512),
    )
    output = []
    for name, n, rate_denominator, scale_denominator in rows:
        k = n // rate_denominator
        reserve = n // scale_denominator + 1
        radius = n - k - reserve
        budget = 8 * n**3
        paid = 0
        while comb(radius + paid + 1, paid + 1) <= budget:
            paid += 1
        if paid != 3 or comb(radius + 4, 4) <= budget:
            raise AssertionError((name, radius, paid))
        output.append((name, paid))
    return tuple(output)


def main() -> None:
    checked, maximum, selectors, maximum_slopes = complete_small_replay()
    thresholds = official_thresholds()
    print(
        "XR_ALL_LINERAY_AFFINE_CORE_BOUND_PASS "
        f"small_lines={checked} max_pairs={maximum} "
        f"selectors={selectors} max_slopes={maximum_slopes} "
        + " ".join(f"{name}:sigma<={paid}" for name, paid in thresholds)
    )


if __name__ == "__main__":
    main()
