#!/usr/bin/env python3
"""Cross-audit the two cell-5 first-pair residual ledgers."""

import ast
import copy
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
PRIMARY = EXP / "rate_half_kb_positive_433_1b_cell5_parallel_de_first_pair_residual_result.json"
AUDIT = EXP / "rate_half_kb_positive_433_1b_cell5_parallel_de_first_pair_audit_result.json"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def totals(payload, independent):
    systems = units = 0
    for row in payload["rows"]:
        require(row["status"] == "COMPLETE", "complete row")
        if independent:
            require(not row["witnesses"] and not row["unresolved"],
                    "independent terminal")
        else:
            require(not row["nonunit_systems"], "primary terminal")
        systems += row["systems"]
        units += row["unit_systems"]
    require((systems, units) == (96, 96), "terminal totals")
    return systems, units


def main():
    ast.parse((NODE / "verify.py").read_text())
    primary = json.loads(PRIMARY.read_text())
    audit = json.loads(AUDIT.read_text())
    require(totals(primary, False) == totals(audit, True),
            "independent agreement")
    hostile = copy.deepcopy(audit)
    hostile["rows"][0]["unit_systems"] -= 1
    try:
        totals(hostile, True)
    except RuntimeError:
        pass
    else:
        raise RuntimeError("hostile unit mutation survived")
    contract = (NODE / "claim_contract.md").read_text()
    require("other 13 active" in contract and "Prize closure" in contract,
            "scope markers")
    print("PASS cell-5 first-pair audit: primary=96 audit=96 hostile=detected")


if __name__ == "__main__":
    main()
