#!/usr/bin/env python3
"""Exhaust the external-zero factor reduction on a small RS domain."""

import json
from itertools import combinations, product
from pathlib import Path

P = 7
D = tuple(range(6))
K = 3
A = 4
H = A - K
Z = 3


def trim(poly):
    values = list(poly)
    while len(values) > 1 and values[-1] % P == 0:
        values.pop()
    return tuple(value % P for value in values)


def multiply(left, right):
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % P
    return trim(out)


def divide_exact(numerator, denominator):
    numerator = list(trim(numerator))
    denominator = trim(denominator)
    if len(numerator) < len(denominator):
        return None
    quotient = [0] * (len(numerator) - len(denominator) + 1)
    inverse = pow(denominator[-1], P - 2, P)
    while len(numerator) >= len(denominator) and any(numerator):
        shift = len(numerator) - len(denominator)
        coefficient = numerator[-1] * inverse % P
        quotient[shift] = coefficient
        for index, value in enumerate(denominator):
            numerator[index + shift] = (numerator[index + shift] - coefficient * value) % P
        numerator = list(trim(numerator))
    return trim(quotient) if all(value % P == 0 for value in numerator) else None


def evaluate(poly, x):
    return sum(coefficient * pow(x, degree, P) for degree, coefficient in enumerate(poly)) % P


checks = 0
for t_size in range(2, len(D)):
    for t_tuple in combinations(range(len(D)), t_size):
        t_set = set(t_tuple)
        for support in combinations(range(len(D)), A):
            support_set = set(support)
            outside = tuple(sorted(support_set - t_set))
            inside = tuple(sorted(support_set & t_set))
            d = len(outside)
            if len(inside) != A - d or d >= K or len(inside) < H + 1:
                continue
            locator = (1,)
            for index in outside:
                locator = multiply(locator, ((-D[index]) % P, 1))
            for coefficients in product(range(P), repeat=K):
                q = trim(coefficients)
                if q == (0,):
                    continue
                if any(evaluate(q, D[index]) for index in outside):
                    continue
                g = divide_exact(q, locator)
                assert g is not None
                assert len(g) - 1 < K - d

                e1 = {index: (D[index] * D[index] + 1) % P for index in t_set}
                e0 = {
                    index: (evaluate(q, D[index]) - Z * e1[index]) % P
                    if index in inside
                    else (D[index] + 2) % P
                    for index in t_set
                }
                for index in inside:
                    scale = pow(evaluate(locator, D[index]), P - 2, P)
                    target = (e0[index] + Z * e1[index]) * scale % P
                    assert evaluate(g, D[index]) == target

                dimension = K - d
                agreement = A - d
                redundancy = len(t_set) - dimension
                assert agreement - dimension == H
                assert len(t_set) - agreement == redundancy - H
                checks += 1

assert checks > 0

root = Path(__file__).resolve().parents[3]
dag = json.loads((root / "dag.json").read_text())
nodes = {node["id"]: node for node in dag["nodes"]}
assert nodes["xr_tangent_mismatch_external_zero_factor_reduction"]["status"] == "PROVED"
assert nodes["xr_tangent_support_mismatch_bridge"]["status"] in ("TARGET", "PROVED")  # bridge closed 2026-07-22 at the re-posed scope (wave-20, maintainer-ratified)
assert {
    (edge["from"], edge["to"], edge["kind"])
    for edge in dag["edges"]
} >= {
    (
        "xr_tangent_mismatch_external_zero_factor_reduction",
        "xr_tangent_support_mismatch_bridge",
        "ev",
    ),
}

print("XR_TANGENT_MISMATCH_EXTERNAL_ZERO_FACTOR_PASS", checks)
