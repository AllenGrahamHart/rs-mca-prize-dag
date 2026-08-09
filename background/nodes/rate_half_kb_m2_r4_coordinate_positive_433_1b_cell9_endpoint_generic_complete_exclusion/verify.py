#!/usr/bin/env python3
"""Verify generic cell-9 endpoint exclusion."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell9_endpoint_residual_modal.py"
RESULT = EXP / "rate_half_kb_positive_433_1b_cell9_endpoint_residual_result.json"
REPLAY = EXP / "rate_half_kb_positive_433_1b_cell9_endpoint_replay_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell9_compact_kernel_result.json"
PINNED = {
    SCRIPT: "a6ca830e67557d28dee406bdcbec1d22cd43b49fb9d8af8af460bac02649f217",
    RESULT: "b1c5db4d2e0759455888787040271466ab59cdd99a584e7b3e34d170c41ae37d",
}
PRIME = 2130706433
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_endpoint_compatibility_decomposition",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_global_common_kernel",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas",
    "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    for path, expected in PINNED.items():
        require(digest(path) == expected, f"hash drift: {path.name}")
    payload = json.loads(RESULT.read_text())
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell9-endpoint-residual-v1"
            and payload["field"] == PRIME
            and payload["source_replay_sha256"] == digest(REPLAY)
            and payload["source_kernel_sha256"] == digest(KERNEL),
            "payload custody")
    signs = tuple(itertools.product((-1, 1), repeat=2))
    expected = {
        (source, endpoint, lane)
        for source in signs for endpoint in ("b", "c") for lane in signs
    }
    seen = set()
    for row in payload["rows"]:
        key = (tuple(row["epsilon"]), row["endpoint"], tuple(row["sigma"]))
        require(key in expected and key not in seen, "row coverage")
        seen.add(key)
        labels = {(item["point_index"], item["pairing_index"])
                  for item in row["rows"]}
        require(row["status"] == "COMPLETE" and row["source_points"] == 4
                and row["systems"] == 60 and row["unit_systems"] == 60
                and not row["nonunit_systems"] and len(row["rows"]) == 60
                and labels == set(itertools.product(range(4), range(15)))
                and all(item["unit"] and item["dimension"] == -1
                        and item["basis_size"] == 1 for item in row["rows"])
                and not row["stderr"], "unit ledger")
    require(seen == expected, "Cartesian row coverage")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(NODE.name in nodes and nodes[NODE.name]["status"] == "PROVED",
            "DAG node")
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    require(all((parent, NODE.name, "req") in edges for parent in PARENTS),
            "DAG parents")
    print("cell=9 generic_endpoint_systems=1920 unit=1920")


if __name__ == "__main__":
    main()
