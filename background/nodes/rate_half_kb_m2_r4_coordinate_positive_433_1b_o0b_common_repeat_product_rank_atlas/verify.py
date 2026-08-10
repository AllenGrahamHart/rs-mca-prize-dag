#!/usr/bin/env python3
"""Verify the repeated-BC product-rank atlas."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
FILES = {
    "compiler": ("rate_half_kb_positive_433_1b_o0b_common_repeat_product_rank_compiler.py", "2ace6910220f8adefbffb205a561df1a4b5981e84edcd310d1c66485b99681d4"),
    "launcher": ("rate_half_kb_positive_433_1b_o0b_common_repeat_product_rank_compiler_modal.py", "b5d84e2faf24d42e366a299cf9cdedc1760c01dbe253478cee7468927e88fa2b"),
    "result": ("rate_half_kb_positive_433_1b_o0b_common_repeat_product_rank_compiler_result.json", "1b29d65f222d41b0d813d3b899df7625d36010e25f7b935dba93ad60f0e88d60"),
}
PARENT = "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_vieta_minor_compiler"
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"
GUARD_ONLY = {"3:-1": [1, 4], "3:1": [1, 4],
              "6:-1": [1, 4], "6:1": [1, 4]}
DEGREES = {"0": 8, "2": 4, "5": 8, "6": 8, "7": 4,
           "8": 4, "9": 80, "10": 52, "11": 6, "12": 6}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def validate(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-repeat-product-rank-v1", "schema")
    require(payload["source_sha256"] == FILES["compiler"][1], "source custody")
    require(payload["status_counts"] == {"COMPLETE": 30}, "completion")
    require(payload["guard_only_cells"] == GUARD_ONLY, "guard-only set")
    require(payload["stripped_degree_histogram"] == DEGREES, "degree histogram")
    expected = set(itertools.product(range(15), (-1, 1)))
    actual = set()
    for row in payload["rows"]:
        case = (row["cell"], row["bc_sign"])
        require(case not in actual and row["status"] == "COMPLETE", "case")
        actual.add(case)
        require(len(row["raw"]) == len(row["stripped"]) == 6 and
                len(row["kernel_cofactor_expressions"]) == 6 and
                len(row["stripped_ledgers"]) == 6, "six cofactors")
        expected_columns = [1, 4] if row["cell"] in {3, 6} else []
        require(row["guard_only_minor_columns"] == expected_columns,
                "row guard-only columns")
    require(actual == expected, "case coverage")


def main():
    for filename, expected in FILES.values():
        require(hashlib.sha256((EXPERIMENTS / filename).read_bytes()).hexdigest()
                == expected, f"file custody {filename}")
    payload = json.loads((EXPERIMENTS / FILES["result"][0]).read_text())
    validate(payload)
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req")) for row in dag["edges"]}
    require(nodes[NODE_ID]["status"] == nodes[PARENT]["status"] == "PROVED", "statuses")
    require((PARENT, NODE_ID, "req") in edges and
            (NODE_ID, CONSUMER, "ev") in edges, "DAG edges")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_PRODUCT_RANK_VERIFY_PASS cases=30 guard_rank5=3,6")


if __name__ == "__main__":
    main()
