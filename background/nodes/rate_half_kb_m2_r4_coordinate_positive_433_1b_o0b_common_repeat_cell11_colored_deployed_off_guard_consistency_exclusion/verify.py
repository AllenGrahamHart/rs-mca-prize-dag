#!/usr/bin/env python3
"""Verify the colored cell-11 deployed off-guard consistency exclusion."""

import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
PARENT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_"
    "cell11_common_kernel_reconstruction"
)
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"
PRIME = 2130706433
FILES = {
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_colored_consistency_modal.py": "c78beb924d657c304cbb408aefbd4d24048490afd80513b106356bd144761b7c",
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_colored_consistency_result.json": "ef33475d85bdb333c8a698b8a449191092dc2e8b9f409a97538be02a46b10c88",
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_symmetric_tower_result.json": "e80940956518b958dafe74eb34e8ce4f00ce729e78646203bb0724057e6f7899",
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_function_field_core.py": "336aace4780acce09d9cb53cc969635d16a038af0a5379338a746e086758aac7",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load(filename):
    return json.loads((EXPERIMENTS / filename).read_text())


def validate_payload(payload, tower):
    require(
        payload["schema"]
        == "kb-positive-433-1b-o0b-cell11-colored-consistency-v1",
        "schema",
    )
    require(payload["source_tower_count"] == len(payload["rows"]) == 8,
            "source tower census")
    require(payload["case_count"] == 16, "case census")
    require(payload["status_counts"] == {"DEPLOYED_OFF_GUARD_UNIT": 16},
            "status census")
    require(payload["non_guard_root_occurrences"] == 0, "non-guard roots")
    require(payload["distinct_non_guard_root_count"] == 0,
            "distinct non-guard roots")

    tower_programs = {
        (row["bc_sign"], tuple(row["epsilon"])): row["program_sha256"]
        for row in tower["rows"]
    }
    require(len(tower_programs) == 8, "tower program census")
    seen = set()
    determinant_hashes = {-1: set(), 1: set()}
    for source in payload["rows"]:
        key = (source["bc_sign"], tuple(source["epsilon"]))
        require(key in tower_programs and key not in seen, "source key")
        seen.add(key)
        require(source["tower_valid"], "tower validation")
        require(source["tower_program_sha256"] == tower_programs[key],
                "tower program custody")
        require(len(source["rows"]) == 2, "colored row count")
        require({row["missing_record"] for row in source["rows"]}
                == {"BE", "CF"}, "colored record cover")
        for row in source["rows"]:
            require(not row["consistency_identity"], "consistency identity")
            require(not row["determinant_zero"], "zero norm")
            require(row["status"] == "DEPLOYED_OFF_GUARD_UNIT", "status")
            require(row["witness_x"] == 2 and row["witness_value"] != 0,
                    "generic witness")
            require(row["non_guard_base_field_roots"] == [],
                    "non-guard root list")
            determinant_hashes[source["bc_sign"]].add(
                row["determinant_numerator_sha256"]
            )
            expected = (
                [(0, 5), (1, 12)] if source["bc_sign"] == -1
                else [(0, 4), (PRIME - 1, 8)]
            )
            actual = [
                (root["x"], root["multiplicity"])
                for root in row["base_field_roots"]
            ]
            require(actual == expected, "base-field roots")
            require(all(not root["construction_guards_nonzero"]
                        for root in row["base_field_roots"]),
                    "root guard classification")
            if source["bc_sign"] == -1:
                require(row["algebra_dimension"] == 6, "BC- dimension")
                require(row["determinant_numerator_degree"] == 33,
                        "BC- numerator degree")
                require(row["determinant_denominator_degree"] == 26,
                        "BC- denominator degree")
            else:
                require(row["algebra_dimension"] == 4, "BC+ dimension")
                require(row["determinant_numerator_degree"] == 36,
                        "BC+ numerator degree")
                require(row["determinant_denominator_degree"] == 32,
                        "BC+ denominator degree")
    require(seen == set(tower_programs), "source coverage")
    require(all(len(values) == 1 for values in determinant_hashes.values()),
            "epsilon/record determinant invariance")


def main():
    for filename, expected in FILES.items():
        actual = hashlib.sha256((EXPERIMENTS / filename).read_bytes()).hexdigest()
        require(actual == expected, f"file custody: {filename}")
    payload = load(
        "rate_half_kb_positive_433_1b_o0b_common_repeat_"
        "cell11_colored_consistency_result.json"
    )
    tower = load(
        "rate_half_kb_positive_433_1b_o0b_common_repeat_"
        "cell11_symmetric_tower_result.json"
    )
    validate_payload(payload, tower)
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {
        (row["from"], row["to"], row.get("kind", "req"))
        for row in dag["edges"]
    }
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    require(nodes[PARENT]["status"] == "PROVED", "parent status")
    require((PARENT, NODE_ID, "req") in edges, "parent edge")
    require((NODE_ID, CONSUMER, "ev") in edges, "consumer edge")
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_O0B_CELL11_COLORED_VERIFY_PASS "
        "towers=8 cases=16 non_guard_roots=0"
    )


if __name__ == "__main__":
    main()

