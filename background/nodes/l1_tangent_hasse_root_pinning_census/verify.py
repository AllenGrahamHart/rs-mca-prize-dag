#!/usr/bin/env python3
"""Finite-field replay of tangent Hasse root pinning and rank loss."""

from __future__ import annotations

import itertools
import json
import math
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_tangent_hasse_root_pinning_census"
PARENT = "l1_pade_remainder_jacobian_tangent_dichotomy"
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


def hasse_one(poly: list[int], x: int, p: int) -> int:
    return sum(j * coefficient * pow(x, j - 1, p) for j, coefficient in enumerate(poly) if j) % p


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


def hermite_matrix(roots: tuple[int, ...], k: int, p: int) -> list[list[int]]:
    rows: list[list[int]] = []
    for x in roots:
        rows.append([pow(x, j, p) for j in range(k)])
        rows.append([0 if j == 0 else j * pow(x, j - 1, p) % p for j in range(k)])
    return rows


def multiplication_matrix(L: list[int], Q: list[int], p: int) -> list[list[int]]:
    a = len(L) - 1
    columns: list[list[int]] = []
    for j in range(a):
        _, remainder = divmod_poly(mul([0] * j + [1], Q, p), L, p)
        columns.append(remainder + [0] * (a - len(remainder)))
    return [[columns[column][row] for column in range(a)] for row in range(a)]


def check_hermite_fibers() -> int:
    checks = 0
    for p, roots, dimensions in (
        (2, (0, 1), (1, 2, 3, 4, 5)),
        (5, (0, 1, 2), (1, 2, 4, 6)),
        (7, (1, 2), (1, 3, 4)),
    ):
        r = len(roots)
        D = locator(roots, p)
        D2 = mul(D, D, p)
        for k in dimensions:
            matrix = hermite_matrix(roots, k, p)
            assert rank_mod(matrix, p) == min(k, 2 * r)
            seed = [(3 * j + 1) % p for j in range(k)]
            target = tuple(
                value
                for x in roots
                for value in (evaluate(seed, x, p), hasse_one(seed, x, p))
            )
            solutions = 0
            for coefficients in itertools.product(range(p), repeat=k):
                P = list(coefficients)
                image = tuple(
                    value
                    for x in roots
                    for value in (evaluate(P, x, p), hasse_one(P, x, p))
                )
                if image == target:
                    solutions += 1
                    _, remainder = divmod_poly(sub(P, seed, p), D2, p)
                    assert remainder == [0]
            assert solutions == p ** max(k - 2 * r, 0)
            checks += 1
    return checks


def check_exact_shell() -> tuple[int, int]:
    p = 7
    H = tuple(range(6))
    k = 2
    a = 3
    w = a - k
    planted_roots = (0, 1, 2)
    L = locator(planted_roots, p)
    Q = locator((0, 6), p)
    planted_P = [3, 2]
    U = add(mul(L, Q, p), planted_P, p)
    e = len(Q) - 1

    strata: Counter[tuple[int, ...]] = Counter()
    tangent_members = 0
    for coefficients in itertools.product(range(p), repeat=k):
        P = list(coefficients)
        agreement = tuple(x for x in H if evaluate(U, x, p) == evaluate(P, x, p))
        if len(agreement) != a:
            continue
        shell_locator = locator(agreement, p)
        shell_Q, remainder = divmod_poly(sub(U, P, p), shell_locator, p)
        assert remainder == [0]
        complement = set(H) - set(agreement)
        assert all(evaluate(shell_Q, x, p) != 0 for x in complement)
        T = gcd_poly(shell_locator, shell_Q, p)
        r = len(T) - 1
        if not r:
            continue
        tangent_members += 1
        assert r <= min(a, e)
        strata[tuple(T)] += 1
        T2 = mul(T, T, p)
        _, double_remainder = divmod_poly(sub(U, P, p), T2, p)
        assert double_remainder == [0]
        tangent_roots = tuple(x for x in H if evaluate(T, x, p) == 0)
        assert len(tangent_roots) == r
        for x in tangent_roots:
            assert evaluate(P, x, p) == evaluate(U, x, p)
            assert hasse_one(P, x, p) == hasse_one(U, x, p)

        matrix = multiplication_matrix(shell_locator, shell_Q, p)
        full_rank = rank_mod(matrix, p)
        high_rank = rank_mod(matrix[k:a], p)
        assert full_rank == a - r
        assert high_rank >= max(0, w - r)

    assert tangent_members > 0
    for D, count in strata.items():
        r = len(D) - 1
        assert count <= p ** max(k - 2 * r, 0)
    aggregate_bound = sum(math.comb(len(H), r) * p ** max(k - 2 * r, 0) for r in range(1, min(a, e) + 1))
    assert tangent_members <= aggregate_bound
    return tangent_members, len(strata)


def main() -> None:
    hermite_checks = check_hermite_fibers()
    tangent_members, strata = check_exact_shell()

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    print(
        "L1_TANGENT_HASSE_ROOT_PINNING_CENSUS_PASS "
        f"hermite_checks={hermite_checks} tangent_members={tangent_members} strata={strata}"
    )


if __name__ == "__main__":
    main()
