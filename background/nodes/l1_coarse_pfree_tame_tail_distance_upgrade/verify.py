#!/usr/bin/env python3
"""Verify the coarse p-free tame-tail distance upgrade."""

from __future__ import annotations

import json
import math
from collections import defaultdict
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_coarse_pfree_tame_tail_distance_upgrade"


def trim(poly: list[int], prime: int) -> list[int]:
    out = [coefficient % prime for coefficient in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def multiply(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % prime
    return trim(out, prime)


def subtract(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * max(len(left), len(right))
    for i in range(len(out)):
        a = left[i] if i < len(left) else 0
        b = right[i] if i < len(right) else 0
        out[i] = (a - b) % prime
    return trim(out, prime)


def derivative(poly: list[int], prime: int) -> list[int]:
    if len(poly) == 1:
        return [0]
    return trim([i * poly[i] for i in range(1, len(poly))], prime)


def locator(points: tuple[int, ...], prime: int) -> list[int]:
    out = [1]
    for point in points:
        out = multiply(out, [-point, 1], prime)
    return out


def wronskian(
    first: tuple[int, ...], second: tuple[int, ...], prime: int
) -> list[int]:
    f = locator(first, prime)
    g = locator(second, prime)
    return subtract(
        multiply(derivative(f, prime), g, prime),
        multiply(f, derivative(g, prime), prime),
        prime,
    )


def main() -> None:
    checks = 0

    # Exhaust the lower-degree theorem on disjoint tails in small prime fields.
    for prime in (2, 3, 5, 7):
        universe = tuple(range(prime))
        for tail in range(1, prime):
            for first in combinations(universe, tail):
                remaining = tuple(point for point in universe if point not in first)
                for second in combinations(remaining, tail):
                    value = wronskian(first, second, prime)
                    assert value != [0]
                    assert len(value) - 1 >= tail - 1
                    checks += 2

    # Sharp tame fixture over F_5.
    fixture = wronskian((0, 1), (2, 4), 5)
    assert fixture == [2, 1]
    assert len(fixture) - 1 == 1
    checks += 2

    # Exhaust coarse p-free fibers and the upgraded packing endpoint.
    for prime in (2, 3, 5, 7):
        universe = tuple(range(prime))
        for size in range(1, prime + 1):
            subsets = tuple(combinations(universe, size))
            for depth in range(1, size + 1):
                exponents = tuple(j for j in range(1, depth + 1) if j % prime)
                fibers: dict[tuple[int, ...], list[tuple[int, ...]]] = defaultdict(list)
                for subset in subsets:
                    key = tuple(
                        sum(pow(point, exponent, prime) for point in subset) % prime
                        for exponent in exponents
                    )
                    fibers[key].append(subset)

                tau = max(
                    math.ceil((depth + 2) / 2),
                    min(depth + 1, prime),
                )
                packing_s = size - tau + 1
                cap = 1
                if 1 <= packing_s <= size:
                    cap = math.comb(prime, packing_s) // math.comb(size, packing_s)
                for fiber in fibers.values():
                    assert len(fiber) <= cap
                    checks += 1
                    for first, second in combinations(fiber, 2):
                        tail = len(set(first) - set(second))
                        assert tail >= tau
                        checks += 1

    # Official specialization uses only integer inequalities.
    n = 2**13
    p = 3583
    assert 24 * p > n
    for depth in (p, 2 * p - 2, 2 * p - 1):
        tau = max(math.ceil((depth + 2) / 2), min(depth + 1, p))
        assert tau >= p
        checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    supplier = "l1_coarse_pfree_wronskian_distance_packing"
    neighbor = "l1_coarse_pfree_wronskian_neighbor_compiler"
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[supplier]["status"] == "PROVED"
    assert (supplier, NODE, "req") in edges
    assert (NODE, neighbor, "req") in edges
    assert (NODE, "l1_mixed_petal_amplification", "ev") in edges
    checks += 5

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in (
        "deg W>=t-1",
        "max(ceil((d+2)/2), min(d+1,p))",
        "t>=p>n/24",
        "W=Z+2",
        "strict inequality is necessary",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_COARSE_PFREE_TAME_TAIL_DISTANCE_UPGRADE_PASS checks={checks}")


if __name__ == "__main__":
    main()
