#!/usr/bin/env python3
"""Verify repeated-BC cells 3 and 6 compact common loci."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
FILES = {
    "launcher": ("rate_half_kb_positive_433_1b_o0b_common_repeat_cells3_6_compact_kernel_modal.py", "9a9f2c7ee41f63b97323722c2a77c696bb1768ced00fc880fa64796bf0ac4673"),
    "result": ("rate_half_kb_positive_433_1b_o0b_common_repeat_cells3_6_compact_kernel_result.json", "713122da1efabb83a8c10598591240e6e7abb1069c1d105f6bea973de6a9d554"),
}
PARENTS = {
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_saturation_classification",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_product_rank_atlas",
}
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"
BASIS_SIZES = {(3, -1): 23, (3, 1): 18, (6, -1): 23, (6, 1): 16}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def validate(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-repeat-cells3-6-kernel-v1", "schema")
    require(payload["field"] == 2130706433, "field")
    require(payload["source_common_sha256"] ==
            "e438d227f5ed7b92c8b787daf075dd56aadb1f6e871f3ffd06e8dd4823b3deea",
            "common custody")
    require(payload["source_product_sha256"] ==
            "1b29d65f222d41b0d813d3b899df7625d36010e25f7b935dba93ad60f0e88d60",
            "product custody")
    expected = set(itertools.product((3, 6), (-1, 1), (-1, 1), (-1, 1)))
    actual = set()
    for row in payload["rows"]:
        case = (row["cell"], *row["epsilon"], row["bc_sign"])
        require(case not in actual and row["status"] == "COMPLETE", "case")
        actual.add(case)
        require(row["product_guard_column"] == 1 and row["sum_pivot"] == 1,
                "pivot metadata")
        require(len(row["kernel"]) == 8 and len(row["compact_equations"]) == 3,
                "kernel/equation census")
        require(row["identically_zero_rows"] ==
                [True, True, True, True, True, True, True, False, False, False],
                "identity pattern")
        require(row["all_rows_zero_mod_common"] and
                row["reduced_remainders"] == ["0"] * 10,
                "complete row reductions")
        require(row["common_dimension"] == 1 and
                row["common_basis_size"] == BASIS_SIZES[(row["cell"], row["bc_sign"])],
                "dimension/basis size")
        require(all(item["terms"] > 0 and
                    hashlib.sha256(item["expression"].encode()).hexdigest()
                    == item["sha256"]
                    for item in row["kernel"] + row["compact_equations"]),
                "nonzero sealed polynomials")
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
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    for parent in PARENTS:
        require(nodes[parent]["status"] == "PROVED" and
                (parent, NODE_ID, "req") in edges, f"parent {parent}")
    require((NODE_ID, CONSUMER, "ev") in edges, "consumer")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_CELLS3_6_COMPACT_VERIFY_PASS rows=16 dim=1 remainders=160/160")


if __name__ == "__main__":
    main()
