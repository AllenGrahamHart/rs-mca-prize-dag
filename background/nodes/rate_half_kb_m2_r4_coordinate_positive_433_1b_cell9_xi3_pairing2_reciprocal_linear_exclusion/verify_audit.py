#!/usr/bin/env python3
"""Cross-audit the cell-9 xi3 pairing-2 ledgers."""

import ast
import copy
import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
PRIMARY = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing2_chart_result/manifest.json"
ROOTS = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing2_frobenius_roots_result.json"
AUDIT = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing2_direct_audit_result.json"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def terminal(payload):
    require(
        payload["status"] == "PASS"
        and payload["rows"] == 144
        and payload["profiles"] == 121
        and payload["profile_visits"] == 2304
        and payload["target_norm_root_count"] == 1584
        and payload["candidate_root_count"] == 2760
        and payload["source_point_count"] == payload["route_point_count"] == 2304
        and payload["missing_free"] == 288
        and payload["missing_impossible"] == 144
        and payload["product_boundaries"] == 144
        and payload["empty_q_branches"] == 144
        and payload["checked"] == 1584
        and payload["common_z_roots"] == 0
        and payload["z_candidate_count"] == payload["z_lifts"] == 0
        and payload["final_color_nonzero"] == 0
        and payload["final_pair_solution_count"] == 0
        and payload["chart_b_paid"] == 144
        and payload["chart_c_paid"] == 288
        and payload["regularized_paid"] == 288
        and payload["target_boundaries"] == 144
        and payload["no_lifts"] == 1920
        and payload["r_boundaries"] == payload["t_boundaries"] == 720,
        "aggregate audit terminal",
    )
    chart_rows = payload["chart_rows"]
    require(
        len(chart_rows) == 6
        and {tuple(row["chart"]) for row in chart_rows}
        == {(b, c) for b in (2, 3) for c in (4, 5, 6)}
        and all(row["status"] == "PASS" and row["rows"] == 24 for row in chart_rows),
        "chart audit cover",
    )


def main():
    ast.parse((NODE / "verify.py").read_text())
    sources = (
        EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing2_chart_scout_modal.py",
        EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing2_frobenius_roots_modal.py",
        EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing2_direct_audit_modal.py",
    )
    for path in sources:
        ast.parse(path.read_text())
    scout_source = sources[0].read_text()
    for marker in (
        "for branch_index in range(3)",
        "for sigma_c_anchor in (-1, 1)",
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
    hostile["common_z_roots"] += 1
    try:
        terminal(hostile)
    except RuntimeError:
        pass
    else:
        raise RuntimeError("hostile common-root mutation survived")
    contract = (NODE / "claim_contract.md").read_text()
    frontier = (NODE / "frontier.md").read_text()
    require(
        "other six active" in contract and "Prize" in contract,
        "scope markers",
    )
    require("24 leading-open labels" in frontier, "frontier marker")
    print(
        "PASS cell-9 xi3 pairing-2 cross-audit: charts=6 profiles=121 "
        "hostile=detected"
    )


if __name__ == "__main__":
    main()
