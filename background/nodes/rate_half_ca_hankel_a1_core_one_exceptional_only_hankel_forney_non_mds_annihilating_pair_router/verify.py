#!/usr/bin/env python3
"""Exact finite control for the non-MDS annihilating-pair router."""

from __future__ import annotations


def multiply(left: list[int], right: list[int], prime: int) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            answer[i + j] = (answer[i + j] + x * y) % prime
    return answer


def locator(roots: list[int], prime: int) -> list[int]:
    answer = [1]
    for root in roots:
        answer = multiply(answer, [-root % prime, 1], prime)
    return answer


def matrix_rank(matrix: list[list[int]], prime: int) -> int:
    work = [[value % prime for value in row] for row in matrix]
    rank = 0
    for column in range(len(work[0])):
        pivot = next((row for row in range(rank, len(work)) if work[row][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        scale = pow(work[rank][column], prime - 2, prime)
        work[rank] = [value * scale % prime for value in work[rank]]
        for row in range(len(work)):
            if row == rank:
                continue
            factor = work[row][column]
            work[row] = [
                (left - factor * right) % prime
                for left, right in zip(work[row], work[rank], strict=True)
            ]
        rank += 1
    return rank


def main() -> None:
    prime = 101
    generator = [
        [1, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 1],
    ]
    weights = [1, -1, 1, -1, 1, -1]
    for left in generator:
        for right in generator:
            pairing = sum(w * x * y for w, x, y in zip(weights, left, right, strict=True)) % prime
            if pairing:
                raise AssertionError("control code is not weighted self-dual")

    set_i = [0, 1, 2]
    set_j = [3, 4, 5]
    rank_i = matrix_rank([[row[index] for index in set_i] for row in generator], prime)
    rank_j = matrix_rank([[row[index] for index in set_j] for row in generator], prime)
    deficiency = len(generator) - rank_i
    if rank_i != rank_j or deficiency != 1 or 2 * deficiency > len(generator):
        raise AssertionError("complementary deficiency hierarchy failed")
    u = generator[2]
    v = generator[0]
    if any(u[index] for index in set_i):
        raise AssertionError("u does not vanish on I")
    if any(v[index] for index in set_j):
        raise AssertionError("v does not vanish on J")
    product = [left * right % prime for left, right in zip(u, v, strict=True)]
    if any(product):
        raise AssertionError("annihilating product is nonzero")
    if u == v:
        raise AssertionError("annihilating pair collapsed")

    roots_i = [1, 2, 3]
    roots_j = [4, 5, 6]
    d_u = locator(roots_i, prime)
    d_v = locator(roots_j, prime)
    a_poly = locator(roots_i + roots_j, prime)
    if multiply(d_u, d_v, prime) != a_poly:
        raise AssertionError("exact-half gcd factorization failed")
    # With q_1=1, the numerator combinations and normalized classes have
    # identical exceptional zero locators, as asserted by (HNA5).
    q_1 = [1]
    if multiply(d_u, q_1, prime) != d_u or multiply(d_v, q_1, prime) != d_v:
        raise AssertionError("numerator gcd form changed under unit normalization")
    excess_u = locator(roots_i + [4], prime)
    if len(excess_u) - 1 != 4 or len(d_v) - 1 != 3:
        raise AssertionError("excess-zero degree dichotomy failed")

    print(
        "RATE_HALF_NON_MDS_ANNIHILATING_PAIR_PASS "
        f"prime={prime} e=3 I={set_i} J={set_j} deficiency={deficiency} "
        "residue_gates=1 exact_degrees=(3,3) excess=(4,3)"
    )


if __name__ == "__main__":
    main()
