#!/usr/bin/env python3
"""Verify the positive 433-1b/O0a signed-edge atlas."""

import hashlib
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
SCRIPT = (
    ROOT / "experiments/prize_resolution/"
    "rate_half_kb_positive_433_1b_o0a_signed_edge_atlas.py"
)
SCRIPT_HASH = "608f4cd11fd9250a72fa6c18a2edda0bdc52b53068b09c0f5278dfc742254e22"
NODE_ID = "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas"
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_residual_loop_workboard",
    "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load_atlas():
    require(hashlib.sha256(SCRIPT.read_bytes()).hexdigest() == SCRIPT_HASH,
            "script custody")
    spec = importlib.util.spec_from_file_location("positive_433_1b_o0a", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    atlas = load_atlas()
    orbits, lanes, defect = atlas.verify()
    require(len(orbits) == 4 and [row[3] for row in orbits] == [32]*4,
            "orbit census")
    require([(row[0], row[1]) for row in orbits] == [
        (-1, -1), (-1, 1), (1, -1), (1, 1),
    ], "orbit invariants")
    require(set(lanes) == {(-1, -1), (-1, 1), (1, -1), (1, 1)} and
            all(len(rows) == 12 for rows in lanes.values()), "lane census")
    require(defect == {
        "loop_A": 1,
        "BC_split_1_plus_1": 0,
        "DE_split_2_plus_1": 2,
        "all_singletons": 0,
        "total": 3,
    }, "defect ledger")

    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement and
            "exactly four gauge orbits of" in statement and
            "128 raw active-sign assignments" in statement,
            "statement claim")
    require("No source placement" in contract and "Prize closure" in contract,
            "contract fence")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in PARENTS:
        require(nodes[parent]["status"] == "PROVED", f"parent {parent}")
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    print("positive 433-1b/O0a signed-edge atlas verified")


if __name__ == "__main__":
    main()
