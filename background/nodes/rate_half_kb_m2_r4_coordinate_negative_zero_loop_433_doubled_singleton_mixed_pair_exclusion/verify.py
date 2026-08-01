#!/usr/bin/env python3
"""Verify the zero-loop 433 mixed doubled-singleton exclusion."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_"
    "doubled_singleton_mixed_pair_exclusion"
)
CHECK_SPEC = importlib.util.spec_from_file_location("check", NODE / "check.py")
CHECK = importlib.util.module_from_spec(CHECK_SPEC)
CHECK_SPEC.loader.exec_module(CHECK)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def canonical(cell):
    singleton, matching = cell
    return singleton, tuple(sorted(tuple(sorted(pair)) for pair in matching))


def main():
    CHECK.check_row(1, 1, 1, CHECK.GUARD_POINTS, (5, 20, 3))

    cells = CHECK.ROUTER_MODULE.BASE.BASE.cells()
    permutations = (
        (0,1,2,3,4), (1,0,3,2,4),
        (2,3,0,1,4), (3,2,1,0,4),
    )
    lookup = {canonical(cell): index for index, cell in enumerate(cells)}
    orbit = set()
    for permutation in permutations:
        singleton, matching = cells[0]
        transported = (
            permutation[singleton],
            tuple((permutation[left], permutation[right])
                  for left, right in matching),
        )
        orbit.add(lookup[canonical(transported)])
    require(sorted(orbit) == [0,4,7,11], "target orbit")

    statement = (NODE / "statement.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("All four cells are therefore empty" in statement, "claim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate",
        "rate_half_kb_m2_r4_coordinate_negative_zero_loop_product_q_weld",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    print(
        "RATE_HALF_KB_ZERO_LOOP_433_MIXED_VERIFY_PASS "
        "cell=0 eps=1,1 orbit=0,4,7,11"
    )


if __name__ == "__main__":
    main()
