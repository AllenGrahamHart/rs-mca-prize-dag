#!/usr/bin/env python3
"""Verify full-external-zero canonicalization on a small RS domain."""

import json
from itertools import combinations, product
from pathlib import Path

P = 7
D = tuple(range(6))
K = 3
A = 4
H = A - K
Z_SLOPE = 3


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
    quotient = [0] * max(1, len(numerator) - len(denominator) + 1)
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
strict_enlargements = 0
for t_size in range(2, len(D)):
    for t_tuple in combinations(range(len(D)), t_size):
        t_set = set(t_tuple)
        outside_t = set(range(len(D))) - t_set
        for support in combinations(range(len(D)), A):
            support_set = set(support)
            witness_external = support_set - t_set
            witness_internal = support_set & t_set
            for coefficients in product(range(P), repeat=K):
                q = trim(coefficients)
                if q == (0,):
                    continue
                if any(evaluate(q, D[index]) for index in witness_external):
                    continue
                full_external = {
                    index for index in outside_t if evaluate(q, D[index]) == 0
                }
                d = len(full_external)
                if d >= K:
                    continue
                locator = (1,)
                for index in sorted(full_external):
                    locator = multiply(locator, ((-D[index]) % P, 1))
                g = divide_exact(q, locator)
                assert g is not None and len(g) - 1 < K - d

                e1 = {index: (D[index] ** 2 + 1) % P for index in t_set}
                e0 = {
                    index: (evaluate(q, D[index]) - Z_SLOPE * e1[index]) % P
                    if index in witness_internal
                    else (D[index] + 2) % P
                    for index in t_set
                }
                internal_agreement = []
                for index in t_set:
                    scale = pow(evaluate(locator, D[index]), P - 2, P)
                    target = (e0[index] + Z_SLOPE * e1[index]) * scale % P
                    if evaluate(g, D[index]) == target:
                        internal_agreement.append(index)
                assert len(internal_agreement) >= A - d
                assert (A - d) - (K - d) == H
                if full_external > witness_external:
                    strict_enlargements += 1
                checks += 1

assert checks > 0 and strict_enlargements > 0

root = Path(__file__).resolve().parents[3]
dag = json.loads((root / "dag.json").read_text())
nodes = {node["id"]: node for node in dag["nodes"]}
assert nodes["xr_tangent_mismatch_full_external_zero_canonicalization"]["status"] == "PROVED"
assert {
    (edge["from"], edge["to"], edge["kind"])
    for edge in dag["edges"]
} >= {
    (
        "xr_tangent_mismatch_full_external_zero_canonicalization",
        "xr_tangent_support_mismatch_bridge",
        "ev",
    ),
}

print(
    "XR_TANGENT_MISMATCH_FULL_EXTERNAL_ZERO_PASS",
    checks,
    strict_enlargements,
)
