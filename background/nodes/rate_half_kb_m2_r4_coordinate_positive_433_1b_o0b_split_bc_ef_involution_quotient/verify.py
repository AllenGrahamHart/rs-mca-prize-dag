#!/usr/bin/env python3
"""Verify the O0b split B/C--E/F involution quotient."""

import hashlib
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_o0b_split_bc_ef_involution.py"
COMMON = EXPERIMENTS / "rate_half_kb_positive_433_1b_common_vieta_compiler.py"
ATLAS = EXPERIMENTS / "rate_half_kb_positive_433_1b_o0b_signed_edge_atlas.py"
DIGESTS = {
    SCRIPT: "79db7fc31be70094d91ead470434be558c3ac2ce31346020ab69db32e7b76ff7",
    COMMON: "a956656cba6c884bae665a2439666964ed468dcf9d0466e80cb825e811a6f845",
    ATLAS: "1caaddce72bc76e142c9f720298932cffb426ccc66c4333c6d7a3c5d4218ea7f",
}
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_split_principal_common_system_adapter",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_signed_edge_atlas",
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
    spec = importlib.util.spec_from_file_location("split_involution", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    result = module.verify()
    require(result == {
        "lanes": 6,
        "raw_states": 360,
        "state_orbits": 180,
        "raw_rows": 37800,
        "row_orbits": 18900,
        "source_scaling": {
            "minus_one": 4,
            "r_inverse_square": 8,
            "identity": 48,
        },
    }, "involution result")

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
        "RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_BC_EF_QUOTIENT_VERIFY_PASS "
        "states=360/180 rows=37800/18900 source_scales=4,8,48"
    )


if __name__ == "__main__":
    main()
