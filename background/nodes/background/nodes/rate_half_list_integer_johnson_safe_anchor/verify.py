#!/usr/bin/env python3
"""Verify the exact-integer Johnson safe anchor and official constants."""

from __future__ import annotations

import json
from math import isqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_integer_johnson_safe_anchor"
FLOOR = "rate_half_cyclic_rotated_prefix_floor"
CONSUMER = "rate_half_list_adjacent_crossing"


def minimum_pair_intersections(length: int, lists: int, agreement: int) -> int:
    degree, remainder = divmod(lists * agreement, length)
    return length * degree * (degree - 1) // 2 + remainder * degree


def certificate_value(length: int, dimension: int, budget: int, agreement: int) -> int:
    lists = budget + 1
    lower = minimum_pair_intersections(length, lists, agreement)
    upper = lists * (lists - 1) // 2 * (dimension - 1)
    return lower - upper


def safe_anchor(length: int, dimension: int, budget: int) -> int:
    lower = dimension - 1
    upper = length
    while lower + 1 < upper:
        middle = (lower + upper) // 2
        if certificate_value(length, dimension, budget, middle) > 0:
            upper = middle
        else:
            lower = middle
    return upper


def dynamic_minimum(length: int, lists: int, incidence_total: int) -> int:
    states = {0: 0}
    for _ in range(length):
        following: dict[int, int] = {}
        for used, cost in states.items():
            for degree in range(lists + 1):
                total = used + degree
                if total > incidence_total:
                    continue
                candidate = cost + degree * (degree - 1) // 2
                following[total] = min(following.get(total, candidate), candidate)
        states = following
    return states[incidence_total]


def check_balanced_formula() -> int:
    checks = 0
    for length in range(3, 9):
        for lists in range(2, 7):
            for total in range(lists * length + 1):
                agreement, remainder = divmod(total, lists)
                if remainder:
                    continue
                expected = minimum_pair_intersections(length, lists, agreement)
                assert dynamic_minimum(length, lists, total) == expected
                checks += 1
    return checks


def check_dag() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[FLOOR]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (FLOOR, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges


def main() -> None:
    balanced_checks = check_balanced_formula()
    n = 1 << 41
    k = 1 << 40
    first_johnson = isqrt(n * (k - 1)) + 1
    threshold = 332_114_441_762
    delta = first_johnson * first_johnson - n * (k - 1)
    generic_list_threshold = (
        n * (first_johnson - (k - 1)) + delta - 1
    ) // delta
    assert delta == 3_015_547_699_344
    assert generic_list_threshold == threshold + 2
    cases = (
        (1, 1_649_267_441_664),
        (3, 1_649_267_441_664),
        ((1 << 32) - 1, 1_554_944_256_063),
        (threshold - 1, first_johnson + 1),
        (threshold, first_johnson),
        ((1 << 128) - 1, first_johnson),
    )
    for budget, expected in cases:
        anchor = safe_anchor(n, k, budget)
        assert anchor == expected
        assert certificate_value(n, k, budget, anchor) > 0
        assert certificate_value(n, k, budget, anchor - 1) <= 0
    assert first_johnson == 1_554_944_255_988
    check_dag()
    print(
        "RATE_HALF_LIST_INTEGER_JOHNSON_SAFE_ANCHOR_PASS "
        f"balanced_checks={balanced_checks} official_cases={len(cases)} "
        f"threshold={threshold} first_johnson={first_johnson} "
        f"generic_list_threshold={generic_list_threshold} dag=2/2"
    )


if __name__ == "__main__":
    main()
