#!/usr/bin/env python3
"""Exact locator-factor and official boundary checks for the compiler."""

from math import comb
import json
from pathlib import Path


P = 17


def trim(poly):
    out = [x % P for x in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def add(left, right, scale=1):
    out = [0] * max(len(left), len(right))
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += scale * value
    return trim(out)


def mul(left, right):
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(out)


def evaluate(poly, x):
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % P
    return value


def interpolate(points, values):
    result = [0]
    for i, x_i in enumerate(points):
        basis = [1]
        denominator = 1
        for j, x_j in enumerate(points):
            if i == j:
                continue
            basis = mul(basis, [(-x_j) % P, 1])
            denominator = denominator * (x_i - x_j) % P
        coefficient = values[i] * pow(denominator, -1, P) % P
        result = add(result, basis, coefficient)
    return trim(result)


checks = 0
D = list(range(8))
u = [(x**3 + 2 * x + 1) % P for x in D]
v = [(x**4 + 3 * x * x + 4) % P for x in D]

for K, X, Y in ((3, (0, 1), (2, 3)), (3, (0,), (1,))):
    t = len(X)
    K_prime = K - t
    locator = [1]
    for x in X:
        locator = mul(locator, [(-x) % P, 1])
    a_x = interpolate(X, [u[x] for x in X])
    b_x = interpolate(X, [v[x] for x in X])
    D0 = [x for x in D if x not in X and x not in Y]

    for z in range(P):
        q = [5] if K_prime == 1 else [5, 7]
        p_z = add(add(a_x, b_x, z), mul(locator, q))
        assert len(p_z) <= K
        for x in X:
            assert evaluate(p_z, x) == (u[x] + z * v[x]) % P
        for x in D0:
            inv_locator = pow(evaluate(locator, x), -1, P)
            u_prime = (u[x] - evaluate(a_x, x)) * inv_locator % P
            v_prime = (v[x] - evaluate(b_x, x)) * inv_locator % P
            original_error = (u[x] + z * v[x] - evaluate(p_z, x)) % P
            reduced_error = (u_prime + z * v_prime - evaluate(q, x)) % P
            assert original_error == evaluate(locator, x) * reduced_error % P
            checks += 1

    q0 = [2] if K_prime == 1 else [2, 6]
    q1 = [3] if K_prime == 1 else [3, 4]
    c0 = add(a_x, mul(locator, q0))
    c1 = add(b_x, mul(locator, q1))
    assert len(c0) <= K and len(c1) <= K
    for x in X:
        assert evaluate(c0, x) == u[x]
        assert evaluate(c1, x) == v[x]


for n, rate_den, scale in (
    (2**10, 4, 256),
    (2**10, 8, 256),
    (2**10, 16, 512),
    (2**41, 4, 256),
    (2**41, 8, 256),
    (2**41, 16, 512),
):
    K = n // rate_den
    h = n // scale + 1
    A = K + h
    R = n - A
    for K_prime in (1, 2):
        t = K - K_prime
        r_prime = R - t
        bound = comb(K_prime + 1 + r_prime, K_prime + 1)
        assert r_prime >= 0
        assert bound < n**3 < 8 * n**3
        checks += 1


root = Path(__file__).resolve().parents[3]
dag = json.loads((root / "dag.json").read_text())
nodes = {node["id"]: node for node in dag["nodes"]}
node_id = "xr_lowcore_oriented_difference_puncture_compiler"
assert nodes[node_id]["status"] == "PROVED"
edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
assert ("xr_lowcore_shift_pair_terminal_fiber_bound", node_id, "req") in edges
assert ("xr_all_lineray_affine_core_bound", node_id, "req") in edges
assert (node_id, "xr_lowcore_spread_heart", "ev") in edges

print("XR_LOWCORE_ORIENTED_DIFFERENCE_PUNCTURE_COMPILER_PASS", checks)
