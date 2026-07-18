#!/usr/bin/env python3
"""Verify the six-row B*=3 split-pencil degree ledger and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_split_pencil_normal_form"
PARENT = "rate_half_list_budget_three_intersection_reduction"
CONSUMER = "rate_half_list_adjacent_crossing"
EDGES = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))

ROWS = (
    ("pendant", (0, 0, 0, 0), (0, 0, 1, 1, 1, 1), (-2, -1, -1, 0), (0, 0, 0, 0, 1, 1), (0, 0, 1, 1, 2, 2), 0),
    ("cycle", (0, 0, 0, 0), (0, 1, 1, 1, 1, 0), (-1, -1, -1, -1), (1, 0, 0, 0, 0, 1), (1, 1, 1, 1, 1, 1), 0),
    ("k4_minus_edge", (0, 0, 0, 0), (0, 1, 1, 1, 1, 1), (-2, -2, -1, -1), (0, 0, 0, 0, 0, 1), (0, 1, 1, 1, 1, 2), 1),
    ("k4", (0, 0, 0, 0), (1, 1, 1, 1, 1, 1), (-2, -2, -2, -2), (0, 0, 0, 0, 0, 0), (1, 1, 1, 1, 1, 1), 2),
    ("path_singleton", (0, 0, 0, 1), (0, 1, 0, 1, 0, 0), (-1, -1, 0, -1), (0, 0, 0, 0, 0, 1), (0, 1, 0, 1, 0, 1), 0),
    ("triangle_singleton", (0, 0, 0, 1), (1, 1, 0, 1, 0, 0), (-1, -1, -1, -2), (0, 0, 0, 0, 0, 0), (1, 1, 0, 1, 0, 0), 1),
)


def check_rows() -> None:
    d = 37
    for name, singletons, pair_counts, offsets, expected_delta, expected_b, n4 in ROWS:
        n1 = sum(singletons)
        n2 = sum(pair_counts)
        triples = 4 * d - n1 - n2 - n4
        pair_degrees = tuple(
            sum(pair_counts[j] for j, edge in enumerate(EDGES) if i in edge)
            for i in range(4)
        )
        omitted = tuple(
            triples + singletons[i] + pair_degrees[i] + n4 - (3 * d - 1)
            for i in range(4)
        )
        assert omitted == tuple(d + offset for offset in offsets), name

        intersections = tuple(
            triples - omitted[i] - omitted[j] + pair_counts[index] + n4
            for index, (i, j) in enumerate(EDGES)
        )
        delta = tuple(2 * d - 1 - value for value in intersections)
        assert delta == expected_delta, name
        b_caps = tuple(pair_counts[index] + delta[index] for index in range(6))
        assert b_caps == expected_b, name
        assert all(value in (0, 1) for value in pair_counts)
        assert max(b_caps) <= 2
        assert sum(value == 2 for value in b_caps) == {
            "pendant": 2,
            "k4_minus_edge": 1,
        }.get(name, 0)

        locator_degrees = tuple(
            n4 + omitted[k] + omitted[l] + pair_counts[index]
            for index, (i, j) in enumerate(EDGES)
            for k, l in [tuple(x for x in range(4) if x not in (i, j))]
        )
        assert locator_degrees == tuple(2 * d - 1 - value for value in delta)

        # Degree check for product(P_ij) W^3 product(e_ij)^2 = Lambda_D^3 J^3.
        left_degree = sum(locator_degrees) + 3 * n1 + 2 * n2
        right_degree = 3 * (4 * d) + 3 * n4
        assert left_degree == right_degree, name


def check_dag() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[PARENT]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges


def main() -> None:
    check_rows()
    check_dag()
    print(
        "RATE_HALF_LIST_BUDGET_THREE_SPLIT_PENCIL_NORMAL_FORM_PASS "
        "types=6 quadratic_slots=3 product_ledgers=6 dag=2/2"
    )


if __name__ == "__main__":
    main()
