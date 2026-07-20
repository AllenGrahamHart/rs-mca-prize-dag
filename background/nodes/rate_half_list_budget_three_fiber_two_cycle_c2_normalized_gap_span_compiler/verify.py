#!/usr/bin/env python3
"""Exact small-field checks for the normalized c=2 gap-span compiler."""

from __future__ import annotations

import json
from pathlib import Path


PRIME = 97
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NODE_ID = "rate_half_list_budget_three_fiber_two_cycle_c2_normalized_gap_span_compiler"
DEPENDENCIES = {
    "rate_half_list_budget_three_maximal_field_degree_collapse",
    "rate_half_list_budget_three_fiber_two_cycle_boundary_transfer",
    "rate_half_list_budget_three_fiber_two_cycle_c2_normalized_pair_torsion_compiler",
}
CONSUMER = "rate_half_list_adjacent_crossing"


def poly_mul(left: list[int], right: list[int], limit: int | None = None) -> list[int]:
    size = len(left) + len(right) - 1
    if limit is not None:
        size = min(size, limit)
    out = [0] * size
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j >= size:
                break
            out[i + j] = (out[i + j] + a * b) % PRIME
    return out


def fourth_power(poly: list[int], limit: int) -> list[int]:
    square = poly_mul(poly, poly, limit)
    return poly_mul(square, square, limit)


def denominator_from_roots(roots: tuple[int, int, int, int]) -> list[int]:
    out = [1]
    for root in roots:
        out = poly_mul(out, [1, -root % PRIME])
    return out


def denominator_from_coordinates(t: int, total: int, product: int) -> list[int]:
    return [
        1,
        -(1 + t + total) % PRIME,
        (t + (1 + t) * total + product) % PRIME,
        -(t * total + (1 + t) * product) % PRIME,
        t * product % PRIME,
    ]


def fourth_root_coefficients(
    denominator: list[int], maximum: int, weight_shift: int = 3
) -> list[int]:
    coefficients = [1]
    for n in range(1, maximum + 1):
        value = sum(
            (4 * n - weight_shift * j)
            * denominator[j]
            * coefficients[n - j]
            for j in range(1, min(4, n) + 1)
        )
        coefficients.append(-value * pow(4 * n, -1, PRIME) % PRIME)
    return coefficients


def inverse_series(poly: list[int], length: int) -> list[int]:
    inverse = [pow(poly[0], -1, PRIME)]
    leading_inverse = inverse[0]
    for n in range(1, length):
        value = sum(
            poly[j] * inverse[n - j]
            for j in range(1, min(n, len(poly) - 1) + 1)
        )
        inverse.append(-leading_inverse * value % PRIME)
    return inverse


def primary_two_window_packet(
    denominator: list[int], height: int
) -> tuple[list[int], list[int], list[int], int, list[int], list[int]]:
    coefficients = fourth_root_coefficients(denominator, 4 * height)
    assert coefficients[2 * height - 2] == 0
    assert coefficients[2 * height - 1] == 0
    leading = coefficients[2 * height]
    assert leading != 0

    degree = 2 * height - 3
    truncation = coefficients[: degree + 1]
    a_fourth = fourth_power(coefficients, 3 * height)
    b_fourth = fourth_power(truncation, 3 * height)
    residual = [
        (a_fourth[index] - b_fourth[index]) % PRIME
        for index in range(3 * height)
    ]
    residual_bar = residual[2 * height : 3 * height]
    alpha = residual_bar[0]

    b_squared = poly_mul(truncation, truncation, height)
    normalized = [
        value * pow(alpha, -1, PRIME) % PRIME for value in residual_bar
    ]
    canonical_square = poly_mul(
        normalized, inverse_series(b_squared, height), height
    )

    low = coefficients[:height]
    high = coefficients[2 * height : 3 * height]
    window_square = [
        value * pow(leading, -1, PRIME) % PRIME
        for value in poly_mul(low, high, height)
    ]
    return coefficients, residual, residual_bar, leading, canonical_square, window_square


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
    height = 3
    roots = (1, 84, 67, 68)
    t = roots[1]
    total = (roots[2] + roots[3]) % PRIME
    product = roots[2] * roots[3] % PRIME
    denominator = denominator_from_coordinates(t, total, product)
    assert denominator == denominator_from_roots(roots)
    assert denominator == [1, 71, 13, 70, 39]

    coefficients, residual, residual_bar, leading, canonical, windows = (
        primary_two_window_packet(denominator, height)
    )
    assert coefficients[:10] == [1, 55, 66, 39, 0, 0, 38, 13, 8, 11]
    assert residual[: 2 * height] == [0] * (2 * height)
    assert residual_bar[0] == 4 * leading % PRIME
    assert canonical == windows == [1, 63, 11]

    inverse_t = pow(t, -1, PRIME)
    reversed_denominator = denominator_from_coordinates(
        inverse_t,
        total * inverse_t % PRIME,
        product * inverse_t * inverse_t % PRIME,
    )
    assert reversed_denominator == [
        coefficient * pow(t, -index, PRIME) % PRIME
        for index, coefficient in enumerate(denominator)
    ]

    product_check = poly_mul(
        denominator,
        fourth_power(coefficients, 3 * height),
        3 * height,
    )
    assert product_check == [1] + [0] * (3 * height - 1)

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_NORMALIZED_GAP_SPAN_PASS "
        "primary_fixture=1 recurrence_checks=9 two_window_checks=3 wiring=3"
    )


if __name__ == "__main__":
    main()
