#!/usr/bin/env python3
"""Verify the O0b split cell-0 component quotient."""

import hashlib
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
SCRIPT = (ROOT / "experiments/prize_resolution" /
          "rate_half_kb_positive_433_1b_o0b_split_cell0_component_quotient.py")
REPRESENTATIVES = (ROOT / "experiments/prize_resolution" /
                   "rate_half_kb_positive_433_1b_o0b_split_cell0_component_representatives.json")
SCRIPT_SHA256 = "58836fd22456cd67c1ab72983201759ae7d47735ffdd11dbf3245b1e3843254c"
REPRESENTATIVES_SHA256 = "658ae5f1f3c0667df2cece818e0c89a752ce9cdf7c4f6f421fc4a721134b8fa4"
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_split_cell0_common_component_classification",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_s0_v4_label_quotient",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_repeated_outside_v4_quotient",
)
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    require(hashlib.sha256(SCRIPT.read_bytes()).hexdigest() == SCRIPT_SHA256,
            "quotient compiler custody")
    require(hashlib.sha256(REPRESENTATIVES.read_bytes()).hexdigest() ==
            REPRESENTATIVES_SHA256, "representative manifest custody")
    spec = importlib.util.spec_from_file_location("component_quotient", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    require(module.verify() == {
        "raw_cases": 2520,
        "s0_profile": {2: 36, 4: 192},
        "repeated_profile": {2: 120, 4: 360},
        "representative_count": 708,
        "representatives_sha256":
            "23d7e403e420307b5466ffaf6d2af59d0cf9a4a93766b4d0bcf68231aba1a741",
        "pilot_stratum_count": 56,
        "pilot_representative_count": 24,
        "pilot_representatives_sha256":
            "47ef7c3a9a92ac2bcb08462377195c0576c2495b0ff1f7c0948103d10e02bc27",
        "component_rows": 4,
    }, "component quotient result")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req"))
             for row in dag["edges"]}
    require(nodes[NODE.name]["status"] == "PROVED", "DAG status")
    for parent in PARENTS:
        require(nodes[parent]["status"] == "PROVED" and
                (parent, NODE.name, "req") in edges, "parent")
    require((NODE.name, CONSUMER, "ev") in edges, "consumer")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELL0_COMPONENT_VERIFY_PASS "
          "raw=2520 reps=708 profile=2:156,4:552")


if __name__ == "__main__":
    main()
