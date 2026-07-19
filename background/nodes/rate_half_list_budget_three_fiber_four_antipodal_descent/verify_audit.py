#!/usr/bin/env python3
"""Audit the antipodal identities on the first two quotient boundaries."""

from __future__ import annotations

from itertools import combinations, permutations, product


PRIME = 17


def add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    answer = [0] * size
    for index in range(size):
        answer[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % PRIME
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def scale(polynomial: list[int], scalar: int) -> list[int]:
    return [scalar * value % PRIME for value in polynomial]


def multiply(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] = (answer[i + j] + a * b) % PRIME
    return answer


def kernel(matrix: list[list[int]], prime: int) -> tuple[int, list[list[int]]]:
    rows = [row[:] for row in matrix]
    pivots = []
    rank = 0
    for column in range(len(rows[0])):
        pivot = next(
            (row for row in range(rank, len(rows)) if rows[row][column]), None
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, prime)
        rows[rank] = [value * inverse % prime for value in rows[rank]]
        for row in range(len(rows)):
            if row != rank and rows[row][column]:
                factor = rows[row][column]
                rows[row] = [
                    (left - factor * right) % prime
                    for left, right in zip(rows[row], rows[rank], strict=True)
                ]
        pivots.append(column)
        rank += 1

    free = [column for column in range(len(rows[0])) if column not in pivots]
    basis = []
    for free_column in free:
        vector = [0] * len(rows[0])
        vector[free_column] = 1
        for row, pivot_column in reversed(list(enumerate(pivots))):
            vector[pivot_column] = -sum(
                rows[row][column] * vector[column] for column in free
            ) % prime
        basis.append(vector)
    return rank, basis


def order_eight_census() -> tuple[int, int]:
    prime = 97
    generator = 5
    quotient = tuple(pow(generator, 12 * exponent, prime) for exponent in range(8))
    half_domain = {
        pow(generator, 6 * exponent, prime) for exponent in range(16)
    }
    square_roots = {
        value: tuple(
            root for root in half_domain if root * root % prime == value
        )
        for value in quotient
    }

    checked = 0
    positive = 0
    for deleted in combinations(quotient, 4):
        complementary = tuple(value for value in quotient if value not in deleted)
        for a_values in product(*(square_roots[value] for value in deleted)):
            for c_values in permutations(complementary):
                checked += 1
                matrix = [
                    [1] * 4,
                    list(c_values),
                    list(a_values),
                    [
                        a * c % prime
                        for a, c in zip(a_values, c_values, strict=True)
                    ],
                ]
                rank, basis = kernel(matrix, prime)
                if rank == 3 and all(basis[0]):
                    positive += 1
    return checked, positive


def main() -> None:
    a_values = (1, 2, 4, 8)
    lambdas = (1, 1, 1, 14)
    assert sum(lambdas) % PRIME == 0
    assert sum(a * value for a, value in zip(a_values, lambdas, strict=True)) % PRIME == 0

    domain = [1]
    relation = [0]
    b_values = set()
    for a, coefficient in zip(a_values, lambdas, strict=True):
        p_locator = [-a % PRIME, 0, 1]
        a_locator = [a, 0, 1]
        domain = multiply(domain, multiply(p_locator, a_locator))
        relation = add(relation, scale(a_locator, coefficient))
        b_values.add(a * a % PRIME)

    expected = [-1 % PRIME] + [0] * 15 + [1]
    assert domain == expected
    assert relation == [0]
    assert b_values == {1, 4, 13, 16}
    checked, positive = order_eight_census()
    assert (checked, positive) == (26_880, 192)
    print(
        "AUDIT_RATE_HALF_LIST_B3_FIBER_FOUR_ANTIPODAL_DESCENT_PASS "
        "field=17 domain_order=16 boundary_s=1 "
        "field=97 quotient_order=8 assignments=26880 positives=192"
    )


if __name__ == "__main__":
    main()
