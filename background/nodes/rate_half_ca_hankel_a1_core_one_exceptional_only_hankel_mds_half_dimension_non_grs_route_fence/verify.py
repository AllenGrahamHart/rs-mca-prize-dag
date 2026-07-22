#!/usr/bin/env python3
"""Exact half-dimension MDS/self-dual non-GRS route-fence witness."""

from __future__ import annotations

from itertools import combinations


PRIME = 11


def inverse(value: int) -> int:
    return pow(value % PRIME, PRIME - 2, PRIME)


def rref(matrix: list[list[int]]) -> tuple[list[list[int]], list[int]]:
    work = [[value % PRIME for value in row] for row in matrix]
    if not work:
        return work, []
    pivot_columns: list[int] = []
    row = 0
    for column in range(len(work[0])):
        pivot = next((index for index in range(row, len(work)) if work[index][column]), None)
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        scale = inverse(work[row][column])
        work[row] = [scale * value % PRIME for value in work[row]]
        for index in range(len(work)):
            if index == row or work[index][column] == 0:
                continue
            factor = work[index][column]
            work[index] = [
                (left - factor * right) % PRIME
                for left, right in zip(work[index], work[row], strict=True)
            ]
        pivot_columns.append(column)
        row += 1
        if row == len(work):
            break
    return work, pivot_columns


def nullspace(matrix: list[list[int]]) -> list[list[int]]:
    reduced, pivots = rref(matrix)
    free = [column for column in range(len(matrix[0])) if column not in pivots]
    basis: list[list[int]] = []
    for free_column in free:
        vector = [0] * len(matrix[0])
        vector[free_column] = 1
        for row, pivot in enumerate(pivots):
            vector[pivot] = -reduced[row][free_column] % PRIME
        basis.append(vector)
    return basis


def determinant(matrix: list[list[int]]) -> int:
    work = [[value % PRIME for value in row] for row in matrix]
    answer = 1
    for column in range(len(work)):
        pivot = next((index for index in range(column, len(work)) if work[index][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            answer = -answer
        value = work[column][column]
        answer = answer * value % PRIME
        scale = inverse(value)
        for row in range(column + 1, len(work)):
            factor = work[row][column] * scale % PRIME
            for entry in range(column, len(work)):
                work[row][entry] = (work[row][entry] - factor * work[column][entry]) % PRIME
    return answer % PRIME


def monomials(degree: int, variables: int = 4) -> list[tuple[int, ...]]:
    if variables == 1:
        return [(degree,)]
    answer: list[tuple[int, ...]] = []
    for first in range(degree, -1, -1):
        answer.extend((first,) + tail for tail in monomials(degree - first, variables - 1))
    return answer


def evaluate_monomial(point: tuple[int, ...], exponent: tuple[int, ...]) -> int:
    value = 1
    for coordinate, power in zip(point, exponent, strict=True):
        value = value * pow(coordinate, power, PRIME) % PRIME
    return value


def main() -> None:
    identity = [
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 1, 0),
        (0, 0, 0, 1),
    ]
    right_rows = [
        [1, 1, 4, 5],
        [1, 7, 5, 1],
        [4, 5, 10, 10],
        [6, 10, 1, 7],
    ]
    right_columns = [tuple(row[index] for row in right_rows) for index in range(4)]
    columns = identity + right_columns

    gram = [
        [
            ((1 if left == right else 0) + sum(right_rows[left][j] * right_rows[right][j] for j in range(4)))
            % PRIME
            for right in range(4)
        ]
        for left in range(4)
    ]
    if any(any(row) for row in gram):
        raise AssertionError("fixture is not Euclidean self-dual")

    minors = [
        determinant([[column[row] for column in selected] for row in range(4)])
        for selected in combinations(columns, 4)
    ]
    if 0 in minors:
        raise AssertionError("fixture is not MDS")

    quadratics = monomials(2)
    evaluation = [
        [evaluate_monomial(point, exponent) for exponent in quadratics]
        for point in columns
    ]
    quad_kernel = nullspace(evaluation)
    if len(quad_kernel) != 3:
        raise AssertionError("quadratic ideal does not have dimension three")

    cubics = monomials(3)
    cubic_index = {exponent: index for index, exponent in enumerate(cubics)}
    syzygy_columns: list[list[int]] = []
    for quadric in quad_kernel:
        for variable in range(4):
            product = [0] * len(cubics)
            for coefficient, exponent in zip(quadric, quadratics, strict=True):
                raised = list(exponent)
                raised[variable] += 1
                product[cubic_index[tuple(raised)]] = coefficient
            syzygy_columns.append(product)
    syzygy_matrix = [list(row) for row in zip(*syzygy_columns, strict=True)]
    _, syzygy_pivots = rref(syzygy_matrix)
    if len(syzygy_pivots) != 12:
        raise AssertionError("quadratic ideal unexpectedly has a linear syzygy")

    transposed = [list(row) for row in zip(*syzygy_matrix, strict=True)]
    _, independent_rows = rref(transposed)
    witness_rows = independent_rows[:12]
    witness_minor = determinant([[syzygy_matrix[row][column] for column in range(12)] for row in witness_rows])
    if witness_minor == 0:
        raise AssertionError("linear-syzygy rank witness vanished")

    print(
        "RATE_HALF_MDS_HALF_DIMENSION_NON_GRS_PASS "
        f"field={PRIME} mds_minors={len(minors)} square_rank={len(quadratics)-len(quad_kernel)} "
        f"quadrics={quad_kernel} syzygy_rows={witness_rows} syzygy_minor={witness_minor}"
    )


if __name__ == "__main__":
    main()
