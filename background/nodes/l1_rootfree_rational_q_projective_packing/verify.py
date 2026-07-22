#!/usr/bin/env python3
"""Finite-field replay of the rational-Q projective cell and packing bound."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_rootfree_rational_q_projective_packing"
PARENT = "l1_boundary_q_planted_root_descent"
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


def scale(c: int, a: list[int], p: int) -> list[int]:
    return trim([(c * x) % p for x in a])


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
    p = 7
    Hprime = (1, 2, 3, 4, 5)
    nprime = len(Hprime)
    j = 2
    d = 1
    w = j - d
    OmegaPrime = locator(Hprime, p)

    # From the planted-root fixture: G=-(X-1)(X-2), W1=X.
    G = scale(-1, locator((1, 2), p), p)
    W1 = [0, 1]
    assert all(evaluate(W1, x, p) != 0 for x in Hprime)

    split_points: dict[tuple[int, int], tuple[int, ...]] = {}
    infinity_split = 0
    projective_parameters = [(1, b) for b in range(p)] + [(0, 1)]
    for a, b in projective_parameters:
        polynomial = add(scale(a, G, p), scale(b, W1, p), p)
        roots = tuple(x for x in Hprime if evaluate(polynomial, x, p) == 0)
        quotient, remainder = divmod_poly(OmegaPrime, polynomial, p)
        is_split = (
            len(polynomial) - 1 == j
            and remainder == [0]
            and len(quotient) - 1 == nprime - j
        )
        assert is_split == (len(roots) == j)
        if is_split:
            split_points[(a, b)] = roots
            if a == 0:
                infinity_split += 1
    assert split_points
    assert infinity_split == 0
    assert all(a == 1 for a, _ in split_points)

    root_sets = list(split_points.values())
    for i, left in enumerate(root_sets):
        for right in root_sets[i + 1 :]:
            assert len(set(left).intersection(right)) <= d - 1
    bound = math.comb(nprime, d) // math.comb(j, d)
    assert len(split_points) <= bound
    assert w == 1 and bound == 2

    # Product estimate (PC4), checked over an integer linear-density grid.
    product_checks = 0
    for N in range(8, 31):
        for J in range((N + 1) // 2, N + 1):
            for dimension in range(1, J // 2 + 1):
                ratio = math.comb(N, dimension) / math.comb(J, dimension)
                assert ratio <= (2 * N / J) ** dimension
                product_checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    print(
        "L1_ROOTFREE_RATIONAL_Q_PROJECTIVE_PACKING_PASS "
        f"split={len(split_points)} infinity={infinity_split} bound={bound} "
        f"product_checks={product_checks}"
    )


if __name__ == "__main__":
    main()
