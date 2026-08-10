#!/usr/bin/env python3
"""Verify the repeated-BC cell-11 common-kernel reconstruction."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
PARENT = "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell11_symmetric_function_field_tower"
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"
FILES = {
    "core": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_function_field_core.py",
        "336aace4780acce09d9cb53cc969635d16a038af0a5379338a746e086758aac7",
    ),
    "launcher": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_function_field_audit_modal.py",
        "3a9c554d4175e50259304d76e14b0cb6420550c5b62ea8ab0e3c4db5f664503c",
    ),
    "result": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_function_field_audit_result.json",
        "920151c6671094217172781a8eb17994bfde007b9057b40f4b3aaaf580dfde4a",
    ),
}
TOWER_SHA256 = "e80940956518b958dafe74eb34e8ce4f00ce729e78646203bb0724057e6f7899"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load():
    return json.loads((EXPERIMENTS / FILES["result"][0]).read_text())


def validate(payload):
    require(payload["schema"].endswith("cell11-function-field-audit-v1"), "schema")
    require(payload["core_sha256"] == FILES["core"][1], "core custody")
    require(payload["tower_sha256"] == TOWER_SHA256, "tower custody")
    require(payload["status_counts"] == {"COMPLETE": 8}, "status census")
    require(len(payload["rows"]) == 8, "row count")
    expected = set(itertools.product((-1, 1), (-1, 1), (-1, 1)))
    actual = set()
    for row in payload["rows"]:
        key = (*row["epsilon"], row["bc_sign"])
        require(key in expected and key not in actual, "case coverage")
        actual.add(key)
        require(row["status"] == "COMPLETE", "row status")
        degree = 6 if row["bc_sign"] == -1 else 4
        guards = 19 if row["bc_sign"] == -1 else 12
        product_degrees = {"numerator": 8, "denominator": 7} if row["bc_sign"] == -1 else {"numerator": 7, "denominator": 6}
        require(row["extension_degree"] == degree, "extension degree")
        require(row["tower_checks"] == [True] * 7 and row["encoded_quadratic_zero"],
                "tower arithmetic")
        require(row["tower_residual_payloads"] == [None] * 7, "tower residuals")
        require(row["product_kernel_checks"] == [True] * 5, "product kernel")
        require(row["sum_kernel_checks"] == [True] * 5, "sum kernel")
        require(row["kernel_nonzero"] == [True] * 6, "nonzero cofactors")
        require(len(row["construction_guards"]) == guards, "guard census")
        require(row["missing_product_degrees"] == product_degrees,
                "missing product degrees")
        require(row["missing_sum_squared_degrees"] == {"numerator": 13, "denominator": 12},
                "missing sum degrees")
    require(actual == expected, "complete sign coverage")


def main():
    for filename, expected in FILES.values():
        actual = hashlib.sha256((EXPERIMENTS / filename).read_bytes()).hexdigest()
        require(actual == expected, f"file custody {filename}")
    validate(load())
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req")) for row in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    require(nodes[PARENT]["status"] == "PROVED" and (PARENT, NODE_ID, "req") in edges,
            "parent")
    require((NODE_ID, CONSUMER, "ev") in edges, "consumer")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_CELL11_COMMON_KERNEL_VERIFY_PASS rows=8 tower=56 product=40 sums=40 cofactors=48")


if __name__ == "__main__":
    main()
