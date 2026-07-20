#!/usr/bin/env python3
"""Exact checks for the c2 official torsion-field router."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NODE_ID = "rate_half_list_budget_three_fiber_two_cycle_c2_torsion_field_router"
DEPENDENCIES = {
    "rate_half_list_budget_three_maximal_field_degree_collapse",
    "rate_half_list_budget_three_fiber_two_cycle_c2_normalized_pair_torsion_compiler",
}
CONSUMER = "rate_half_list_adjacent_crossing"

PRIME = 31
NONSQUARE = 3
ZERO = (0, 0)
ONE = (1, 0)
TWO = (2, 0)


def add(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    return ((left[0] + right[0]) % PRIME, (left[1] + right[1]) % PRIME)


def neg(value: tuple[int, int]) -> tuple[int, int]:
    return (-value[0] % PRIME, -value[1] % PRIME)


def multiply(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    a, b = left
    c, d = right
    return (
        (a * c + NONSQUARE * b * d) % PRIME,
        (a * d + b * c) % PRIME,
    )


def power(value: tuple[int, int], exponent: int) -> tuple[int, int]:
    out = ONE
    while exponent:
        if exponent & 1:
            out = multiply(out, value)
        value = multiply(value, value)
        exponent >>= 1
    return out


def inverse(value: tuple[int, int]) -> tuple[int, int]:
    assert value != ZERO
    return power(value, PRIME * PRIME - 2)


def primitive_element() -> tuple[int, int]:
    order = PRIME * PRIME - 1
    for a in range(PRIME):
        for b in range(PRIME):
            candidate = (a, b)
            if candidate != ZERO and all(
                power(candidate, order // factor) != ONE for factor in (2, 3, 5)
            ):
                return candidate
    raise AssertionError("primitive element not found")


def poly_multiply(
    left: list[tuple[int, int]], right: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    out = [ZERO] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = add(out[i + j], multiply(a, b))
    return out


def denominator(roots: tuple[tuple[int, int], ...]) -> list[tuple[int, int]]:
    out = [ONE]
    for root in roots:
        out = poly_multiply(out, [ONE, neg(root)])
    return out


def torsion_recurrence(
    t: tuple[int, int],
    total: tuple[int, int],
    product: tuple[int, int],
    levels: int,
    recurrence_constant: int = 2,
) -> tuple[tuple[int, int], tuple[int, int], tuple[int, int]]:
    scalar = (recurrence_constant % PRIME, 0)
    for _ in range(levels):
        t = multiply(t, t)
        total = add(multiply(total, total), neg(multiply(scalar, product)))
        product = multiply(product, product)
    return t, total, product


def check_wiring() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    incoming = {
        edge["from"]
        for edge in dag["edges"]
        if edge["to"] == NODE_ID and edge.get("kind") == "req"
    }
    outgoing = {
        edge["to"]
        for edge in dag["edges"]
        if edge["from"] == NODE_ID and edge.get("kind") == "ev"
    }
    assert nodes[NODE_ID]["status"] == "PROVED"
    assert incoming == DEPENDENCIES
    assert CONSUMER in outgoing


def main() -> None:
    check_wiring()
    assert pow(NONSQUARE, (PRIME - 1) // 2, PRIME) == PRIME - 1

    generator = primitive_element()
    field_order = PRIME * PRIME - 1
    order = 16
    omega = power(generator, field_order // order)
    assert power(omega, order) == ONE
    assert power(omega, order // 2) != ONE

    roots = (ONE, omega, power(omega, 3), power(omega, 6))
    for exponent, root in zip((0, 1, 3, 6), roots):
        assert power(root, PRIME) == inverse(root)
        assert power(power(generator, field_order // (2 * order) * exponent), 2) == root

    t, c, d = roots[1:]
    total = add(c, d)
    product = multiply(c, d)
    assert torsion_recurrence(t, total, product, 4) == (ONE, TWO, ONE)

    e_poly = denominator(roots)
    leading = e_poly[4]
    reciprocal = [multiply(inverse(leading), e_poly[4 - j]) for j in range(5)]
    frobenius = [power(coefficient, PRIME) for coefficient in e_poly]
    assert frobenius == reciprocal

    # Prime-field analogue: 2*32 divides 193-1, so mu_32 consists of squares.
    prime = 193
    primitive = next(
        value
        for value in range(2, prime)
        if pow(value, 96, prime) != 1 and pow(value, 64, prime) != 1
    )
    omega_prime = pow(primitive, (prime - 1) // 32, prime)
    assert pow(omega_prime, 32, prime) == 1
    for exponent in (0, 1, 7, 12):
        root = pow(omega_prime, exponent, prime)
        square_root = pow(primitive, (prime - 1) // 64 * exponent, prime)
        assert square_root * square_root % prime == root
        assert pow(root, prime, prime) == root

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_TORSION_FIELD_ROUTER_PASS "
        "unitary_order=16 fixed_order=32 split_square=4 reciprocal_coefficients=5 wiring=3"
    )


if __name__ == "__main__":
    main()
