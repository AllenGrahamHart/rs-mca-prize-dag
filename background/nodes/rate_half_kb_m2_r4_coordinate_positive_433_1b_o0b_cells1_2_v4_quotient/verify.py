#!/usr/bin/env python3
"""Verify the repeated-BC cells 1/2 Klein-four quotient."""

import hashlib
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_o0b_cells1_2_v4_quotient.py"
COMPILER = EXPERIMENTS / "rate_half_kb_positive_433_1b_o0b_common_repeat_vieta_compiler.py"
ROUTER = EXPERIMENTS / "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_outside_label_router.py"
DIGESTS = {
    SCRIPT: "337dcbf9d30cd22df6a12f494a69bde09bfa5361d9937425e4e56919ef30ab8b",
    COMPILER: "e438d227f5ed7b92c8b787daf075dd56aadb1f6e871f3ffd06e8dd4823b3deea",
    ROUTER: "1de5f3755d635c5c4b5bd21807e305bd149877f6de41ae1c60c3ea8e127ed412",
}
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_vieta_minor_compiler",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_saturation_classification",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell3_outside_label_quotient",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_repeated_outside_v4_quotient",
)
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    for path, expected in DIGESTS.items():
        require(digest(path) == expected, f"custody {path.name}")
    spec = importlib.util.spec_from_file_location("cells1_2_v4", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    require(module.verify() == {
        "common_rows": 8,
        "states": 16,
        "raw_rows": 1680,
        "orbits": 456,
        "profile": {2: 72, 4: 384},
        "owner_orbits": 11076,
    }, "cells1/2 quotient result")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req"))
             for row in dag["edges"]}
    require(nodes[NODE.name]["status"] == "PROVED", "DAG status")
    for parent in PARENTS:
        require(nodes[parent]["status"] == "PROVED" and
                (parent, NODE.name, "req") in edges, "parent")
    require((NODE.name, CONSUMER, "ev") in edges, "consumer")
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_O0B_CELLS1_2_V4_VERIFY_PASS "
        "rows=1680/456 profile=2:72,4:384 owner=11076"
    )


if __name__ == "__main__":
    main()
