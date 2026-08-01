#!/usr/bin/env python3
"""Verify the positive 433-1a common Vieta pivot-chart reduction."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
PARENT = "rate_half_kb_m2_r4_coordinate_positive_433_1a_common_vieta_minor_compiler"
CHARTS = {
    1: ("12", "13", "14"),
    2: ("12", "23", "24"),
    3: ("13", "23", "34"),
    4: ("14", "24", "34"),
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    pairs = {f"{left}{right}" for left in range(1, 5)
             for right in range(left + 1, 5)}
    require(set().union(*map(set, CHARTS.values())) == pairs, "minor cover")
    for pivot, minors in CHARTS.items():
        require(len(minors) == 3, f"chart {pivot} size")
        require(all(str(pivot) in minor for minor in minors),
                f"chart {pivot} incidence")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    require((PARENT, NODE_ID, "req") in edges, "parent edge")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer edge")
    statement = (NODE / "statement.md").read_text()
    require("all-zero branch" in statement and "rank B<6" in statement,
            "retained branches")
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_COMMON_VIETA_PIVOT_CHART_VERIFY_PASS "
        "quotient_dimension=2 pivot_charts=4 minors_per_chart=3 zero_branch=1"
    )


if __name__ == "__main__":
    main()
