#!/usr/bin/env python3
"""Canonical check of the exceptional Hankel rank-one flag."""

from __future__ import annotations


def mat_vec(matrix: list[list[int]], vector: list[int], prime: int) -> list[int]:
    return [sum(a * b for a, b in zip(row, vector)) % prime for row in matrix]


def pairing(
    left: list[int], matrix: list[list[int]], right: list[int], prime: int
) -> int:
    image = mat_vec(matrix, right, prime)
    return sum(a * b for a, b in zip(left, image)) % prime


def rank(matrix: list[list[int]], prime: int) -> int:
    work = [row[:] for row in matrix]
    pivot_row = 0
    for column in range(len(work[0])):
        pivot = next(
            (row for row in range(pivot_row, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        inverse = pow(work[pivot_row][column], -1, prime)
        work[pivot_row] = [value * inverse % prime for value in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row or work[row][column] == 0:
                continue
            factor = work[row][column]
            work[row] = [
                (a - factor * b) % prime
                for a, b in zip(work[row], work[pivot_row])
            ]
        pivot_row += 1
    return pivot_row


def main() -> None:
    prime = 101
    e = 2
    size = 2 * e + 2
    m_0 = [[0] * size for _ in range(size)]
    m_1 = [[0] * size for _ in range(size)]
    for row in range(e):
        m_0[e + 1 + row][row + 1] = 1
        m_0[row + 1][e + 1 + row] = 1
        m_1[e + 1 + row][row] = 1
        m_1[row][e + 1 + row] = 1
    m_1[-1][-1] = 1

    w_q = []
    for index in range(e + 1):
        vector = [0] * size
        vector[index] = -1 if index % 2 else 1
        w_q.append([value % prime for value in vector])
    v = [0] * size
    v[-1] = 1
    h_q = w_q + [v]

    gram_0 = [[pairing(a, m_0, b, prime) for b in h_q] for a in h_q]
    gram_1 = [[pairing(a, m_1, b, prime) for b in h_q] for a in h_q]
    if rank(h_q, prime) != e + 2:
        raise AssertionError("flag dimension is incorrect")
    if rank(gram_0, prime) != 0 or rank(gram_1, prime) != 1:
        raise AssertionError("restricted rank profile is incorrect")
    if gram_1[-1][-1] == 0 or any(gram_1[i][-1] for i in range(e + 1)):
        raise AssertionError("regular quotient line is not isolated")

    print(
        "RATE_HALF_HANKEL_COEFFICIENT_RANK_ONE_FLAG_PASS "
        f"prime={prime} e={e} flag_dimension={e+2}"
    )


if __name__ == "__main__":
    main()
