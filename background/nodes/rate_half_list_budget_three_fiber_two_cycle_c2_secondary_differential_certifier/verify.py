#!/usr/bin/env python3
"""Checks for the c2 secondary differential certifier."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NODE_ID = "rate_half_list_budget_three_fiber_two_cycle_c2_secondary_differential_certifier"
DEPENDENCY = "rate_half_list_budget_three_antipodal_generic_two_window_square_reduction"
CONSUMER = "rate_half_list_adjacent_crossing"


def add(prime: int, *terms: tuple[int, list[int]]) -> list[int]:
    out = [0] * max(len(poly) for _, poly in terms)
    for scale, poly in terms:
        for index, value in enumerate(poly):
            out[index] = (out[index] + scale * value) % prime
    return out


def multiply(prime: int, left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % prime
    return out


def derivative(prime: int, poly: list[int]) -> list[int]:
    return [index * poly[index] % prime for index in range(1, len(poly))]


def shift(poly: list[int]) -> list[int]:
    return [0] + poly


def coefficients(prime: int, height: int, e_poly: list[int]) -> list[int]:
    out = [1]
    for n in range(1, 3 * height):
        value = sum(
            (4 * n - 3 * j) * e_poly[j] * out[n - j]
            for j in range(1, min(4, n) + 1)
        )
        out.append(-value * pow(4 * n, -1, prime) % prime)
    return out


def residual(prime: int, e_poly: list[int], b_poly: list[int]) -> list[int]:
    return add(
        prime,
        (1, multiply(prime, derivative(prime, e_poly), b_poly)),
        (4, multiply(prime, e_poly, derivative(prime, b_poly))),
    )


def differential_phi(
    prime: int,
    height: int,
    e_poly: list[int],
    b_poly: list[int],
    c_poly: list[int],
    leading: int,
) -> list[int]:
    top = b_poly[-1]
    kappa = e_poly[4] * top * pow(leading, -1, prime) % prime
    c_squared = multiply(prime, c_poly, c_poly)
    c_c_prime = multiply(prime, c_poly, derivative(prime, c_poly))
    out = add(
        prime,
        (1, multiply(prime, shift(derivative(prime, e_poly)), c_squared)),
        (4 * height, multiply(prime, e_poly, c_squared)),
        (4, multiply(prime, shift(e_poly), c_c_prime)),
        (-4 * height, b_poly),
        (4 * (height - 1) * kappa, shift(b_poly)),
    )
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


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
    assert incoming == {DEPENDENCY}
    assert CONSUMER in outgoing


def main() -> None:
    check_wiring()
    prime = 53
    height = 8
    e_poly = [1, 1, 11, 34, 43]
    a = coefficients(prime, height, e_poly)
    b_poly = a[: 2 * height - 2]
    leading = a[2 * height]
    assert (a[2 * height - 2], a[2 * height - 1], leading) == (0, 0, 2)

    actual_residual = residual(prime, e_poly, b_poly)
    expected_residual = [0] * (2 * height + 1)
    expected_residual[2 * height - 1] = -8 * height * leading % prime
    expected_residual[2 * height] = (
        8 * (height - 1) * e_poly[4] * b_poly[-1] % prime
    )
    assert actual_residual == expected_residual

    c_poly = [1, 22, 49, 3, 16]
    phi = differential_phi(prime, height, e_poly, b_poly, c_poly, leading)
    assert phi[:height] == [0] * height
    assert phi[height:] == [22, 7, 18, 13, 44]
    assert len(phi) - 1 <= 2 * height - 2

    low = a[:height]
    high = a[2 * height : 3 * height]
    window = multiply(prime, low, high)[:height]
    square = multiply(prime, c_poly, c_poly)[:height]
    assert window == [leading * value % prime for value in square]

    # A nonzero-b primary survivor exercises both residual endpoints.
    prime_two = 97
    height_two = 7
    e_two = [1]
    for root in (1, 6, 50, 3):
        e_two = multiply(prime_two, e_two, [1, -root % prime_two])
    a_two = coefficients(prime_two, height_two, e_two)
    b_two = a_two[: 2 * height_two - 2]
    assert e_two == [1, 37, 42, 87, 27]
    assert (a_two[12], a_two[13], a_two[14], b_two[-1]) == (0, 0, 71, 13)
    assert residual(prime_two, e_two, b_two)[13:] == [1, 67]
    assert 1 == -8 * height_two * a_two[14] % prime_two
    assert 67 == 8 * (height_two - 1) * e_two[4] * b_two[-1] % prime_two

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_SECONDARY_DIFFERENTIAL_PASS "
        "residual_terms=2 quotient_degree=4 equivalence_fixture=1 nonzero_b=1 wiring=2"
    )


if __name__ == "__main__":
    main()
