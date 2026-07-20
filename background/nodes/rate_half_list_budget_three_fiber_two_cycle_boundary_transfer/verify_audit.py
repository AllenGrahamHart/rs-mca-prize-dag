#!/usr/bin/env python3
"""Independent arithmetic and PGL-matching audit for the boundary transfer."""

from __future__ import annotations


PRIMES = (101, 193, 257)


def determinant(matrix: list[list[int]], prime: int) -> int:
    work = [[entry % prime for entry in row] for row in matrix]
    answer = 1
    for column in range(4):
        pivot = next(
            (row for row in range(column, 4) if work[row][column]),
            None,
        )
        if pivot is None:
            return 0
        if pivot != column:
            work[pivot], work[column] = work[column], work[pivot]
            answer = -answer
        value = work[column][column]
        answer = answer * value % prime
        inverse = pow(value, -1, prime)
        work[column] = [entry * inverse % prime for entry in work[column]]
        for row in range(column + 1, 4):
            factor = work[row][column]
            work[row] = [
                (left - factor * right) % prime
                for left, right in zip(work[row], work[column], strict=True)
            ]
    return answer % prime


def matching_audit(prime: int) -> None:
    completion_roots = (2, 5, 9, 17)
    outer_roots = tuple(
        (7 * value + 3) * pow(11 * value + 13, -1, prime) % prime
        for value in completion_roots
    )
    matrix = [
        [1, source, target, source * target]
        for source, target in zip(completion_roots, outer_roots, strict=True)
    ]
    assert determinant(matrix, prime) == 0

    wrong_sources = (2, 5, 9, 19)
    wrong = [
        [1, source, target, source * target]
        for source, target in zip(wrong_sources, outer_roots, strict=True)
    ]
    assert determinant(wrong, prime) != 0


def arithmetic_audit() -> None:
    s = 1 << 38
    r = s - 1
    generic_v = s // 2 - 2
    intermediate_v = (2 * s - 5) // 3
    assert r + 4 - 2 * (r - generic_v) == 1
    assert r + 4 - 3 * (r - intermediate_v) == 1
    assert 2 * (r - generic_v) == s + 2
    assert 3 * (r - intermediate_v) == s + 2


def main() -> None:
    arithmetic_audit()
    for prime in PRIMES:
        matching_audit(prime)
    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_CYCLE_BOUNDARY_TRANSFER_AUDIT_PASS "
        f"fields={len(PRIMES)} doubled_rounding=1 completion_match=1 mutation=1"
    )


if __name__ == "__main__":
    main()
