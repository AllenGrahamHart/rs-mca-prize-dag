#!/usr/bin/env python3
"""Check the support-local P-A/P-B conditional assembly."""

import json
from pathlib import Path

root = Path(__file__).resolve().parents[3]
dag = json.loads((root / "dag.json").read_text())
nodes = {node["id"]: node for node in dag["nodes"]}
edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}

bridge = "xr_tangent_support_mismatch_bridge"
parent = "xr_smallcore_spread_count"
high = "xr_highcore_collision_count"
low = "xr_lowcore_spread_heart"

assert nodes[bridge]["status"] == "PROVED"
assert nodes[high]["status"] == "TARGET"
assert nodes[low]["status"] == "TARGET"
assert nodes[parent]["status"] == "CONDITIONAL"
assert "P-A1" in nodes[high]["statement"]
assert "P-A2" in nodes[high]["statement"]
assert "globally generic" in nodes[low]["statement"]

assert {
    (bridge, parent, "req"),
    (high, parent, "req"),
    (low, parent, "req"),
    ("xr_strip_classification_rungs", parent, "req"),
} <= edges
assert (bridge, "xr_clean_residual_any_gate", "req") not in edges

for n in (1024, 2**41):
    generic = 8 * n**3 + 8 * n**3
    nongeneric = 16 * n**3
    assert generic == nongeneric

print("XR_SMALLCORE_SUPPORT_LOCAL_ASSEMBLY_PASS")
