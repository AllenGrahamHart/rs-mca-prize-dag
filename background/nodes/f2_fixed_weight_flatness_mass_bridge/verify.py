#!/usr/bin/env python3
"""Fail-closed checks for the fixed-weight to full-cube mass bridge."""

from __future__ import annotations

import itertools
import math
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


def matrix_rank(rows: list[list[int]], prime: int) -> int:
    matrix = [[value % prime for value in row] for row in rows]
    rank = 0
    width = len(matrix[0]) if matrix else 0
    for column in range(width):
        pivot = next(
            (index for index in range(rank, len(matrix)) if matrix[index][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = pow(matrix[rank][column], -1, prime)
        matrix[rank] = [(inverse * value) % prime for value in matrix[rank]]
        for index, row in enumerate(matrix):
            if index != rank and row[column]:
                factor = row[column]
                matrix[index] = [
                    (left - factor * right) % prime
                    for left, right in zip(row, matrix[rank])
                ]
        rank += 1
        if rank == len(matrix):
            break
    return rank


def verify_case(prime: int, width: int, rows: list[list[int]]) -> None:
    layers = [Counter() for _ in range(width + 1)]
    full = Counter()
    all_one = syndrome(rows, (1,) * width, prime)
    for bits in itertools.product((0, 1), repeat=width):
        value = syndrome(rows, bits, prime)
        layers[sum(bits)][value] += 1
        full[value] += 1

    mass = Fraction(0)
    for word in itertools.product((-1, 0, 1), repeat=width):
        if not any(syndrome(rows, word, prime)):
            mass += Fraction(1, 1 << sum(value != 0 for value in word))
    check((1 << width) * mass == sum(size * size for size in full.values()), "mass")

    for weight, layer in enumerate(layers):
        population = math.comb(width, weight)
        maximum = max(layer.values())
        collision = sum(size * size for size in layer.values())
        check(sum(layer.values()) == population, "layer population")
        check(collision <= maximum * population, "layer collision")
        complement = Counter()
        for value, count in layer.items():
            shifted = tuple((a - v) % prime for a, v in zip(all_one, value))
            complement[shifted] = count
        check(complement == layers[width - weight], "complement fibers")

    rank = matrix_rank(rows, prime)
    codomain = prime**rank
    for good in (set(range(width + 1)), set(range(2, max(2, width - 1)))):
        loss = Fraction(1)
        for weight in good:
            population = math.comb(width, weight)
            maximum = max(layers[weight].values())
            loss = max(loss, Fraction(maximum * codomain, codomain + population))
            check(
                maximum <= loss * (1 + Fraction(population, codomain)),
                "mean-plus-one premise",
            )

        tail = sum(
            math.comb(width, weight)
            for weight in range(width + 1)
            if weight not in good
        )
        general_bound = (
            Fraction(3 * tail * tail, 1 << width)
            + 3 * loss * (width + 1 + Fraction(1 << width, codomain))
        )
        check(mass <= general_bound, "banded bridge")
        if len(good) == width + 1:
            all_weight_bound = 2 * loss * (
                width + 1 + Fraction(1 << width, codomain)
            )
            check(mass <= all_weight_bound, "all-weight bridge")


def main() -> None:
    cases = (
        (3, 4, []),
        (3, 5, [[1, 0, 1, 2, 1], [0, 1, 1, 1, 2]]),
        (5, 6, [[1, 2, 3, 4, 0, 1], [2, 4, 1, 3, 0, 2]]),
        (7, 7, [[1, 1, 1, 1, 1, 1, 1], [0, 1, 2, 3, 4, 5, 6]]),
    )
    for case in cases:
        verify_case(*case)
    print(
        "F2_FIXED_WEIGHT_FLATNESS_MASS_BRIDGE_PASS "
        f"checks={CHECKS} cases={len(cases)}"
    )


if __name__ == "__main__":
    main()
