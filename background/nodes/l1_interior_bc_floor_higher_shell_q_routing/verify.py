#!/usr/bin/env python3
"""Exact replay of the interior BC floor's routing to higher-shell Q."""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_interior_bc_floor_higher_shell_q_routing"
PARENTS = {
    "l1_pade_split_section_support_moment_inversion",
    "l1_exact_shell_balanced_shifted_lattice_reduction",
}
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


def main() -> None:
    p = 11
    H = tuple(range(7))
    n = len(H)
    k = 2
    m = 3
    w = m - k
    d1 = w + 2
    mprime = k - 1 + d1
    assert mprime == 4 and mprime + d1 <= n and mprime > m

    Omega = locator(H, p)
    fibers: dict[tuple[int, ...], list[tuple[tuple[int, ...], list[int]]]] = {}
    for support in itertools.combinations(H, mprime):
        L = locator(support, p)
        prefix = tuple(L[mprime - j] for j in range(1, d1))
        fibers.setdefault(prefix, []).append((support, L))
    prefix, fiber = max(fibers.items(), key=lambda item: (len(item[1]), item[0]))
    assert fiber

    U = [0] * (mprime + 1)
    U[mprime] = 1
    for j, coefficient in enumerate(prefix, start=1):
        U[mprime - j] = coefficient

    deleted_supports = 0
    exact_higher = set()
    for support, L in fiber:
        codeword = sub(U, L, p)
        assert len(codeword) - 1 < k
        agreement = tuple(x for x in H if evaluate(U, x, p) == evaluate(codeword, x, p))
        assert agreement == support
        exact_higher.add(tuple(codeword))

        for subset in itertools.combinations(support, m):
            LT = locator(subset, p)
            Q, remainder = divmod_poly(L, LT, p)
            assert remainder == [0] and len(Q) - 1 == mprime - m
            W, remainder = divmod_poly(Omega, LT, p)
            assert remainder == [0]
            _, common_remainder = divmod_poly(W, Q, p)
            assert common_remainder == [0]  # gcd(Q,W) is nontrivial.
            deleted_supports += 1

    assert deleted_supports == len(fiber) * math.comb(mprime, m)
    assert len(exact_higher) == len(fiber)
    assert d1 == (mprime - k) + 1

    inversion = sum(
        (-1) ** (level - m) * math.comb(level, m) * math.comb(mprime, level)
        for level in range(m, mprime + 1)
    )
    assert inversion == 0

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for parent in PARENTS:
        assert (parent, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    print(
        "L1_INTERIOR_BC_FLOOR_HIGHER_SHELL_Q_ROUTING_PASS "
        f"fiber={len(fiber)} deleted={deleted_supports} higher={len(exact_higher)}"
    )


if __name__ == "__main__":
    main()
