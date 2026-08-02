#!/usr/bin/env python3
"""Verify complete exclusion of positive 433-1b cells 1 and 2."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_principal_common_charts_modal.py"
RESULT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cells1_2_principal_common_charts_result.json"
SCRIPT_SHA256 = "d2de06b6011105ddb5ddd95e93eff865ce01491d4b9b612dbac2cc703271b577"
RESULT_SHA256 = "a466fa1850647a8bfa9a988229f8d3f8f03bd510ca739edb6cf256315b22531a"
COMMON = EXPERIMENTS / "rate_half_kb_positive_433_1b_common_vieta_compiler.py"
PRODUCT = EXPERIMENTS / "rate_half_kb_positive_433_1b_product_base_rank_compiler_result.json"
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_common_vieta_minor_compiler",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_product_rankdrop_common_exception_classifier",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_product_rankdrop_complete_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas",
    "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
    "rate_half_kb_m2_r4_order2_coordinate_source_facet_signature",
)
ROLE_SHAPES = {
    1: ("LA", [["AB", "BC+"], ["AC", "BC-"]]),
    2: ("LA", [["AB", "BC-"], ["AC", "BC+"]]),
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_payload(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-principal-common-charts-v1", "schema")
    require(payload["app"] == "rs-mca-positive-433-1b-principal-common-charts" and
            payload["field"] == 2130706433, "app/field")
    require(payload["source_common_sha256"] == digest(COMMON) and
            payload["source_product_sha256"] == digest(PRODUCT), "source custody")
    require(payload["case_count"] == 48 and
            payload["status_counts"] == {"COMPLETE": 48} and
            payload["unit_count"] == 48 and payload["nonunit_count"] == 0,
            "aggregate")
    expected = set(itertools.product((1, 2), (-1, 1), (-1, 1), range(6)))
    actual = set()
    program_hashes = set()
    for row in payload["rows"]:
        key = (row["cell"], *row["epsilon"], row["chart"])
        require(key not in actual, "duplicate row")
        actual.add(key)
        require((row["singleton"], row["matching"]) == ROLE_SHAPES[row["cell"]],
                "role shape")
        require(row["status"] == "COMPLETE" and row["unit"] and
                row["dimension"] == -1 and row["basis_size"] == 1 and
                "UNIT=1" in row["stdout"] and "END" in row["stdout"] and
                not row["stderr"], "unit chart")
        require(len(row["program_sha256"]) == 64, "program digest")
        program_hashes.add(row["program_sha256"])
    require(actual == expected and len(program_hashes) == 48, "Cartesian census")


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(NODE_ID in nodes and nodes[NODE_ID]["status"] == "PROVED", "DAG node")
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges, f"missing parent {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")


def main():
    require(digest(SCRIPT) == SCRIPT_SHA256, "script custody")
    require(digest(RESULT) == RESULT_SHA256, "result custody")
    verify_payload(json.loads(RESULT.read_text()))
    verify_dag()
    print("cells=1,2 principal_charts=48 unit=48 rankdrop=closed")


if __name__ == "__main__":
    main()
