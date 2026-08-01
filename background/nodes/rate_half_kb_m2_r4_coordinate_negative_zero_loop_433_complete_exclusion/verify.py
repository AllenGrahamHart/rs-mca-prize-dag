#!/usr/bin/env python3
"""Verify structure and exact shard coverage for the complete exclusion."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_complete_exclusion"
)
SPEC = importlib.util.spec_from_file_location("check", NODE / "check.py")
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    CHECK.ROUTER.field_audit()
    shards = (
        "verify_cell12_z2.py", "verify_cell12_z3.py",
        "verify_cell13.py", "verify_cell14.py",
    )
    require(all((NODE / shard).is_file() for shard in shards), "shard coverage")
    statement = (NODE / "statement.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("no complete negative zero-loop 433 packet" in statement, "claim")
    require("384" in statement and "algebraic" in statement,
            "family exactness")
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    parent = (
        "rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_"
        "complete_vieta_exclusion_router"
    )
    require((parent, NODE_ID, "req") in edges, "dependency")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    print(
        "RATE_HALF_KB_ZERO_LOOP_433_COMPLETE_EXCLUSION_VERIFY_PASS "
        "shards=4 family_certificates=384"
    )


if __name__ == "__main__":
    main()
