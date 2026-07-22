#!/usr/bin/env python3
"""Exact finite-field replay of tangent-to-primitive shell descent."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_tangent_double_root_descent_to_primitive_shell"
PARENT = "l1_tangent_hasse_root_pinning_census"
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
    return [(coefficient * inverse) % p for coefficient in a]


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


def exact_shell_record(U: list[int], P: list[int], H: tuple[int, ...], a: int, p: int):
    agreement = tuple(x for x in H if evaluate(U, x, p) == evaluate(P, x, p))
    if len(agreement) != a:
        return None
    L = locator(agreement, p)
    Q, remainder = divmod_poly(sub(U, P, p), L, p)
    assert remainder == [0]
    complement = set(H) - set(agreement)
    assert all(evaluate(Q, x, p) != 0 for x in complement)
    return agreement, L, Q


def check_descent_fixture() -> tuple[int, int]:
    p = 7
    H = tuple(range(6))
    n = len(H)
    k = 4
    a = 5
    w = a - k
    D = locator((0,), p)
    r = 1
    D2 = mul(D, D, p)
    L0 = locator((1, 2, 3, 4), p)
    Q0 = locator((6,), p)
    planted_P = [1, 2, 3, 4]
    U = add(mul(mul(D, L0, p), mul(D, Q0, p), p), planted_P, p)
    e = 2

    _, P_D = divmod_poly(U, D2, p)
    W_D, remainder = divmod_poly(sub(U, P_D, p), D2, p)
    assert remainder == [0]
    H_prime = tuple(x for x in H if evaluate(D, x, p) != 0)
    k_prime = k - 2 * r
    a_prime = a - r

    original: dict[tuple[int, ...], tuple[int, ...]] = {}
    for coefficients in itertools.product(range(p), repeat=k):
        P = list(coefficients)
        record = exact_shell_record(U, P, H, a, p)
        if record is None:
            continue
        _, L, Q = record
        if gcd_poly(L, Q, p) != D:
            continue
        R, rem = divmod_poly(sub(P, P_D, p), D2, p)
        assert rem == [0] and len(R) - 1 < k_prime
        original[tuple(P)] = tuple(R)

    reduced: dict[tuple[int, ...], tuple[int, ...]] = {}
    for coefficients in itertools.product(range(p), repeat=k_prime):
        R = list(coefficients)
        record = exact_shell_record(W_D, R, H_prime, a_prime, p)
        if record is None:
            continue
        _, reduced_L, reduced_Q = record
        omega_prime = locator(H_prime, p)
        if len(gcd_poly(reduced_Q, omega_prime, p)) != 1:
            continue
        P = add(P_D, mul(D2, R, p), p)
        lifted = exact_shell_record(U, P, H, a, p)
        assert lifted is not None
        _, lifted_L, lifted_Q = lifted
        assert gcd_poly(lifted_L, lifted_Q, p) == D
        reduced[tuple(P)] = tuple(R)

    assert original == reduced
    assert tuple(planted_P) in original
    assert (n - r, k_prime, a_prime, e - r, a_prime - k_prime) == (5, 2, 4, 1, w + r)
    return len(original), len(reduced)


def check_rigid_fixture() -> int:
    p = 7
    H = tuple(range(6))
    k = 3
    a = 4
    D = locator((0, 1), p)
    r = 2
    assert 2 * r > k
    D2 = mul(D, D, p)
    L0 = locator((2, 3), p)
    Q0 = locator((6,), p)
    planted_P = [2, 4, 1]
    U = add(mul(mul(D, L0, p), mul(D, Q0, p), p), planted_P, p)

    congruent = []
    exact_owned = []
    for coefficients in itertools.product(range(p), repeat=k):
        P = list(coefficients)
        _, remainder = divmod_poly(sub(U, P, p), D2, p)
        if remainder == [0]:
            congruent.append(P)
        record = exact_shell_record(U, P, H, a, p)
        if record is not None and gcd_poly(record[1], record[2], p) == D:
            exact_owned.append(P)
    assert len(congruent) == 1
    assert len(exact_owned) <= 1
    assert congruent[0] == planted_P
    return len(exact_owned)


def main() -> None:
    original, reduced = check_descent_fixture()
    rigid = check_rigid_fixture()

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    print(
        "L1_TANGENT_DOUBLE_ROOT_DESCENT_PASS "
        f"original={original} reduced={reduced} rigid={rigid}"
    )


if __name__ == "__main__":
    main()
