#!/usr/bin/env python3
"""Verify the positive 433-1b cell-14 fixed-a chain exclusion."""

import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
FILES = {
    "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_flint_profile_modal.py":
        "68d5e882b92e3ac9a824a4fb8429487d7f71a732efd3820970cc6785592f50db",
    "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_flint_profile_result.json":
        "29d4bbe4a44ab2f743ff63e2c2440037302faa9c0aca1b627e2053bdba6be3dc",
    "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_root_replay_modal.py":
        "06ad966aeffcccc5a2442f36d14acec6a7fcb984eb062e3456eb1313c6e75c67",
    "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_root_replay_result.json":
        "8ec021bb765e1ce82b5d765083a87860d123ba75c23f66cf4058911bdea286eb",
    "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_census.py":
        "1788c48729c5a3cf84b05fa67e9447baeb3869cf3c0629a1be195b5f30ee716d",
    "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_census_result.json":
        "fb1f069d18e21490ebdda77c89c0e3f6e0524aa8de442be2c73f684dbfe1f8ce",
}
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell14_quadratic_curve_structure",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas",
    "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell14_rankone_target_projection_exclusion",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    result = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024*1024), b""):
            result.update(block)
    return result.hexdigest()


def verify_payload(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell14-fixed-a-census-v1", "schema")
    require(payload["status"] == "PASS", "status")
    require(payload["case_count"] == 432 and
            payload["remaining_allmixed_case_count"] == 144, "case census")
    require(payload["root_count"] == 9456 and
            payload["guard_boundary_count"] == 5248 and
            payload["checked_root_count"] == 4208, "root census")
    require(payload["direct_fiber_count"] == 8736 and
            payload["target_boundary_count"] == 480, "fiber census")
    require(payload["maximum_eliminant_degree"] == 15680 and
            payload["decompressed_eliminant_bytes"] == 84729848,
            "eliminant census")
    require(payload["compiler_sha256"] == FILES[
        "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_flint_profile_modal.py"],
        "compiler custody")
    require(payload["ledger_sha256"] == FILES[
        "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_flint_profile_result.json"],
        "ledger custody")
    require(payload["replay_script_sha256"] == FILES[
        "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_root_replay_modal.py"],
        "replay source custody")
    require(payload["replay_sha256"] == FILES[
        "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_root_replay_result.json"],
        "replay custody")


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(NODE_ID in nodes and nodes[NODE_ID]["status"] == "PROVED", "DAG node")
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges, f"parent: {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")


def main():
    for name, expected in FILES.items():
        require(digest(EXPERIMENTS / name) == expected, f"custody: {name}")
    payload = json.loads((EXPERIMENTS /
        "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_census_result.json").read_text())
    verify_payload(payload)
    verify_dag()
    print("cell14 fixed-a chain: cases=432 roots=9456 retained=144")


if __name__ == "__main__":
    main()
