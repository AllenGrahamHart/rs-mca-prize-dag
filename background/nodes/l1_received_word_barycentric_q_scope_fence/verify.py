#!/usr/bin/env python3
"""Finite-field replay of the received-word barycentric Q scope fence."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_received_word_barycentric_q_scope_fence"
PARENT = "l1_exact_shell_prefix_hankel_bridge"
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


def derivative_at(points: tuple[int, ...], x: int, p: int) -> int:
    out = 1
    for y in points:
        if y != x:
            out = out * (x - y) % p
    return out


def barycentric_moments(
    points: tuple[int, ...], values: dict[int, int], count: int, p: int
) -> tuple[int, ...]:
    return tuple(
        sum(
            values[x] * pow(x, j, p) * pow(derivative_at(points, x, p), -1, p)
            for x in points
        )
        % p
        for j in range(count)
    )


def coeff(poly: list[int], degree: int) -> int:
    return poly[degree] if degree < len(poly) else 0


def main() -> None:
    p = 7
    H = (0, 1, 2, 3, 5, 6)
    U = {x: pow(x, 4, p) for x in H}

    # Depth one: the barycentric scalar is exactly the top interpolant
    # coefficient on every triple.
    checked_depth_one = 0
    prefixes: dict[tuple[int, ...], int] = {}
    for A in itertools.combinations(H, 3):
        I = interpolate(A, [U[x] for x in A], p)
        prefix = coeff(I, 2)
        moments = barycentric_moments(A, U, 1, p)
        assert moments == (prefix,)
        e1 = sum(A) % p
        e2 = sum(x * y for x, y in itertools.combinations(A, 2)) % p
        assert prefix == (e1 * e1 - e2) % p
        prefixes[A] = prefix
        checked_depth_one += 1

    same_a = (0, 1, 2)
    same_b = (1, 3, 6)
    locator_a = locator(same_a, p)
    locator_b = locator(same_b, p)
    assert coeff(locator_a, 2) == coeff(locator_b, 2) == 4
    assert prefixes[same_a] == 0
    assert prefixes[same_b] == 3

    exchange = (
        prefixes[(0, 1, 2)]
        + prefixes[(0, 3, 5)]
        - prefixes[(0, 1, 3)]
        - prefixes[(0, 2, 5)]
    ) % p
    assert exchange == 4

    exact_poly = interpolate(same_a, [U[x] for x in same_a], p)
    assert exact_poly == [0, 1]
    exact_agreement = tuple(x for x in H if evaluate(exact_poly, x, p) == U[x])
    assert exact_agreement == same_a

    # Depth two: moment vanishing and the two high coefficients vanish
    # together. This exercises the triangular rather than coordinatewise form.
    U2 = {x: (pow(x, 5, p) + 2 * pow(x, 3, p) + x + 1) % p for x in H}
    checked_depth_two = 0
    non_coordinatewise = 0
    for A in itertools.combinations(H, 4):
        I = interpolate(A, [U2[x] for x in A], p)
        top = (coeff(I, 3), coeff(I, 2))
        moments = barycentric_moments(A, U2, 2, p)
        assert all(x == 0 for x in top) == all(x == 0 for x in moments)
        if top != moments:
            non_coordinatewise += 1
        checked_depth_two += 1
    assert non_coordinatewise > 0

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    print(
        "L1_RECEIVED_WORD_BARYCENTRIC_Q_SCOPE_FENCE_PASS "
        f"depth1={checked_depth_one} depth2={checked_depth_two} "
        f"triangular_nonidentity={non_coordinatewise} exchange={exchange}"
    )


if __name__ == "__main__":
    main()
