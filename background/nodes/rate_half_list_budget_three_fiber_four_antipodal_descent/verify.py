#!/usr/bin/env python3
"""Verify the antipodal fiber-four quotient identities and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_fiber_four_antipodal_descent"
DEPENDENCY = "rate_half_list_budget_three_fiber_four_rank_gate"
CONSUMER = "rate_half_list_adjacent_crossing"
PRIME = 1_000_003


def add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    answer = [0] * size
    for index in range(size):
        answer[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % PRIME
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def scale(polynomial: list[int], scalar: int) -> list[int]:
    return [scalar * value % PRIME for value in polynomial]


def multiply(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] = (answer[i + j] + a * b) % PRIME
    return answer


def compose_four(polynomial: list[int]) -> list[int]:
    answer = [0] * (4 * (len(polynomial) - 1) + 1)
    for degree, coefficient in enumerate(polynomial):
        answer[4 * degree] = coefficient
    return answer


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges


def main() -> None:
    a_values = (1, 2, 3, 4)
    lambdas = (1, -3, 3, -1)
    g_values = [[a, 0, 0, 1] for a in a_values]
    h_values = [
        multiply([-a * a % PRIME, 1], g)
        for a, g in zip(a_values, g_values, strict=True)
    ]
    a_locators = [
        multiply([a, 0, 1], compose_four(g))
        for a, g in zip(a_values, g_values, strict=True)
    ]
    p_locators = [[-a % PRIME, 0, 1] for a in a_values]

    first_relation = [0]
    second_relation = [0]
    locator_relation = [0]
    for a, coefficient, g, locator in zip(
        a_values, lambdas, g_values, a_locators, strict=True
    ):
        first_relation = add(first_relation, scale(g, coefficient))
        second_relation = add(second_relation, scale(g, coefficient * a))
        locator_relation = add(locator_relation, scale(locator, coefficient))
    assert first_relation == [0]
    assert second_relation == [0]
    assert locator_relation == [0]

    for p_locator, a_locator, h in zip(
        p_locators, a_locators, h_values, strict=True
    ):
        assert multiply(p_locator, a_locator) == compose_four(h)
    packet_check()
    print(
        "RATE_HALF_LIST_B3_FIBER_FOUR_ANTIPODAL_DESCENT_PASS "
        "pencil_relations=2 local_factorizations=4"
    )


if __name__ == "__main__":
    main()
