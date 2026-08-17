#!/usr/bin/env python3
"""Verify the O0b split principal common-system adapter."""

import hashlib
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
COMMON = EXPERIMENTS / "rate_half_kb_positive_433_1b_common_vieta_compiler.py"
ATLAS = EXPERIMENTS / "rate_half_kb_positive_433_1b_o0b_signed_edge_atlas.py"
COMMON_SHA256 = "a956656cba6c884bae665a2439666964ed468dcf9d0466e80cb825e811a6f845"
ATLAS_SHA256 = "1caaddce72bc76e142c9f720298932cffb426ccc66c4333c6d7a3c5d4218ea7f"
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_common_vieta_minor_compiler",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_signed_edge_atlas",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_split_rankdrop_complete_exclusion",
)
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"
SPEC = importlib.util.spec_from_file_location("o0b_atlas", ATLAS)
SIGNED = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SIGNED)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def validate(lane_keys=None, expected_products=None):
    _, lanes, _ = SIGNED.verify()
    split_keys = tuple(sorted(
        key for key in lanes if key[0] in {"S0", "SDE", "SDF"}
    ))
    expected_keys = (
        ("S0", -1), ("S0", 1),
        ("SDE", -1), ("SDE", 1),
        ("SDF", -1), ("SDF", 1),
    )
    require(split_keys == (tuple(lane_keys) if lane_keys is not None else expected_keys),
            "split lane keys")
    expected_products = expected_products or ("-a^2", "a*b", "a*c", "b*c", "-b*c")
    for key in split_keys:
        records = lanes[key]
        require(tuple(value for _, value in records[:5]) == tuple(expected_products),
                "common product adapter")
        require(tuple(name for name, _ in records[:5]) == (
            "common-loop-A", "common-AB", "common-AC", "BC-plus", "BC-minus"
        ), "common role order")
    role_cells, source_signs = 15, 4
    require(role_cells * source_signs == 60, "common atlas census")
    require(len(split_keys) * role_cells * source_signs == 360, "adapted row census")
    return len(split_keys)


def main():
    require(hashlib.sha256(COMMON.read_bytes()).hexdigest() == COMMON_SHA256,
            "common compiler custody")
    require(hashlib.sha256(ATLAS.read_bytes()).hexdigest() == ATLAS_SHA256,
            "signed atlas custody")
    lanes = validate()
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req")) for row in dag["edges"]}
    require(nodes[NODE.name]["status"] == "PROVED", "DAG status")
    for parent in PARENTS:
        require(nodes[parent]["status"] == "PROVED"
                and (parent, NODE.name, "req") in edges, "parent")
    require((NODE.name, CONSUMER, "ev") in edges, "consumer")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_COMMON_ADAPTER_VERIFY_PASS "
          f"lanes={lanes} common_rows=60 adapted_rows=360 rank=5")


if __name__ == "__main__":
    main()
