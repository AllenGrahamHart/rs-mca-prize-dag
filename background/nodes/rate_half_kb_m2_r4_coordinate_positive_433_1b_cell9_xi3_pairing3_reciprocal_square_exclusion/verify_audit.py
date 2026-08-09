#!/usr/bin/env python3
"""Cross-audit the cell-9 xi3 pairing-3 ledgers."""

import ast
import copy
import hashlib
import json
from pathlib import Path

NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
PRIMARY = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing3_chart_result/manifest.json"
ROOTS = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing3_frobenius_roots_result.json"
AUDIT = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing3_direct_audit_result.json"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def terminal(payload):
    require(
        payload["status"] == "PASS" and payload["rows"] == 48
        and payload["profiles"] == 69 and payload["profile_visits"] == 672
        and payload["target_norm_root_count"] == 600
        and payload["candidate_root_count"] == 896
        and payload["source_point_count"] == payload["route_point_count"] == 672
        and payload["missing_free"] == 96 and payload["missing_impossible"] == 48
        and payload["product_boundaries"] == 48 and payload["checked"] == 480
        and payload["common_z_roots"] == payload["d_lifts"] == 96
        and payload["lane_records"] == 192 and payload["common_q_roots"] == 0
        and payload["q_candidate_count"] == payload["final_pair_solution_count"] == 0
        and payload["chart_b_paid"] == 48 and payload["chart_c_paid"] == 96
        and payload["regularized_paid"] == 96
        and payload["target_boundaries"] == 48
        and payload["no_lifts"] == 640
        and payload["r_boundaries"] == payload["t_boundaries"] == 240,
        "aggregate terminal",
    )
    require(
        len(payload["chart_rows"]) == 6
        and {tuple(row["chart"]) for row in payload["chart_rows"]}
        == {(b, c) for b in (2, 3) for c in (4, 5, 6)}
        and all(row["status"] == "PASS" and row["rows"] == 8 for row in payload["chart_rows"]),
        "chart cover",
    )


def main():
    ast.parse((NODE / "verify.py").read_text())
    sources = (
        EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing3_chart_scout_modal.py",
        EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing3_frobenius_roots_modal.py",
        EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing3_direct_audit_modal.py",
    )
    for path in sources:
        ast.parse(path.read_text())
    direct_source = sources[2].read_text()
    for marker in (
        "def paired_coefficients(", "def field_roots(",
        "common_q == []", "regularized base custody",
    ):
        require(marker in direct_source, f"direct construction: {marker}")
    roots = json.loads(ROOTS.read_text())
    audit = json.loads(AUDIT.read_text())
    require(audit["source_manifest_sha256"] == hashlib.sha256(PRIMARY.read_bytes()).hexdigest(), "manifest join")
    require(audit["source_roots_sha256"] == hashlib.sha256(ROOTS.read_bytes()).hexdigest(), "root join")
    require(roots["source_manifest_sha256"] == hashlib.sha256(PRIMARY.read_bytes()).hexdigest(), "root custody join")
    terminal(audit)
    hostile = copy.deepcopy(audit)
    hostile["common_q_roots"] += 1
    try:
        terminal(hostile)
    except RuntimeError:
        pass
    else:
        raise RuntimeError("hostile q-root mutation survived")
    require("other five active" in (NODE / "claim_contract.md").read_text(), "scope marker")
    require("20 leading-open labels" in (NODE / "frontier.md").read_text(), "frontier marker")
    print("PASS cell-9 xi3 pairing-3 cross-audit: charts=6 profiles=69 hostile=detected")


if __name__ == "__main__":
    main()
