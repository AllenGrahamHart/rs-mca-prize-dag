#!/usr/bin/env python3
"""Finite-field replay of the L1 decorated shift-pair compiler."""

from __future__ import annotations

import itertools
import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_growing_cofactor_decorated_shift_pair_compiler"
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


def divmod_poly(num: list[int], den: list[int], p: int) -> tuple[list[int], list[int]]:
    rem = trim(num[:])
    out = [0] * max(1, len(rem) - len(den) + 1)
    while rem != [0] and len(rem) >= len(den):
        shift = len(rem) - len(den)
        c = rem[-1] * pow(den[-1], -1, p) % p
        out[shift] = c
        for i, value in enumerate(den):
            rem[i + shift] = (rem[i + shift] - c * value) % p
        trim(rem)
    return trim(out), trim(rem)


def divide_exact(num: list[int], den: list[int], p: int) -> list[int]:
    quo, rem = divmod_poly(num, den, p)
    assert rem == [0]
    return quo


def gcd_poly(a: list[int], b: list[int], p: int) -> list[int]:
    a, b = trim(a[:]), trim(b[:])
    while b != [0]:
        _, rem = divmod_poly(a, b, p)
        a, b = b, rem
    return scale(a, pow(a[-1], -1, p), p)


def prefix(poly: list[int], degree: int, depth: int) -> tuple[int, ...]:
    return tuple(poly[degree - t] for t in range(1, depth + 1))


def exact_shell(U_poly: list[int], H: tuple[int, ...], k: int, a: int, p: int):
    U = {x: evaluate(U_poly, x, p) for x in H}
    rows = []
    for S in itertools.combinations(H, a):
        P = interpolate(S, [U[x] for x in S], p)
        if len(P) > k:
            continue
        if tuple(x for x in H if evaluate(P, x, p) == U[x]) != S:
            continue
        L = locator(S, p)
        Q = divide_exact(add(U_poly, neg(P, p), p), L, p)
        rows.append({"S": S, "P": P, "L": L, "Q": Q})
    return rows


def compile_pair(row1, row2, H: tuple[int, ...], k: int, a: int, p: int):
    s1, s2 = set(row1["S"]), set(row2["S"])
    common = tuple(x for x in H if x in s1 and x in s2)
    only1 = tuple(x for x in H if x in s1 and x not in s2)
    only2 = tuple(x for x in H if x in s2 and x not in s1)
    neither = tuple(x for x in H if x not in s1 and x not in s2)
    G = locator(common, p)
    A = locator(only1, p)
    B = locator(only2, p)
    N = locator(neither, p)
    g, d, w = len(common), len(only1), a - k
    R = add(mul(A, row1["Q"], p), neg(mul(B, row2["Q"], p), p), p)
    omega = locator(H, p)
    assert mul(mul(G, A, p), mul(B, N, p), p) == omega
    assert d == len(only2) and d >= w + 1 and g <= k - 1
    assert R != [0] and len(R) - 1 <= d - w - 1
    assert mul(G, R, p) == add(row2["P"], neg(row1["P"], p), p)
    assert all(evaluate(row1["Q"], x, p) != 0 for x in only2 + neither)
    assert all(evaluate(row2["Q"], x, p) != 0 for x in only1 + neither)
    D = gcd_poly(row1["Q"], row2["Q"], p)
    if len(D) > 1:
        assert divmod_poly(R, D, p)[1] == [0]
        assert all(evaluate(D, x, p) != 0 for x in only1 + only2 + neither)
    return A, B, R, D, d, w


def main() -> None:
    p = 13
    H = tuple(x for x in range(1, p) if pow(x, 6, p) == 1)
    k = 2
    a = 3
    w = a - k

    # Scalar cofactor: choose a colliding locator-prefix fiber.
    support_fibers: dict[tuple[int, ...], list[tuple[int, ...]]] = defaultdict(list)
    for S in itertools.combinations(H, a):
        L = locator(S, p)
        support_fibers[prefix(L, a, w)].append(S)
    scalar_supports = next(rows for rows in support_fibers.values() if len(rows) > 1)
    L0 = locator(scalar_supports[0], p)
    U0 = add(scale(L0, 3, p), [2, 5], p)
    rows0 = exact_shell(U0, H, k, a, p)
    assert len(rows0) == len(scalar_supports) >= 2
    scalar_records = 0
    for i, row1 in enumerate(rows0):
        for j, row2 in enumerate(rows0):
            if i == j:
                continue
            A, B, _, _, d, _ = compile_pair(row1, row2, H, k, a, p)
            assert row1["Q"] == row2["Q"] == [3]
            assert len(add(A, neg(B, p), p)) - 1 <= d - w - 1
            scalar_records += 1
    assert scalar_records == len(rows0) * (len(rows0) - 1)

    # Positive cofactor actual pair from the fixed-cofactor replay.
    source = (1, 3, 4)
    L1 = locator(source, p)
    U1 = add(mul([4, 3], L1, p), [1, 6], p)
    rows1 = exact_shell(U1, H, k, a, p)
    assert len(rows1) == 2
    decorated_records = 0
    first_A = first_B = None
    for i, row1 in enumerate(rows1):
        for j, row2 in enumerate(rows1):
            if i == j:
                continue
            A, B, _, D, _, _ = compile_pair(row1, row2, H, k, a, p)
            assert len(row1["Q"]) - 1 == w
            assert D == [1]
            if first_A is None:
                first_A, first_B = A, B
            decorated_records += 1
    assert decorated_records == len(rows1) * (len(rows1) - 1)

    # Exhaust the primitive decorations for one ordered support pair.
    assert first_A is not None and first_B is not None
    primitive = []
    d = len(first_A) - 1
    for c1, c2 in itertools.product(range(p), repeat=2):
        Q1, Q2 = [c1, U1[-1]], [c2, U1[-1]]
        R = add(mul(first_A, Q1, p), neg(mul(first_B, Q2, p), p), p)
        if R != [0] and len(R) - 1 <= d - w - 1 and gcd_poly(Q1, Q2, p) == [1]:
            primitive.append((tuple(Q1), tuple(Q2)))
    assert len(primitive) == 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    print(
        "L1_GROWING_COFACTOR_DECORATED_SHIFT_PAIR_COMPILER_PASS "
        f"scalar_records={scalar_records} decorated_records={decorated_records} "
        f"primitive_fixed_pair={len(primitive)}"
    )


if __name__ == "__main__":
    main()
