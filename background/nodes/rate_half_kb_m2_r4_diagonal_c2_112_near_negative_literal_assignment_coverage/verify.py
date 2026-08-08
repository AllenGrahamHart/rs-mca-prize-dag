#!/usr/bin/env python3
"""Verify the 48-cell near-negative literal certificate."""

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
    "near_negative_literal_classify.sage": "9e0c4c1af8d1c46e4b138ed5583d69a81a514fc48e6edfed0b0d0677f68881db",
    "near_negative_literal_classify_modal.py": "66801696eae7078ea2671e63c146000a84b618b2ded3bac39a45645d541cb918",
    "near_negative_literal_all_output.json": "15aee9e84681ad08447606f5342dac924d327336859042492ff872e45422f47d",
    "near_negative_literal_all_sequential_output.json": "95050b6e0f925dbaefb2db75115ebf9c89f43e8075534d6a33eee69df436dfa7",
}
ASSIGNMENTS = (
    "F00", "F01", "F02", "F03", "F04", "F05",
    "F06", "F07", "M00", "M01", "M02", "M03",
)
ROOTS = ("A", "TA", "OB", "OI")
CELLS = {f"{assignment}-{root}" for assignment in ASSIGNMENTS for root in ROOTS}
UNIT_DIGEST = "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"
AGREEMENT_FIELDS = (
    "assignment", "assignment_kind", "common_vertex", "target_root",
    "minus_branch", "consistency_factor_count", "survivor_component_count",
    "localizer_count", "localizer_product_degree", "localizer_product_terms",
    "localizer_product_sha256",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


for name, expected in HASHES.items():
    observed = hashlib.sha256((NODE / name).read_bytes()).hexdigest()
    require(observed == expected, f"hash: {name}")

primary = json.loads((NODE / "near_negative_literal_all_output.json").read_text())
audit = json.loads((NODE / "near_negative_literal_all_sequential_output.json").read_text())
require(primary["schema"] == "kb-c2-112-near-negative-literal-modal-v1", "primary schema")
require(audit["schema"] == "kb-c2-112-near-negative-literal-modal-v1", "audit schema")
require(primary["saturation_mode"] == "rabinowitsch", "primary mode")
require(audit["saturation_mode"] == "sequential", "audit mode")
require(set(primary["results"]) == CELLS == set(audit["results"]), "cell census")

payloads = []
equation_digests = set()
localizer_digests = set()
component_count = 0
for cell in sorted(CELLS):
    left = primary["results"][cell]
    right = audit["results"][cell]
    assignment, root = cell.split("-")
    for label, row, mode in (("primary", left, "rabinowitsch"), ("audit", right, "sequential")):
        require(row["status"] == "PASS" and row["returncode"] == 0, f"{label}: {cell}")
        payload = row["payload"]
        require(payload["schema"] == "kb-c2-112-near-negative-literal-cell-v1", f"schema: {cell}")
        require(payload["cell"] == cell and payload["assignment"] == assignment, f"identity: {cell}")
        require(payload["target_root"] == root, f"root: {cell}")
        require(payload["assignment_kind"] == ("fixed-moving" if assignment.startswith("F") else "moving-moving"), f"kind: {cell}")
        require(payload["saturation_mode"] == mode, f"mode: {cell}")
        require(payload["consistency_factor_count"] == 5, f"consistency factors: {cell}")
        expected_components = 1 if assignment.startswith("F") else 2
        require(payload["survivor_component_count"] == expected_components, f"components: {cell}")
        require(len(payload["components"]) == expected_components, f"component rows: {cell}")
        require(payload["localizer_count"] in (23, 24), f"localizers: {cell}")
        require(payload["terminal"] == "NEAR_NEGATIVE_LITERAL_UNIT", f"terminal: {cell}")
        for component in payload["components"]:
            require(component["equation_count"] == 5, f"equations: {cell}")
            require(component["saturation_mode"] == mode, f"component mode: {cell}")
            require(component["unit_ideal"] is True, f"unit: {cell}")
            require(component["basis_size"] == 1 and component["basis_sha256"] == UNIT_DIGEST, f"basis: {cell}")
    require(all(left["payload"][field] == right["payload"][field] for field in AGREEMENT_FIELDS), f"payload agreement: {cell}")
    left_components = left["payload"]["components"]
    right_components = right["payload"]["components"]
    require([item["factor_sha256"] for item in left_components] == [item["factor_sha256"] for item in right_components], f"factor agreement: {cell}")
    require([item["equation_tuple_sha256"] for item in left_components] == [item["equation_tuple_sha256"] for item in right_components], f"equation agreement: {cell}")
    component_count += len(left_components)
    equation_digests.update(item["equation_tuple_sha256"] for item in left_components)
    localizer_digests.add(left["payload"]["localizer_product_sha256"])
    payloads.append(left["payload"])

require(Counter(item["assignment_kind"] for item in payloads) == Counter({"fixed-moving": 32, "moving-moving": 16}), "kind census")
require(Counter(item["target_root"] for item in payloads) == Counter({root: 12 for root in ROOTS}), "root census")
require(Counter(item["common_vertex"] for item in payloads) == Counter({f"v{index}": 12 for index in range(4)}), "common census")
require(Counter(item["localizer_count"] for item in payloads) == Counter({23: 24, 24: 24}), "localizer count census")
require(component_count == 64 and len(equation_digests) == 64, "component census")
require(len(localizer_digests) == 48, "localizer fingerprints")

dag = json.loads((ROOT / "dag.json").read_text())
nodes = {item["id"]: item for item in dag["nodes"]}
edges = {(item["from"], item["to"], item["kind"]) for item in dag["edges"]}
require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
require((NODE_ID, PARENT, "ev") in edges, "consumer edge")

print(
    "KB_C2_112_NEAR_NEGATIVE_LITERAL_ASSIGNMENT_COVERAGE_PASS "
    "cells=48 fixed=32 moving=16 components=64 primary=64 audit=64"
)
