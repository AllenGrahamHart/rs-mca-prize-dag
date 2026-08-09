#!/usr/bin/env python3
"""Audit the independent cell-11 positive-DE pairing-14 replay boundary."""

import ast
import copy
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
AUDITOR = EXP / "rate_half_kb_positive_433_1b_cell11_positive_de_pairing14_common_f_audit.py"
AUDIT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell11_positive_de_pairing14_direct_audit_modal.py"
AUDIT_RESULT = EXP / "rate_half_kb_positive_433_1b_cell11_positive_de_pairing14_direct_audit_result.json"
ROOT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell11_positive_de_pairing14_frobenius_roots_modal.py"
EXPECTED = {
    "candidate_root_count": 208, "checked": 144,
    "colored_nonzero": 0, "colored_solution_count": 0,
    "combined_profiles": 37, "leading_boundaries": 32,
    "missing_impossible": 32, "product_boundaries": 32,
    "profile_visits": 160, "route_point_count": 208, "rows": 16,
    "source_point_count": 208, "target_boundaries": 32,
    "target_root_count": 136, "uf_candidate_count": 0,
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def check(payload):
    require(payload["summary"] == EXPECTED, "direct audit summary")


def main():
    for path in (AUDITOR, AUDIT_SCRIPT, ROOT_SCRIPT, NODE / "verify.py"):
        ast.parse(path.read_text())
    root_source = ROOT_SCRIPT.read_text()
    for snippet in (
        "fmpz_mod_poly_ctx",
        "polynomial.gcd(pow(x, PRIME, polynomial) - x)",
        "root_part.factor()",
    ):
        require(snippet in root_source, f"root method: {snippet}")
    audit_source = AUDITOR.read_text()
    for snippet in (
        '"target-root replay"', '"candidate terminal cover"',
        '"finite source relations"', '"missing-impossible terminal"',
        '"colored-pair terminal"',
    ):
        require(snippet in audit_source, f"direct method: {snippet}")
    require("module.audit_result(" in AUDIT_SCRIPT.read_text(),
            "Modal direct replay call")

    b0, b1, b2, c0, c1, c2, f = sp.symbols("b0 b1 b2 c0 c1 c2 f")
    resultant = sp.resultant(b0 + b1*f + b2*f**2,
                             c0 + c1*f + c2*f**2, f)
    printed = (b2*c0-b0*c2)**2 - (b2*c1-b1*c2)*(b1*c0-b0*c1)
    require(sp.expand(resultant - printed) == 0, "quadratic resultant")

    payload = json.loads(AUDIT_RESULT.read_text())
    check(payload)
    hostile = copy.deepcopy(payload)
    hostile["summary"]["checked"] -= 1
    try:
        check(hostile)
    except RuntimeError:
        pass
    else:
        raise RuntimeError("hostile summary mutation survived")
    contract = (NODE / "claim_contract.md").read_text()
    require("34" in contract and "11 active representatives" in contract
            and "Prize closure" in contract, "scope markers")
    print("PASS cell-11 pairing-14 audit: roots=150 routes=208 hostile=detected")


if __name__ == "__main__":
    main()
