#!/usr/bin/env python3
"""Verify the cell-9 xi3 pairing-3 reciprocal-square exclusion."""

import hashlib
import importlib.util
import itertools
import json
import sys
from pathlib import Path

NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
sys.path.insert(0, str(ROOT))
from tools.sharded_result import iter_records, verify

EXP = ROOT / "experiments/prize_resolution"
PRIMARY = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing3_chart_result/manifest.json"
SUMMARY = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing3_chart_scout_result.json"
ROOTS = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing3_frobenius_roots_result.json"
AUDIT = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing3_direct_audit_result.json"
ROUTER = EXP / "rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
HASHES = {
    PRIMARY: "144ec97cf2175a669c5a37a18ee5f8d203d5ad798e2aed69d87a3c2ab81dda8e",
    SUMMARY: "01fbdab66175437e48d41f211ec195144b6d7d9d16097c709fa526eee07261fe",
    ROOTS: "0e8f6da9cc04d81b413f1483369b19dd21494b40c29971b7f24b7e414c20d7e4",
    AUDIT: "a5213a7a9f4edc592d4ccec0725659b631ba7c9864ec789713fc012a9e9f6883",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    for path, expected_hash in HASHES.items():
        require(hashlib.sha256(path.read_bytes()).hexdigest() == expected_hash, f"hash: {path.name}")
    require(
        verify(PRIMARY) == {"shards": 2, "records": 48, "bytes": 3385114},
        "sharded custody",
    )
    signs = tuple(itertools.product((-1, 1), repeat=2))
    expected = {
        (epsilon, sigma_c, b_index, c_index)
        for epsilon in signs
        for sigma_c in (-1, 1)
        for b_index in (2, 3)
        for c_index in (4, 5, 6)
    }
    seen = set()
    for row in iter_records(PRIMARY):
        key = (
            tuple(row["epsilon"]), row["sigma_c"],
            row["b_row_index"], row["c_row_index"],
        )
        require(key in expected and key not in seen, "primary Cartesian row")
        seen.add(key)
        require(
            row["status"] == "COMPLETE"
            and row["excluded"] and row["target_excluded"]
            and row["xi_index"] == 3 and row["pairing_index"] == 3
            and (row["missing_cut_degree"], row["colored_z_cut_degree"])
            == (2, 4)
            and row["colored_sign_free_degree"] == 4
            and row["remainder_degree"] == 1
            and not row["witnesses"] and not row["unresolved"]
            and not row["q_candidates"] and not row["final_pair_solutions"],
            "primary terminal",
        )
    require(seen == expected, "primary complete cover")

    summary = json.loads(SUMMARY.read_text())
    require(
        len(summary["rows"]) == 48
        and all(
            row["status"] == "COMPLETE" and row["excluded"]
            and not row["witnesses"] and not row["unresolved"]
            for row in summary["rows"]
        ),
        "compact summary",
    )
    roots = json.loads(ROOTS.read_text())
    require(
        roots["field"] == 2130706433 and len(roots["rows"]) == 69
        and sum(len(row["roots"]) for row in roots["rows"]) == 324
        and max(row["degree"] for row in roots["rows"]) == 1428,
        "external root census",
    )
    audit = json.loads(AUDIT.read_text())
    require(
        audit["status"] == "PASS" and audit["rows"] == 48
        and audit["profiles"] == 69 and audit["profile_visits"] == 672
        and audit["target_norm_root_count"] == 600
        and audit["candidate_root_count"] == 896
        and audit["source_point_count"] == audit["route_point_count"] == 672
        and audit["missing_free"] == 96 and audit["missing_impossible"] == 48
        and audit["product_boundaries"] == 48 and audit["checked"] == 480
        and audit["common_z_roots"] == audit["d_lifts"] == 96
        and audit["lane_records"] == 192 and audit["common_q_roots"] == 0
        and audit["q_candidate_count"] == 0
        and audit["final_pair_solution_count"] == 0
        and audit["chart_b_paid"] == 48 and audit["chart_c_paid"] == 96
        and audit["regularized_paid"] == 96,
        "direct replay terminal",
    )

    spec = importlib.util.spec_from_file_location("label_router", ROUTER)
    router = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(router)
    selected = [orbit for orbit in router.compile_orbits() if (3, 3) in orbit]
    require(
        selected == [[(3, 3), (3, 6), (4, 3), (4, 6)]],
        "four-label orbit transport",
    )
    print("PASS cell-9 xi3 pairing-3 reciprocal-square exclusion: rows=48 routes=672 z=96 q=0 labels=4")


if __name__ == "__main__":
    main()
