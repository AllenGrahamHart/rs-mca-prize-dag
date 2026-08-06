#!/usr/bin/env python3
"""Exact counterexample to naive two-factor private-linear rank induction."""

from __future__ import annotations

from fractions import Fraction
from itertools import product


A = 1
B = 3
H = 2
PARAMS = ((2, 3), (5, 7))
RELATION = (81, -450, 625, -72, 472, -800, 16, -128, 256)


def poly_mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x == 0:
            continue
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_pow_linear(root: int, exponent: int) -> list[int]:
    out = [1]
    factor = [-root, 1]
    for _ in range(exponent):
        out = poly_mul(out, factor)
    return out


def rows() -> list[list[int]]:
    out = []
    for b_exponents in product(range(B), repeat=2):
        base = [1]
        for b_exp, (alpha, beta) in zip(b_exponents, PARAMS):
            base = poly_mul(base, poly_pow_linear(alpha, H * b_exp))
            base = poly_mul(base, poly_pow_linear(beta, H * (B - 1 - b_exp)))
        out.append(base)
    return out


def rank_over_q(items: list[list[int]]) -> int:
    width = max(len(row) for row in items)
    mat = [
        [Fraction(value) for value in row + [0] * (width - len(row))]
        for row in items
    ]
    rank = 0
    for col in range(width):
        pivot = None
        for row in range(rank, len(mat)):
            if mat[row][col]:
                pivot = row
                break
        if pivot is None:
            continue
        mat[rank], mat[pivot] = mat[pivot], mat[rank]
        inv = 1 / mat[rank][col]
        mat[rank] = [value * inv for value in mat[rank]]
        for row in range(len(mat)):
            if row == rank or not mat[row][col]:
                continue
            factor = mat[row][col]
            mat[row] = [
                value - factor * pivot_value
                for value, pivot_value in zip(mat[row], mat[rank])
            ]
        rank += 1
        if rank == len(mat):
            break
    return rank


def relation_polynomial(items: list[list[int]]) -> list[int]:
    width = max(len(row) for row in items)
    out = [0] * width
    for coeff, row in zip(RELATION, items):
        padded = row + [0] * (width - len(row))
        for idx, value in enumerate(padded):
            out[idx] += coeff * value
    return out


def main() -> None:
    items = rows()
    expected_naive = min(A * B**2, A + 2 * H * (B - 1))
    actual_rank = rank_over_q(items)
    relation = relation_polynomial(items)

    if expected_naive != 9:
        raise AssertionError(expected_naive)
    if actual_rank != 8:
        raise AssertionError(actual_rank)
    if any(relation):
        raise AssertionError(relation)

    print("h=3 private-linear two-factor induction guardrail")
    print(f"A={A} B={B} H={H} params={PARAMS}")
    print(f"naive predicted rank={expected_naive}")
    print(f"exact rational rank={actual_rank}")
    print(f"integer relation={RELATION}")
    print("H3_PRIVATE_LINEAR_TWO_FACTOR_GUARDRAIL_PASS")


if __name__ == "__main__":
    main()
