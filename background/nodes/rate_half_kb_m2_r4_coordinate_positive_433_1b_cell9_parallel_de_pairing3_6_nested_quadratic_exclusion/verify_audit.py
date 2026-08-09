#!/usr/bin/env python3
"""Cross-audit the cell-9 pairing-3 sharded and replay ledgers."""

import ast
import copy
import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
PRIMARY = EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing3_chart_result/manifest.json"
ROOTS = EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing3_frobenius_roots_result.json"
AUDIT = EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing3_direct_audit_result.json"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def terminal(payload):
    require(payload["status"] == "PASS" and payload["rows"] == 192
            and payload["profiles"] == 69 and payload["profile_visits"] == 1920
            and payload["target_root_count"] == 2160
            and payload["candidate_root_count"] == 3344
            and payload["source_point_count"] == payload["route_point_count"]
            == 2784 and payload["missing_free"] == 384
            and payload["missing_impossible"] == 192
            and payload["product_boundaries"] == 192
            and payload["checked"] == 2016
            and payload["missing_sum_nonzero"] == 3968
            and payload["uv_candidate_count"] == payload["uv_checked"] == 384
            and payload["f_rows"] == payload["colored_nonzero"] == 768
            and payload["f_boundaries"] == 0
            and payload["colored_solution_count"] == 0
            and payload["chart_b_paid"] == 192
            and payload["chart_c_paid"] == 384
            and payload["regularized_paid"] == 384
            and payload["target_boundaries"] == 192,
            "aggregate audit terminal")
    chart_rows = payload["chart_rows"]
    require(len(chart_rows) == 6
            and {tuple(row["chart"]) for row in chart_rows}
            == {(b, c) for b in (2, 3) for c in (4, 5, 6)}
            and all(row["status"] == "PASS" and row["rows"] == 32
                    for row in chart_rows), "chart audit cover")


def main():
    ast.parse((NODE / "verify.py").read_text())
    for path in (
        EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing3_chart_scout_modal.py",
        EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing3_frobenius_roots_modal.py",
        EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing3_direct_audit_modal.py",
    ):
        ast.parse(path.read_text())
    roots = json.loads(ROOTS.read_text())
    audit = json.loads(AUDIT.read_text())
    require(audit["source_manifest_sha256"]
            == hashlib.sha256(PRIMARY.read_bytes()).hexdigest(),
            "manifest join")
    require(audit["source_roots_sha256"]
            == hashlib.sha256(ROOTS.read_bytes()).hexdigest(), "root join")
    require(roots["source_manifest_sha256"]
            == hashlib.sha256(PRIMARY.read_bytes()).hexdigest(),
            "root custody join")
    terminal(audit)
    hostile = copy.deepcopy(audit)
    hostile["uv_checked"] -= 1
    try:
        terminal(hostile)
    except RuntimeError:
        pass
    else:
        raise RuntimeError("hostile uv mutation survived")
    contract = (NODE / "claim_contract.md").read_text()
    require("other 16 active" in contract and "Prize" in contract,
            "scope markers")
    print("PASS cell-9 pairing-3 cross-audit: charts=6 profiles=69 "
          "hostile=detected")


if __name__ == "__main__":
    main()
