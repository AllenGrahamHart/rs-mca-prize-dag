#!/usr/bin/env python3
"""Verify the deleted-pair constant ODE and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_generic_deleted_pair_constant_ode"
DEPENDENCIES = {
    "rate_half_list_budget_three_antipodal_generic_deleted_pair_even_factorization",
    "rate_half_list_budget_three_antipodal_reverse_residual_stratification",
}
CONSUMER = "rate_half_list_adjacent_crossing"


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


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
    return trim([i * poly[i] for i in range(1, len(poly))] or [0])


def shift_x(poly: list[int]) -> list[int]:
    return [0] + poly


def operator_direct(m_value: int, deleted: list[int], u_poly: list[int]) -> list[int]:
    return add(
        add(
            scale(multiply(deleted, u_poly), 16 * m_value - 4),
            scale(shift_x(multiply(derivative(deleted), u_poly)), -2),
        ),
        scale(shift_x(multiply(deleted, derivative(u_poly))), -8),
    )


def operator_formula(m_value: int, deleted: list[int], u_poly: list[int]) -> list[int]:
    d0, d1 = deleted[:2]
    answer = []
    for degree in range(len(u_poly) + 2):
        value = 0
        if degree < len(u_poly):
            value += d0 * (16 * m_value - 4 - 8 * degree) * u_poly[degree]
        if 0 <= degree - 1 < len(u_poly):
            value += d1 * (16 * m_value + 2 - 8 * degree) * u_poly[degree - 1]
        if 0 <= degree - 2 < len(u_poly):
            value += (16 * m_value + 8 - 8 * degree) * u_poly[degree - 2]
        answer.append(value)
    return trim(answer)


def algebra_check() -> None:
    for m_value in range(1, 8):
        deleted = [3 + m_value, 2 - m_value, 1]
        u_poly = [(-1) ** i * (i + 2) for i in range(2 * m_value)]
        assert operator_direct(m_value, deleted, u_poly) == operator_formula(
            m_value, deleted, u_poly
        )
        for degree in range(1, 2 * m_value):
            denominator = 16 * m_value - 4 - 8 * degree
            assert 4 <= denominator <= 16 * m_value - 12

    # M=1 exact constant-forcing fixture.
    deleted = [40, 8, 1]
    u_poly = [-2, 1]
    assert operator_direct(1, deleted, u_poly) == [-960]
    assert deleted[1] * u_poly[1] + 4 * u_poly[0] == 0


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
        "constant-forcing ODE",
        "d_1u_(2M-1)+4u_(2M-2)=0",
        "at most one monic",
        "simple root at zero",
        "does not classify",
    ):
        assert marker in statement


def main() -> None:
    algebra_check()
    wiring_check()
    print(
        "RATE_HALF_ANTIPODAL_DELETED_PAIR_CONSTANT_ODE_PASS "
        "half_degree=1 terminal_constraints=1 exceptional_roots=1"
    )


if __name__ == "__main__":
    main()
