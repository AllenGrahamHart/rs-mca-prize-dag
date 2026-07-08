#!/usr/bin/env python3
"""Replay the private-linear one-factor rank formula."""

from __future__ import annotations


P = 769


def poly_mul(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x == 0:
            continue
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return out


def poly_pow_linear(root: int, exponent: int, p: int) -> list[int]:
    out = [1]
    factor = [(-root) % p, 1]
    for _ in range(exponent):
        out = poly_mul(out, factor, p)
    return out


def shifted_monomial(poly: list[int], shift: int) -> list[int]:
    return [0] * shift + poly


def rank_mod_p(rows: list[list[int]], p: int) -> int:
    if not rows:
        return 0
    width = max(len(row) for row in rows)
    mat = [row + [0] * (width - len(row)) for row in rows]
    rank = 0
    for col in range(width):
        pivot = None
        for row in range(rank, len(mat)):
            if mat[row][col] % p:
                pivot = row
                break
        if pivot is None:
            continue
        mat[rank], mat[pivot] = mat[pivot], mat[rank]
        inv = pow(mat[rank][col] % p, -1, p)
        mat[rank] = [(value * inv) % p for value in mat[rank]]
        for row in range(len(mat)):
            if row == rank or mat[row][col] % p == 0:
                continue
            factor = mat[row][col] % p
            mat[row] = [
                (value - factor * pivot_value) % p
                for value, pivot_value in zip(mat[row], mat[rank])
            ]
        rank += 1
        if rank == len(mat):
            break
    return rank


def expected_rank(a_count: int, b_count: int, h_order: int) -> int:
    return min(a_count * b_count, a_count + h_order * (b_count - 1))


def one_factor_rows(
    a_count: int, b_count: int, h_order: int, alpha: int, beta: int, p: int
) -> list[list[int]]:
    rows = []
    for b_exp in range(b_count):
        left = poly_pow_linear(alpha, h_order * b_exp, p)
        right = poly_pow_linear(beta, h_order * (b_count - 1 - b_exp), p)
        base = poly_mul(left, right, p)
        for a_exp in range(a_count):
            rows.append(shifted_monomial(base, a_exp))
    return rows


def interval_union_rank(a_count: int, b_count: int, h_order: int) -> int:
    degrees = set()
    for b_exp in range(b_count):
        degrees.update(range(h_order * b_exp, h_order * b_exp + a_count))
    return len(degrees)


def main() -> None:
    cases = [
        (5, 4, 32, 2, 3),
        (5, 4, 4, 2, 3),
        (5, 4, 3, 2, 3),
        (12, 5, 4, 5, 17),
        (9, 6, 9, 11, 29),
        (17, 7, 5, 13, 31),
    ]
    for a_count, b_count, h_order, alpha, beta in cases:
        if alpha == beta:
            raise AssertionError((alpha, beta))
        rank = rank_mod_p(
            one_factor_rows(a_count, b_count, h_order, alpha, beta, P),
            P,
        )
        expected = expected_rank(a_count, b_count, h_order)
        interval_rank = interval_union_rank(a_count, b_count, h_order)
        if rank != expected or interval_rank != expected:
            raise AssertionError(
                (a_count, b_count, h_order, rank, interval_rank, expected)
            )
        print(
            f"A={a_count} B={b_count} H={h_order}: "
            f"rank={rank} expected={expected}"
        )

    print("valuation interval formula: dim = min(A B, A + H(B-1))")
    print("H3_PRIVATE_LINEAR_ONE_FACTOR_RANK_PASS")


if __name__ == "__main__":
    main()
