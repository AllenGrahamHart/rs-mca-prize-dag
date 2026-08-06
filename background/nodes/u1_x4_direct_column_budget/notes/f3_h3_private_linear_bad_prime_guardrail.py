#!/usr/bin/env python3
"""Private-linear p-specific rank-drop guardrail for h=3."""

from __future__ import annotations

from itertools import product


A = 1
B = 5
H = 9
PARAMS = ((2, 3), (5, 7), (11, 13))
PRIMES = (1009, 1013, 1019, 1231, 2027, 5003, 10007, 65537)
EXPECTED_RANKS = {
    1009: 108,
    1013: 109,
    1019: 109,
    1231: 109,
    2027: 109,
    5003: 109,
    10007: 109,
    65537: 109,
}


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


def rank_mod_p(rows: list[list[int]], p: int) -> int:
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
        if rank == width:
            break
    return rank


def rows_mod_p(p: int) -> list[list[int]]:
    cache: dict[tuple[int, int], list[int]] = {}
    rows = []
    for b_exponents in product(range(B), repeat=3):
        base = [1]
        for b_exp, (alpha, beta) in zip(b_exponents, PARAMS):
            for root, exponent in (
                (alpha, H * b_exp),
                (beta, H * (B - 1 - b_exp)),
            ):
                key = (root, exponent)
                if key not in cache:
                    cache[key] = poly_pow_linear(root, exponent, p)
                base = poly_mul(base, cache[key], p)
        rows.append(base)
    return rows


def main() -> None:
    degree_space_dim = A + 3 * H * (B - 1)
    coeff_box = A * B**3
    if degree_space_dim != 109 or coeff_box != 125:
        raise AssertionError((degree_space_dim, coeff_box))

    ranks = {p: rank_mod_p(rows_mod_p(p), p) for p in PRIMES}
    if ranks != EXPECTED_RANKS:
        raise AssertionError((ranks, EXPECTED_RANKS))
    if max(ranks.values()) != degree_space_dim:
        raise AssertionError((ranks, degree_space_dim))

    print("h=3 private-linear p-specific rank-drop guardrail")
    print(f"A={A} B={B} H={H} degree_space_dim={degree_space_dim}")
    for p in PRIMES:
        print(f"p={p}: rank={ranks[p]}")
    print("rank 109 modulo 1013 proves rational degree-space fullness")
    print("rank 108 modulo 1009 shows a p-specific rank drop")
    print("H3_PRIVATE_LINEAR_BAD_PRIME_GUARDRAIL_PASS")


if __name__ == "__main__":
    main()
