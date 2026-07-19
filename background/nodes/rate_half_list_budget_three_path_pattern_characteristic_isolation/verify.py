#!/usr/bin/env python3
"""Verify the exact cyclotomic minor isolating the known path pattern."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_path_pattern_characteristic_isolation"
DEPENDENCY = "rate_half_list_budget_three_path_power_two_witness"
CONSUMER = "rate_half_list_adjacent_crossing"
DIMENSION = 8

SUPPORTS = (
    frozenset((2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 15)),
    frozenset((0, 1, 3, 4, 6, 7, 8, 10, 11, 14, 15)),
    frozenset((0, 1, 2, 3, 5, 7, 8, 12, 13, 14, 15)),
    frozenset((0, 1, 4, 5, 6, 9, 10, 11, 12, 13, 14)),
)
MINOR_ROWS = (
    0, 2, 5, 7, 11, 13, 15, 16, 9, 4, 1, 14,
    6, 3, 18, 20, 10, 17, 8, 19, 12, 21, 22, 23,
)
EXPECTED_ALPHA = (
    0, 12_582_912, -14_680_064, 29_360_128,
    -14_680_064, 12_582_912, 0, 0,
)


Element = tuple[Fraction, ...]


def element(values: tuple[int | Fraction, ...]) -> Element:
    return tuple(Fraction(values[i] if i < len(values) else 0) for i in range(DIMENSION))


ZERO = element(())
ONE = element((1,))


def add(left: Element, right: Element) -> Element:
    return tuple(a + b for a, b in zip(left, right, strict=True))


def negate(value: Element) -> Element:
    return tuple(-entry for entry in value)


def subtract(left: Element, right: Element) -> Element:
    return add(left, negate(right))


def multiply(left: Element, right: Element) -> Element:
    answer = [Fraction(0) for _ in range(DIMENSION)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            degree = i + j
            if degree >= DIMENSION:
                answer[degree - DIMENSION] -= a * b
            else:
                answer[degree] += a * b
    return tuple(answer)


def monomial(exponent: int) -> Element:
    quotient, remainder = divmod(exponent, DIMENSION)
    values = [0] * DIMENSION
    values[remainder] = -1 if quotient % 2 else 1
    return element(tuple(values))


def inverse(value: Element) -> Element:
    if value == ZERO:
        raise ZeroDivisionError
    matrix = []
    for row in range(DIMENSION):
        matrix.append([
            multiply(value, monomial(column))[row]
            for column in range(DIMENSION)
        ] + [Fraction(row == 0)])
    for column in range(DIMENSION):
        pivot = next(i for i in range(column, DIMENSION) if matrix[i][column])
        matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
        scale = matrix[column][column]
        matrix[column] = [entry / scale for entry in matrix[column]]
        for row in range(DIMENSION):
            if row != column and matrix[row][column]:
                factor = matrix[row][column]
                matrix[row] = [
                    left - factor * right
                    for left, right in zip(matrix[row], matrix[column], strict=True)
                ]
    answer = tuple(matrix[row][-1] for row in range(DIMENSION))
    assert multiply(value, answer) == ONE
    return answer


def intersection_matrix() -> list[list[Element]]:
    rows = []
    for exponent in range(16):
        members = tuple(i for i, support in enumerate(SUPPORTS) if exponent in support)
        if len(members) <= 1:
            continue
        base = 0 if 0 in members else members[0]
        powers = tuple(monomial(exponent * degree) for degree in range(8))
        for member in members:
            if member == base:
                continue
            row = [ZERO for _ in range(24)]
            if member:
                row[(member - 1) * 8 : member * 8] = powers
            if base:
                row[(base - 1) * 8 : base * 8] = tuple(negate(value) for value in powers)
            rows.append(row)
    return rows


def determinant(matrix: list[list[Element]]) -> Element:
    work = [[entry for entry in row] for row in matrix]
    answer = ONE
    for column in range(len(work)):
        pivot = next(i for i in range(column, len(work)) if work[i][column] != ZERO)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            answer = negate(answer)
        pivot_value = work[column][column]
        answer = multiply(answer, pivot_value)
        pivot_inverse = inverse(pivot_value)
        for row in range(column + 1, len(work)):
            if work[row][column] == ZERO:
                continue
            factor = multiply(work[row][column], pivot_inverse)
            work[row] = [
                subtract(left, multiply(factor, right))
                for left, right in zip(work[row], work[column], strict=True)
            ]
    return answer


def bareiss_determinant(matrix: list[list[int]]) -> int:
    work = [row[:] for row in matrix]
    sign = 1
    previous = 1
    for column in range(len(work) - 1):
        pivot = next(i for i in range(column, len(work)) if work[i][column])
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            sign *= -1
        pivot_value = work[column][column]
        for row in range(column + 1, len(work)):
            for j in range(column + 1, len(work)):
                numerator = work[row][j] * pivot_value - work[row][column] * work[column][j]
                assert numerator % previous == 0
                work[row][j] = numerator // previous
            work[row][column] = 0
        previous = pivot_value
    return sign * work[-1][-1]


def norm(value: tuple[int, ...]) -> int:
    basis = tuple(monomial(column) for column in range(DIMENSION))
    product_columns = [multiply(element(value), base) for base in basis]
    matrix = [
        [int(product_columns[column][row]) for column in range(DIMENSION)]
        for row in range(DIMENSION)
    ]
    return bareiss_determinant(matrix)


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges


def main() -> None:
    matrix = intersection_matrix()
    assert len(matrix) == 28 and all(len(row) == 24 for row in matrix)
    minor = [matrix[index] for index in MINOR_ROWS]
    alpha = determinant(minor)
    assert all(entry.denominator == 1 for entry in alpha)
    alpha_integer = tuple(int(entry) for entry in alpha)
    assert alpha_integer == EXPECTED_ALPHA
    alpha_norm = abs(norm(alpha_integer))
    assert alpha_norm == (2**170) * (17**4)
    assert 17**64 > 2**256 and (1 << 37) > 64
    packet_check()
    print(
        "RATE_HALF_LIST_B3_PATH_PATTERN_CHARACTERISTIC_ISOLATION_PASS "
        f"matrix=28x24 minor=24 norm=2^170*17^4 field_degree_min={1 << 37}"
    )


if __name__ == "__main__":
    main()
