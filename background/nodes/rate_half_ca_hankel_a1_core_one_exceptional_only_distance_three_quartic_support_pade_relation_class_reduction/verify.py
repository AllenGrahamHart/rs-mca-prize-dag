#!/usr/bin/env python3
"""Exact controls for the Pade relation-class reduction."""

from __future__ import annotations

from itertools import combinations, permutations
from math import comb


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index in range(len(out)):
        out[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % prime
    return trim(out)


def scale(poly: list[int], scalar: int, prime: int) -> list[int]:
    return trim([scalar * value % prime for value in poly])


def mul(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % prime
    return trim(out)


def determinant(matrix: list[list[list[int]]], prime: int) -> list[int]:
    size = len(matrix)
    out = [0]
    for perm in permutations(range(size)):
        inversions = sum(
            1
            for left in range(size)
            for right in range(left + 1, size)
            if perm[left] > perm[right]
        )
        term = [1]
        for row, column in enumerate(perm):
            term = mul(term, matrix[row][column], prime)
        out = add(out, scale(term, -1 if inversions % 2 else 1, prime), prime)
    return trim(out)


def relation_fixture() -> tuple[int, int, int]:
    prime = 101
    tail = 1
    size = 2 * (tail + 1)
    first_class = (2, 3, 5, 11, 96)
    second_class = (5, 7, 13, 17, 96)
    q_values: dict[int, list[int]] = {}

    # R_1(U,Z)=U^2+Z and R_2(U,Z)=U^2+25/Z agree at Z=5,-5.
    for gamma in first_class:
        q_values[gamma] = [gamma, 0, 1]
    for gamma in second_class:
        second_value = 25 * pow(gamma, -1, prime) % prime
        if gamma in q_values:
            need(q_values[gamma] == [second_value, 0, 1], "relation overlap drifted")
        else:
            q_values[gamma] = [second_value, 0, 1]

    zero_circuits = 0
    for relation_class in (first_class, second_class):
        for subset in combinations(relation_class, size):
            matrix = [
                [[1], [gamma], q_values[gamma], scale(q_values[gamma], gamma, prime)]
                for gamma in subset
            ]
            need(determinant(matrix, prime) == [0], "relation subset was not singular")
            zero_circuits += 1
    need(zero_circuits == 2 * comb(len(first_class), size), "wrong relation circuit count")
    intersection = len(set(first_class) & set(second_class))
    need(intersection <= 2 * tail, "relation classes exceeded intersection cap")
    return zero_circuits, intersection, size


def official_shadow_bounds() -> tuple[int, int]:
    e = 2**38 - 1
    outputs = []
    for tail, boundary_loss in ((6, 2), (8, 3)):
        size = 2 * (tail + 1)
        orbit_count = 3 * e - tail - boundary_loss
        all_subsets = comb(3 * e, size)
        own_subsets = comb(e, size)
        denominator = orbit_count - size
        circuit_lower = (
            orbit_count * own_subsets
            - size * all_subsets
            + denominator
            - 1
        ) // denominator
        shadow = comb(3 * e, size - 1)
        class_lower = size - 1 + (size * circuit_lower + shadow - 1) // shadow
        outputs.append(class_lower)
    need(outputs == [172410, 2128], "official relation-class bounds drifted")
    return outputs[0], outputs[1]


def main() -> None:
    fixture = relation_fixture()
    bounds = official_shadow_bounds()
    print(
        "RATE_HALF_DISTANCE_THREE_PADE_RELATION_CLASS_PASS "
        f"fixture={fixture} class_bounds={bounds}"
    )


if __name__ == "__main__":
    main()
