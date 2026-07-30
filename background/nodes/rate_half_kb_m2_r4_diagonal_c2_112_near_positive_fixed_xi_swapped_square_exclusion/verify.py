#!/usr/bin/env python3
"""Verify the swapped chart contract and primary pair (0,0)."""

import hashlib
import json
import runpy
import sys
from pathlib import Path

NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
HELPER = (ROOT / "critical/nodes/rate_half_band_closure/notes/"
          "kb_c2_112_near_fixed_xi_square_direct.py")
EXPECTED = "d42b13b0cff26e448ad93e9925ce0e4283797d03c8a2f4d630175dddd457e5f3"
if hashlib.sha256(HELPER.read_bytes()).hexdigest() != EXPECTED:
    raise RuntimeError("primary helper hash")
statement = (NODE / "statement.md").read_text()
if "- **status:** PROVED" not in statement or "other 16 affine charts" not in statement:
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
sys.argv = [str(HELPER), "0", "0", "--swap"]
runpy.run_path(str(HELPER), run_name="__main__")
