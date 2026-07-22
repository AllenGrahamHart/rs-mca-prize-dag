#!/usr/bin/env python3
"""Exact finite-field replay of the boundary-Q planted-root descent."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_boundary_q_planted_root_descent"
PARENT = "l1_boundary_shifted_lattice_affine_q_cell"
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
    return [(-x) % p for x in a]


def sub(a: list[int], b: list[int], p: int) -> list[int]:
    return add(a, neg(b, p), p)


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


def scalar_multiple(a: list[int], b: list[int], p: int) -> bool:
    a = trim(a[:])
    b = trim(b[:])
    if a == [0] or b == [0] or len(a) != len(b):
        return False
    scalar = a[-1] * pow(b[-1], -1, p) % p
    return a == [(scalar * x) % p for x in b]


def determinant(v1: tuple[list[int], list[int]], v2: tuple[list[int], list[int]], p: int) -> list[int]:
    return sub(mul(v1[0], v2[1], p), mul(v2[0], v1[1], p), p)


def main() -> None:
    p = 7
    H = tuple(range(6))
    n = len(H)
    k = 2
    m = 3
    w = m - k
    omega = n - m
    Omega = locator(H, p)

    # A genuine nonconstant boundary vector with one planted domain root.
    D = locator((0,), p)
    residual_received = locator((1, 2), p)
    W1 = D
    N1 = mul(D, residual_received, p)
    OmegaD, remainder = divmod_poly(Omega, D, p)
    assert remainder == [0]
    quotient, N2 = divmod_poly(OmegaD, residual_received, p)
    W2 = neg(quotient, p)
    g1 = (W1, N1)
    g2 = (W2, N2)
    assert max(len(W1) - 1, len(N1) - k) == w + 1
    assert max(len(W2) - 1, len(N2) - k) == omega
    assert determinant(g1, g2, p) == Omega

    values = tuple(
        0 if x == 0 else evaluate(residual_received, x, p)
        for x in H
    )
    for x in H:
        assert evaluate(N1, x, p) == evaluate(W1, x, p) * values[x] % p
        assert evaluate(N2, x, p) == evaluate(W2, x, p) * values[x] % p

    S = tuple(x for x in H if evaluate(W1, x, p) == 0)
    Hprime = tuple(x for x in H if x not in S)
    assert S == (0,)
    assert all(evaluate(W1, x, p) != 0 for x in Hprime)

    exact_by_agreement: dict[int, tuple[int, ...]] = {}
    exact_by_reduced_split: dict[int, tuple[int, ...]] = {}
    for coefficient in range(p):
        P = [0, coefficient]  # P=P_S+D*R, with R constant.
        agreement = tuple(x for x in H if evaluate(P, x, p) == values[x])
        reduced = sub(P, residual_received, p)
        reduced_roots = tuple(x for x in Hprime if evaluate(reduced, x, p) == 0)
        split = len(reduced_roots) == m - len(S)
        if len(agreement) == m:
            exact_by_agreement[coefficient] = agreement
            assert set(S).issubset(agreement)
            L = locator(agreement, p)
            Lbar, remainder = divmod_poly(L, D, p)
            assert remainder == [0] and scalar_multiple(reduced, Lbar, p)
            W, remainder = divmod_poly(Omega, L, p)
            assert remainder == [0]
            v = (W, mul(W, P, p))
            assert scalar_multiple(determinant(g1, v, p), Omega, p)
        if split:
            exact_by_reduced_split[coefficient] = S + reduced_roots
    assert exact_by_agreement == exact_by_reduced_split
    assert exact_by_agreement
    assert (m - len(S)) - (k - len(S)) == w

    # Two planted values determine a degree-below-two codeword uniquely.
    rigid = []
    for a, b in itertools.product(range(p), repeat=2):
        if a == 3 and (a + b) % p == 5:
            rigid.append((a, b))
    assert len(rigid) == 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    print(
        "L1_BOUNDARY_Q_PLANTED_ROOT_DESCENT_PASS "
        f"exact={len(exact_by_agreement)} planted={len(S)} residual_depth={w}"
    )


if __name__ == "__main__":
    main()
