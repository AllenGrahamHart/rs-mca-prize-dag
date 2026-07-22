#!/usr/bin/env python3
"""Replay gcd descent and the first high-cofactor sharpness family."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_decorated_shift_pair_gcd_descent_sharpness"
PARENT = "l1_growing_cofactor_decorated_shift_pair_compiler"
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


def gcd_poly(a: list[int], b: list[int], p: int) -> list[int]:
    a, b = trim(a[:]), trim(b[:])
    while b != [0]:
        _, rem = divmod_poly(a, b, p)
        a, b = b, rem
    return scale(a, pow(a[-1], -1, p), p)


def agreement(U: list[int], P: list[int], H: tuple[int, ...], p: int) -> tuple[int, ...]:
    return tuple(x for x in H if evaluate(U, x, p) == evaluate(P, x, p))


def gcd_descent_replay() -> int:
    p = 17
    roots_a = (0, 1, 2, 6)
    roots_b = (3, 4, 5, 7)
    common = (8,)
    H = roots_a + roots_b + common
    A, B, G = locator(roots_a, p), locator(roots_b, p), locator(common, p)
    D = G
    q1, q2 = [4, 1], [14, 1]
    r = [2, 14]
    Q1, Q2, R = mul(D, q1, p), mul(D, q2, p), mul(D, r, p)
    assert add(mul(A, q1, p), neg(mul(B, q2, p), p), p) == r
    assert add(mul(A, Q1, p), neg(mul(B, Q2, p), p), p) == R
    assert gcd_poly(Q1, Q2, p) == D
    assert gcd_poly(q1, q2, p) == [1]

    d, w, e, c = 4, 1, 2, 1
    assert len(R) - 1 <= d - w - 1
    assert len(r) - 1 <= d - (w + c) - 1
    assert e - c <= w + c
    assert all(evaluate(D, x, p) != 0 for x in roots_a + roots_b)
    assert evaluate(D, common[0], p) == 0

    U = mul(mul(G, A, p), Q1, p)
    P1 = [0]
    P2 = mul(G, R, p)
    assert len(U) - 1 == 7 < len(H)
    assert len(P1) - 1 < 4 and len(P2) - 1 < 4
    assert agreement(U, P1, H, p) == tuple(sorted(common + roots_a))
    assert agreement(U, P2, H, p) == tuple(sorted(common + roots_b))
    return 1


def sharpness_replay() -> int:
    p = 13
    H = (0, 1, 3, 4, 9, 12)
    roots_a, roots_b, common, neither = (3, 4), (9, 12), (1,), (0,)
    A, B, G = locator(roots_a, p), locator(roots_b, p), locator(common, p)
    valid = []
    for t in range(p):
        Q1 = [t, (4 * t + 2) % p, 1]
        Q2 = [(5 * t + 5) % p, (4 * t + 3) % p, 1]
        R = add(mul(A, Q1, p), neg(mul(B, Q2, p), p), p)
        assert R == [(5 * t + 6) % p]
        assert gcd_poly(Q1, Q2, p) == [1]
        if t in (0, 4, 12):
            continue
        assert R != [0]
        assert all(evaluate(Q1, x, p) != 0 for x in roots_b + neither)
        assert all(evaluate(Q2, x, p) != 0 for x in roots_a + neither)
        U = mul(mul(G, A, p), Q1, p)
        P1 = [0]
        P2 = mul(G, R, p)
        assert len(U) - 1 == 5 < len(H)
        assert len(P2) - 1 < 2
        assert agreement(U, P1, H, p) == tuple(sorted(common + roots_a))
        assert agreement(U, P2, H, p) == tuple(sorted(common + roots_b))
        valid.append(t)
    assert valid == [1, 2, 3, 5, 6, 7, 8, 9, 10, 11]
    return len(valid)


def main() -> None:
    descent = gcd_descent_replay()
    sharp = sharpness_replay()
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    print(
        "L1_DECORATED_SHIFT_PAIR_GCD_DESCENT_SHARPNESS_PASS "
        f"descent={descent} sharp_witnesses={sharp}"
    )


if __name__ == "__main__":
    main()
