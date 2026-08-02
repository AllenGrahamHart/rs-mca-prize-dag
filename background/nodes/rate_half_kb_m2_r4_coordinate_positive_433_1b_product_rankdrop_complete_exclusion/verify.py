#!/usr/bin/env python3
"""Verify complete exclusion of the positive 433-1b rank-drop branch."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_rankdrop_outside_product_modal.py"
RESULT = EXPERIMENTS / "rate_half_kb_positive_433_1b_rankdrop_outside_product_result.json"
POINTS = EXPERIMENTS / "rate_half_kb_positive_433_1b_rankdrop_fglm_profile_result.json"
SCRIPT_SHA256 = "d97d2f426030594e8f25e3ba68236a9937ee8133fb744140dee26d7671444b26"
RESULT_SHA256 = "3db58a423fa33999ce25d0b4bb859daa010871817d80829c95be588a1c846a22"
POINTS_SHA256 = "1ef0469634892459a35ea9b7b2b72d112d0b10a099ddab2c6754cc9c8e184017"
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_product_rankdrop_deployed_rational_classifier",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas",
    "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
    "rate_half_kb_m2_r4_order2_coordinate_source_facet_signature",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def pairings(values):
    values = tuple(values)
    if not values:
        yield ()
        return
    first = values[0]
    for index in range(1, len(values)):
        rest = values[1:index] + values[index + 1:]
        for tail in pairings(rest):
            yield ((first, values[index]),) + tail


def verify_payload(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-rankdrop-outside-product-v2",
            "schema")
    require(payload["app"] ==
            "rs-mca-positive-433-1b-rankdrop-outside-product", "app")
    require(payload["source_points_sha256"] == POINTS_SHA256,
            "point source custody")
    require(payload["point_count"] == 16 and payload["lane_count"] == 64 and
            payload["case_count"] == 6720 and
            payload["status_counts"] == {"COMPLETE": 6720},
            "aggregate census")
    expected_lanes = set(itertools.product(range(16), (-1, 1), (-1, 1)))
    actual_lanes = set()
    expected_cases = set(itertools.product(range(7), range(15)))
    program_hashes = set()
    for lane in payload["lanes"]:
        lane_key = (lane["point_id"], lane["sigma_c"], lane["sigma_o"])
        require(lane_key not in actual_lanes, "duplicate lane")
        actual_lanes.add(lane_key)
        require(lane["status"] == "COMPLETE" and lane["case_count"] == 105 and
                lane["unit_count"] == 105 and lane["survivor_count"] == 0 and
                lane["rational_candidate_cases"] == 0,
                "lane closure")
        actual_cases = set()
        for row in lane["rows"]:
            case = (row["xi_index"], row["pairing_index"])
            require(case not in actual_cases, "duplicate case")
            actual_cases.add(case)
            require(row["status"] == "COMPLETE" and row["unit"] and
                    "UNIT=1" in row["stdout"] and not row["stderr"],
                    "unit certificate")
            require("lex_status" not in row, "unexpected fallback")
            require(len(row["program_sha256"]) == 64, "program hash")
            program_hashes.add(row["program_sha256"])
        require(actual_cases == expected_cases, "case coverage")
    require(actual_lanes == expected_lanes, "lane coverage")
    require(len(program_hashes) == 2880, "program digest census")


def main():
    require(hashlib.sha256(SCRIPT.read_bytes()).hexdigest() == SCRIPT_SHA256,
            "script custody")
    require(hashlib.sha256(RESULT.read_bytes()).hexdigest() == RESULT_SHA256,
            "result custody")
    require(hashlib.sha256(POINTS.read_bytes()).hexdigest() == POINTS_SHA256,
            "points custody")
    verify_payload(json.loads(RESULT.read_text()))
    source = SCRIPT.read_text()
    require("ideal I=q0,q1,q2,q3,q4,u*guard-1" in source,
            "five-equation localized ideal")
    require("missing_label*b1_missing*b1_missing" in source and
            "squared_sums[xi_index]*a2_missing*a2_missing" in source,
            "missing-mate sum cut")
    require(len(tuple(pairings(range(6)))) == 15, "matching count")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges, f"parent {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer edge")
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_RANKDROP_COMPLETE_VERIFY_PASS "
        "points=16 lanes=64 ledgers=6720 unit=6720"
    )


if __name__ == "__main__":
    main()
