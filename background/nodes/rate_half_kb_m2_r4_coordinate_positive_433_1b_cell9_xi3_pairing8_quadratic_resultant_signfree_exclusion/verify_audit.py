#!/usr/bin/env python3
"""Cross-audit the cell-9 xi3 pairing-8 ledgers."""

import ast
import copy
import hashlib
import json
from pathlib import Path

NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
PRIMARY = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing8_chart_result/manifest.json"
ROOTS = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing8_frobenius_roots_result.json"
AUDIT = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing8_direct_audit_result.json"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def terminal(payload):
    require(
        payload["status"] == "PASS"
        and payload["rows"] == 48
        and payload["profiles"] == 65
        and payload["profile_visits"] == 672
        and payload["target_norm_root_count"] == 576
        and payload["candidate_root_count"] == 872
        and payload["source_point_count"] == payload["route_point_count"] == 816
        and payload["missing_free"] == 96
        and payload["missing_impossible"] == 48
        and payload["product_boundaries"] == 48
        and payload["checked"] == 624
        and payload["missing_z_roots"] == payload["d_lifts"] == 1824
        and payload["q_intersections"] == 1824
        and payload["common_q_roots"] == payload["q_candidate_count"] == 240
        and payload["lane_checks"] == payload["third_pair_nonzero"] == 480
        and payload["final_pair_solution_count"] == 0
        and payload["chart_b_paid"] == 48
        and payload["chart_c_paid"] == 96
        and payload["regularized_paid"] == 96
        and payload["target_boundaries"] == 48
        and payload["no_lifts"] == 520
        and payload["r_boundaries"] == payload["t_boundaries"] == 240,
        "aggregate terminal",
    )
    require(
        len(payload["chart_rows"]) == 6
        and {tuple(row["chart"]) for row in payload["chart_rows"]}
        == {(b, c) for b in (2, 3) for c in (4, 5, 6)}
        and all(
            row["status"] == "PASS"
            and row["rows"] == 8
            and row["lane_checks"] == row["third_pair_nonzero"] == 80
            for row in payload["chart_rows"]
        ),
        "chart cover",
    )


def main():
    ast.parse((NODE / "verify.py").read_text())
    sources = (
        EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing8_chart_scout_modal.py",
        EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing8_frobenius_roots_modal.py",
        EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing8_direct_audit_modal.py",
    )
    for path in sources:
        ast.parse(path.read_text())
    direct_source = sources[2].read_text()
    for marker in (
        "def paired_left_coefficients(",
        "def field_roots(",
        '"bf q quadratic"',
        '"cf q quadratic"',
        "a_values, b_values, -1,\n                        bv * f_value",
        "a_values, b_values, 1,\n                        sigma_c * cv * f_value",
        "sigma_c * cv * f_value",
        "THIRD_PAIR_NONZERO",
        "q-candidate ledger",
        "regularized base custody",
    ):
        require(marker in direct_source, f"direct construction: {marker}")
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
    hostile["third_pair_nonzero"] -= 1
    try:
        terminal(hostile)
    except RuntimeError:
        pass
    else:
        raise RuntimeError("hostile final-lane mutation survived")
    require(
        "remaining cell-9 pairing-11 orbit"
        in (NODE / "claim_contract.md").read_text(),
        "scope marker",
    )
    require(
        "four leading-open labels" in (NODE / "frontier.md").read_text(),
        "frontier marker",
    )
    print(
        "PASS cell-9 xi3 pairing-8 cross-audit: "
        "charts=6 profiles=65 lanes=480 hostile=detected"
    )


if __name__ == "__main__":
    main()
