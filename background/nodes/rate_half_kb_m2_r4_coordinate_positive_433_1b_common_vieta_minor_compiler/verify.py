#!/usr/bin/env python3
"""Verify the positive 433-1b common Vieta minor compiler."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = "rate_half_kb_m2_r4_coordinate_positive_433_1b_common_vieta_minor_compiler"
FILES = {
    "compiler": (
        "rate_half_kb_positive_433_1b_common_vieta_compiler.py",
        "a956656cba6c884bae665a2439666964ed468dcf9d0466e80cb825e811a6f845",
    ),
    "launcher": (
        "rate_half_kb_positive_433_1b_common_vieta_compiler_modal.py",
        "49d37b7ee090c4387dfb25df8d199ac59ef5fe1406a0e95a0e8c34363046816c",
    ),
    "result": (
        "rate_half_kb_positive_433_1b_common_vieta_compiler_result.json",
        "6445c4ae4a698789b6e1199b7f59d5375bd625bff95d639f7188f8fe2148b52f",
    ),
}
PARENTS = (
    "rate_half_kb_m2_r4_order2_coordinate_source_facet_signature",
    "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas",
)
ROLES = {"LA", "AB", "AC", "BC+", "BC-"}
EXPECTED_SUMMARIES = {
    "raw": {
        "completed_cases": 60,
        "maximum_terms": 204,
        "minimum_terms": 80,
        "minor_count": 360,
        "minor_degree_histogram": {
            "18": 72, "19": 84, "21": 104, "22": 88, "23": 4, "24": 8,
        },
        "unique_minor_digests": 165,
        "within_row_unique_histogram": {"6": 60},
    },
    "stripped": {
        "completed_cases": 60,
        "maximum_terms": 100,
        "minimum_terms": 20,
        "minor_count": 360,
        "minor_degree_histogram": {
            "8": 4, "9": 52, "10": 16, "12": 120, "13": 144, "14": 24,
        },
        "unique_minor_digests": 165,
        "within_row_unique_histogram": {"6": 60},
    },
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify_payload(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-common-vieta-compiler-v1",
            "schema")
    require(payload["source_sha256"] == FILES["compiler"][1], "source custody")
    require(payload["app"] == "rs-mca-positive-433-1b-common-vieta-compiler",
            "Modal app")
    require(payload["case_count"] == 120 and
            payload["status_counts"] == {"COMPLETE": 120}, "completion")
    require(payload["summaries"] == EXPECTED_SUMMARIES, "aggregate summaries")

    expected_cases = set(itertools.product(
        ("raw", "stripped"), range(15), (-1, 1), (-1, 1),
    ))
    actual_cases = set()
    for row in payload["rows"]:
        require(row["status"] == "COMPLETE" and row["cell_count"] == 15 and
                row["matrix_shape"] == [10, 8] and
                row["base_rank_guard"] == 6 and row["minor_count"] == 6,
                "row metadata")
        case = (row["mode"], row["cell"], *row["epsilon"])
        require(case not in actual_cases, "duplicate case")
        actual_cases.add(case)
        role_list = [row["singleton"]] + [
            role for pair in row["matching"] for role in pair
        ]
        require(len(role_list) == 5 and set(role_list) == ROLES,
                "role partition")
        minors = row["minor_summaries"]
        require(len(minors) == 6 and
                len({minor["sha256"] for minor in minors}) == 6,
                "row minor census")
        require(all(minor["terms"] > 0 and minor["total_degree"] > 0
                    for minor in minors), "nonzero minors")
    require(actual_cases == expected_cases, "case coverage")


def main():
    for filename, expected in FILES.values():
        require(hashlib.sha256((EXPERIMENTS / filename).read_bytes()).hexdigest()
                == expected, f"file custody {filename}")
    payload = json.loads((EXPERIMENTS / FILES["result"][0]).read_text())
    verify_payload(payload)

    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement and
            "all sixty rows" in statement and "degree at most 14" in contract,
            "claim text")
    require("Base rank below six remains separate" in contract and
            "No common-point" in contract, "scope fence")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in PARENTS:
        require(nodes[parent]["status"] == "PROVED", f"parent {parent}")
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    print("positive 433-1b common Vieta minor compiler verified")


if __name__ == "__main__":
    main()
