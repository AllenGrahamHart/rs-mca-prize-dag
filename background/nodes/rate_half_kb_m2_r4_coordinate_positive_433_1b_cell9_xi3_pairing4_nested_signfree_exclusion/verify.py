#!/usr/bin/env python3
"""Verify the cell-9 xi3 pairing-4 nested sign-free exclusion."""

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
PRIMARY = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing4_chart_result/manifest.json"
SUMMARY = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing4_chart_scout_result.json"
ROOTS = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing4_frobenius_roots_result.json"
AUDIT = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing4_direct_audit_result.json"
ROUTER = EXP / "rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
HASHES = {
    PRIMARY: "4acd34bf3c3757f3f45c5021ed364d38f4cd354c0499366258c0b1fb1537666e",
    SUMMARY: "11b4dd520326439610b5ed96e67a70841fdf2904ffb5afc0ef29845974239bfc",
    ROOTS: "27f3cad05cd595b02446c13ea2c24e48b6cd12f7aa8566c557ccd92c029ec1d4",
    AUDIT: "afda24acca26dd0d531caa4abac41ae57863e13314625036dbf9e7880ecee967",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    for path, expected_hash in HASHES.items():
        require(hashlib.sha256(path.read_bytes()).hexdigest() == expected_hash, f"hash: {path.name}")
    require(verify(PRIMARY) == {"shards": 1, "records": 24, "bytes": 5680636}, "sharded custody")
    signs = tuple(itertools.product((-1, 1), repeat=2))
    expected = {
        (epsilon, b_index, c_index)
        for epsilon in signs
        for b_index in (2, 3)
        for c_index in (4, 5, 6)
    }
    seen = set()
    for row in iter_records(PRIMARY):
        key = (tuple(row["epsilon"]), row["b_row_index"], row["c_row_index"])
        require(key in expected and key not in seen, "primary Cartesian row")
        seen.add(key)
        require(
            row["status"] == "COMPLETE" and row["excluded"] and row["target_excluded"]
            and row["xi_index"] == 3 and row["pairing_index"] == 4
            and row["missing_cut_degree"] == 2 and row["antipodal_u_degree"] == 2
            and row["second_target_z_degree"] == 8 and row["z_sign_free_degree"] == 3
            and row["remainder_z_degree"] == 3
            and row["remainder_u_z_degrees"] == [4, 4]
            and row["remainder_degree"] == 1
            and not row["witnesses"] and not row["unresolved"]
            and not row["z_candidates"] and not row["q_candidates"]
            and not row["final_pair_solutions"],
            "primary terminal",
        )
    require(seen == expected, "primary complete cover")

    summary = json.loads(SUMMARY.read_text())
    require(
        len(summary["rows"]) == 24
        and all(row["status"] == "COMPLETE" and row["excluded"]
                and not row["witnesses"] and not row["unresolved"]
                for row in summary["rows"]),
        "compact summary",
    )
    roots = json.loads(ROOTS.read_text())
    require(
        roots["field"] == 2130706433 and len(roots["rows"]) == 69
        and sum(len(row["roots"]) for row in roots["rows"]) == 320
        and max(row["degree"] for row in roots["rows"]) == 6282,
        "external root census",
    )
    audit = json.loads(AUDIT.read_text())
    require(
        audit["status"] == "PASS" and audit["rows"] == 24
        and audit["profiles"] == 69 and audit["profile_visits"] == 384
        and audit["target_norm_root_count"] == 240
        and audit["candidate_root_count"] == 460
        and audit["source_point_count"] == audit["route_point_count"] == 384
        and audit["missing_free"] == 48 and audit["missing_impossible"] == 24
        and audit["product_boundaries"] == 24 and audit["checked"] == 288
        and audit["missing_z_roots"] == audit["d_lifts"] == 720
        and audit["q_intersections"] == 720 and audit["common_q_roots"] == 0
        and audit["q_candidate_count"] == audit["final_pair_solution_count"] == 0
        and audit["chart_b_paid"] == 24 and audit["chart_c_paid"] == 48
        and audit["regularized_paid"] == 48,
        "direct replay terminal",
    )
    spec = importlib.util.spec_from_file_location("label_router", ROUTER)
    router = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(router)
    selected = [orbit for orbit in router.compile_orbits() if (3, 4) in orbit]
    require(selected == [[(3, 4), (3, 9), (4, 4), (4, 9)]], "four-label orbit transport")
    print("PASS cell-9 xi3 pairing-4 nested sign-free exclusion: rows=24 routes=384 z=720 q=0 labels=4")


if __name__ == "__main__":
    main()
