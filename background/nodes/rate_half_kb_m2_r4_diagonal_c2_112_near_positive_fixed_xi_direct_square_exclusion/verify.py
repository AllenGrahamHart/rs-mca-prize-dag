#!/usr/bin/env python3
"""Replay primary left-line shard zero and verify the node contract."""

import hashlib
import json
import runpy
import sys
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
HELPER = (ROOT / "critical/nodes/rate_half_band_closure/notes/"
          "kb_c2_112_near_fixed_xi_square_direct.py")
EXPECTED = "7d3892fddcb4ab95f1fd6f6fa58127cf77c72c024e3272fab9511152df27db93"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


statement = (NODE / "statement.md").read_text()
require("- **status:** PROVED" in statement, "status")
require("other 17 affine positive charts" in statement, "scope fence")
require(hashlib.sha256(HELPER.read_bytes()).hexdigest() == EXPECTED,
        "primary helper hash")
dag = json.loads((ROOT / "dag.json").read_text())
nodes = {node["id"]: node for node in dag["nodes"]}
require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
parents = {
    "rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction",
    "rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate",
}
require(all((parent, NODE_ID, "req") in edges for parent in parents),
        "DAG dependencies")
require((NODE_ID, "rate_half_band_closure", "ev") in edges, "DAG consumer")
sys.argv = [str(HELPER), "0"]
runpy.run_path(str(HELPER), run_name="__main__")
