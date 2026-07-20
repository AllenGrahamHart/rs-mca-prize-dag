#!/usr/bin/env python3
"""Replay the matching-free boundary-power router on the F_17 fixture."""

from __future__ import annotations

import json
from pathlib import Path


P = 17
E = 1
N = 16
CORE = 1
OMITTED = 14
NODE = (
    "rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_"
    "matching_free_boundary_power_router"
)
DEP = (
    "rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_"
    "boundary_root_unity_router"
)


def inv(value: int) -> int:
    return pow(value % P, P - 2, P)


def locator(roots: tuple[int, ...], x: int) -> int:
    out = 1
    for root in roots:
        out = out * (x - root) % P
    return out


def derivative_at(roots: tuple[int, ...], x: int) -> int:
    return locator(tuple(root for root in roots if root != x), x)


def p_x_derivative(x: int, omitted: int = OMITTED) -> int:
    return N * inv(x) * inv((x - CORE) * (x - omitted)) % P


def value_poly(roots: list[int]) -> list[int]:
    coeffs = [1]
    for root in roots:
        nxt = [0] * (len(coeffs) + 1)
        for degree, coeff in enumerate(coeffs):
            nxt[degree] = (nxt[degree] - root * coeff) % P
            nxt[degree + 1] = (nxt[degree + 1] + coeff) % P
        coeffs = nxt
    return coeffs


def k_a(a: int, roots_a: tuple[int, ...], triple: tuple[int, ...], omitted: int) -> int:
    denominator = pow(locator(triple, a) * derivative_at(roots_a, a), 4, P)
    return p_x_derivative(a, omitted) * inv(denominator) % P


def k_b(t: int, roots_a: tuple[int, ...], triple: tuple[int, ...]) -> int:
    denominator = pow(locator(roots_a, t), 4, P) * derivative_at(triple, t) % P
    return p_x_derivative(t) * inv(denominator) % P


def main() -> None:
    roots_a = (2, 5)
    triple = (3, 13, 15)
    a, b = roots_a

    y_a = pow(k_a(a, roots_a, triple, OMITTED), E, P)
    y_b = pow(k_a(b, roots_a, triple, OMITTED), E, P)
    assert y_a == -y_b % P
    polynomial = value_poly([y_a, y_b])
    assert all(coeff == 0 for degree, coeff in enumerate(polynomial) if degree % 2)

    a_i_a = 1
    a_i_b = 1
    u_ab = locator(triple, a) * a_i_a * inv(locator(triple, b) * a_i_b) % P
    zeta = -p_x_derivative(a) * inv(p_x_derivative(b)) * inv(pow(u_ab, 4, P)) % P
    assert zeta == -k_a(a, roots_a, triple, OMITTED) * inv(
        k_a(b, roots_a, triple, OMITTED)
    ) % P
    assert (pow(zeta, E, P) == 1) == (y_a == -y_b % P)

    z_values = [pow(k_b(t, roots_a, triple), E, P) for t in triple]
    assert len(set(z_values)) == 1
    for index, t in enumerate(triple):
        for u in triple[index + 1 :]:
            eta = k_b(t, roots_a, triple) * inv(k_b(u, roots_a, triple)) % P
            assert (pow(eta, E, P) == 1) == (
                pow(k_b(t, roots_a, triple), E, P)
                == pow(k_b(u, roots_a, triple), E, P)
            )

    mutated = [
        pow(k_a(x, roots_a, triple, 4), E, P) for x in roots_a
    ]
    assert mutated[0] != -mutated[1] % P
    mutated_poly = value_poly(mutated)
    assert any(coeff != 0 for degree, coeff in enumerate(mutated_poly) if degree % 2)

    root = Path(__file__).resolve().parents[3]
    dag = json.loads((root / "dag.json").read_text())
    node = next(item for item in dag["nodes"] if item["id"] == NODE)
    assert node["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (DEP, NODE, "req") in edges
    assert (NODE, "rate_half_band_closure", "ev") in edges

    print(
        "RATE_HALF_DISTANCE_THREE_MATCHING_FREE_BOUNDARY_POWER_PASS "
        f"pair_values={(y_a, y_b)} triple_value={z_values[0]} mutation={mutated}"
    )


if __name__ == "__main__":
    main()
