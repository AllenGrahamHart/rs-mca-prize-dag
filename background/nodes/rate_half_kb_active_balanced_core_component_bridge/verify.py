#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = json.loads((Path(__file__).with_name("node.json")).read_text())

expected = {
    "rate_half_kb_active_balanced_core_witness_compiler",
    "rate_half_kb_active_bc_q6_endpoint_realization",
}
actual = {edge["from"] for edge in NODE["requires"]}
assert NODE["node"]["status"] == "CONDITIONAL"
assert actual == expected

for node_id in expected:
    matches = list(ROOT.glob(f"*/nodes/{node_id}/node.json"))
    assert len(matches) == 1, (node_id, matches)

proof = Path(__file__).with_name("conditional.md").read_text()
for token in ("(2,2,4)", "(2,4,2)", "(2,8,1)", "finite fiber"):
    assert token in proof

print("PASS active-BC component bridge conditional dependencies=2")
