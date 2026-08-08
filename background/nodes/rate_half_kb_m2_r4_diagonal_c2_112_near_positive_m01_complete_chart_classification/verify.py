#!/usr/bin/env python3
"""Verify the M01 complete-chart and quotient exclusion packet."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path


NODE = Path(__file__).resolve().parent
HASHES = {
    "direct_complete_chart_classify.sage": "27b814e963f42265b22591310a4fb1079a4dccc02cc779e718f7c330cfcd2620",
    "direct_complete_chart_classify_modal.py": "64b7de428278ba8759ffba7b36a4e993d5f6de19d6f78db4acad24ad5989a7c6",
    "direct_complete_chart_classification_output.json": "d3aa138ff815fc987ed6a870c97d787e6df2f969b5e61a0e1bda86004a78a6aa",
    "direct_complete_chart_audit.sage": "2b0be72a3c7d9f8345e2cee94ea3373efbab10acfcbaa4efcbe596de8c0b468d",
    "direct_complete_chart_audit_modal.py": "430ebf5d022405df64a5b871885ee419c70d547de09631d25adb4b130bb489bc",
    "direct_complete_chart_audit_output.json": "66e2c0b02cce3fdc4834ec563ebcea0a51c31112dc255c0c8e0f0afece6450b0",
    "m01_a_rl_field_sieve.sage": "58491201ff763ff1d2d89b7bb7ff3c2aa20a2bcd6670ddce816a0fa1bc99de3e",
    "m01_a_rl_field_sieve_modal.py": "42973336eb145ce51c9f89b31576958069f8e433f2167efcd23a99787b502c25",
    "m01_a_rl_field_sieve_output.json": "9e1170c54bc16132cfcd0b8d23cd014dd3cb9f68eb3e6eeb0ab6309a1fd8ed66",
    "m01_a_rl_first_quotient_probe.sage": "281be609ae3664cbf54c47bccf975deec5176bafdb91fb1b0700d0e05270ca37",
    "m01_a_rl_first_quotient_modal.py": "d68a37ecf390090d098701dd9abde3dd44b35f202bfe16f590d9830b8c697862",
    "m01_a_rl_first_quotient_output.json": "fbbdb3c0ae95beb4f5a7453cfa073d9423ce89d01412df90c9af67b9489f1a39",
}
CELLS = {
    "M01-A-RX", "M01-A-RL", "M01-A-RM",
    "M01-OB-RX", "M01-OB-RL", "M01-OB-RM",
}
EQUATION_DIGESTS = {
    "M01-A-RL": "ddfcca81c090d6b8d9e3e4d3182e46d8cd986669460bda44f13e239bb80dc0b0",
    "M01-A-RM": "483f6aa954d9372dd912ea14558f22ad82576a9ccd2da58d211e8e3154b98afd",
    "M01-A-RX": "834d9b667ab48607affaabd147ccad0803baca0a27b504200b2337b0e7957bbb",
    "M01-OB-RL": "10ff94658d47faf74ec087e1759192055359f7afee18ed033ce5b6d6d338c1b6",
    "M01-OB-RM": "735e697ca6b13b9ab5425774ec816ea0e5ac4c3aba95a8bdc4cede2f7fa5ff0b",
    "M01-OB-RX": "0f99cbb861c2f3403c5fac221cedf874bc157d89432703aba05f8e72979aa3be",
}
SURVIVOR_DIGEST = "340df1fa9c7cc15843f8d6043df5c70f27d8757c0e398ce620973ddcdc5cc1dd"
LOCALIZER_DIGEST = "a2255e8d33926ec265d309e516597a6beded506ec0bc9f3a86eab9d6a290a819"
LEX_BASIS = [
    "b^2 + 253153238*b - 400825962",
    "c + 1065353216",
    "d + 1",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


for name, expected in HASHES.items():
    require(hashlib.sha256((NODE / name).read_bytes()).hexdigest() == expected, f"hash: {name}")

primary = json.loads((NODE / "direct_complete_chart_classification_output.json").read_text())
require(primary["schema"] == "kb-c2-112-near-positive-m01-complete-chart-modal-v1", "primary schema")
require(set(primary["results"]) == CELLS, "primary cells")
for cell, row in primary["results"].items():
    require(row["status"] == "PASS" and row["returncode"] == 0, f"primary: {cell}")
    result = row["payload"]
    require(result["equation_count"] == 4, f"equations: {cell}")
    require(result["equation_tuple_sha256"] == EQUATION_DIGESTS[cell], f"digest: {cell}")
    require(result["recorded_localizer_count"] == 11, f"recorded: {cell}")
    require(result["complete_localizer_count"] == 15, f"complete: {cell}")
    if cell == "M01-A-RL":
        require(result["terminal"] == "COMPLETE_CHART_NONUNIT_IDEAL", "survivor terminal")
        require(result["dimension"] == 0 and result["basis_size"] == 3, "survivor dimension")
        require(result["basis_sha256"] == SURVIVOR_DIGEST, "survivor digest")
    else:
        require(result["terminal"] == "COMPLETE_CHART_UNIT_IDEAL", f"unit: {cell}")
        require(result["unit_ideal"] is True and result["progress"][-1]["basis_size"] == 1, f"basis: {cell}")

audit = json.loads((NODE / "direct_complete_chart_audit_output.json").read_text())
require(audit["schema"] == "kb-c2-112-near-positive-m01-complete-chart-audit-modal-v1", "audit schema")
require(set(audit["results"]) == CELLS, "audit cells")
for cell, row in audit["results"].items():
    require(row["status"] == "PASS" and row["returncode"] == 0, f"audit: {cell}")
    result = row["payload"]
    require(result["equation_tuple_sha256"] == EQUATION_DIGESTS[cell], f"audit digest: {cell}")
    require(result["localizer_count"] == 15, f"audit localizers: {cell}")
    require(result["localizer_product_degree"] == 25, f"audit degree: {cell}")
    require(result["localizer_product_terms"] == 464, f"audit terms: {cell}")
    require(result["localizer_product_sha256"] == LOCALIZER_DIGEST, f"audit product: {cell}")
    expected_unit = cell != "M01-A-RL"
    require(result["unit_ideal"] is expected_unit, f"audit class: {cell}")
    require(result["expected_unit_ideal"] is expected_unit, f"audit expected: {cell}")

field = json.loads((NODE / "m01_a_rl_field_sieve_output.json").read_text())
require(field["schema"] == "kb-c2-112-near-positive-m01-a-rl-field-sieve-modal-v1", "field schema")
require(field["result"]["status"] == "PASS", "field status")
field_result = field["result"]["payload"]
require(field_result["lex_basis"] == LEX_BASIS, "lex basis")
require(field_result["lex_basis_sha256"] == SURVIVOR_DIGEST, "lex digest")
require(field_result["localizer_count"] == 15, "field localizers")
require(field_result["terminal"] == "F_P6_COMPATIBLE_FACTOR_REMAINS", "field terminal")

quotient = json.loads((NODE / "m01_a_rl_first_quotient_output.json").read_text())
require(quotient["schema"] == "kb-c2-112-near-positive-m01-a-rl-first-quotient-modal-v1", "quotient schema")
require(quotient["result"]["status"] == "PASS", "quotient status")
quotient_result = quotient["result"]["payload"]
require(quotient_result["terminal"] == "FIRST_QUOTIENT_REJECTS_ALL", "quotient terminal")
require(quotient_result["orientations"] == 8 and quotient_result["residue_degree"] == 1, "orientations")
records = quotient_result["records"]
require(Counter((row["assignment"], row["orbit"]) for row in records) == Counter({
    ("M01", "A"): 2, ("M02", "A"): 2,
    ("M01", "TA"): 2, ("M02", "TA"): 2,
}), "literal companion census")
for row in records:
    require(row["complete_localizer_count"] == 15, "quotient localizer count")
    require(row["complete_localizers_nonzero"] is True, "quotient localizers")
    require(row["endpoint_passes"] == [True, True], "endpoint control")
    require(row["q_slice_pass"] is True, "q-slice control")
    require(row["first_quotient_norm_pass"] is False, "quotient rejection")
    require(row["first_mismatch_count"] == 299, "quotient mismatches")

print(
    "KB_C2_112_NEAR_POSITIVE_M01_COMPLETE_CHART_CLASSIFICATION_PASS "
    "direct_cells=6 unit=5 survivor_points=2 literal_points=8 quotient_rejected=8 frontier=6"
)
