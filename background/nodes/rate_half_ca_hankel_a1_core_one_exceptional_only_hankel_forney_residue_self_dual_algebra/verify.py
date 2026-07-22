#!/usr/bin/env python3
"""Exact normalized-frame checks for the Forney residue algebra."""

from __future__ import annotations


def polynomial_from_roots(roots: tuple[int, ...], prime: int) -> list[int]:
    out = [1]
    for root in roots:
        next_out = [0] * (len(out) + 1)
        for index, value in enumerate(out):
            next_out[index] = (next_out[index] - root * value) % prime
            next_out[index + 1] = (next_out[index + 1] + value) % prime
        out = next_out
    return out


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
    e = 3
    blocks = ((1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12))
    beta = [100, 5, 91, 10, 96, 1]
    columns = [polynomial_from_roots(block, prime) for block in blocks]
    q_1 = [column[0] for column in columns]
    normalized = [
        [value * pow(column[0], -1, prime) % prime for value in column]
        for column in columns
    ]
    generator = [[column[row] for column in normalized] for row in range(e)]
    mu = [beta[i] * q_1[i] * q_1[i] % prime for i in range(2 * e)]

    gram = [
        [
            sum(mu[k] * generator[i][k] * generator[j][k] for k in range(2 * e))
            % prime
            for j in range(e)
        ]
        for i in range(e)
    ]
    if generator[0] != [1] * (2 * e) or any(value for row in gram for value in row):
        raise AssertionError("normalized residue Gram identity failed")

    products = [
        [generator[i][k] * generator[j][k] % prime for k in range(2 * e)]
        for i in range(e)
        for j in range(i, e)
    ]
    product_rank = rank(products, prime)
    if product_rank != 2 * e - 1:
        raise AssertionError("positive control should have codimension-one product span")
    if any(sum(mu[k] * row[k] for k in range(2 * e)) % prime for row in products):
        raise AssertionError("Forney functional does not annihilate the product span")

    print(
        "RATE_HALF_HANKEL_FORNEY_RESIDUE_ALGEBRA_PASS "
        f"prime={prime} e={e} product_dimension={product_rank}"
    )


if __name__ == "__main__":
    main()
