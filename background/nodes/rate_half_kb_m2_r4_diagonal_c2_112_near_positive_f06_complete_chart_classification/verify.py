#!/usr/bin/env python3
"""Verify the F06 complete-chart exclusion packet."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
HASHES = {
    "direct_complete_chart_classify.sage": "24bc724ddcf77e29605404090f5a3fefa05269fd0d6897cb63761079b7216e39",
    "direct_complete_chart_classify_modal.py": "e5e11bfd2e6240e988ea39cb928f039ec713ae70d16dff260092dbb4c6ff79a2",
    "direct_complete_chart_classification_output.json": "6c5cd3f8f3502bf0ec42a7255027ab434b8099e9e749435cc564555cf540f46d",
    "direct_complete_chart_audit.sage": "c3eaeb6866f95d71ab086d4087fa823a7d9b37d71c5fa18d150681d13e89947c",
    "direct_complete_chart_audit_modal.py": "42604aa6b69bf5b6ba4c6f20a6b22dd592b04bf5ca80090353a64b80268184f4",
    "direct_complete_chart_audit_output.json": "0d8ecaf55b445900e4a59d4ad1f1fa0a0fdb97eb2093718eb08db4c660ef05eb",
}
CELLS = {
    "F06-A-RX", "F06-A-RL", "F06-A-RM",
    "F06-OB-RX", "F06-OB-RL", "F06-OB-RM",
}
EQUATION_DIGESTS = {
    "F06-A-RL": "6e5bdc3ea08b112c23bf86c11a0b138d078557fcc8c0c5cec34426192df3fdbe",
    "F06-A-RM": "4d9164308a864fa53c0078cf4a0d3aedf053cc7927aa9208efdb82d42a10b182",
    "F06-A-RX": "89fa40a0cae53abfa1a2f6562b0e273a91728c7f06a06129621f6e8020935d42",
    "F06-OB-RL": "b9e1220cbd8ce5eac30c8cbc08245d25dd34118147e3ec4d49e27ec2524ef6ab",
    "F06-OB-RM": "d13ac0b7d1addb89d8afecce2677a062cbdd60b0b9af03c4c07018c30002d72e",
    "F06-OB-RX": "8ecf00bf8aff9d070c80f7056c42f4b71ef1d6f110c77fbc3c69d779637dd733",
}
TERMINAL_FACTORS = {
    "F06-A-RL": (7, "recorded:b*c - 1"),
    "F06-A-RM": (15, "chart:c-d"),
    "F06-A-RX": (7, "recorded:b*c - 1"),
    "F06-OB-RL": (7, "recorded:b*c - 1"),
    "F06-OB-RM": (15, "chart:c-d"),
    "F06-OB-RX": (11, "recorded:b^2*c^2*d - b*c^2 - b*c*d - b^2 + b*c + b*d - c*d + c"),
}
LOCALIZER_DIGEST = "f29b4351caccad2aabb06696f4bb5b0b6526ec572b96dbe09dabd42526a1a96b"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


for name, expected in HASHES.items():
    require(hashlib.sha256((NODE / name).read_bytes()).hexdigest() == expected, f"hash: {name}")

primary = json.loads((NODE / "direct_complete_chart_classification_output.json").read_text())
require(primary["schema"] == "kb-c2-112-near-positive-f06-complete-chart-modal-v1", "primary schema")
require(set(primary["results"]) == CELLS, "primary cells")
for cell, row in primary["results"].items():
    require(row["status"] == "PASS" and row["returncode"] == 0, f"primary: {cell}")
    result = row["payload"]
    require(result["cell"] == cell and result["equation_count"] == 4, f"equations: {cell}")
    require(result["equation_tuple_sha256"] == EQUATION_DIGESTS[cell], f"digest: {cell}")
    require(result["recorded_localizer_count"] == 12, f"recorded: {cell}")
    require(result["complete_localizer_count"] == 16, f"complete: {cell}")
    require(result["unit_ideal"] is True and result["terminal"] == "COMPLETE_CHART_UNIT_IDEAL", f"unit: {cell}")
    final = result["progress"][-1]
    require(final["unit"] is True and final["basis_size"] == 1, f"basis: {cell}")
    require((final["index"], final["factor"]) == TERMINAL_FACTORS[cell], f"factor: {cell}")

audit = json.loads((NODE / "direct_complete_chart_audit_output.json").read_text())
require(audit["schema"] == "kb-c2-112-near-positive-f06-complete-chart-audit-modal-v1", "audit schema")
require(set(audit["results"]) == CELLS, "audit cells")
for cell, row in audit["results"].items():
    require(row["status"] == "PASS" and row["returncode"] == 0, f"audit: {cell}")
    result = row["payload"]
    require(result["cell"] == cell and result["equation_count"] == 4, f"audit equations: {cell}")
    require(result["equation_tuple_sha256"] == EQUATION_DIGESTS[cell], f"audit digest: {cell}")
    require(result["localizer_count"] == 16, f"localizers: {cell}")
    require(result["localizer_product_degree"] == 26, f"degree: {cell}")
    require(result["localizer_product_terms"] == 566, f"terms: {cell}")
    require(result["localizer_product_sha256"] == LOCALIZER_DIGEST, f"product: {cell}")
    require(result["basis_size"] == 1 and result["unit_ideal"] is True, f"audit unit: {cell}")
    require(result["terminal"] == "RABINOWITSCH_UNIT_IDEAL", f"audit terminal: {cell}")

print(
    "KB_C2_112_NEAR_POSITIVE_F06_COMPLETE_CHART_CLASSIFICATION_PASS "
    "cells=6 primary=sequential_saturation audit=rabinowitsch frontier=12"
)
