#!/usr/bin/env python3
"""Finite-field replay of the L1 cofactor-prefix Pade graph."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_cofactor_prefix_pade_graph_normal_form"
PARENT = "l1_exact_shell_fixed_cofactor_prefix_transport"
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


def scale(a: list[int], c: int, p: int) -> list[int]:
    return trim([(c * x) % p for x in a])


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


def prefix(poly: list[int], degree: int, depth: int) -> tuple[int, ...]:
    return tuple(poly[degree - t] for t in range(1, depth + 1))


def high_series(poly: list[int], degree: int, depth: int) -> list[int]:
    return [poly[degree - t] if degree - t < len(poly) else 0 for t in range(depth + 1)]


def series_div(num: list[int], den: list[int], depth: int, p: int) -> list[int]:
    assert den[0] % p
    out = [0] * (depth + 1)
    den0_inv = pow(den[0], -1, p)
    for t in range(depth + 1):
        carry = sum(den[i] * out[t - i] for i in range(1, min(t, len(den) - 1) + 1))
        out[t] = (num[t] - carry) * den0_inv % p
    return out


def graph(U: list[int], h: int, e: int, d: int, p: int):
    uhat = high_series(U, h, d)
    c = uhat[0]
    targets: dict[tuple[int, ...], tuple[int, ...]] = {}
    for tail in itertools.product(range(p), repeat=e):
        qhat = (c,) + tail
        lhat = series_div(uhat, list(qhat), d, p)
        target = tuple(lhat[1:])
        assert target not in targets
        recovered = tuple(series_div(uhat[: e + 1], list(lhat[: e + 1]), e, p))
        assert recovered == qhat
        assert all(value == 0 for value in series_div(uhat, lhat, d, p)[e + 1 :])
        targets[target] = qhat
    return targets


def run_case(p: int, n: int, k: int, a: int, e: int) -> tuple[int, int]:
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
    P0 = [((5 + i) % p) for i in range(k)]
    U = add(mul(L0, Q0, p), P0, p)
    h = len(U) - 1
    assert h == a + e
    w = a - k
    d = w + e
    assert d < a

    targets = graph(U, h, e, d, p)
    assert len(targets) == p**e
    assert len({target[:e] for target in targets}) == p**e

    expected: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()
    found: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()
    for A in itertools.combinations(H, a):
        L = locator(A, p)
        target = prefix(L, a, d)
        qhat = targets.get(target)
        if qhat is None:
            continue
        Q = tuple(reversed(qhat))
        P = add(U, neg(mul(L, list(Q), p), p), p)
        assert len(P) <= k
        outside = set(H) - set(A)
        if all(evaluate(list(Q), x, p) != 0 for x in outside):
            expected.add((tuple(L), Q))

        agreement = tuple(x for x in H if evaluate(P, x, p) == evaluate(U, x, p))
        if agreement == A:
            found.add((tuple(L), Q))

    assert found == expected
    assert (tuple(L0), tuple(Q0)) in found
    return len(targets), len(found)


def main() -> None:
    cases = (
        run_case(13, 6, 2, 4, 0),
        run_case(13, 6, 2, 3, 1),
        run_case(17, 8, 3, 4, 2),
    )

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    print(f"L1_COFACTOR_PREFIX_PADE_GRAPH_PASS cases={cases}")


if __name__ == "__main__":
    main()
