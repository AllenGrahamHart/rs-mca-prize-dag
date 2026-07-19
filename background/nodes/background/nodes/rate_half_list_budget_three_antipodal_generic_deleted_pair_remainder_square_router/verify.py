#!/usr/bin/env python3
"""Verify the deleted-pair Euclidean remainder-square router."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_generic_deleted_pair_remainder_square_router"
DEPENDENCIES = {
    "rate_half_list_budget_three_antipodal_generic_deleted_pair_constant_ode",
    "rate_half_list_budget_three_antipodal_generic_deleted_pair_mobius_ratio_router",
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


def divide(dividend: list[int], divisor: list[int]) -> tuple[list[int], list[int]]:
    dividend = trim(dividend[:])
    divisor = trim(divisor[:])
    quotient = [0] * max(1, len(dividend) - len(divisor) + 1)
    inverse_lead = pow(divisor[-1], -1, PRIME)
    while len(dividend) >= len(divisor) and dividend != [0]:
        shift = len(dividend) - len(divisor)
        coefficient = dividend[-1] * inverse_lead % PRIME
        quotient[shift] = coefficient
        for index, value in enumerate(divisor):
            dividend[index + shift] -= coefficient * value
        dividend = trim(dividend)
    return trim(quotient), trim(dividend)


def algebra_check() -> None:
    m_value = 2
    u_poly = [3, 5, 7, 1]
    a_poly = [0] + multiply(u_poly, u_poly)
    w_poly = [4, 1]
    z_poly = multiply(w_poly, w_poly)

    q_value = 4
    q_poly = multiply(
        add(a_poly, z_poly),
        add(a_poly, scale(z_poly, q_value)),
    )
    residual = add(q_poly, scale(multiply(a_poly, a_poly), -1))
    quotient, remainder = divide(residual, a_poly)
    assert quotient == scale(z_poly, 1 + q_value)
    assert remainder == scale(multiply(z_poly, z_poly), q_value)
    inverse_sum = pow(1 + q_value, -1, PRIME)
    recovered = scale(quotient, inverse_sum)
    assert recovered == z_poly
    assert remainder == scale(
        multiply(quotient, quotient),
        q_value * inverse_sum * inverse_sum,
    )
    assert len(quotient) - 1 == 2 * m_value - 2
    assert len(remainder) - 1 == 4 * m_value - 4

    harmonic_q = multiply(add(a_poly, z_poly), add(a_poly, scale(z_poly, -1)))
    harmonic_residual = add(
        harmonic_q, scale(multiply(a_poly, a_poly), -1)
    )
    assert scale(harmonic_residual, -1) == multiply(z_poly, z_poly)
    assert multiply(z_poly, z_poly) == multiply(
        multiply(w_poly, w_poly), multiply(w_poly, w_poly)
    )


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
        "R=A S+T",
        "T=q S^2/(1+q)^2",
        "Z:=S/(1+q)",
        "-R=W^4",
        "exact fourth",
        "no coefficient of `V_0`",
        "does not prove",
    ):
        assert marker in statement


def main() -> None:
    algebra_check()
    wiring_check()
    print(
        "RATE_HALF_ANTIPODAL_DELETED_PAIR_REMAINDER_SQUARE_PASS "
        "nonharmonic_quotients=1 harmonic_fourth_power=1 free_V=0"
    )


if __name__ == "__main__":
    main()
