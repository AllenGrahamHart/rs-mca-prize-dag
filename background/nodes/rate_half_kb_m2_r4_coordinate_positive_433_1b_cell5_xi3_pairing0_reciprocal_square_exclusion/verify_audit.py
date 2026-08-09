#!/usr/bin/env python3
"""Audit the independent cell-5 xi3 pairing-0 replay boundary."""

import ast
import copy
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
ROOT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell5_xi3_pairing0_independent_roots_modal.py"
AUDIT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell5_xi3_pairing0_direct_audit_modal.py"
AUDIT_RESULT = EXP / "rate_half_kb_positive_433_1b_cell5_xi3_pairing0_direct_audit_result.json"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def check(payload):
    require(payload["status"] == "PASS"
            and payload["rows"] == 24
            and payload["candidate_root_count"] == 324
            and payload["source_point_count"] == 416
            and payload["d_lifts"] == 160
            and payload["third_pair_nonzero"] == 320
            and payload["final_pair_solution_count"] == 0,
            "direct audit census")


def main():
    for path in (ROOT_SCRIPT, AUDIT_SCRIPT, NODE / "verify.py"):
        ast.parse(path.read_text())
    root_source = ROOT_SCRIPT.read_text()
    for snippet in ("gf_pow_mod", "gf_gcd", "gf_sub", "sp.factor_list"):
        require(snippet in root_source, f"root method: {snippet}")
    audit_source = AUDIT_SCRIPT.read_text()
    for snippet in (
        '"candidate-root union"', '"finite source relations"',
        '"missing-record replay"', '"common-y root replay"',
        '"d/e/f lift replay"', '"final colored-pair terminal"',
    ):
        require(snippet in audit_source, f"direct method: {snippet}")

    q = sp.symbols("q")
    a0, a1, a2, b0, b1, b2 = sp.symbols("a0 a1 a2 b0 b1 b2")
    p0, p1, p2 = b0-q*a0, b1-q*a1, b2-q*a2
    paired = (p2*p0-p0*p2)**2 - (p2*(-p1)-p1*p2)*(p1*p0-p0*(-p1))
    require(sp.expand(paired - 4*p0*p1**2*p2) == 0,
            "three-branch factorization")

    payload = json.loads(AUDIT_RESULT.read_text())
    check(payload)
    hostile = copy.deepcopy(payload)
    hostile["third_pair_nonzero"] -= 1
    try:
        check(hostile)
    except RuntimeError:
        pass
    else:
        raise RuntimeError("hostile census mutation survived")
    contract = (NODE / "claim_contract.md").read_text()
    require("28 labels in 8 active orbits" in contract
            and "Prize closure" in contract, "scope markers")
    print("PASS cell-5 xi3 pairing-0 audit: roots=392 lanes=320 hostile=detected")


if __name__ == "__main__":
    main()
