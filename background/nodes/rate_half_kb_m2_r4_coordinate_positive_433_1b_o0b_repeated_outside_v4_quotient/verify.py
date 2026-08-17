#!/usr/bin/env python3
"""Verify the O0b repeated-outside Klein-four quotient."""

import hashlib
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_o0b_repeated_outside_v4_quotient.py"
BC_SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_o0b_split_bc_ef_involution.py"
ROUTER = EXPERIMENTS / "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_outside_label_router.py"
DIGESTS = {
    SCRIPT: "1aa489851431a79ac8422efa1a60a250c601bda04565fe83a4aa1bf23afc86dd",
    BC_SCRIPT: "79db7fc31be70094d91ead470434be558c3ac2ce31346020ab69db32e7b76ff7",
    ROUTER: "1de5f3755d635c5c4b5bd21807e305bd149877f6de41ae1c60c3ea8e127ed412",
}
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_split_bc_ef_involution_quotient",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell3_outside_label_quotient",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_s0_v4_label_quotient",
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
    spec = importlib.util.spec_from_file_location("repeated_v4", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    require(module.verify() == {
        "repeated_lanes": 4,
        "repeated_states": 240,
        "repeated_raw_rows": 25200,
        "repeated_orbits": 7200,
        "repeated_profile": {2: 1800, 4: 5400},
        "split_orbits": 10620,
    }, "repeated-outside quotient result")

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
        "RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEATED_OUTSIDE_V4_VERIFY_PASS "
        "repeated=25200/7200 profile=2:1800,4:5400 split=10620"
    )


if __name__ == "__main__":
    main()
