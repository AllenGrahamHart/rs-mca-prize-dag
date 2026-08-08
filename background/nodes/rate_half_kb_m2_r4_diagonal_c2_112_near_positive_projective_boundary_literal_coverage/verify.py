#!/usr/bin/env python3
"""Verify the 48-cell literal projective-boundary packet."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path


NODE = Path(__file__).resolve().parent
HASHES = {
    "literal_boundary_classify.sage": "b095e6bd9dc9c0a8f58c8f96034f8650485e9cf41a4978e08a127a9492f66068",
    "literal_boundary_classify_modal.py": "53cd581574acd90e4f040adcb70810f77870ab899c086eb446f95bdf94744ed3",
    "literal_boundary_classification_output.json": "50fe7f422d8edd2e2600aa6ae7cf8abd98e7f04cea67a9d20609a7281ca1d3c7",
    "literal_boundary_sequential_audit_modal.py": "ad9efe70b883e8c2ea454b4d9b072765ab18783c20453ad1f2e453d57e80f0cc",
    "literal_boundary_sequential_audit_output.json": "a94b62570c0fc08f706501a0a442640d262430195ae276e17990ecaec13f38b7",
}
ASSIGNMENTS = (
    "F00", "F01", "F02", "F03", "F04", "F05",
    "F06", "F07", "M00", "M01", "M02", "M03",
)
ROOTS = ("A", "TA", "OB", "OI")
CELLS = {f"{assignment}-{root}" for assignment in ASSIGNMENTS for root in ROOTS}
UNIT_DIGEST = "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"
AGREEMENT_FIELDS = (
    "equation_tuple_sha256",
    "localizer_count",
    "localizer_product_degree",
    "localizer_product_terms",
    "localizer_product_sha256",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


for name, expected in HASHES.items():
    require(hashlib.sha256((NODE / name).read_bytes()).hexdigest() == expected, f"hash: {name}")

primary = json.loads((NODE / "literal_boundary_classification_output.json").read_text())
audit = json.loads((NODE / "literal_boundary_sequential_audit_output.json").read_text())
require(primary["schema"] == "kb-c2-112-near-positive-projective-boundary-literal-modal-v1", "primary schema")
require(audit["schema"] == "kb-c2-112-near-positive-projective-boundary-literal-sequential-audit-modal-v1", "audit schema")
require(set(primary["results"]) == CELLS == set(audit["results"]), "cell census")

equation_digests = set()
localizer_digests = set()
for cell in sorted(CELLS):
    assignment, root = cell.split("-")
    left = primary["results"][cell]
    right = audit["results"][cell]
    for label, row, mode in (("primary", left, "rabinowitsch"), ("audit", right, "sequential")):
        require(row["status"] == "PASS" and row["returncode"] == 0, f"{label}: {cell}")
        payload = row["payload"]
        require(payload["schema"] == "kb-c2-112-near-positive-projective-boundary-literal-cell-v1", f"payload schema: {cell}")
        require(payload["cell"] == cell and payload["assignment"] == assignment, f"identity: {cell}")
        require(payload["target_root"] == root, f"root: {cell}")
        require(payload["assignment_kind"] == ("fixed-moving" if assignment.startswith("F") else "moving-moving"), f"kind: {cell}")
        require(payload["saturation_mode"] == mode, f"mode: {cell}")
        require(payload["equation_count"] == 4, f"equations: {cell}")
        require(payload["localizer_count"] in (13, 14), f"localizers: {cell}")
        require(payload["unit_ideal"] is True, f"unit: {cell}")
        require(payload["basis_size"] == 1 and payload["basis_sha256"] == UNIT_DIGEST, f"basis: {cell}")
        require(payload["terminal"] == "LITERAL_BOUNDARY_UNIT_IDEAL", f"terminal: {cell}")
    require(all(left["payload"][key] == right["payload"][key] for key in AGREEMENT_FIELDS), f"certificate agreement: {cell}")
    equation_digests.add(left["payload"]["equation_tuple_sha256"])
    localizer_digests.add(left["payload"]["localizer_product_sha256"])

rows = [row["payload"] for row in primary["results"].values()]
require(Counter(row["assignment_kind"] for row in rows) == Counter({"fixed-moving": 32, "moving-moving": 16}), "kind census")
require(Counter(row["target_root"] for row in rows) == Counter({root: 12 for root in ROOTS}), "target census")
require(Counter(row["common_vertex"] for row in rows) == Counter({f"v{index}": 12 for index in range(4)}), "common census")
require(Counter(row["localizer_count"] for row in rows) == Counter({13: 32, 14: 16}), "localizer census")
require(len(equation_digests) == 48, "equation fingerprints")
require(len(localizer_digests) == 3, "localizer fingerprints")

print(
    "KB_C2_112_NEAR_POSITIVE_PROJECTIVE_BOUNDARY_LITERAL_COVERAGE_PASS "
    "cells=48 fixed=32 moving=16 roots=4 common_vertices=4 unit=48 audit=48"
)
