#!/usr/bin/env python3
"""Verify the zero-loop 433 cell-1 orbit exclusion."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_"
    "doubled_singleton_opposite_pair_exclusion"
)
SPEC = importlib.util.spec_from_file_location("check", NODE / "check.py")
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def canonical(cell):
    singleton, matching = cell
    return singleton, tuple(sorted(tuple(sorted(pair)) for pair in matching))


def main():
    b = CHECK.ROUTER.sp.symbols("b")
    extra = ((1047557337,1605884903),(1678774983,1605884903))
    q_points = tuple(sorted(CHECK.GUARD_POINTS+extra))
    roots = CHECK.check_row(
        1, 1, 8, 18, b*b-595625887*b+1,
        q_points, (4,14,5),
    )
    require(roots == 2, "projected root count")

    cells = CHECK.ROUTER.BASE.BASE.cells()
    permutations = (
        (0,1,2,3,4), (1,0,3,2,4),
        (2,3,0,1,4), (3,2,1,0,4),
    )
    lookup = {canonical(cell): index for index, cell in enumerate(cells)}
    orbit = set()
    for permutation in permutations:
        singleton, matching = cells[1]
        transported = (
            permutation[singleton],
            tuple((permutation[left], permutation[right])
                  for left, right in matching),
        )
        orbit.add(lookup[canonical(transported)])
    require(sorted(orbit) == [1,3,8,10], "target orbit")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate",
        "rate_half_kb_m2_r4_coordinate_negative_zero_loop_product_q_weld",
    ):
        require((parent,NODE_ID,"req") in edges, f"dependency {parent}")
    require((NODE_ID,"rate_half_band_closure","ev") in edges, "consumer")
    print(
        "RATE_HALF_KB_ZERO_LOOP_433_OPPOSITE_VERIFY_PASS "
        "cell=1 eps=1,1 orbit=1,3,8,10"
    )


if __name__ == "__main__":
    main()
