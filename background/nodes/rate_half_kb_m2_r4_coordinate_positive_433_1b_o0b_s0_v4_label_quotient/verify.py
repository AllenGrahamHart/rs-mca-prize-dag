#!/usr/bin/env python3
"""Verify the O0b S0 Klein-four label quotient."""

import hashlib
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_o0b_s0_v4_label_quotient.py"
BC_SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_o0b_split_bc_ef_involution.py"
D_SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_outside_label_router.py"
DIGESTS = {
    SCRIPT: "3e8163cd19b528ce1166022b54963b7063659b760ad133e2dc37d90093c42021",
    BC_SCRIPT: "79db7fc31be70094d91ead470434be558c3ac2ce31346020ab69db32e7b76ff7",
    D_SCRIPT: "1de5f3755d635c5c4b5bd21807e305bd149877f6de41ae1c60c3ea8e127ed412",
}
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_split_bc_ef_involution_quotient",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell3_outside_label_quotient",
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
    spec = importlib.util.spec_from_file_location("s0_v4", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    require(module.verify() == {
        "s0_lanes": 2,
        "s0_states": 120,
        "s0_raw_rows": 12600,
        "s0_orbits": 3420,
        "s0_profile": {2: 540, 4: 2880},
        "split_orbits": 16020,
    }, "S0 quotient result")

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
        "RATE_HALF_KB_POSITIVE_433_1B_O0B_S0_V4_QUOTIENT_VERIFY_PASS "
        "S0=12600/3420 profile=2:540,4:2880 split=16020"
    )


if __name__ == "__main__":
    main()
