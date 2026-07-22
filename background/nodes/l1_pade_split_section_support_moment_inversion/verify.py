#!/usr/bin/env python3
"""Exact finite-field replay of Pade/support-moment inversion."""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_pade_split_section_support_moment_inversion"
PARENTS = (
    "l1_full_locator_pade_section_all_cofactors",
    "f5_lineray_saturation_instrument",
)
CONSUMER = "l1_mixed_petal_amplification"


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


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


def profile(U: list[int], H: tuple[int, ...], k: int, p: int) -> dict[int, int]:
    out = {a: 0 for a in range(len(H) + 1)}
    for coefficients in itertools.product(range(p), repeat=k):
        agreements = sum(evaluate(U, x, p) == evaluate(list(coefficients), x, p) for x in H)
        out[agreements] += 1
    return out


def support_count(U: list[int], H: tuple[int, ...], k: int, m: int, p: int) -> tuple[int, int]:
    valid = 0
    pade = 0
    codewords = [list(coefficients) for coefficients in itertools.product(range(p), repeat=k)]
    for support in itertools.combinations(H, m):
        explaining = [P for P in codewords if all(evaluate(U, x, p) == evaluate(P, x, p) for x in support)]
        assert len(explaining) <= 1
        valid += bool(explaining)
        L = locator(support, p)
        _, remainder = divmod_poly(U, L, p)
        pade += len(remainder) - 1 < k
        assert bool(explaining) == (len(remainder) - 1 < k)
    return valid, pade


def main() -> None:
    p = 7
    H = (0, 1, 2, 3, 4)
    n = len(H)
    k = 2
    received = (
        [1, 3, 2, 4, 1],
        [2, 1, 1, 0, 3],
        [5, 0, 6, 2],
    )
    checks = 0
    for U in received:
        z = profile(U, H, k, p)
        moments: dict[int, int] = {}
        for m in range(k, n + 1):
            census, pade = support_count(U, H, k, m, p)
            expected = sum(math.comb(a, m) * z[a] for a in range(m, n + 1))
            assert census == pade == expected
            moments[m] = census
            assert z[m] <= census
        for a in range(k, n + 1):
            inverted = sum((-1) ** (m - a) * math.comb(m, a) * moments[m] for m in range(a, n + 1))
            assert inverted == z[a]
            checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for parent in PARENTS:
        assert (parent, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    print(f"L1_PADE_SPLIT_SECTION_SUPPORT_MOMENT_PASS checks={checks}")


if __name__ == "__main__":
    main()
