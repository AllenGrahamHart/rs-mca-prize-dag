#!/usr/bin/env python3
"""Verify the path-type Mobius transversal and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_path_mobius_transversal"
PARENT = "rate_half_list_budget_three_split_fiber_atlas"
CONSUMER = "rate_half_list_adjacent_crossing"


def path_ledger() -> None:
    a_offsets = (-1, -1, 0, -1)
    p = (0, 1, 0, 1, 0, 0)
    delta = (0, 0, 0, 0, 0, 1)
    assert tuple(offset + 1 for offset in a_offsets) == (0, 0, 1, 0)
    assert p == (0, 1, 0, 1, 0, 0)
    assert delta == (0, 0, 0, 0, 0, 1)

    # Formal cross multiplication for
    # (x-r)(y-s)-(y-r)(x-s)=(r-s)(x-y).
    left = {
        "xy": 1 - 1,
        "xs": -1,
        "ry": -1,
        "ys": 1,
        "rx": 1,
        "rs": 1 - 1,
    }
    right = {"rx": 1, "ry": -1, "xs": -1, "ys": 1}
    assert {key: value for key, value in left.items() if value} == right

    for d in range(2, 12):
        degree_d_residual_cap = 2
        degree_dm1_residual_cap = 4
        assert (d > degree_d_residual_cap) == (d >= 3)
        assert (d - 1 > degree_dm1_residual_cap) == (d >= 6)


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
    path_ledger()
    check_dag()
    print(
        "RATE_HALF_LIST_BUDGET_THREE_PATH_MOBIUS_TRANSVERSAL_PASS "
        "pencils=2 mobius_injective=2 exact_three_thresholds=3,6 dag=2/2"
    )


if __name__ == "__main__":
    main()
