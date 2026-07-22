#!/usr/bin/env python3
"""Finite-field replay of the all-cofactor full-locator Pade section."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_full_locator_pade_section_all_cofactors"
PARENT = "l1_cofactor_prefix_pade_graph_normal_form"
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


def evaluate(poly: list[int], x: int, p: int) -> int:
    out = 0
    for coefficient in reversed(poly):
        out = (out * x + coefficient) % p
    return out


def locator(points: tuple[int, ...], p: int) -> list[int]:
    out = [1]
    for x in points:
        out = mul(out, [(-x) % p, 1], p)
    return out


def high_series(poly: list[int], degree: int, depth: int) -> list[int]:
    return [poly[degree - t] if 0 <= degree - t < len(poly) else 0 for t in range(depth + 1)]


def series_div(num: list[int], den: list[int], depth: int, p: int) -> list[int]:
    out = [0] * (depth + 1)
    for t in range(depth + 1):
        carry = sum(den[i] * out[t - i] for i in range(1, min(t, len(den) - 1) + 1))
        out[t] = (num[t] - carry) % p
    return out


def section_data(U: list[int], h: int, L: list[int], a: int, e: int, w: int, p: int):
    d = e + w
    uhat = high_series(U, h, d)
    lhat = high_series(L, a, a)
    quotient = series_div(uhat, lhat, d, p)
    in_section = all(value == 0 for value in quotient[e + 1 : e + w + 1])
    Q = list(reversed(quotient[: e + 1]))
    return in_section, Q


def run_case(p: int, n: int, k: int, a: int, e: int) -> tuple[int, int, int]:
    H = tuple(x for x in range(1, p) if pow(x, n, p) == 1)
    assert len(H) == n
    A0 = next(iter(itertools.combinations(H, a)))
    L0 = locator(A0, p)
    outside0 = set(H) - set(A0)
    Q0 = next(
        list(tail) + [2]
        for tail in itertools.product(range(p), repeat=e)
        if all(evaluate(list(tail) + [2], x, p) != 0 for x in outside0)
    )
    P0 = [((3 + i) % p) for i in range(k)]
    U = add(mul(L0, Q0, p), P0, p)
    h = len(U) - 1
    assert h == a + e < n
    w = a - k

    expected: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()
    found: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()
    split_section = 0
    for A in itertools.combinations(H, a):
        L = locator(A, p)
        in_section, Q = section_data(U, h, L, a, e, w, p)
        if not in_section:
            continue
        split_section += 1
        P = add(U, neg(mul(L, Q, p), p), p)
        assert len(P) <= k
        outside = set(H) - set(A)
        if all(evaluate(Q, x, p) != 0 for x in outside):
            expected.add((tuple(L), tuple(Q)))
        agreement = tuple(x for x in H if evaluate(P, x, p) == evaluate(U, x, p))
        if agreement == A:
            found.add((tuple(L), tuple(Q)))

    assert found == expected
    assert (tuple(L0), tuple(Q0)) in found

    ambient_section = 0
    for coefficients in itertools.product(range(p), repeat=a):
        lhat = [1] + list(coefficients)
        d = e + w
        quotient = series_div(high_series(U, h, d), lhat, d, p)
        if all(value == 0 for value in quotient[e + 1 : e + w + 1]):
            ambient_section += 1
    if e < k:
        assert ambient_section == p**k

    return ambient_section, split_section, len(found)


def main() -> None:
    cases = (
        run_case(7, 6, 2, 4, 0),
        run_case(7, 6, 2, 3, 1),
        run_case(7, 6, 2, 3, 2),
        run_case(17, 8, 2, 3, 3),
        run_case(17, 8, 2, 3, 4),
    )

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    print(f"L1_FULL_LOCATOR_PADE_SECTION_ALL_COFACTORS_PASS cases={cases}")


if __name__ == "__main__":
    main()
