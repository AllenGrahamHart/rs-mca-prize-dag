#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
node = json.loads((HERE / "node.json").read_text())
deps = {edge["from"] for edge in node["requires"]}
expected = {
    "rate_half_kb_active_balanced_core_witness_compiler",
    "rate_half_mca_order32_partial_relative_harvest",
}
assert node["node"]["status"] == "PROVED"
assert deps == expected

for dep in deps:
    matches = list(ROOT.glob(f"*/nodes/{dep}/node.json"))
    assert len(matches) == 1
    assert json.loads(matches[0].read_text())["node"]["status"] == "PROVED"

schema = json.loads((ROOT / "critical/nodes/rate_half_kb_active_balanced_core_witness_compiler/certificate_schema.json").read_text())
assert schema["row"]["agreement"] == 1116048
assert schema["canonical_selector"]["selected_per_active_slope"] == 1

proof = (HERE / "proof.md").read_text()
for token in ("at most 31", "32-element slope subset", "maximal agreement set", "No endpoint record"):
    assert token in proof

print("PASS active-BC order32 adapter threshold=31 tuple_size=32 owner_preserved=1")
