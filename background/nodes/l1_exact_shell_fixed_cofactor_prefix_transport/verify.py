#!/usr/bin/env python3
"""Finite-field replay of fixed-cofactor locator-prefix transport."""

from __future__ import annotations

import itertools
import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_exact_shell_fixed_cofactor_prefix_transport"
PARENT = "l1_exact_shell_complement_toeplitz_normal_form"
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
    for c in reversed(poly):
        out = (out * x + c) % p
    return out


def locator(points: tuple[int, ...], p: int) -> list[int]:
    out = [1]
    for x in points:
        out = mul(out, [(-x) % p, 1], p)
    return out


def interpolate(points: tuple[int, ...], values: list[int], p: int) -> list[int]:
    out = [0]
    for i, x in enumerate(points):
        basis = [1]
        den = 1
        for j, y in enumerate(points):
            if i == j:
                continue
            basis = mul(basis, [(-y) % p, 1], p)
            den = den * (x - y) % p
        out = add(out, scale(basis, values[i] * pow(den, -1, p), p), p)
    return trim(out)


def divide_exact(num: list[int], den: list[int], p: int) -> list[int]:
    rem = trim(num[:])
    out = [0] * max(1, len(rem) - len(den) + 1)
    while rem != [0] and len(rem) >= len(den):
        shift = len(rem) - len(den)
        c = rem[-1] * pow(den[-1], -1, p) % p
        out[shift] = c
        for i, value in enumerate(den):
            rem[i + shift] = (rem[i + shift] - c * value) % p
        trim(rem)
    assert rem == [0]
    return trim(out)


def prefix(poly: list[int], degree: int, depth: int) -> tuple[int, ...]:
    return tuple(poly[degree - t] if degree - t < len(poly) else 0 for t in range(1, depth + 1))


def exact_shell(U_poly: list[int], H: tuple[int, ...], k: int, a: int, p: int):
    U = {x: evaluate(U_poly, x, p) for x in H}
    rows = []
    for A in itertools.combinations(H, a):
        P = interpolate(A, [U[x] for x in A], p)
        if len(P) > k:
            continue
        agreement = tuple(x for x in H if evaluate(P, x, p) == U[x])
        if agreement != A:
            continue
        L = locator(A, p)
        Q = divide_exact(add(U_poly, neg(P, p), p), L, p)
        rows.append((A, tuple(L), tuple(Q)))
    return rows


def all_prefix_fibers(H: tuple[int, ...], a: int, depth: int, p: int):
    fibers: dict[tuple[int, ...], set[tuple[int, ...]]] = defaultdict(set)
    for A in itertools.combinations(H, a):
        L = locator(A, p)
        fibers[prefix(L, a, depth)].add(tuple(L))
    return fibers


def main() -> None:
    p = 13
    n = 6
    k = 2
    H = tuple(x for x in range(1, p) if pow(x, n, p) == 1)
    assert len(H) == n

    # Scalar cofactor: the exact shell equals one complete locator-prefix fiber.
    a0 = 4
    A0 = next(iter(itertools.combinations(H, a0)))
    L0 = locator(A0, p)
    scalar = 3
    U0 = add(scale(L0, scalar, p), [2, 5], p)
    assert len(U0) - 1 == a0
    rows0 = exact_shell(U0, H, k, a0, p)
    w0 = a0 - k
    target0 = prefix(L0, a0, w0)
    expected0 = all_prefix_fibers(H, a0, w0, p)[target0]
    found0 = {L for _, L, Q in rows0 if Q == (scalar,)}
    assert found0 == expected0
    assert len(found0) > 0
    assert exact_shell(U0, H, k, a0 + 1, p) == []

    # Positive bounded cofactor: each fixed Q has one deeper prefix target.
    a1 = 3
    e1 = 1
    A1 = next(iter(itertools.combinations(H, a1)))
    L1 = locator(A1, p)
    Q1 = [4, 3]
    U1 = add(mul(Q1, L1, p), [1, 6], p)
    assert len(U1) - 1 == a1 + e1
    rows1 = exact_shell(U1, H, k, a1, p)
    depth1 = a1 - k + e1
    by_q1: dict[tuple[int, ...], list[tuple[int, ...]]] = defaultdict(list)
    for _, L, Q in rows1:
        assert len(Q) - 1 == e1
        assert Q[-1] == U1[-1]
        by_q1[Q].append(L)
    assert tuple(Q1) in by_q1
    for locators in by_q1.values():
        assert len({prefix(list(L), a1, depth1) for L in locators}) == 1
    max_fiber1 = max(len(v) for v in all_prefix_fibers(H, a1, depth1, p).values())
    assert len(rows1) <= p**e1 * max_fiber1
    assert exact_shell(U1, H, k, a1 + e1 + 1, p) == []

    # e >= k: every fixed cofactor determines the whole locator.
    a2 = 3
    e2 = 2
    A2 = next(iter(itertools.combinations(H, a2)))
    L2 = locator(A2, p)
    Q2 = [5, 4, 2]
    U2 = add(mul(Q2, L2, p), [3, 1], p)
    assert len(U2) - 1 == a2 + e2
    rows2 = exact_shell(U2, H, k, a2, p)
    by_q2: dict[tuple[int, ...], list[tuple[int, ...]]] = defaultdict(list)
    for _, L, Q in rows2:
        assert len(Q) - 1 == e2
        by_q2[Q].append(L)
    assert tuple(Q2) in by_q2
    assert all(len(set(locators)) == 1 for locators in by_q2.values())
    assert len(rows2) <= p**e2

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    print(
        "L1_EXACT_SHELL_FIXED_COFACTOR_PREFIX_TRANSPORT_PASS "
        f"scalar={len(rows0)} e1={len(rows1)} e2={len(rows2)} "
        f"qgroups={len(by_q1) + len(by_q2)}"
    )


if __name__ == "__main__":
    main()
