#!/usr/bin/env python3
"""Audit the independent cell-5 xi3 pairings-1/2 replay boundary."""

import ast
import copy
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
ROOT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell5_xi3_pairings1_2_independent_roots_modal.py"
AUDIT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell5_xi3_pairings1_2_direct_audit_modal.py"
AUDIT_RESULT = EXP / "rate_half_kb_positive_433_1b_cell5_xi3_pairings1_2_direct_audit_result.json"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def check(payload):
    pairing_one = payload["pairing_totals"]["1"]
    pairing_two = payload["pairing_totals"]["2"]
    require(payload["status"] == "PASS" and payload["rows"] == 36
            and pairing_one["rows"] == 12 and pairing_two["rows"] == 24
            and pairing_one["z_lifts"] == 48
            and pairing_two["z_lifts"] == 16
            and pairing_one["final_color_nonzero"] == 192
            and pairing_two["final_color_nonzero"] == 32
            and pairing_one["final_pair_solution_count"] == 0
            and pairing_two["final_pair_solution_count"] == 0,
            "pairing-separated direct census")


def main():
    for path in (ROOT_SCRIPT, AUDIT_SCRIPT, NODE / "verify.py"):
        ast.parse(path.read_text())
    root_source = ROOT_SCRIPT.read_text()
    for snippet in ("gf_pow_mod", "gf_gcd", "gf_sub", "sp.factor_list"):
        require(snippet in root_source, f"root method: {snippet}")
    audit_source = AUDIT_SCRIPT.read_text()
    for snippet in (
        '"candidate-root union"', '"finite source relations"',
        '"missing-record replay"', '"common-z root replay"',
        '"z/d/e/f lift replay"', '"final colored-pair terminal"',
        '"pairing_totals"',
    ):
        require(snippet in audit_source, f"direct method: {snippet}")
    payload = json.loads(AUDIT_RESULT.read_text())
    check(payload)
    for pairing in ("1", "2"):
        hostile = copy.deepcopy(payload)
        hostile["pairing_totals"][pairing]["final_color_nonzero"] -= 1
        try:
            check(hostile)
        except RuntimeError:
            pass
        else:
            raise RuntimeError(f"hostile pairing-{pairing} mutation survived")
    contract = (NODE / "claim_contract.md").read_text()
    require("24 labels in 6 active orbits" in contract
            and "Prize closure" in contract, "scope markers")
    print("PASS cell-5 xi3 pairings-1/2 audit: roots=596 lanes=224 hostile=detected")


if __name__ == "__main__":
    main()
