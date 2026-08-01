#!/usr/bin/env python3
"""Verify the (+,+) row and orbit of the zero-loop cell-2 classifier."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_"
    "aligned_doubled_pair_finite_classifier"
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
    root_gcd = (
        b**8+527279086*b**7-32385165*b**6-285229632*b**5
        -613639525*b**4-285229632*b**3-32385165*b**2+527279086*b+1
    )
    packets = (
        (8467609,2130706431,1722993073,1547071505),
        (1061119412,1065353216,1722993073,1547071505),
        (1069587021,1065353216,374290000,583634934),
        (2122238824,2130706431,374290000,583634934),
    )
    q_points = tuple(sorted(CHECK.GUARD_POINTS+(
        (0,2113994754),(283519617,756068675),(1319907736,756068675),
    )))
    require(CHECK.check_row(
        1,1,8,18,root_gcd,packets,q_points,(4,16,5)
    ) == (8,4), "same-positive row")

    cells = CHECK.ROUTER.BASE.BASE.cells()
    permutations = (
        (0,1,2,3,4),(1,0,3,2,4),
        (2,3,0,1,4),(3,2,1,0,4),
    )
    lookup = {canonical(cell):index for index,cell in enumerate(cells)}
    orbit = set()
    for permutation in permutations:
        singleton, matching = cells[2]
        transported = (
            permutation[singleton],
            tuple((permutation[left],permutation[right])
                  for left,right in matching),
        )
        orbit.add(lookup[canonical(transported)])
    require(sorted(orbit) == [2,5,6,9], "target orbit")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]:node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"],edge["to"],edge.get("kind","req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate",
        "rate_half_kb_m2_r4_coordinate_negative_zero_loop_product_q_weld",
    ):
        require((parent,NODE_ID,"req") in edges,f"dependency {parent}")
    require((NODE_ID,"rate_half_band_closure","ev") in edges,"consumer")
    print(
        "RATE_HALF_KB_ZERO_LOOP_433_FINITE_VERIFY_PASS "
        "cell=2 packets=8 orbit_packets=32"
    )


if __name__ == "__main__":
    main()
