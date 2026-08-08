#!/usr/bin/env python3
"""Verify the 24-cell aligned-negative literal certificate."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
PARENT = "rate_half_kb_m2_r4_diagonal_c2_112_source_line_literal_assignment_coverage"
HASHES = {
    "aligned_negative_literal_identity.sage": "e5f8aa2b6057348091cc128f2885ba2db1e048d842b09371a55e84aa800a7271",
    "aligned_negative_literal_identity_modal.py": "c1a9304b682d510897d23ebdaa69fb7dee729d986a37d3d25af55e87f507c075",
    "aligned_negative_literal_identity_all_output.json": "0837f56d5864c4104d56b42f1328c78518ee7a98aaf62db253fbbc43ec7c9227",
    "aligned_negative_literal_identity_long_generic_output.json": "10deb7aa34d47112918ad2ae24ed808122bca0b50a53988a19c95ce5a08bf9b9",
}
ASSIGNMENTS = (
    "F00", "F01", "F02", "F03", "F04", "F05",
    "F06", "F07", "M00", "M01", "M02", "M03",
)
CELLS = {
    f"{assignment}:{chart}"
    for assignment in ASSIGNMENTS
    for chart in ("generic", "sum-zero")
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


for name, expected in HASHES.items():
    observed = hashlib.sha256((NODE / name).read_bytes()).hexdigest()
    require(observed == expected, f"hash: {name}")

primary = json.loads((NODE / "aligned_negative_literal_identity_all_output.json").read_text())
long = json.loads((NODE / "aligned_negative_literal_identity_long_generic_output.json").read_text())
require(primary["schema"] == "kb-c2-112-aligned-negative-literal-identity-modal-v2", "primary schema")
require(long["schema"] == "kb-c2-112-aligned-negative-literal-identity-modal-v2", "long schema")
require(set(primary["results"]) == CELLS, "primary census")
require(set(long["results"]) == {"M01:generic", "M02:generic"}, "long census")
require(all(primary["results"][cell]["status"] == "TIMEOUT" for cell in long["results"]), "guard provenance")

rows = dict(primary["results"])
rows.update(long["results"])
require(set(rows) == CELLS, "merged census")
payloads = []
for cell in sorted(CELLS):
    row = rows[cell]
    require(row["status"] == "PASS" and row["returncode"] == 0, f"run: {cell}")
    payload = row["payload"]
    assignment, chart = cell.split(":")
    require(payload["schema"] == "kb-c2-112-aligned-negative-literal-identity-v2", f"schema: {cell}")
    require(payload["assignment"] == assignment and payload["chart"] == chart, f"identity: {cell}")
    require(payload["assignment_kind"] == ("fixed-moving" if assignment.startswith("F") else "moving-moving"), f"kind: {cell}")
    require(payload["omitted_row"] == (2 if chart == "generic" else 3), f"minor chart: {cell}")
    require(payload["cover_factor"] == ("c + d" if chart == "generic" else "c*d + 1"), f"cover factor: {cell}")
    require(payload["cover_factor_pass"] is True, f"cover: {cell}")
    require(payload["consistency_factor_count"] == 5, f"consistency factors: {cell}")
    expected_components = 1 if assignment.startswith("F") else 2
    require(payload["survivor_component_count"] == expected_components, f"components: {cell}")
    require(len(payload["components"]) == expected_components, f"component rows: {cell}")
    require(all(component["constant_identity_pass"] for component in payload["components"]), f"constant identities: {cell}")
    require(all(component["outer_identity_pass"] for component in payload["components"]), f"outer identities: {cell}")
    require(payload["constant_identity_pass"] and payload["outer_identity_pass"], f"aggregate identities: {cell}")
    require(payload["terminal"] == "ALIGNED_NEGATIVE_LITERAL_IDENTITIES_PASS", f"terminal: {cell}")
    payloads.append(payload)

require(Counter(item["assignment_kind"] for item in payloads) == Counter({"fixed-moving": 16, "moving-moving": 8}), "kind census")
require(Counter(item["chart"] for item in payloads) == Counter({"generic": 12, "sum-zero": 12}), "chart census")
require(Counter(item["common_vertex"] for item in payloads) == Counter({f"v{index}": 6 for index in range(4)}), "common census")
require(sum(item["survivor_component_count"] for item in payloads) == 32, "component census")

dag = json.loads((ROOT / "dag.json").read_text())
nodes = {item["id"]: item for item in dag["nodes"]}
edges = {(item["from"], item["to"], item["kind"]) for item in dag["edges"]}
require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
require((NODE_ID, PARENT, "ev") in edges, "consumer edge")

print(
    "KB_C2_112_ALIGNED_NEGATIVE_LITERAL_ASSIGNMENT_COVERAGE_PASS "
    "cells=24 fixed=16 moving=8 charts=12+12 components=32"
)
