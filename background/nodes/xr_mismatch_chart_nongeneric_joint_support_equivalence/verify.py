#!/usr/bin/env python3
"""Verify the chart-nongenericity/joint-support equivalence."""

import json
from itertools import combinations, product
from pathlib import Path

P = 7
D = tuple(range(6))
T = (0, 1, 2, 3)
OUTSIDE = (4, 5)
K = 3
A = 4


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
for d in range(len(OUTSIDE) + 1):
    for zero_indices in combinations(OUTSIDE, d):
        locator = (1,)
        for index in zero_indices:
            locator = multiply(locator, ((-D[index]) % P, 1))
        k_prime = K - d
        a_prime = A - d
        assert k_prime >= 1 and a_prime <= len(T)
        max_errors = len(T) - a_prime
        for e_size in range(max_errors + 1):
            for error_set in combinations(T, e_size):
                agreement = tuple(index for index in T if index not in error_set)
                for g0 in product(range(P), repeat=k_prime):
                    for g1 in product(range(P), repeat=k_prime):
                        c0_prime = multiply(locator, g0)
                        c1_prime = multiply(locator, g1)
                        assert len(c0_prime) - 1 < K and len(c1_prime) - 1 < K

                        e0 = {
                            index: evaluate(c0_prime, D[index])
                            if index in agreement else (D[index] + 1) % P
                            for index in T
                        }
                        e1 = {
                            index: evaluate(c1_prime, D[index])
                            if index in agreement else (D[index] + 2) % P
                            for index in T
                        }
                        for index in agreement:
                            scale = pow(evaluate(locator, D[index]), P - 2, P)
                            assert e0[index] * scale % P == evaluate(g0, D[index])
                            assert e1[index] * scale % P == evaluate(g1, D[index])
                        for index in zero_indices:
                            assert evaluate(c0_prime, D[index]) == 0
                            assert evaluate(c1_prime, D[index]) == 0

                        recovered0 = divide_exact(c0_prime, locator)
                        recovered1 = divide_exact(c1_prime, locator)
                        assert recovered0 == trim(g0)
                        assert recovered1 == trim(g1)
                        assert len(zero_indices) + len(agreement) >= A
                        checks += 1

assert checks > 0

# Distinct degree-below-K codewords agree on at most K-1 domain points.
for coefficients in product(range(P), repeat=K):
    polynomial = trim(coefficients)
    if polynomial == (0,):
        continue
    assert sum(evaluate(polynomial, x) == 0 for x in D) <= K - 1

root = Path(__file__).resolve().parents[3]
dag = json.loads((root / "dag.json").read_text())
nodes = {node["id"]: node for node in dag["nodes"]}
assert nodes["xr_mismatch_chart_nongeneric_joint_support_equivalence"]["status"] == "PROVED"
assert {
    (edge["from"], edge["to"], edge["kind"])
    for edge in dag["edges"]
} >= {
    (
        "xr_mismatch_chart_nongeneric_joint_support_equivalence",
        "xr_tangent_support_mismatch_bridge",
        "ev",
    ),
}

print("XR_MISMATCH_CHART_NONGENERIC_EQUIVALENCE_PASS", checks)
