#!/usr/bin/env python3
"""Independent Mobius-pair determinant audit for the cycle embedding."""

from __future__ import annotations


PRIMES = (101, 193, 257)


def determinant(matrix: list[list[int]], prime: int) -> int:
    work = [[entry % prime for entry in row] for row in matrix]
    answer = 1
    for column in range(len(work)):
        pivot = next(
            (row for row in range(column, len(work)) if work[row][column]),
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
        for row in range(column + 1, len(work)):
            factor = work[row][column]
            work[row] = [
                (left - factor * right) % prime
                for left, right in zip(work[row], work[column], strict=True)
            ]
    return answer % prime


def audit(prime: int) -> None:
    roots = (2, 5, 9, 17)
    # T(x)=(3x+7)/(11x+13).
    targets = tuple(
        (3 * root + 7) * pow(11 * root + 13, -1, prime) % prime
        for root in roots
    )
    matrix = [
        [1, root, target, root * target]
        for root, target in zip(roots, targets, strict=True)
    ]
    assert determinant(matrix, prime) == 0

    mutated = [row[:] for row in matrix]
    mutated[-1][2] = (mutated[-1][2] + 1) % prime
    mutated[-1][3] = roots[-1] * mutated[-1][2] % prime
    assert determinant(mutated, prime) != 0

    pairing_rows = (
        ((2, 5, 9, 17), ()),
        ((2, prime - 2, 5, 9), (17,)),
        ((2, prime - 2, 5, prime - 5), (9, 17)),
    )
    for deleted, residual_pairs in pairing_rows:
        coefficient_squares = {value * value % prime for value in deleted}
        denominator_roots = coefficient_squares | {
            value * value % prime for value in residual_pairs
        }
        assert len(denominator_roots) == 4


def main() -> None:
    for prime in PRIMES:
        audit(prime)
    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_CYCLE_QUOTIENT_EMBEDDING_AUDIT_PASS "
        f"fields={len(PRIMES)} pairing_strata=3 mobius_rank=3 mutation_rank=4"
    )


if __name__ == "__main__":
    main()
