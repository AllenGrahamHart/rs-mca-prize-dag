#!/usr/bin/env python3
"""Verify the positive 433-1a cell-5 exceptional branch certificate."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
PARENT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "cell5_ratio_chart_compiler"
)
COMPILER = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_433_1a_cell5_ratio_exceptional_compiler.py"
)
RESULT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_433_1a_cell5_ratio_exceptional_result.json"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    specification = importlib.util.spec_from_file_location("compiler", COMPILER)
    compiler = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(compiler)
    compiled = compiler.compile_program()
    compiled.pop("program")
    observed = json.loads(RESULT.read_text())
    for key, value in compiled.items():
        require(observed[key] == value, f"compiled field {key}")
    require(observed["status"] == "COMPLETE", "certificate status")
    require(observed["stderr"] == "", "certificate stderr")
    require(observed["stdout"] == (
        "EXCEPTIONAL\n-1\n1\n0\nBEGIN_BASIS\nG[1]=1\nEND_BASIS\n"
    ), "unit basis output")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    require((PARENT, NODE_ID, "req") in edges, "parent edge")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer edge")
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_CELL5_RATIO_EXCEPTIONAL_VERIFY_PASS "
        "basis=1 generic=open outside=open route=open"
    )


if __name__ == "__main__":
    main()
