#!/usr/bin/env python3
"""Verify the cell-9 xi3 pairing-7 quadratic-resultant exclusion."""

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
PRIMARY = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing7_chart_result/manifest.json"
SUMMARY = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing7_chart_scout_result.json"
ROOTS = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing7_frobenius_roots_result.json"
AUDIT = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing7_direct_audit_result.json"
ROUTER = EXP / "rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
HASHES = {
    PRIMARY: "be65d444165a06c5b6c5c7551f3f525b005cce441cc37e675230e02c9af90960",
    SUMMARY: "81afc776b83e5bedca7c9b8ff7bc73621610fa5e1872ed22fb86b74d849bdb0b",
    ROOTS: "5c5bedf700d743a557755d5bfa5116379071e36b3c78f5925ba78e726d0cc1de",
    AUDIT: "3acdd66f4e32eef7c0831b9c496b31fd9c298f8c69a1755bd372ee4d0b0ddd71",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    for path, expected_hash in HASHES.items():
        require(
            hashlib.sha256(path.read_bytes()).hexdigest() == expected_hash,
            f"hash: {path.name}",
        )
    require(
        verify(PRIMARY) == {"shards": 2, "records": 48, "bytes": 9244692},
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
    routes = z_candidates = q_candidates = lanes = 0
    for row in iter_records(PRIMARY):
        key = (
            tuple(row["epsilon"]),
            row["sigma_c"],
            row["b_row_index"],
            row["c_row_index"],
        )
        require(key in expected and key not in seen, "primary Cartesian row")
        seen.add(key)
        lane_rows = [
            lane
            for finite in row["finite_rows"]
            for z_row in finite.get("z_rows", [])
            for q_row in z_row.get("q_rows", [])
            for lane in q_row.get("lanes", [])
        ]
        q_count = 4 if row["sigma_c"] == -1 else 6
        require(
            row["status"] == "COMPLETE"
            and row["excluded"]
            and row["target_excluded"]
            and row["xi_index"] == 3
            and row["pairing_index"] == 7
            and row["missing_cut_degree"] == 2
            and row["bf_q_z_degrees"] == [2, 2, 2]
            and row["cf_q_z_degrees"] == [2, 2, 2]
            and row["pair23_target_z_degree"] == 8
            and row["z_sign_free_degree"] == 3
            and row["remainder_z_degree"] == 3
            and row["remainder_degree"] == 1
            and row["z_candidate_count"] == len(row["z_candidates"]) == q_count
            and row["q_candidate_count"] == len(row["q_candidates"]) == q_count
            and len(lane_rows) == 2 * q_count
            and all(
                lane["status"] == "THIRD_PAIR_NONZERO"
                and lane["final_pair_cut"] != 0
                for lane in lane_rows
            )
            and not row["witnesses"]
            and not row["unresolved"]
            and not row["final_pair_solutions"],
            "primary terminal",
        )
        routes += row["route_point_count"]
        z_candidates += row["z_candidate_count"]
        q_candidates += row["q_candidate_count"]
        lanes += len(lane_rows)
    require(
        seen == expected
        and routes == 816
        and z_candidates == q_candidates == 240
        and lanes == 480,
        "primary complete cover",
    )

    summary = json.loads(SUMMARY.read_text())
    require(
        len(summary["rows"]) == 48
        and all(
            row["status"] == "COMPLETE"
            and row["excluded"]
            and row["z_candidate_count"] == row["q_candidate_count"]
            == (4 if row["sigma_c"] == -1 else 6)
            and not row["witnesses"]
            and not row["unresolved"]
            for row in summary["rows"]
        ),
        "compact summary",
    )
    roots = json.loads(ROOTS.read_text())
    require(
        roots["field"] == 2130706433
        and len(roots["rows"]) == 65
        and sum(len(row["roots"]) for row in roots["rows"]) == 300
        and max(row["degree"] for row in roots["rows"]) == 5052,
        "external root census",
    )
    audit = json.loads(AUDIT.read_text())
    require(
        audit["status"] == "PASS"
        and audit["rows"] == 48
        and audit["profiles"] == 65
        and audit["profile_visits"] == 672
        and audit["target_norm_root_count"] == 576
        and audit["candidate_root_count"] == 872
        and audit["source_point_count"] == audit["route_point_count"] == 816
        and audit["missing_free"] == 96
        and audit["missing_impossible"] == 48
        and audit["product_boundaries"] == 48
        and audit["checked"] == 624
        and audit["missing_z_roots"] == audit["d_lifts"] == 1824
        and audit["q_intersections"] == 1824
        and audit["common_q_roots"] == audit["q_candidate_count"] == 240
        and audit["lane_checks"] == audit["third_pair_nonzero"] == 480
        and audit["final_pair_solution_count"] == 0
        and audit["chart_b_paid"] == 48
        and audit["chart_c_paid"] == 96
        and audit["regularized_paid"] == 96,
        "direct replay terminal",
    )
    spec = importlib.util.spec_from_file_location("label_router", ROUTER)
    router = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(router)
    selected = [orbit for orbit in router.compile_orbits() if (3, 7) in orbit]
    require(
        selected == [[(3, 7), (3, 10), (4, 7), (4, 10)]],
        "four-label orbit transport",
    )
    print(
        "PASS cell-9 xi3 pairing-7 quadratic-resultant exclusion: "
        "rows=48 routes=816 z=1824 q=240 lanes=480 labels=4"
    )


if __name__ == "__main__":
    main()
