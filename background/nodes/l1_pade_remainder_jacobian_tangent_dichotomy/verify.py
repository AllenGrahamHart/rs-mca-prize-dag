#!/usr/bin/env python3
"""Exact matrix replay of the Pade-remainder Jacobian dichotomy."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_pade_remainder_jacobian_tangent_dichotomy"
PARENT = "l1_full_locator_pade_section_all_cofactors"
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


def neg(a: list[int], p: int) -> list[int]:
    return trim([(-x) % p for x in a])


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
        pivot = next((r for r in range(rank, len(rows)) if rows[r][column] % p), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, p)
        rows[rank] = [(value * inverse) % p for value in rows[rank]]
        for r in range(len(rows)):
            if r == rank:
                continue
            factor = rows[r][column] % p
            if factor:
                rows[r] = [(x - factor * y) % p for x, y in zip(rows[r], rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return rank


def multiplication_matrix(L: list[int], Q: list[int], p: int) -> list[list[int]]:
    a = len(L) - 1
    columns: list[list[int]] = []
    for j in range(a):
        D = [0] * j + [1]
        quotient, remainder = divmod_poly(mul(D, Q, p), L, p)
        delta_p = neg(remainder, p)
        delta_q = neg(quotient, p)
        identity = add(add(mul(D, Q, p), mul(L, delta_q, p), p), delta_p, p)
        assert identity == [0]
        columns.append(delta_p + [0] * (a - len(delta_p)))
    return [[columns[column][row] for column in range(a)] for row in range(a)]


def main() -> None:
    primitive_checks = []
    for p, n, a, k, roots, Q in (
        (13, 6, 4, 2, (1, 3, 4, 9), [2, 1]),
        (17, 8, 3, 2, (1, 2, 4), [3, 0, 2, 1, 1]),
    ):
        H = tuple(x for x in range(1, p) if pow(x, n, p) == 1)
        assert set(roots) <= set(H)
        L = locator(roots, p)
        assert len(gcd_poly(L, Q, p)) == 1
        matrix = multiplication_matrix(L, Q, p)
        full_rank = rank_mod(matrix, p)
        high_rank = rank_mod(matrix[k:a], p)
        assert full_rank == a
        assert high_rank == a - k
        primitive_checks.append((full_rank, high_rank))

    p = 17
    n = 8
    H = tuple(x for x in range(1, p) if pow(x, n, p) == 1)
    roots = H[:4]
    L = locator(roots, p)
    Q = locator(roots[:2], p)
    complement = set(H) - set(roots)
    assert all(evaluate(Q, x, p) != 0 for x in complement)
    tangent_gcd = gcd_poly(L, Q, p)
    assert len(tangent_gcd) - 1 == 2
    tangent_matrix = multiplication_matrix(L, Q, p)
    tangent_full_rank = rank_mod(tangent_matrix, p)
    tangent_high_rank = rank_mod(tangent_matrix[1:4], p)
    assert tangent_full_rank == 2
    assert tangent_high_rank < 3

    P = [5]
    U = add(mul(L, Q, p), P, p)
    agreement = tuple(x for x in H if evaluate(U, x, p) == evaluate(P, x, p))
    assert agreement == roots

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    print(
        "L1_PADE_REMAINDER_JACOBIAN_TANGENT_DICHOTOMY_PASS "
        f"primitive={primitive_checks} tangent={(tangent_full_rank, tangent_high_rank)}"
    )


if __name__ == "__main__":
    main()
