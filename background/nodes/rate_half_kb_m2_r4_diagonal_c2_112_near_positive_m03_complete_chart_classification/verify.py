#!/usr/bin/env python3
"""Verify the M03 complete-chart and quotient exclusion packet."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path


NODE = Path(__file__).resolve().parent
HASHES = {
    "direct_complete_chart_classify.sage": "307e6085ce9197a4bf9509a968b17db81916cd7a0f668ed94f942fcfc376d980",
    "direct_complete_chart_classify_modal.py": "f93f2beb9bd82cbf62952ec61a6f2281bdfd2398e03ab84e8eb27c0fe0660613",
    "direct_complete_chart_classification_output.json": "a06471bf0fd676644e2ffd8d16108835c437ca32d3ea2d5d71332a63a354f96d",
    "direct_complete_chart_audit.sage": "8b5356b26e4d11708849787869541c50612eb5052f31fbc120d4ebcd83a63b2f",
    "direct_complete_chart_audit_modal.py": "4a8dafcab3b459759e0dd88a05fa5f7530be5fa5fb8df9f17fd5c13e383b0675",
    "direct_complete_chart_audit_output.json": "c9641f2d1658927e008583a7ff50b4fbb09c30ed3172d8c02b487d43121400d1",
    "m03_ob_rl_field_sieve.sage": "3b4abd06c88a729cdd57537242bc0bdab4a7b62f118b41c5fcb8a675db00cd35",
    "m03_ob_rl_field_sieve_modal.py": "a9f1709a896538d0e915fbe5f843e225098d861d4748e4d99733936dfad93a57",
    "m03_ob_rl_field_sieve_output.json": "d704fcd22a00959b1980dd6b598c88ac8ad6354808c3f3838629d0cb39fd84bc",
    "m03_ob_rl_first_quotient_probe.sage": "559d0327507bfcf6e7ec563f92c46a51e7ae6fb4e2743c2bb175a962a55b1211",
    "m03_ob_rl_first_quotient_modal.py": "c367faf6bcabd225d8cdac8e4309c017805079d9c82d3237cbc0dcd404c13fad",
    "m03_ob_rl_first_quotient_output.json": "be4c7d04c4dd24cf5d45816c083c3237f32721e6ed13634605aee85442e648e0",
}
CELLS = {
    "M03-A-RX", "M03-A-RL", "M03-A-RM",
    "M03-OB-RX", "M03-OB-RL", "M03-OB-RM",
}
EQUATION_DIGESTS = {
    "M03-A-RL": "943ab987e8392b91b0e1b8a90702faa5a6d8209b88a563a13a579feb13e5f5b9",
    "M03-A-RM": "5ab0d40ec95746620743fb6bbb1b9a9ff088107e62619ba7ceb6c0d5c0277cc8",
    "M03-A-RX": "c9ce453a3c66cf949811275d896f16f02282fa3061ae81e87155b25d3e95bca8",
    "M03-OB-RL": "429fa5ad98e19e14bbced4bbe182e7dbed2b00b6a20bc8ede240ca40dd541e3a",
    "M03-OB-RM": "f885d4a2d1b8b23546e26b7e6170e79ba7507beacd5a2d3baa30426be5f7f898",
    "M03-OB-RX": "641e2f2c40048332ef85b3c72d5f0cc64e3f90eac700c00ba2e774a76412f818",
}
PRIMARY_SURVIVOR_DIGEST = "4006c1563f261cf7fcbb0e5d4023443e7b3a28841f944f6408bb7ca6d81e76a1"
LOCALIZER_DIGEST = "51788fdf71e758362bba74b0c96bde7f330dc088d19eff63d335c127ba877efc"
UNIT_BASIS_DIGEST = "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"
AUDIT_SURVIVOR_DIGEST = "71d676489038b0111eb1f8a047e67f4fe668c543321ca352c8944e5f2ba4ccfa"
LEX_BASIS = [
    "b + c^3 + 819502469*c^2 - 327800980*c + 819502469",
    "c^4 + 819502469*c^3 - 327800980*c^2 + 819502469*c + 1",
    "d + 1",
]
C_FACTORS = [
    "c^2 + 148474327*c + 1",
    "c^2 + 671028142*c + 1",
]
MISMATCH_DIGESTS = {
    "137782ab9d113674cedc23b452faaa83590080b63c407e7a1e123261c79b15e6",
    "7273685d2dbaa51af218b0efff2111b341e438616a6b583012eb3dc62b1a38ad",
    "352d1f1fd85c9769608b5e31cdfd1bf1796f5bfa5980d39a5df070cd26ace773",
    "1d2866b6214484e000339201f85b049232233580562cddace2d10e238af3932a",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


for name, expected in HASHES.items():
    require(hashlib.sha256((NODE / name).read_bytes()).hexdigest() == expected, f"hash: {name}")

primary = json.loads((NODE / "direct_complete_chart_classification_output.json").read_text())
require(primary["schema"] == "kb-c2-112-near-positive-m03-complete-chart-modal-v1", "primary schema")
require(set(primary["results"]) == CELLS, "primary cells")
for cell, row in primary["results"].items():
    require(row["status"] == "PASS" and row["returncode"] == 0, f"primary: {cell}")
    result = row["payload"]
    require(result["equation_count"] == 4, f"equations: {cell}")
    require(result["equation_tuple_sha256"] == EQUATION_DIGESTS[cell], f"digest: {cell}")
    require(result["recorded_localizer_count"] == 11, f"recorded: {cell}")
    require(result["complete_localizer_count"] == 15, f"complete: {cell}")
    if cell == "M03-OB-RL":
        require(result["terminal"] == "COMPLETE_CHART_NONUNIT_IDEAL", "survivor terminal")
        require(result["dimension"] == 0 and result["basis_size"] == 4, "survivor dimension")
        require(result["basis_sha256"] == PRIMARY_SURVIVOR_DIGEST, "survivor digest")
    else:
        require(result["terminal"] == "COMPLETE_CHART_UNIT_IDEAL", f"unit: {cell}")
        require(result["unit_ideal"] is True and result["progress"][-1]["basis_size"] == 1, f"basis: {cell}")

audit = json.loads((NODE / "direct_complete_chart_audit_output.json").read_text())
require(audit["schema"] == "kb-c2-112-near-positive-m03-complete-chart-audit-modal-v1", "audit schema")
require(set(audit["results"]) == CELLS, "audit cells")
for cell, row in audit["results"].items():
    require(row["status"] == "PASS" and row["returncode"] == 0, f"audit: {cell}")
    result = row["payload"]
    require(result["equation_tuple_sha256"] == EQUATION_DIGESTS[cell], f"audit digest: {cell}")
    require(result["localizer_count"] == 15, f"audit localizers: {cell}")
    require(result["localizer_product_degree"] == 19, f"audit degree: {cell}")
    require(result["localizer_product_terms"] == 132, f"audit terms: {cell}")
    require(result["localizer_product_sha256"] == LOCALIZER_DIGEST, f"audit product: {cell}")
    expected_unit = cell != "M03-OB-RL"
    require(result["unit_ideal"] is expected_unit, f"audit class: {cell}")
    require(result["expected_unit_ideal"] is expected_unit, f"audit expected: {cell}")
    if expected_unit:
        require(result["basis_size"] == 1 and result["basis_sha256"] == UNIT_BASIS_DIGEST, f"audit unit basis: {cell}")
    else:
        require(result["basis_size"] == 7 and result["basis_sha256"] == AUDIT_SURVIVOR_DIGEST, "audit survivor basis")

field = json.loads((NODE / "m03_ob_rl_field_sieve_output.json").read_text())
require(field["schema"] == "kb-c2-112-near-positive-m03-ob-rl-field-sieve-modal-v1", "field schema")
require(field["result"]["status"] == "PASS", "field status")
field_result = field["result"]["payload"]
require(field_result["lex_basis"] == LEX_BASIS, "lex basis")
require(field_result["lex_basis_sha256"] == "3322ad7d8d8efb28dc60a861306faad5f382ebc0c275efa879b86932d38605fa", "lex digest")
require(field_result["primary_basis_sha256"] == PRIMARY_SURVIVOR_DIGEST, "field primary digest")
require(field_result["localizer_count"] == 15, "field localizers")
require(field_result["c_eliminant_degree"] == 4, "c degree")
require(field_result["c_eliminant_sha256"] == "a42ee333b8ee435b4961cc9d9d0039586d1282be3d4d386e9250a7669f368f9c", "c digest")
require(field_result["c_factors"] == C_FACTORS, "c factors")
require(field_result["c_factor_degrees"] == [{"degree": 2, "multiplicity": 1}] * 2, "c factor degrees")
require(field_result["f_p6_compatible_degrees"] == [{"degree": 2, "multiplicity": 1}] * 2, "field compatibility")
require(field_result["terminal"] == "F_P6_COMPATIBLE_FACTOR_REMAINS", "field terminal")

quotient = json.loads((NODE / "m03_ob_rl_first_quotient_output.json").read_text())
require(quotient["schema"] == "kb-c2-112-near-positive-m03-ob-rl-first-quotient-modal-v1", "quotient schema")
require(quotient["result"]["status"] == "PASS", "quotient status")
quotient_result = quotient["result"]["payload"]
require(quotient_result["terminal"] == "FIRST_QUOTIENT_REJECTS_ALL", "quotient terminal")
require(quotient_result["direct_points"] == 4 and quotient_result["literal_points"] == 8, "point census")
require(quotient_result["residue_degree"] == 2 and quotient_result["c_factor_degrees"] == [2, 2], "residue degree")
require(quotient_result["tw_closure_pass"] is True, "inversion closure")
records = quotient_result["records"]
require(Counter((row["assignment"], row["orbit"]) for row in records) == Counter({
    ("M03", "OB"): 4,
    ("M03", "OI"): 4,
}), "literal companion census")
require(Counter(row["first_mismatch_sha256"] for row in records) == Counter({digest: 2 for digest in MISMATCH_DIGESTS}), "mismatch digest census")
for row in records:
    require(row["complete_localizer_count"] == 15, "quotient localizer count")
    require(row["complete_localizers_nonzero"] is True, "quotient localizers")
    require(row["endpoint_passes"] == [True, True], "endpoint control")
    require(row["q_slice_pass"] is True, "q-slice control")
    require(row["first_quotient_norm_pass"] is False, "quotient rejection")
    require(row["first_mismatch_count"] == 299, "quotient mismatches")

print(
    "KB_C2_112_NEAR_POSITIVE_M03_COMPLETE_CHART_CLASSIFICATION_PASS "
    "direct_cells=6 unit=5 survivor_points=4 literal_points=8 quotient_rejected=8 frontier=0"
)
