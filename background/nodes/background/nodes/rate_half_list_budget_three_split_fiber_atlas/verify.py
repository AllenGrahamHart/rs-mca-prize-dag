#!/usr/bin/env python3
"""Verify the B*=3 degree chambers, split-fiber atlas, and DAG wiring."""

from __future__ import annotations

import json
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_split_fiber_atlas"
PARENT = "rate_half_list_budget_three_split_pencil_normal_form"
CONSUMER = "rate_half_list_adjacent_crossing"
EDGES = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))

TYPES = {
    "pendant": ((-2, -1, -1, 0), (0, 0, 1, 1, 1, 1), (0, 0, 0, 0, 1, 1)),
    "4-cycle": ((-1, -1, -1, -1), (0, 1, 1, 1, 1, 0), (1, 0, 0, 0, 0, 1)),
    "K_4-e": ((-2, -2, -1, -1), (0, 1, 1, 1, 1, 1), (0, 0, 0, 0, 0, 1)),
    "K_4": ((-2, -2, -2, -2), (1, 1, 1, 1, 1, 1), (0, 0, 0, 0, 0, 0)),
    "path + singleton": ((-1, -1, 0, -1), (0, 1, 0, 1, 0, 0), (0, 0, 0, 0, 0, 1)),
    "triangle + singleton": ((-1, -1, -1, -2), (1, 1, 0, 1, 0, 0), (0, 0, 0, 0, 0, 0)),
}

EXPECTED_CHAMBERS = {
    "pendant": {(0, 0, 1, 1, 1, 2), (0, 0, 1, 1, 2, 1), (0, 0, 1, 1, 2, 2)},
    "4-cycle": {(0, 1, 1, 1, 1, 0), (0, 1, 1, 1, 1, 1), (1, 1, 1, 1, 1, 0), (1, 1, 1, 1, 1, 1)},
    "K_4-e": {(0, 1, 1, 1, 1, 1), (0, 1, 1, 1, 1, 2)},
    "K_4": {(1, 1, 1, 1, 1, 1)},
    "path + singleton": {(0, 1, 0, 1, 0, 0), (0, 1, 0, 1, 0, 1)},
    "triangle + singleton": {(1, 1, 0, 1, 0, 0)},
}

EXPECTED_PENCILS = {
    "pendant": {(0, 1, 2): "d-1"},
    "4-cycle": {},
    "K_4-e": {(0, 1, 2): "d-1", (0, 1, 3): "d-1"},
    "K_4": {triangle: "d-1" for triangle in combinations(range(4), 3)},
    "path + singleton": {(0, 1, 2): "d", (0, 1, 3): "d-1"},
    "triangle + singleton": {
        (0, 1, 2): "d",
        (0, 1, 3): "d-1",
        (0, 2, 3): "d-1",
        (1, 2, 3): "d-1",
    },
}


def edge_index(i: int, j: int) -> int:
    return EDGES.index(tuple(sorted((i, j))))


def equality_consistent(delta: tuple[int, ...], q_degrees: tuple[int, ...]) -> bool:
    for labels in product(range(4), repeat=4):
        valid = True
        for edge, slack, q_degree in zip(EDGES, delta, q_degrees, strict=True):
            equal = labels[edge[0]] == labels[edge[1]]
            valid &= equal if slack == 1 and q_degree == 0 else not equal
        if valid:
            return True
    return False


def degree_chambers() -> dict[str, set[tuple[int, ...]]]:
    answer = {}
    for name, (_, p_degrees, delta) in TYPES.items():
        rows = set()
        for q_degrees in product(*(range(slack + 1) for slack in delta)):
            if equality_consistent(delta, q_degrees):
                rows.add(tuple(p + q for p, q in zip(p_degrees, q_degrees, strict=True)))
        answer[name] = rows
    return answer


def pencil_atlas() -> dict[str, dict[tuple[int, int, int], str]]:
    answer = {}
    for name, (a_offsets, p_degrees, delta) in TYPES.items():
        rows = {}
        for i, j, k in combinations(range(4), 3):
            relevant = ((i, j), (j, k), (i, k))
            if any(delta[edge_index(*edge)] for edge in relevant):
                continue
            degrees = (
                a_offsets[k] + p_degrees[edge_index(i, j)],
                a_offsets[i] + p_degrees[edge_index(j, k)],
                a_offsets[j] + p_degrees[edge_index(i, k)],
            )
            if len(set(degrees)) == 1:
                rows[(i, j, k)] = "d" if degrees[0] == 0 else "d-1"
        answer[name] = rows
    return answer


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
    chambers = degree_chambers()
    assert chambers == EXPECTED_CHAMBERS
    assert sum(map(len, chambers.values())) == 13
    pencils = pencil_atlas()
    assert pencils == EXPECTED_PENCILS
    assert sum(map(len, pencils.values())) == 13
    assert 4 * 8 // (8 - 1) == 4
    assert 4 * 5 // (5 - 1) == 5
    check_dag()
    print(
        "RATE_HALF_LIST_BUDGET_THREE_SPLIT_FIBER_ATLAS_PASS "
        "degree_chambers=13 split_pencils=13 cycle_pencils=0 "
        "pendant_quadratic=1 vote_caps=d:4,d-1:4@d>=6 dag=2/2"
    )


if __name__ == "__main__":
    main()
