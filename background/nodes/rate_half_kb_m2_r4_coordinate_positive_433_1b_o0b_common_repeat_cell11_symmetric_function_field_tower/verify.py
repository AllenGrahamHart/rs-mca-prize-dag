#!/usr/bin/env python3
"""Verify the repeated-BC cell-11 symmetric function-field tower."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
PARENT = "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell11_selected_rank_fiber_partition"
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"
FILES = {
    "symmetric_launcher": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_symmetric_tower_modal.py",
        "e2a275a00abdf260d29b1c277c1e83ba27bef09db3a64dbdc3034d16e4f163a2",
    ),
    "symmetric_result": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_symmetric_tower_result.json",
        "e80940956518b958dafe74eb34e8ce4f00ce729e78646203bb0724057e6f7899",
    ),
    "two_launcher": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_two_relation_tower_modal.py",
        "76fe8f95cab64a5c9c9d481845a866a6ab54fc8b3dd76c4140829a6d52b17bf3",
    ),
    "two_result": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_two_relation_tower_result.json",
        "d38f1bdbef9528a48bbf4b9c0bda3ff7d1a85335fa5051dbec85040e1ea77183",
    ),
    "chart_launcher": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_chart_coverage_modal.py",
        "99946dc4afc5e4c1f86bde5e5c8e1a706d4b96ee868a1d78cdb80d272e8c0ec4",
    ),
    "chart_result": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_chart_coverage_result.json",
        "6eb057ca4d01517438643c7e09f5de2c4c52220e79292540e58597120abc006a",
    ),
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load(label):
    return json.loads((EXPERIMENTS / FILES[label][0]).read_text())


def cases(payload, status):
    require(len(payload["rows"]) == 8, "row count")
    expected = set(itertools.product((-1, 1), (-1, 1), (-1, 1)))
    actual = set()
    for row in payload["rows"]:
        key = (*row["epsilon"], row["bc_sign"])
        require(key in expected and key not in actual, "case coverage")
        actual.add(key)
        require(row["status"] == status, "row status")
    require(actual == expected, "complete sign coverage")


def validate_symmetric(payload):
    require(payload["schema"].endswith("cell11-symmetric-tower-v1"), "symmetric schema")
    require(payload["status_counts"] == {"COMPLETE": 8}, "symmetric status")
    cases(payload, "COMPLETE")
    for row in payload["rows"]:
        require(row["full_dimension"] == 1, "source dimension")
        require(row["tower_size"] == 4 and row["ordered_lift_size"] == 5,
                "tower sizes")
        lift = [line.rstrip(",") for line in row["ordered_lift_output"].splitlines()[2:]
                if line.strip()]
        require(len(lift) == 5 and lift[-1][0] == "b" and "b" not in lift[-1][1:],
                "monic linear b lift")
        expected = row["epsilon"][0] * row["epsilon"][1]
        require(row["substitution"] == f"t={expected}*r^2", "t substitution")


def validate_two(payload):
    require(payload["schema"].endswith("cell11-two-relation-tower-v1"), "two schema")
    require(payload["source_sha256"] == FILES["symmetric_result"][1], "two source")
    require(payload["status_counts"] == {"COMPLETE": 8}, "two status")
    cases(payload, "COMPLETE")
    for row in payload["rows"]:
        degree = 6 if row["bc_sign"] == -1 else 4
        require(row["generic_extension_degree"] == degree, "extension degree")
        require(row["localized_full_dimension"] == 1 and
                row["localized_two_relation_dimension"] == 1, "localized dimensions")
        require(row["quadratic_relation_index"] == 1, "quadratic index")
        require(row["full_generators_mod_two_relation"] == ["0"] * 4,
                "two-relation containment")
        require(row["chart"] == "x*y*(x-1)*(x+1)", "chart")


def validate_chart(payload):
    require(payload["schema"].endswith("cell11-chart-coverage-v1"), "chart schema")
    require(payload["status_counts"] == {"UNIT": 8}, "chart status")
    cases(payload, "UNIT")
    for row in payload["rows"]:
        require(row["chart"] == "b*c*(b+c)*(b*c-1)*(b*c+1)", "source chart")
        require(row["basis_size"] == 1 and row["one_remainder"] == "0",
                "unit certificate")


def main():
    for filename, expected in FILES.values():
        actual = hashlib.sha256((EXPERIMENTS / filename).read_bytes()).hexdigest()
        require(actual == expected, f"file custody {filename}")
    validate_symmetric(load("symmetric_result"))
    validate_two(load("two_result"))
    validate_chart(load("chart_result"))
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req")) for row in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    require(nodes[PARENT]["status"] == "PROVED" and (PARENT, NODE_ID, "req") in edges,
            "parent")
    require((NODE_ID, CONSUMER, "ev") in edges, "consumer")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_CELL11_SYMMETRIC_TOWER_VERIFY_PASS rows=8 degrees=6,4 containments=32 chart_units=8")


if __name__ == "__main__":
    main()
