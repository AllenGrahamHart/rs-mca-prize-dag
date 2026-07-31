#!/usr/bin/env python3
"""Verify the moving-moving a-xi mixed contract and one primary shard."""
import hashlib, json, os, runpy, sys
from pathlib import Path

NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
HELPER = ROOT / "critical/nodes/rate_half_band_closure/notes/kb_c2_112_near_moving_template_probe.py"
EXPECTED = "deb385db95bf5737a7eef419af359714829c19b5a92a63d087f0fc3451afd32c"
if hashlib.sha256(HELPER.read_bytes()).hexdigest() != EXPECTED:
    raise RuntimeError("primary helper hash")
statement = (NODE / "statement.md").read_text()
if "- **status:** PROVED" not in statement or "other two relative xi orbits" not in statement:
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
mode = os.environ.get("MOVING_A_MIXED_PRIMARY_MODE", "cores")
sys.argv = [str(HELPER), "a", "mixed", mode, "--prove"]
runpy.run_path(str(HELPER), run_name="__main__")
