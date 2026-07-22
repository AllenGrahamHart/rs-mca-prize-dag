#!/usr/bin/env python3
"""Finite-field replay of near-rational deletion and balanced necessity."""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_exact_shell_balanced_shifted_lattice_reduction"
PARENT = "l1_pade_split_section_support_moment_inversion"
CONSUMER = "l1_mixed_petal_amplification"


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * max(len(a), len(b))
    for i in range(len(out)):
        out[i] = ((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p
    return trim(out)


def sub(a: list[int], b: list[int], p: int) -> list[int]:
    return add(a, [(-x) % p for x in b], p)


def mul(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return trim(out)


def divmod_poly(num: list[int], den: list[int], p: int) -> tuple[list[int], list[int]]:
    rem = trim(num[:])
    quotient = [0] * max(1, len(rem) - len(den) + 1)
    while rem != [0] and len(rem) >= len(den):
        shift = len(rem) - len(den)
        coefficient = rem[-1] * pow(den[-1], -1, p) % p
        quotient[shift] = coefficient
        for i, value in enumerate(den):
            rem[i + shift] = (rem[i + shift] - coefficient * value) % p
        trim(rem)
    return trim(quotient), trim(rem)


def gcd_poly(a: list[int], b: list[int], p: int) -> list[int]:
    a = trim(a[:])
    b = trim(b[:])
    while b != [0]:
        _, remainder = divmod_poly(a, b, p)
        a, b = b, remainder
    inverse = pow(a[-1], -1, p)
    return [(coefficient * inverse) % p for coefficient in a]


def locator(points: tuple[int, ...], p: int) -> list[int]:
    out = [1]
    for x in points:
        out = mul(out, [(-x) % p, 1], p)
    return out


def evaluate(poly: list[int], x: int, p: int) -> int:
    out = 0
    for coefficient in reversed(poly):
        out = (out * x + coefficient) % p
    return out


def rank_mod(matrix: list[list[int]], p: int) -> int:
    rows = [row[:] for row in matrix]
    rank = 0
    columns = len(rows[0]) if rows else 0
    for column in range(columns):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][column] % p), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, p)
        rows[rank] = [(value * inverse) % p for value in rows[rank]]
        for i in range(len(rows)):
            if i == rank:
                continue
            factor = rows[i][column] % p
            if factor:
                rows[i] = [(x - factor * y) % p for x, y in zip(rows[i], rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return rank


def minimal_shifted_degree(U: list[int], H: tuple[int, ...], k: int, p: int) -> int:
    for d in range(len(H) + 1):
        columns = (d + 1) + (d + k)
        matrix = []
        for x in H:
            ux = evaluate(U, x, p)
            matrix.append(
                [ux * pow(x, j, p) % p for j in range(d + 1)]
                + [(-pow(x, j, p)) % p for j in range(d + k)]
            )
        if rank_mod(matrix, p) < columns:
            return d
    raise AssertionError("nonzero interpolation module not found")


def codeword_profile(U: list[int], H: tuple[int, ...], k: int, p: int) -> dict[int, int]:
    out = {a: 0 for a in range(len(H) + 1)}
    for coefficients in itertools.product(range(p), repeat=k):
        P = list(coefficients)
        agreement = sum(evaluate(U, x, p) == evaluate(P, x, p) for x in H)
        out[agreement] += 1
    return out


def support_census(U: list[int], H: tuple[int, ...], k: int, m: int, p: int) -> int:
    profile = codeword_profile(U, H, k, p)
    return sum(math.comb(a, m) * count for a, count in profile.items() if a >= m)


def exact_guard_count(U: list[int], H: tuple[int, ...], k: int, m: int, p: int) -> int:
    omega_poly = locator(H, p)
    count = 0
    for coefficients in itertools.product(range(p), repeat=k):
        P = list(coefficients)
        agreement = tuple(x for x in H if evaluate(U, x, p) == evaluate(P, x, p))
        if len(agreement) != m:
            continue
        L = locator(agreement, p)
        W, rem = divmod_poly(omega_poly, L, p)
        assert rem == [0]
        Q, rem = divmod_poly(sub(U, P, p), L, p)
        assert rem == [0]
        assert len(gcd_poly(Q, W, p)) == 1
        N = mul(W, P, p)
        assert max(len(W) - 1, (len(N) - 1) - (k - 1)) <= len(H) - m
        count += 1
    return count


def main() -> None:
    p = 7
    H = tuple(range(6))
    n = len(H)
    k = 2
    m = 3
    w = m - k
    omega = n - m
    assert 2 * m <= n + k - 1

    codeword = [2, 3]
    near_values = [evaluate(codeword, x, p) for x in H]
    near_values[-1] = (near_values[-1] + 1) % p
    # Interpolate by brute force in the monomial basis of degree below n.
    vandermonde = [[pow(x, j, p) for j in range(n)] for x in H]

    def solve_values(values: list[int]) -> list[int]:
        matrix = [row[:] + [value] for row, value in zip(vandermonde, values)]
        for column in range(n):
            pivot = next(i for i in range(column, n) if matrix[i][column] % p)
            matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
            inverse = pow(matrix[column][column], -1, p)
            matrix[column] = [(x * inverse) % p for x in matrix[column]]
            for i in range(n):
                if i != column and matrix[i][column]:
                    factor = matrix[i][column]
                    matrix[i] = [(x - factor * y) % p for x, y in zip(matrix[i], matrix[column])]
        return trim([matrix[i][-1] for i in range(n)])

    near_U = solve_values(near_values)
    near_d1 = minimal_shifted_degree(near_U, H, k, p)
    near_profile = codeword_profile(near_U, H, k, p)
    assert near_d1 == 1 <= w
    assert support_census(near_U, H, k, m, p) == math.comb(n - near_d1, m)
    assert near_profile[m] == 0
    assert exact_guard_count(near_U, H, k, m, p) == 0

    L = locator((0, 1, 2), p)
    Q = mul(locator((6,), p), locator((6,), p), p)
    balanced_P = [1, 4]
    balanced_U = add(mul(L, Q, p), balanced_P, p)
    balanced_d1 = minimal_shifted_degree(balanced_U, H, k, p)
    balanced_profile = codeword_profile(balanced_U, H, k, p)
    assert balanced_profile[m] > 0
    assert balanced_d1 >= w + 1
    assert balanced_d1 <= omega
    assert exact_guard_count(balanced_U, H, k, m, p) == balanced_profile[m]

    # The cap-space dimension follows directly from the interpolation system.
    columns = (omega + 1) + (omega + k)
    module_matrix = []
    for x in H:
        ux = evaluate(balanced_U, x, p)
        module_matrix.append(
            [ux * pow(x, j, p) % p for j in range(omega + 1)]
            + [(-pow(x, j, p)) % p for j in range(omega + k)]
        )
    assert columns - rank_mod(module_matrix, p) == omega - w + 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    print(
        "L1_EXACT_SHELL_BALANCED_LATTICE_PASS "
        f"near={(near_d1, support_census(near_U, H, k, m, p))} "
        f"balanced={(balanced_d1, balanced_profile[m])}"
    )


if __name__ == "__main__":
    main()
