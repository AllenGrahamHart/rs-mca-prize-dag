#!/usr/bin/env python3
"""Checks for the c2 reciprocal affine collapse."""

from __future__ import annotations

import json
from math import isqrt
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RESULT = (
    ROOT
    / "experiments/prize_resolution"
    / "rate_half_list_c2_reciprocal_affine_torsion_result.json"
)
NODE_ID = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_reciprocal_affine_collapse"
GLOBAL_DEP = "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_degree_defect_global_gate_router"
FIELD_DEP = "rate_half_list_budget_three_fiber_two_cycle_c2_torsion_field_router"
CONSUMER = "rate_half_list_adjacent_crossing"


def mul(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    """Multiply x+y*a pairs modulo a^2=-2 over the rationals."""
    x, y = left
    z, w = right
    return x * z - 2 * y * w, x * w + y * z


def trace_test(prime: int, levels: int) -> int:
    value = -2 * pow(3, -1, prime) % prime
    for _ in range(levels):
        value = (value * value - 2) % prime
    return value


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
    assert incoming == {GLOBAL_DEP, FIELD_DEP}
    assert CONSUMER in outgoing

    # Pair coordinates represent numerators over the displayed denominator.
    y_num = (7, 4)
    r_num = (-1, 2)
    assert mul(r_num, r_num) == (-7, -4)
    assert y_num == tuple(-value for value in mul(r_num, r_num))

    # Evaluate A and B at y=(7+4a)/9 with denominator 9.
    a_plus_two = (2, 1)
    a_plus_one = (1, 1)
    a_minus_one = (-1, 1)
    two_minus_a = (2, -1)
    a_num = tuple(x - 9 * z for x, z in zip(mul(a_plus_two, y_num), a_plus_one))
    b_num = tuple(x + 9 * z for x, z in zip(mul(a_minus_one, y_num), two_minus_a))
    assert a_num == (-3, 6) and b_num == (3, -6)

    # Exact small passing control: p=31=-1 mod 32.
    assert trace_test(31, 5) == 2

    order = 1 << 40
    lower = isqrt(3 * (1 << 128) - 1) + 1
    upper = 1 << 65
    k_min = (lower + 1 + order - 1) // order
    k_max = upper // order
    assert lower == 31_950_697_969_885_030_204
    assert (k_min, k_max, k_max - k_min + 1) == (
        29_058_991,
        33_554_432,
        4_495_442,
    )
    assert k_min * order - 1 >= lower
    assert k_max * order - 1 < upper

    packet = json.loads(RESULT.read_text())
    assert packet["all_complete"] and packet["coverage_exact"]
    assert packet["expected_candidates"] == packet["processed"] == 4_495_442
    assert packet["k_start"] == k_min and packet["k_stop"] == k_max + 1
    assert packet["hits"] == []
    assert packet["app_id"] == "ap-Ifv7cgmA0WCon3SfgP1aSo"

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_RECIPROCAL_AFFINE_COLLAPSE_PASS "
        "frobenius=1 fixed_point=1 trace=40 fields=4495442 hits=0 wiring=3"
    )


if __name__ == "__main__":
    main()
