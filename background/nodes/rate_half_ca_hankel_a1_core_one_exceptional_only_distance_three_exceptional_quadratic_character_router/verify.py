#!/usr/bin/env python3
"""Replay the exceptional quadratic-character gate on the F_17 packet."""

from __future__ import annotations

import json
from pathlib import Path


P = 17
N = 16
E = 1
CORE = 1
OMITTED = 14
ROOTS_A = (2, 5)
TRIPLE = (3, 13, 15)
NODE = (
    "rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_"
    "exceptional_quadratic_character_router"
)
DEPS = {
    "rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_"
    "matching_free_boundary_power_router",
    "rate_half_residual_prime_field_collapse",
}


def inv(value: int) -> int:
    return pow(value % P, P - 2, P)


def locator(roots: tuple[int, ...], x: int) -> int:
    out = 1
    for root in roots:
        out = out * (x - root) % P
    return out


def derivative_at(roots: tuple[int, ...], x: int) -> int:
    return locator(tuple(root for root in roots if root != x), x)


def p_x_derivative(x: int, omitted: int) -> int:
    return N * inv(x) * inv((x - CORE) * (x - omitted)) % P


def k_value(a: int, omitted: int) -> int:
    denominator = pow(locator(TRIPLE, a) * derivative_at(ROOTS_A, a), 4, P)
    return p_x_derivative(a, omitted) * inv(denominator) % P


def character(value: int) -> int:
    return pow(value % P, (P - 1) // 2, P)


def support_gate(omitted: int) -> int:
    value = -locator(ROOTS_A, 0) * locator(ROOTS_A, CORE) * locator(ROOTS_A, omitted)
    return value % P


def main() -> None:
    y_values = [pow(k_value(a, OMITTED), E, P) for a in ROOTS_A]
    assert y_values[0] == -y_values[1] % P

    product_k = k_value(ROOTS_A[0], OMITTED) * k_value(ROOTS_A[1], OMITTED) % P
    assert character(-product_k) == 1
    gate = support_gate(OMITTED)
    assert gate == 15
    assert character(gate) == 1

    derivative_product = 1
    for a in ROOTS_A:
        derivative_product = derivative_product * p_x_derivative(a, OMITTED) % P
    expected = (
        pow(N, 2 * E, P)
        * inv(locator(ROOTS_A, 0) * locator(ROOTS_A, CORE) * locator(ROOTS_A, OMITTED))
    ) % P
    assert derivative_product == expected

    mutated_y = [pow(k_value(a, 4), E, P) for a in ROOTS_A]
    assert mutated_y[0] != -mutated_y[1] % P
    mutated_gate = support_gate(4)
    assert mutated_gate == 12
    assert character(mutated_gate) == P - 1

    root = Path(__file__).resolve().parents[3]
    dag = json.loads((root / "dag.json").read_text())
    node = next(item for item in dag["nodes"] if item["id"] == NODE)
    assert node["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    for dep in DEPS:
        assert (dep, NODE, "req") in edges
    assert (NODE, "rate_half_band_closure", "ev") in edges

    print(
        "RATE_HALF_DISTANCE_THREE_EXCEPTIONAL_QUADRATIC_CHARACTER_PASS "
        f"gate={gate} mutation={mutated_gate} field={P}"
    )


if __name__ == "__main__":
    main()
