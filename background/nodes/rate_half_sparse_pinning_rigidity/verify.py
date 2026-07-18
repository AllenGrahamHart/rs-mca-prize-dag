#!/usr/bin/env python3
"""Tiny exhaustive replay of sparse pinning and match rigidity."""

from __future__ import annotations

import json
from collections import defaultdict
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def evaluate(poly: tuple[int, ...], x: int, prime: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % prime
    return value


def degree(poly: tuple[int, ...]) -> int:
    for index in range(len(poly) - 1, -1, -1):
        if poly[index]:
            return index
    return -1


def replay() -> tuple[int, int]:
    prime, n, k, a = 5, 4, 1, 2
    tau, r, m = a - k, n - a, n - k
    domain = tuple(range(n))
    polys = tuple(product(range(prime), repeat=k))
    code = tuple(tuple(evaluate(poly, x, prime) for x in domain) for poly in polys)
    words = tuple(product(range(prime), repeat=n))
    checked_bad = 0
    checked_nontangent = 0

    for first in words:
        for second in words:
            support = tuple(i for i in range(n) if first[i] or second[i])
            e = len(support)
            if e > r:
                continue
            active = tuple(i for i in support if second[i])
            A = len(active)
            slopes_by_poly: dict[int, set[int]] = defaultdict(set)

            for gamma in range(prime):
                line = tuple((x + gamma * y) % prime for x, y in zip(first, second, strict=True))
                tangent = any(line[i] == 0 for i in support)
                failing: list[tuple[int, tuple[int, ...]]] = []

                for z_index, z in enumerate(code):
                    matches = tuple(i for i in range(n) if line[i] == z[i])
                    if len(matches) < a:
                        continue
                    first_extends = any(all(first[i] == c[i] for i in matches) for c in code)
                    second_extends = any(all(second[i] == c[i] for i in matches) for c in code)
                    if not (first_extends and second_extends):
                        failing.append((z_index, matches))

                if not failing:
                    continue
                checked_bad += 1
                if not active:
                    raise AssertionError("epsilon_2=0 produced a bad slope")
                if e <= tau:
                    assert tangent
                if tangent:
                    continue

                checked_nontangent += 1
                z_index, matches = failing[0]
                poly, z = polys[z_index], code[z_index]
                assert degree(poly) >= 0
                matched_active = tuple(i for i in active if i in matches)
                assert matched_active
                assert any(
                    gamma == (z[i] - first[i]) * pow(second[i], -1, prime) % prime
                    for i in matched_active
                )

                inactive = tuple(i for i in support if i not in active)
                T = len(matched_active)
                u = sum(i not in matches for i in inactive)
                outside = tuple(i for i in domain if i not in support)
                w_out = sum(z[i] != 0 for i in outside)
                roots = sum(z[i] == 0 for i in outside)
                assert (A - T) + u + w_out <= r
                assert roots >= a - e
                assert degree(poly) - roots <= e - tau - 1
                assert T >= A - e + tau + 1 + u
                slopes_by_poly[z_index].add(gamma)

            for slopes in slopes_by_poly.values():
                assert len(slopes) <= A

    assert checked_bad > 0
    assert checked_nontangent > 0
    assert m == n - k and r == m - tau
    return checked_bad, checked_nontangent


def official_tangent_budget() -> None:
    n, k = 1 << 41, 1 << 40
    tau = 1
    r = n - (k + tau)
    q = 1 << 168
    assert r == (1 << 40) - 1
    assert r <= q // (1 << 128)

    for q_bits in (129, 160, 166, 167, 168, 256):
        budget = 1 << (q_bits - 128)
        radius = min((n - k) // 2, budget)
        excess = (n - k) - radius
        assert radius <= excess
        assert radius <= budget
    assert min((n - k) // 2, 1 << (167 - 128)) == 1 << 39


def main() -> None:
    bad, nontangent = replay()
    official_tangent_budget()

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_sparse_pinning_rigidity"]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (
        "rate_half_sparse_pinning_rigidity",
        "rate_half_band_closure",
        "ev",
    ) in edges

    print(
        "RATE_HALF_SPARSE_PINNING_RIGIDITY_PASS "
        f"bad_witnesses={bad} nontangent={nontangent} tangent_bits=40"
    )


if __name__ == "__main__":
    main()
