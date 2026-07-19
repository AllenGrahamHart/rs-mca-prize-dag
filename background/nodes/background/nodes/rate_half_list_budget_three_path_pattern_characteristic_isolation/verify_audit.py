#!/usr/bin/env python3
"""Audit the path-pattern determinant in finite characteristics."""

from __future__ import annotations


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


def primes(limit: int) -> list[int]:
    answer = []
    for candidate in range(3, limit + 1, 2):
        if all(candidate % prime for prime in answer if prime * prime <= candidate):
            answer.append(candidate)
    return answer


def primitive_roots_16(prime: int) -> tuple[int, ...]:
    return tuple(
        value for value in range(2, prime)
        if pow(value, 8, prime) == prime - 1
    )


def matrix(root: int, prime: int) -> list[list[int]]:
    rows = []
    for exponent in range(16):
        members = tuple(i for i, support in enumerate(SUPPORTS) if exponent in support)
        if len(members) <= 1:
            continue
        base = 0 if 0 in members else members[0]
        powers = tuple(pow(root, exponent * degree, prime) for degree in range(8))
        for member in members:
            if member == base:
                continue
            row = [0] * 24
            if member:
                row[(member - 1) * 8 : member * 8] = powers
            if base:
                row[(base - 1) * 8 : base * 8] = tuple(-value % prime for value in powers)
            rows.append(row)
    return rows


def determinant_mod(rows: list[list[int]], prime: int) -> int:
    work = [row[:] for row in rows]
    answer = 1
    for column in range(len(work)):
        pivot = next((i for i in range(column, len(work)) if work[i][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            answer = -answer % prime
        pivot_value = work[column][column]
        answer = answer * pivot_value % prime
        inverse = pow(pivot_value, -1, prime)
        for row in range(column + 1, len(work)):
            factor = work[row][column] * inverse % prime
            work[row] = [
                (left - factor * right) % prime
                for left, right in zip(work[row], work[column], strict=True)
            ]
    return answer


def alpha(root: int, prime: int) -> int:
    return (
        (2**21)
        * (6 * root**5 - 7 * root**4 + 14 * root**3 - 7 * root**2 + 6 * root)
    ) % prime


def rank(rows: list[list[int]], prime: int) -> int:
    work = [row[:] for row in rows]
    answer = 0
    for column in range(len(work[0])):
        pivot = next((i for i in range(answer, len(work)) if work[i][column]), None)
        if pivot is None:
            continue
        work[answer], work[pivot] = work[pivot], work[answer]
        inverse = pow(work[answer][column], -1, prime)
        work[answer] = [value * inverse % prime for value in work[answer]]
        for row in range(len(work)):
            if row != answer and work[row][column]:
                factor = work[row][column]
                work[row] = [
                    (left - factor * right) % prime
                    for left, right in zip(work[row], work[answer], strict=True)
                ]
        answer += 1
    return answer


def main() -> None:
    checked = 0
    for prime in primes(2000):
        for root in primitive_roots_16(prime):
            rows = matrix(root, prime)
            minor = [rows[index] for index in MINOR_ROWS]
            determinant = determinant_mod(minor, prime)
            assert determinant == alpha(root, prime)
            if prime not in (2, 17):
                assert determinant != 0
            checked += 1
    ranks_17 = tuple(rank(matrix(root, 17), 17) for root in primitive_roots_16(17))
    assert ranks_17.count(23) == 2 and ranks_17.count(24) == 6
    print(
        "AUDIT_RATE_HALF_LIST_B3_PATH_PATTERN_CHARACTERISTIC_ISOLATION_PASS "
        f"minor_reductions={checked} ranks17={ranks_17}"
    )


if __name__ == "__main__":
    main()
