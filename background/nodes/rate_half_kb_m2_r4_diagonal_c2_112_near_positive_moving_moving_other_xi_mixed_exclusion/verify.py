#!/usr/bin/env python3
"""Verify the mixed other-xi node contract and artifact ledger."""

import json
from pathlib import Path

from verify_runner import audit, check_hashes


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
statement = (NODE / "statement.md").read_text()
if "- **status:** PROVED" not in statement or "last of the 18" not in statement:
    raise RuntimeError("statement contract")
dag = json.loads((ROOT / "dag.json").read_text())
nodes = {node["id"]: node for node in dag["nodes"]}
if nodes[NODE.name]["status"] != "PROVED":
    raise RuntimeError("DAG status")
edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
parents = {
    "rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction",
    "rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate",
}
if not all((parent, NODE.name, "req") in edges for parent in parents):
    raise RuntimeError("DAG dependencies")
if (NODE.name, "rate_half_band_closure", "ev") not in edges:
    raise RuntimeError("DAG consumer")
check_hashes()
audit("artifacts")
print("KB_C2_112_NEAR_MOVING_OTHER_MIXED_VERIFY_PASS")
