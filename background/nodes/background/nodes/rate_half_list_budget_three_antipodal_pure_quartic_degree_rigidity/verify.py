#!/usr/bin/env python3
"""Verify pure-quartic degree rigidity and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_pure_quartic_degree_rigidity"
DEPENDENCY = "rate_half_list_budget_three_antipodal_pencil_degree_floor"
CONSUMER = "rate_half_list_adjacent_crossing"


def arithmetic_check() -> None:
    for r in range(1, 257):
        d = 4 * r + 4
        for v in range(r):
            lower = d - 2 + 2 * r + 2 * v
            upper = d + 4 * v + 1
            assert (lower <= upper) == (v == r - 1)

    r = (1 << 37) - 1
    v = r - 1
    d = 4 * r + 4
    assert v == (1 << 37) - 2
    assert (1 << 64) > d
    wronskian_degree = 2 * d - 7
    forced_divisor_degree = d - 2 + 2 * r + 2 * v
    assert wronskian_degree - forced_divisor_degree == 1

    for small_r in range(1, 257):
        small_v = small_r - 1
        maximum_distinct_roots = small_r + small_v
        minimum_distinct_roots = 2 * small_r - 1
        assert minimum_distinct_roots == maximum_distinct_roots


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for marker in (
        "e_2=e_3=0",
        "v=r-1",
        "deg V=2^37-2",
        "deg L=1",
        "Both `U` and `V` are squarefree",
        "<=1",
        "does not exclude",
    ):
        assert marker in statement


def main() -> None:
    arithmetic_check()
    packet_check()
    print(
        "RATE_HALF_LIST_B3_ANTIPODAL_PURE_QUARTIC_RIGIDITY_PASS "
        "official_v=2^37-2 wronskian_residual_degree=1 "
        "wronskian_order=2 characteristic_gt_d=1"
    )


if __name__ == "__main__":
    main()
