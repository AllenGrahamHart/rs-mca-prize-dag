#!/usr/bin/env python3
"""Cross-audit the cell-9 xi3 pairing-1 ledgers."""

import ast
import copy
import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
PRIMARY = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing1_chart_result/manifest.json"
ROOTS = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing1_frobenius_roots_result.json"
AUDIT = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing1_direct_audit_result.json"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def terminal(payload):
    require(
        payload["status"] == "PASS"
        and payload["rows"] == 72
        and payload["profiles"] == 121
        and payload["profile_visits"] == 1152
        and payload["target_norm_root_count"] == 744
        and payload["candidate_root_count"] == 1332
        and payload["source_point_count"] == payload["route_point_count"] == 1296
        and payload["missing_free"] == 144
        and payload["missing_impossible"] == 72
        and payload["product_boundaries"] == 72
        and payload["empty_q_branches"] == 72
        and payload["checked"] == 936
        and payload["common_z_roots"] == 144
        and payload["z_candidate_count"] == payload["z_lifts"] == 144
        and payload["final_color_nonzero"] == 576
        and payload["final_pair_solution_count"] == 0
        and payload["chart_b_paid"] == 72
        and payload["chart_c_paid"] == 144
        and payload["regularized_paid"] == 144
        and payload["target_boundaries"] == 72
        and payload["no_lifts"] == 792
        and payload["r_boundaries"] == payload["t_boundaries"] == 360,
        "aggregate audit terminal",
    )
    chart_rows = payload["chart_rows"]
    require(
        len(chart_rows) == 6
        and {tuple(row["chart"]) for row in chart_rows}
        == {(b, c) for b in (2, 3) for c in (4, 5, 6)}
        and all(row["status"] == "PASS" and row["rows"] == 12 for row in chart_rows),
        "chart audit cover",
    )


def main():
    ast.parse((NODE / "verify.py").read_text())
    sources = (
        EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing1_chart_scout_modal.py",
        EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing1_frobenius_roots_modal.py",
        EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing1_direct_audit_modal.py",
    )
    for path in sources:
        ast.parse(path.read_text())
    scout_source = sources[0].read_text()
    for marker in (
        "for branch_index in range(3)",
        "(epsilon_1, epsilon_2, branch_index, 0, 1)",
        "source_template_sha256",
        "source_base_sha256",
    ):
        require(marker in scout_source, f"compiler construction: {marker}")

    roots = json.loads(ROOTS.read_text())
    audit = json.loads(AUDIT.read_text())
    require(
        audit["source_manifest_sha256"]
        == hashlib.sha256(PRIMARY.read_bytes()).hexdigest(),
        "manifest join",
    )
    require(
        audit["source_roots_sha256"]
        == hashlib.sha256(ROOTS.read_bytes()).hexdigest(),
        "root join",
    )
    require(
        roots["source_manifest_sha256"]
        == hashlib.sha256(PRIMARY.read_bytes()).hexdigest(),
        "root custody join",
    )
    terminal(audit)
    hostile = copy.deepcopy(audit)
    hostile["final_color_nonzero"] -= 1
    try:
        terminal(hostile)
    except RuntimeError:
        pass
    else:
        raise RuntimeError("hostile final-color mutation survived")
    contract = (NODE / "claim_contract.md").read_text()
    frontier = (NODE / "frontier.md").read_text()
    require(
        "other seven active" in contract and "Prize" in contract,
        "scope markers",
    )
    require("26 leading-open labels" in frontier, "frontier marker")
    print(
        "PASS cell-9 xi3 pairing-1 cross-audit: charts=6 profiles=121 "
        "hostile=detected"
    )


if __name__ == "__main__":
    main()
