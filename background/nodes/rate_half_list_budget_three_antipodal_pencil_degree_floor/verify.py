#!/usr/bin/env python3
"""Verify the antipodal pencil degree floor and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_pencil_degree_floor"
DEPENDENCIES = {
    "rate_half_list_budget_three_antipodal_mobius_weld",
    "rate_half_list_budget_three_maximal_field_degree_collapse",
}
CONSUMER = "rate_half_list_adjacent_crossing"


def ceiling_half(value: int) -> int:
    return (value + 1) // 2


def arithmetic_check() -> None:
    for r in range(1, 257):
        floor = ceiling_half(r - 4)
        intermediate_floor = (2 * r - 2) // 3
        for v in range(0, r):
            h = r - v
            contradiction = 2 * h - 1 > r + 3
            assert contradiction == (v < floor)
            intermediate_contradiction = 3 * h - 1 > r + 3
            assert intermediate_contradiction == (v < intermediate_floor)

    d = 1 << 39
    r = (1 << 37) - 1
    floor = ceiling_half(r - 4)
    assert d == 4 * (r + 1)
    assert floor == (1 << 36) - 2
    assert (2 * r - 2) // 3 == ((1 << 38) - 4) // 3
    assert r - floor == (1 << 36) + 1
    assert (1 << 64) > d


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert all(nodes[dependency]["status"] == "PROVED" for dependency in DEPENDENCIES)
    assert all((dependency, NODE, "req") in edges for dependency in DEPENDENCIES)
    assert (NODE, CONSUMER, "ev") in edges

    statement = (
        ROOT / "background" / "nodes" / NODE / "statement.md"
    ).read_text()
    for marker in (
        "v >=ceil((r-4)/2)",
        "v>=2^36-2",
        "v>=(2^38-4)/3",
        "constant or low-degree translation",
        "does not exclude pencils meeting",
    ):
        assert marker in statement


def main() -> None:
    arithmetic_check()
    packet_check()
    print(
        "RATE_HALF_LIST_B3_ANTIPODAL_PENCIL_DEGREE_FLOOR_PASS "
        "official_vmin=2^36-2 e2_zero_vmin=(2^38-4)/3 "
        "reverse_contact=2(r-v) characteristic_gt_d=1"
    )


if __name__ == "__main__":
    main()
