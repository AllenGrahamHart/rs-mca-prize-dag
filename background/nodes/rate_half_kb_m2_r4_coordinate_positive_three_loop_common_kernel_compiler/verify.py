#!/usr/bin/env python3
"""Verify the positive three-loop common-kernel compiler."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_positive_three_loop_common_kernel_compiler"
SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_three_loop_common_kernel.py"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    specification = importlib.util.spec_from_file_location("common_kernel", SCRIPT)
    common_kernel = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(common_kernel)
    result = common_kernel.verify()
    require(set(result) == {"442", "433"}, "profile coverage")
    require(all(value["rows"] == 4 and value["columns"] == 4
                for value in result.values()), "matrix dimensions")
    require(all(value["residual_total_degree"] == 6
                for value in result.values()), "residual degrees")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    for parent in (
        "rate_half_kb_m2_r4_coordinate_coefficient_normal_form",
        "rate_half_kb_m2_r4_coordinate_positive_loop_ramification_gate",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    statement = (NODE / "statement.md").read_text()
    require("R_442" in statement and "R_433" in statement, "residuals")
    require("does not prove that either residual" in statement, "nonclaim")
    print(
        "RATE_HALF_KB_POSITIVE_THREE_LOOP_COMMON_KERNEL_VERIFY_PASS "
        "profiles=2 matrices=4x4,4x4 residual_degrees=6,6"
    )


if __name__ == "__main__":
    main()
