#!/usr/bin/env python3
"""Cross-audit the cell-9 pairing-4 sharded and replay ledgers."""

import ast
import copy
import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
PRIMARY = EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing4_chart_result/manifest.json"
ROOTS = EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing4_frobenius_roots_result.json"
AUDIT = EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing4_direct_audit_result.json"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def terminal(payload):
    require(payload["status"] == "PASS" and payload["rows"] == 192
            and payload["profiles"] == 61 and payload["profile_visits"] == 1920
            and payload["target_root_count"] == 3072
            and payload["candidate_root_count"] == 4256
            and payload["source_point_count"] == payload["route_point_count"]
            == 4032 and payload["missing_free"] == 384
            and payload["missing_impossible"] == 192
            and payload["product_boundaries"] == 192
            and payload["checked"] == 3264
            and payload["missing_relation_nonzero"] == 6080
            and payload["uf_candidate_count"] == payload["uf_checked"] == 960
            and payload["colored_nonzero"] == 960
            and payload["f_boundaries"] == payload["d_boundaries"] == 0
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
        EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing4_chart_scout_modal.py",
        EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing4_frobenius_roots_modal.py",
        EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing4_direct_audit_modal.py",
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
    hostile["uf_checked"] -= 1
    try:
        terminal(hostile)
    except RuntimeError:
        pass
    else:
        raise RuntimeError("hostile uf mutation survived")
    contract = (NODE / "claim_contract.md").read_text()
    require("other 14 active" in contract and "Prize" in contract,
            "scope markers")
    print("PASS cell-9 pairing-4 cross-audit: charts=6 profiles=61 "
          "hostile=detected")


if __name__ == "__main__":
    main()
