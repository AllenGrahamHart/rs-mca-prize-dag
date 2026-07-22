#!/usr/bin/env python3
"""Finite-field replay of the complement Toeplitz exact-shell normal form."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_exact_shell_complement_toeplitz_normal_form"
PARENT = "l1_received_word_barycentric_q_scope_fence"
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


def coeff(poly: list[int], degree: int) -> int:
    return poly[degree] if degree < len(poly) else 0


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
    inv_lead = pow(den[-1], -1, p)
    while rem != [0] and len(rem) >= len(den):
        shift = len(rem) - len(den)
        c = rem[-1] * inv_lead % p
        out[shift] = c
        for i, value in enumerate(den):
            rem[i + shift] = (rem[i + shift] - c * value) % p
        trim(rem)
    assert rem == [0]
    return trim(out)


def derivative_at(points: tuple[int, ...], x: int, p: int) -> int:
    out = 1
    for y in points:
        if y != x:
            out = out * (x - y) % p
    return out


def moments(A: tuple[int, ...], U: dict[int, int], w: int, p: int) -> tuple[int, ...]:
    return tuple(
        sum(
            U[x] * pow(x, j, p) * pow(derivative_at(A, x, p), -1, p)
            for x in A
        )
        % p
        for j in range(w)
    )


def run_coset(beta: int) -> tuple[int, int, int]:
    p = 13
    n = 6
    k = 2
    H = tuple(x for x in range(1, p) if pow(x, n, p) == beta)
    assert len(H) == n
    omega = locator(H, p)
    assert omega == [(-beta) % p] + [0] * (n - 1) + [1]

    words = (
        [0],
        [0, 0, 0, 0, 1],
        [3, 4, 1, 6, 2, 5],
    )
    checks = 0
    exact_total = 0
    shift_checks = 0
    for U_poly in words:
        U_poly = trim(U_poly[:])
        U = {x: evaluate(U_poly, x, p) for x in H}
        shifted_poly = add(U_poly, [5, 7], p)
        for a in (3, 4, 5):
            w = a - k
            r = n - a
            exact_divisors: set[tuple[int, ...]] = set()
            exact_supports: set[tuple[int, ...]] = set()
            for A in itertools.combinations(H, a):
                comp = tuple(x for x in H if x not in A)
                L = locator(A, p)
                M = locator(comp, p)
                assert mul(L, M, p) == omega
                assert len(M) - 1 == r

                I = interpolate(A, [U[x] for x in A], p)
                bary = moments(A, U, w, p)
                UM = mul(U_poly, M, p)
                extracted = tuple(coeff(UM, n - j - 1) for j in range(w))
                assert bary == extracted
                gap = tuple(coeff(UM, degree) for degree in range(n - w, n))
                assert (len(I) <= k) == all(value == 0 for value in gap)

                shifted_gap = tuple(
                    coeff(mul(shifted_poly, M, p), degree)
                    for degree in range(n - w, n)
                )
                assert shifted_gap == gap
                shift_checks += 1

                if all(value == 0 for value in gap):
                    Q = divide_exact(add(U_poly, neg(I, p), p), L, p)
                    guard = all(evaluate(Q, y, p) != 0 for y in comp)
                    agreement = tuple(x for x in H if evaluate(I, x, p) == U[x])
                    exact = agreement == A
                    assert guard == exact
                    if guard:
                        exact_divisors.add(tuple(M))
                        exact_supports.add(A)
                checks += 1
            assert len(exact_divisors) == len(exact_supports)
            exact_total += len(exact_supports)
    return checks, exact_total, shift_checks


def main() -> None:
    checks_1, exact_1, shifts_1 = run_coset(1)
    checks_2, exact_2, shifts_2 = run_coset(12)
    assert exact_1 + exact_2 > 0

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    print(
        "L1_EXACT_SHELL_COMPLEMENT_TOEPLITZ_NORMAL_FORM_PASS "
        f"checks={checks_1 + checks_2} exact={exact_1 + exact_2} "
        f"shift_checks={shifts_1 + shifts_2} cosets=2"
    )


if __name__ == "__main__":
    main()
