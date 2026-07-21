#!/usr/bin/env python3
"""Exact checks for the c2 one-antipodal primary/torsion reducer."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NODE_ID = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_primary_torsion_reducer"
DEPENDENCIES = {
    "rate_half_list_budget_three_fiber_two_cycle_c2_normalized_gap_span_compiler",
    "rate_half_list_budget_three_fiber_two_cycle_c2_torsion_field_router",
}
CONSUMER = "rate_half_list_adjacent_crossing"


def coefficients(total: int, product: int, height: int, prime: int) -> list[int]:
    denominator = (1, -total, product - 1, total, -product)
    out = [1]
    for n in range(1, 2 * height + 1):
        value = sum(
            (4 * n - 3 * j) * denominator[j] * out[n - j]
            for j in range(1, min(4, n) + 1)
        )
        out.append(-value * pow(4 * n, -1, prime) % prime)
    return out


def sign_free_torsion(
    square_total: int,
    product: int,
    levels: int,
    prime: int,
    initial_shift: int = 2,
) -> tuple[int, int]:
    u = (square_total - initial_shift * product) % prime
    v = product * product % prime
    for _ in range(levels - 1):
        u = (u * u - 2 * v) % prime
        v = v * v % prime
    return u, v


def subgroup_generator(prime: int, order: int) -> int:
    return next(
        root
        for root in range(2, prime)
        if pow(root, order, prime) == 1 and pow(root, order // 2, prime) != 1
    )


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

    # At H=4 the two-antipodal pure quartet has E=1-z^4 and the primary gap.
    prime = 97
    pure = coefficients(0, 1, 4, prime)
    assert pure[6] == pure[7] == 0
    assert pure[8] != 0

    # Coefficient parity gives the sign-free F_H,G_H representation.
    total, product = 11, 7
    positive = coefficients(total, product, 5, prime)
    negative = coefficients(-total % prime, product, 5, prime)
    for index, value in enumerate(positive):
        assert negative[index] == ((-1) ** index) * value % prime
    assert positive[9] * pow(total, -1, prime) % prime == (
        negative[9] * pow(-total, -1, prime) % prime
    )

    # A genuine order-16 complementary pair satisfies the 3-update circuit.
    omega = subgroup_generator(prime, 16)
    c, d = omega, pow(omega, 3, prime)
    total = (c + d) % prime
    product = c * d % prime
    square_total = total * total % prime
    assert sign_free_torsion(square_total, product, 4, prime) == (2, 1)
    assert square_total != 0
    assert (square_total - 4 * product) % prime != 0
    assert ((1 + product) ** 2 - square_total) % prime != 0

    packet = coefficients(total, product, 3, prime)
    assert packet[4] != 0 or packet[5] != 0

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_ONE_ANTIPODAL_REDUCER_PASS "
        "primary_fixture=1 parity_checks=11 torsion_levels=4 wiring=3"
    )


if __name__ == "__main__":
    main()
