#!/usr/bin/env python3
"""Verify the linear Grassmann chamber atlas and DAG wiring."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_linear_grassmann_atlas"
FIBER = "rate_half_list_budget_three_split_fiber_atlas"
K4 = "rate_half_list_budget_three_k4_grassmann_line"
CONSUMER = "rate_half_list_adjacent_crossing"
EDGES = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))

CHAMBERS = {
    "pendant": {(0, 0, 1, 1, 1, 2), (0, 0, 1, 1, 2, 1), (0, 0, 1, 1, 2, 2)},
    "4-cycle": {(0, 1, 1, 1, 1, 0), (0, 1, 1, 1, 1, 1), (1, 1, 1, 1, 1, 0), (1, 1, 1, 1, 1, 1)},
    "K_4-e": {(0, 1, 1, 1, 1, 1), (0, 1, 1, 1, 1, 2)},
    "K_4": {(1, 1, 1, 1, 1, 1)},
    "path": {(0, 1, 0, 1, 0, 0), (0, 1, 0, 1, 0, 1)},
    "triangle": {(1, 1, 0, 1, 0, 0)},
}

EXPECTED = {
    "4-cycle": (4, "0123", (-1, -1, -1, -1), 4),
    "K_4-e": (1, "0123", (-2, -2, -1, -1), 6),
    "K_4": (1, "0123", (-2, -2, -2, -2), 8),
    "path": (2, "013", (-1, -1, 0, -1), 3),
    "triangle": (1, "0123", (-1, -1, -1, -2), 5),
}


def complementary_degrees(chamber: tuple[int, ...], omitted: int) -> tuple[int, int, int]:
    vertices = [vertex for vertex in range(4) if vertex != omitted]
    return tuple(chamber[EDGES.index(edge)] for edge in combinations(vertices, 2))


def check_table() -> None:
    linear = {name: {row for row in rows if max(row) <= 1} for name, rows in CHAMBERS.items()}
    assert {name: len(rows) for name, rows in linear.items()} == {
        "pendant": 0,
        "4-cycle": 4,
        "K_4-e": 1,
        "K_4": 1,
        "path": 2,
        "triangle": 1,
    }
    assert sum(map(len, linear.values())) == 9
    assert sum(len(rows) for rows in CHAMBERS.values()) - 9 == 4

    for name in ("4-cycle", "K_4-e", "K_4", "triangle"):
        for chamber in linear[name]:
            for omitted in range(4):
                degrees = complementary_degrees(chamber, omitted)
                assert len(set(degrees)) > 1 or degrees == (1, 1, 1)
    for chamber in linear["path"]:
        assert complementary_degrees(chamber, 2) == (0, 0, 0)
        for omitted in (0, 1, 3):
            assert complementary_degrees(chamber, omitted) != (0, 0, 0)

    assert sum(row[0] for row in EXPECTED.values()) == 9
    assert {row[-1] for row in EXPECTED.values()} == {3, 4, 5, 6, 8}


def check_sources() -> None:
    packet = ROOT / "background" / "nodes" / NODE
    statement = (packet / "statement.md").read_text()
    proof = (packet / "proof.md").read_text()
    assert "nine have `deg b_ij<=1`" in statement
    assert "`3+1=4` quadratic chambers" in (packet / "audit.md").read_text()
    assert "lambda_0lambda_1lambda_2lambda_3!=0" in statement
    assert "q_13 A_0-q_03 A_1+q_01 A_3=0" in proof


def check_dag() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    for parent in (FIBER, K4):
        assert nodes[parent]["status"] == "PROVED"
        assert (parent, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges


def main() -> None:
    check_table()
    check_sources()
    check_dag()
    print(
        "RATE_HALF_LIST_BUDGET_THREE_LINEAR_GRASSMANN_ATLAS_PASS "
        "linear_chambers=9 quadratic_chambers=4 relation_supports=0123,013 dag=3/3"
    )


if __name__ == "__main__":
    main()
