#!/usr/bin/env python3
"""Verify the deleted-pair fourth-root differential gcd gate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_generic_deleted_pair_fourth_root_gcd_gate"
DEPENDENCIES = {
    "rate_half_list_budget_three_antipodal_generic_deleted_pair_constant_ode",
    "rate_half_list_budget_three_antipodal_generic_deleted_pair_nonharmonic_fourth_power_router",
}
CONSUMER = "rate_half_list_adjacent_crossing"
PRIME = 97


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] % PRIME == 0:
        poly.pop()
    return [value % PRIME for value in poly]


def add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    return trim([
        (left[i] if i < len(left) else 0)
        + (right[i] if i < len(right) else 0)
        for i in range(size)
    ])


def scale(poly: list[int], scalar: int) -> list[int]:
    return trim([scalar * value for value in poly])


def multiply(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, value in enumerate(left):
        for j, other in enumerate(right):
            answer[i + j] += value * other
    return trim(answer)


def derivative(poly: list[int]) -> list[int]:
    return trim([index * poly[index] for index in range(1, len(poly))] or [0])


def shift(poly: list[int], amount: int) -> list[int]:
    return [0] * amount + poly


def remainder(dividend: list[int], divisor: list[int]) -> list[int]:
    dividend = trim(dividend[:])
    divisor = trim(divisor[:])
    inverse_lead = pow(divisor[-1], -1, PRIME)
    while len(dividend) >= len(divisor) and dividend != [0]:
        offset = len(dividend) - len(divisor)
        coefficient = dividend[-1] * inverse_lead % PRIME
        for index, value in enumerate(divisor):
            dividend[index + offset] -= coefficient * value
        dividend = trim(dividend)
    return dividend


def algebra_check() -> None:
    n_value = 8
    t_value = 29
    assert (5 * t_value * t_value + 2 * t_value + 5) % PRIME == 0
    d_poly = [t_value, -(1 + t_value), 1]
    u_zero = 2 * t_value * pow(5 * (t_value + 1), -1, PRIME) % PRIME
    u_poly = [u_zero, 1]

    ode = add(
        add(
            scale(multiply(d_poly, u_poly), 2 * n_value - 4),
            scale(shift(multiply(derivative(d_poly), u_poly), 1), -2),
        ),
        scale(shift(multiply(d_poly, derivative(u_poly)), 1), -8),
    )
    assert len(ode) == 1 and ode[0] != 0
    kappa = ode[0]

    a_poly = shift(multiply(u_poly, u_poly), 1)
    x_to_n_minus_one = [PRIME - 1] + [0] * (n_value - 1) + [1]
    numerator_r = add(
        x_to_n_minus_one,
        scale(multiply(d_poly, multiply(a_poly, a_poly)), -1),
    )

    # Clear the denominator D from R=numerator_r/D in (FGG3).
    left = scale(
        shift(add(
            multiply(derivative(numerator_r), d_poly),
            scale(multiply(numerator_r, derivative(d_poly)), -1),
        ), 1),
        2,
    )
    p_poly = add(
        [2 * n_value],
        scale(shift(multiply(multiply(u_poly, u_poly), u_poly), 2), kappa),
    )
    nd_minus_xdprime = add(
        scale(d_poly, n_value),
        scale(shift(derivative(d_poly), 1), -1),
    )
    right = add(
        multiply(p_poly, d_poly),
        scale(multiply(nd_minus_xdprime, numerator_r), 2),
    )
    assert left == right

    # The formal divisibility implication requires no coprimality assumptions.
    w_poly = [2, 1]
    w_squared = multiply(w_poly, w_poly)
    model_r = multiply(w_squared, [3, 4, 1])
    model_p = add(
        scale(shift(multiply(d_poly, derivative(model_r)), 1), 2),
        scale(multiply(nd_minus_xdprime, model_r), -2),
    )
    assert remainder(model_p, w_poly) == [0]
    assert remainder(multiply(model_p, model_p), w_squared) == [0]


def wiring_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for marker in (
        "P=2N+kappa x^2U_0^3",
        "2xD_0R'=P+2(ND_0-xD_0')R",
        "W divides P",
        "S divides P^2",
        "deg gcd(S,P)>=M-1",
        "necessary gate, not a converse",
        "does not prove",
    ):
        assert marker in statement


def main() -> None:
    algebra_check()
    wiring_check()
    print(
        "RATE_HALF_ANTIPODAL_DELETED_PAIR_FOURTH_ROOT_GCD_PASS "
        "differential_identities=1 gcd_floor=M-1 root_free_divisibility=1"
    )


if __name__ == "__main__":
    main()
