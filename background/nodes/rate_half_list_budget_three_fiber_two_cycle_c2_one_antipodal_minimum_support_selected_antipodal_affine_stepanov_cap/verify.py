#!/usr/bin/env python3
"""Checks for the selected-antipodal affine Stepanov cap."""

from __future__ import annotations

import json
from math import isqrt
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NODE_ID = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_minimum_support_selected_antipodal_affine_stepanov_cap"
AFFINE_DEP = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_minimum_support_selected_antipodal_infinity_affine_intersection_compiler"
STEPANOV_DEP = "f3_h2_stepanov_inhouse"
FIELD_DEP = "rate_half_list_budget_three_maximal_field_degree_collapse"
CONSUMER = "rate_half_list_adjacent_crossing"


def floor_rational_cuberoot(numerator: int, denominator: int) -> int:
    low, high = 0, 1
    while denominator * high**3 <= numerator:
        high *= 2
    while low + 1 < high:
        middle = (low + high) // 2
        if denominator * middle**3 <= numerator:
            low = middle
        else:
            high = middle
    return low


def main() -> None:
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
    assert incoming == {AFFINE_DEP, STEPANOV_DEP, FIELD_DEP}
    assert CONSUMER in outgoing

    n = 1 << 40
    a_0 = floor_rational_cuberoot(27 * n * n, 64)
    b_0 = floor_rational_cuberoot(125 * n, 64) + 1
    d_0 = a_0
    assert (a_0, b_0, d_0) == (79_896_510, 12_902, 79_896_510)
    assert d_0 * (a_0 + d_0) < a_0 * b_0 * b_0
    assert a_0 * b_0 <= n
    assert (a_0 + 2 * n * b_0) ** 3 < 64 * d_0**3 * n * n

    degree_budget = a_0 + n * b_0
    p_min = isqrt(3 * (1 << 128) - 1) + 1
    assert degree_budget == 14_185_899_101_462_462
    assert p_min == 31_950_697_969_885_030_204
    assert degree_budget < p_min

    numerator = a_0 + 2 * n * b_0
    quotient, remainder = divmod(numerator, d_0)
    assert (quotient, remainder) == (355_106_851, 51_038_404)
    assert quotient < 1 << 29

    prime = 97
    a = 80
    assert a * a % prime == -2 % prime
    determinant = ((a + 2) * (2 - a) + (a + 1) * (a - 1)) % prime
    assert determinant == 3

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_SELECTED_ANTIPODAL_AFFINE_STEPANOV_PASS "
        "parameters=3 inequalities=4 field_chambers=3 cap=355106851 wiring=4"
    )


if __name__ == "__main__":
    main()
