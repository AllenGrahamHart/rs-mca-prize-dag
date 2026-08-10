#!/usr/bin/env python3
"""Verify the repeated-BC 433-1b/O0b common Vieta compiler."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
FILES = {
    "compiler": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_vieta_compiler.py",
        "e438d227f5ed7b92c8b787daf075dd56aadb1f6e871f3ffd06e8dd4823b3deea",
    ),
    "launcher": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_vieta_compiler_modal.py",
        "49c5aa9d2ec265b69114ef035b2683e99fd4fcf4bc3289e2bfb6e33de88a0af2",
    ),
    "result": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_vieta_compiler_result.json",
        "09f23b511fd22195e251aafe45c1a958448be224f2d5e0bd549c9adf69820117",
    ),
}
PARENTS = {
    "rate_half_kb_m2_r4_order2_coordinate_source_facet_signature",
    "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_signed_edge_atlas",
}
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"
ROLES = {"LA", "AB", "AC", "BC1", "BC2"}
CELL_ORBITS = [[0], [1, 2], [3], [4, 5], [6], [7, 8], [9, 12], [10, 13], [11, 14]]
DEGREES = {"18": 72, "19": 84, "21": 104, "22": 88, "23": 4, "24": 8}
STRIPPED_DEGREES = {"7": 8, "8": 32, "9": 24, "10": 72, "11": 176, "12": 48}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def expected_summary(mode, bc_sign):
    if mode == "raw":
        return {
            "completed_cases": 60,
            "maximum_terms": 240 if bc_sign == -1 else 168,
            "minimum_terms": 64 if bc_sign == -1 else 48,
            "minor_count": 360,
            "minor_degree_histogram": DEGREES,
            "unique_minor_digests": 99,
            "within_row_unique_histogram": {"6": 60},
        }
    return {
        "completed_cases": 60,
        "maximum_terms": 66 if bc_sign == -1 else 56,
        "minimum_terms": 16 if bc_sign == -1 else 12,
        "minor_count": 360,
        "minor_degree_histogram": STRIPPED_DEGREES,
        "unique_minor_digests": 99,
        "within_row_unique_histogram": {"6": 60},
    }


def verify_payload(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-common-repeat-vieta-v1",
            "schema")
    require(payload["source_sha256"] == FILES["compiler"][1], "source custody")
    require(payload["app"] ==
            "rs-mca-positive-433-1b-o0b-common-repeat-vieta", "Modal app")
    require(payload["case_count"] == 240 and
            payload["status_counts"] == {"COMPLETE": 240}, "completion")
    for mode in ("raw", "stripped"):
        for bc_sign in (-1, 1):
            require(payload["summaries"][mode][str(bc_sign)] ==
                    expected_summary(mode, bc_sign),
                    f"summary {mode} {bc_sign}")

    expected = set(itertools.product(
        ("raw", "stripped"), range(15), (-1, 1), (-1, 1), (-1, 1),
    ))
    actual = set()
    for row in payload["rows"]:
        require(row["status"] == "COMPLETE" and row["cell_count"] == 15 and
                row["cell_orbits"] == CELL_ORBITS and
                row["matrix_shape"] == [10, 8] and
                row["base_rank_guard"] == 6 and row["minor_count"] == 6,
                "row metadata")
        case = (row["mode"], row["cell"], *row["epsilon"], row["bc_sign"])
        require(case not in actual, "duplicate case")
        actual.add(case)
        role_list = [row["singleton"]] + [
            role for pair in row["matching"] for role in pair
        ]
        require(len(role_list) == 5 and set(role_list) == ROLES,
                "role partition")
        minors = row["minor_summaries"]
        require(len(minors) == 6 and
                len({minor["sha256"] for minor in minors}) == 6 and
                all(minor["terms"] > 0 and minor["total_degree"] > 0
                    for minor in minors), "minor census")
    require(actual == expected, "case coverage")


def main():
    for filename, expected_hash in FILES.values():
        require(hashlib.sha256((EXPERIMENTS / filename).read_bytes()).hexdigest()
                == expected_hash, f"file custody {filename}")
    payload = json.loads((EXPERIMENTS / FILES["result"][0]).read_text())
    verify_payload(payload)

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req"))
             for row in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    for parent in PARENTS:
        require(nodes[parent]["status"] == "PROVED", f"parent {parent}")
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, CONSUMER, "ev") in edges, "consumer evidence edge")
    statement = (NODE / "statement.md").read_text()
    require("all 120 repeated-BC common algebra rows" in
            (NODE / "result.md").read_text(), "result census")
    require("does not exclude base-rank" in statement.lower() and
            "or prove either Prize result" in statement, "scope fence")
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_O0B_COMMON_REPEAT_VERIFY_PASS "
        "cases=240 algebra_rows=120 cells=15 cell_orbits=9 minors=1440 "
        "stripped_degree=7..12"
    )


if __name__ == "__main__":
    main()
