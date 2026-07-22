#!/usr/bin/env python3
"""Exhaustive replay of the exact polynomial-led interior Q-curve split."""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_polynomial_led_interior_to_deeper_q_curve"
PARENT = "l1_interior_bc_floor_higher_shell_q_routing"
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


def sub(a: list[int], b: list[int], p: int) -> list[int]:
    return add(a, [(-x) % p for x in b], p)


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


def gcd_poly(a: list[int], b: list[int], p: int) -> list[int]:
    a = trim(a[:])
    b = trim(b[:])
    while b != [0]:
        _, remainder = divmod_poly(a, b, p)
        a, b = b, remainder
    inverse = pow(a[-1], -1, p)
    return [(inverse * x) % p for x in a]


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


def curve(z: tuple[int, ...], s: tuple[int, ...], e: int, w: int, p: int) -> tuple[tuple[int, ...], list[int]]:
    a = [1] + list(s)
    r = [1]
    for j in range(1, e + 1):
        value = z[j - 1]
        for ell in range(j):
            value -= r[ell] * a[j - ell]
        r.append(value % p)
    for j in range(e + 1, e + w + 1):
        value = z[j - 1]
        for ell in range(1, e + 1):
            value -= r[ell] * a[j - ell]
        a.append(value % p)
    R = list(reversed(r))
    return tuple(a[1:]), R


def find_fixture(p: int, H: tuple[int, ...], k: int, m: int, e: int) -> tuple[object, ...]:
    n = len(H)
    w = m - k
    assert 1 <= e <= k and m + e < n
    depth = w + e
    Omega = locator(H, p)
    locators = [(support, locator(support, p)) for support in itertools.combinations(H, m)]

    chosen = None
    for z in itertools.product(range(p), repeat=depth):
        U = [0] * (m + e + 1)
        U[m + e] = 1
        for j, coefficient in enumerate(z, start=1):
            U[m + e - j] = coefficient

        exact_direct = set()
        for coefficients in itertools.product(range(p), repeat=k):
            P = list(coefficients)
            agreement = tuple(x for x in H if evaluate(U, x, p) == evaluate(P, x, p))
            if len(agreement) == m:
                exact_direct.add(agreement)

        exact_curve = set()
        unguarded = 0
        deleted = 0
        used_prefixes = set()
        for s in itertools.product(range(p), repeat=e):
            theta, R = curve(z, s, e, w, p)
            assert theta[:e] == s
            assert theta not in used_prefixes
            used_prefixes.add(theta)
            for support, L in locators:
                prefix = tuple(L[m - j] for j in range(1, depth + 1))
                if prefix != theta:
                    continue
                unguarded += 1
                P = sub(U, mul(L, R, p), p)
                assert len(P) - 1 < k
                W, remainder = divmod_poly(Omega, L, p)
                assert remainder == [0]
                if len(gcd_poly(R, W, p)) == 1:
                    exact_curve.add(support)
                else:
                    deleted += 1
        assert exact_curve == exact_direct
        if exact_direct and deleted:
            chosen = (z, len(exact_direct), unguarded, deleted, len(used_prefixes))
            break
    assert chosen is not None
    z, exact, unguarded, deleted, slices = chosen
    assert slices == p**e

    average_term = math.comb(n, m) * p ** (-w)
    deeper_average_times_slices = p**e * math.comb(n, m) * p ** (-(w + e))
    assert abs(average_term - deeper_average_times_slices) < 1e-12
    return (e, z, exact, unguarded, deleted, slices)


def main() -> None:
    fixtures = [
        find_fixture(11, tuple(range(7)), 2, 3, 1),
        find_fixture(7, tuple(range(7)), 2, 3, 2),
    ]
    assert [fixture[0] for fixture in fixtures] == [1, 2]

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    print(
        "L1_POLYNOMIAL_LED_INTERIOR_TO_DEEPER_Q_CURVE_PASS "
        + " ".join(
            f"e={e}:z={z}:exact={exact}:unguarded={unguarded}:deleted={deleted}:slices={slices}"
            for e, z, exact, unguarded, deleted, slices in fixtures
        )
    )


if __name__ == "__main__":
    main()
