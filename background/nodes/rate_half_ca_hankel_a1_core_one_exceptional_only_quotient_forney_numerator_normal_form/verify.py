#!/usr/bin/env python3
"""Verify the quotient Forney-numerator identities on exact finite fixtures."""

from __future__ import annotations

import json
from pathlib import Path


P = 1009
R = 7
NODE = (
    "rate_half_ca_hankel_a1_core_one_exceptional_only_"
    "quotient_forney_numerator_normal_form"
)
DEPS = {
    "rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_distance_gap",
    "rate_half_ca_hankel_a1_core_one_exceptional_only_"
    "kernel_plane_transversality",
    "rate_half_ca_hankel_a1_core_one_exceptional_only_"
    "two_sided_resultant_saturation",
}


def inv(x: int) -> int:
    return pow(x % P, P - 2, P)


def product(values: list[int]) -> int:
    out = 1
    for value in values:
        out = out * value % P
    return out


def eval_poly(coeffs: list[int], x: int) -> int:
    out = 0
    for coeff in reversed(coeffs):
        out = (out * x + coeff) % P
    return out


def root_poly_value(roots: list[int], x: int) -> int:
    return product([(x - root) % P for root in roots])


def root_derivative(roots: list[int], x: int) -> int:
    return product([(x - root) % P for root in roots if root != x])


def fixture(h: int) -> None:
    roots_a = list(range(1, R))
    roots_t = list(range(20, 20 + h))
    roots_c = roots_a + roots_t
    degree_f = h - 3
    coeffs_f = [7 + 2 * i for i in range(degree_f + 1)]
    while any(eval_poly(coeffs_f, x) == 0 for x in roots_c):
        coeffs_f[0] += 1
    theta = coeffs_f[-1] % P

    weights = {
        x: eval_poly(coeffs_f, x) * inv(root_derivative(roots_c, x)) % P
        for x in roots_c
    }
    for degree in range(R + 1):
        assert sum(weights[x] * pow(x, degree, P) for x in roots_c) % P == 0
    terminal = sum(weights[x] * pow(x, R + 1, P) for x in roots_c) % P
    assert terminal == theta != 0

    omega = {
        t: weights[t] * inv(root_poly_value(roots_a, t)) % P for t in roots_t
    }
    for t in roots_t:
        denominator = (
            pow(root_poly_value(roots_a, t), 2, P)
            * root_derivative(roots_t, t)
        ) % P
        assert omega[t] == eval_poly(coeffs_f, t) * inv(denominator) % P
        assert eval_poly(coeffs_f, t) != 0

    for a in roots_a:
        q1_at_a = weights[a]
        assert q1_at_a != 0
        rhs = (
            q1_at_a
            * root_derivative(roots_a, a)
            * root_poly_value(roots_t, a)
        ) % P
        assert eval_poly(coeffs_f, a) == rhs
        assert eval_poly(coeffs_f, a) != 0

    theta_from_t = sum(
        omega[t]
        * pow(root_poly_value(roots_a, t), 2, P)
        * pow(t, 2, P)
        for t in roots_t
    ) % P
    assert theta_from_t == theta

    mutated = dict(weights)
    mutated[roots_t[0]] = (mutated[roots_t[0]] + 1) % P
    assert sum(mutated[x] for x in roots_c) % P != 0


def main() -> None:
    for h in (3, 4, 6):
        fixture(h)

    root = Path(__file__).resolve().parents[3]
    dag = json.loads((root / "dag.json").read_text())
    node = next(item for item in dag["nodes"] if item["id"] == NODE)
    assert node["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    for dep in DEPS:
        assert (dep, NODE, "req") in edges
    assert (NODE, "rate_half_band_closure", "ev") in edges

    print("RATE_HALF_QUOTIENT_FORNEY_NUMERATOR_PASS fixtures=3 mutations=3")


if __name__ == "__main__":
    main()
