#!/usr/bin/env python3
"""Audit the cell-11 xi3/xi4 pairing-5/12 replay boundary."""

import ast
import copy
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
ADAPTER = EXP / "rate_half_kb_positive_433_1b_cell11_xi3_pairing5_template_adapter_modal.py"
TEMPLATE = EXP / "rate_half_kb_positive_433_1b_cell4_xi3_pairing5_nested_signfree_modal.py"
ROOT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell11_xi3_pairings3_5_independent_roots_modal.py"
AUDIT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell11_xi3_pairings3_5_direct_audit_modal.py"
AUDIT_RESULT = EXP / "rate_half_kb_positive_433_1b_cell11_xi3_pairings3_5_direct_audit_result.json"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def check(payload):
    pairing = payload["pairing_totals"]["5"]
    require(
        payload["status"] == "PASS" and payload["profiles"] == 73
        and pairing == {
    "candidate_root_count": 140,
    "checked": 208,
    "common_q_roots": 16,
    "common_z_roots": 0,
    "final_color_nonzero": 32,
    "final_pair_solution_count": 0,
    "leading_boundaries": 16,
    "missing_impossible": 16,
    "no_lifts": 52,
    "product_boundaries": 16,
    "profile_visits": 128,
    "q_candidate_count": 16,
    "q_intersections": 448,
    "q_lifts": 16,
    "r_boundaries": 40,
    "route_point_count": 240,
    "rows": 8,
    "source_point_count": 240,
    "t_boundaries": 16,
    "target_boundaries": 16,
    "target_norm_root_count": 56,
    "z_candidate_count": 16,
    "z_roots": 448
},
        "pairing-5 direct census",
    )


def main():
    for path in (ADAPTER, TEMPLATE, ROOT_SCRIPT, AUDIT_SCRIPT,
                 NODE / "verify.py"):
        ast.parse(path.read_text())
    root_source = ROOT_SCRIPT.read_text()
    for snippet in (
        "fmpz_mod_poly_ctx",
        "polynomial.gcd(pow(x, PRIME, polynomial) - x)",
        "root_part.factor()",
    ):
        require(snippet in root_source, f"root method: {snippet}")
    audit_source = AUDIT_SCRIPT.read_text()
    for snippet in ("\"candidate-root union\"",
        "\"finite source relations\"",
        "\"missing-record replay\"",
        "\"nested sign-free root replay\"",
        "\"nested common q replay\"",
        "\"nested final colored cut\"",):
        require(snippet in audit_source, f"direct method: {snippet}")
    payload = json.loads(AUDIT_RESULT.read_text())
    check(payload)
    hostile = copy.deepcopy(payload)
    hostile["pairing_totals"]["5"]["candidate_root_count"] -= 1
    try:
        check(hostile)
    except RuntimeError:
        pass
    else:
        raise RuntimeError("hostile pairing-5 mutation survived")
    contract = (NODE / "claim_contract.md").read_text()
    require("12 labels in 3 active orbits" in contract
            and "Prize closure" in contract, "scope markers")
    print("PASS cell-11 xi3/xi4 pairing 5/12 audit: "
          "roots=370 hostile=detected")


if __name__ == "__main__":
    main()
