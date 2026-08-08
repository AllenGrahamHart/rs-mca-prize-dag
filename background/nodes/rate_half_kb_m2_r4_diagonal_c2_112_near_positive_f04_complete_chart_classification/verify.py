#!/usr/bin/env python3
"""Verify the F04 complete-chart exclusion packet."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
HASHES = {
    "direct_complete_chart_classify.sage":
        "648207609ded916a62a544d5ce5bda2a0fa3434885b564298ec1dc449d5586f8",
    "direct_complete_chart_classify_modal.py":
        "fe2a32bc3aefc0801a95dfd46cecdf6db7e274384ec3acaddf403ce7314a0fdf",
    "direct_complete_chart_classification_output.json":
        "1e80a9e74711d649c8df2281117019bb6e02503ca81d40a0826df4c6895e5941",
    "direct_complete_chart_audit.sage":
        "31eaa8782c77751d38a3094d66ac02a148bc28ae4366c6c4cb8897ae88dacebf",
    "direct_complete_chart_audit_modal.py":
        "a102e6ce60100a894b2a4ce8125e08d1c6c121dae46fcc5a168a7ca52dad6426",
    "direct_complete_chart_audit_output.json":
        "b0460a44f92d885944ef3916bbdf0c8295e04ef7a3442057e5683c949d0f60aa",
}
CELLS = {
    "F04-A-RX", "F04-A-RL", "F04-A-RM",
    "F04-OB-RX", "F04-OB-RL", "F04-OB-RM",
}
EQUATION_DIGESTS = {
    "F04-A-RL": "851145047a1909d9ecc7b352b1ae2fb359791d137514c44f5ac774206056bbcb",
    "F04-A-RM": "482525689e7c45a46a48dd14973858ad9f2742d48ac2d12b877723524857c0f7",
    "F04-A-RX": "dfa14073e2ca51e53a5c5a2ca69a618ed6a16c341ae7cc7947cd4bdb2ca0de2b",
    "F04-OB-RL": "1684c501cbf5ee04edf64fac4b53dd9ce5c3fb78604ffcdc101842b2de289716",
    "F04-OB-RM": "e421b9fc4ca8db936e207371ed80d577bd58cfab0ee1af397d7e57dca389b32d",
    "F04-OB-RX": "db3231f22134f5c3b2da7ca5f5c45884e4278b017f5da722d13e598bc6ee1430",
}
TERMINAL_FACTORS = {
    "F04-A-RL": (7, "recorded:b*c - 1"),
    "F04-A-RM": (15, "chart:c-d"),
    "F04-A-RX": (7, "recorded:b*c - 1"),
    "F04-OB-RL": (7, "recorded:b*c - 1"),
    "F04-OB-RM": (15, "chart:c-d"),
    "F04-OB-RX": (
        11,
        "recorded:b^2*c^2*d - b*c^2 - b*c*d - b^2 + b*c + b*d - c*d + c",
    ),
}
LOCALIZER_DIGEST = (
    "9776700913d12aba7cc9e506024dd43ba8d27c00a6f3a2ddf2838ee16fa152b2"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


for name, expected in HASHES.items():
    actual = hashlib.sha256((NODE / name).read_bytes()).hexdigest()
    require(actual == expected, f"hash: {name}")

primary = json.loads(
    (NODE / "direct_complete_chart_classification_output.json").read_text()
)
require(
    primary["schema"] == "kb-c2-112-near-positive-f04-complete-chart-modal-v1",
    "primary schema",
)
require(set(primary["results"]) == CELLS, "primary cells")

for cell, row in primary["results"].items():
    require(row["status"] == "PASS" and row["returncode"] == 0, f"primary: {cell}")
    result = row["payload"]
    require(result["cell"] == cell and result["equation_count"] == 4, f"equations: {cell}")
    require(result["equation_tuple_sha256"] == EQUATION_DIGESTS[cell], f"digest: {cell}")
    require(result["recorded_localizer_count"] == 12, f"recorded: {cell}")
    require(result["complete_localizer_count"] == 16, f"complete: {cell}")
    require(result["unit_ideal"] is True, f"unit: {cell}")
    require(result["terminal"] == "COMPLETE_CHART_UNIT_IDEAL", f"terminal: {cell}")
    final = result["progress"][-1]
    require(final["unit"] is True and final["basis_size"] == 1, f"basis: {cell}")
    require((final["index"], final["factor"]) == TERMINAL_FACTORS[cell], f"factor: {cell}")

audit = json.loads((NODE / "direct_complete_chart_audit_output.json").read_text())
require(
    audit["schema"] == "kb-c2-112-near-positive-f04-complete-chart-audit-modal-v1",
    "audit schema",
)
require(set(audit["results"]) == CELLS, "audit cells")

for cell, row in audit["results"].items():
    require(row["status"] == "PASS" and row["returncode"] == 0, f"audit: {cell}")
    result = row["payload"]
    require(result["cell"] == cell and result["equation_count"] == 4, f"audit equations: {cell}")
    require(result["equation_tuple_sha256"] == EQUATION_DIGESTS[cell], f"audit digest: {cell}")
    require(result["localizer_count"] == 16, f"localizers: {cell}")
    require(result["localizer_product_degree"] == 26, f"degree: {cell}")
    require(result["localizer_product_terms"] == 562, f"terms: {cell}")
    require(result["localizer_product_sha256"] == LOCALIZER_DIGEST, f"product: {cell}")
    require(result["basis_size"] == 1 and result["unit_ideal"] is True, f"audit unit: {cell}")
    require(result["terminal"] == "RABINOWITSCH_UNIT_IDEAL", f"audit terminal: {cell}")

print(
    "KB_C2_112_NEAR_POSITIVE_F04_COMPLETE_CHART_CLASSIFICATION_PASS "
    "cells=6 primary=sequential_saturation audit=rabinowitsch frontier=18"
)
