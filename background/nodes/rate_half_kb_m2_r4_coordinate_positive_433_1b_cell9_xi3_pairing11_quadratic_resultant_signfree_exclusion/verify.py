#!/usr/bin/env python3
"""Verify the cell-9 xi3 pairing-11 quadratic-resultant exclusion."""

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
PRIMARY = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing11_chart_result/manifest.json"
SUMMARY = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing11_chart_scout_result.json"
ROOTS = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing11_frobenius_roots_result.json"
AUDIT = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing11_direct_audit_result.json"
ROUTER = EXP / "rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
HASHES = {
    PRIMARY: "814f3db973f837caa2ea019986364df3e019531e54cc4c194c4881743344cb84",
    SUMMARY: "d42458b19e28bff9c2c19deff41c79056a1b9493180c21695bd732e7375a995b",
    ROOTS: "3a8888337339d3f9df32a53f6bdf0dca9e8d20ccc9de27739e1e7e7e6d7a04a9",
    AUDIT: "35058ff77fa7b804c8e06c7d899dca3e4d61373a13f5964f153d247118ce5cd0",
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
        verify(PRIMARY) == {"shards": 2, "records": 48, "bytes": 8454588},
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
        q_count = 2 if row["sigma_c"] == -1 else 4
        require(
            row["status"] == "COMPLETE"
            and row["excluded"]
            and row["target_excluded"]
            and row["xi_index"] == 3
            and row["pairing_index"] == 11
            and row["missing_cut_degree"] == 2
            and row["bf_q_z_degrees"] == [2, 2, 2]
            and row["cf_q_z_degrees"] == [2, 2, 2]
            and row["pair23_target_z_degree"] == 6
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
        and routes == 672
        and z_candidates == q_candidates == 144
        and lanes == 288,
        "primary complete cover",
    )

    summary = json.loads(SUMMARY.read_text())
    require(
        len(summary["rows"]) == 48
        and all(
            row["status"] == "COMPLETE"
            and row["excluded"]
            and row["z_candidate_count"] == row["q_candidate_count"]
            == (2 if row["sigma_c"] == -1 else 4)
            and not row["witnesses"]
            and not row["unresolved"]
            for row in summary["rows"]
        ),
        "compact summary",
    )
    roots = json.loads(ROOTS.read_text())
    require(
        roots["field"] == 2130706433
        and len(roots["rows"]) == 69
        and sum(len(row["roots"]) for row in roots["rows"]) == 312
        and max(row["degree"] for row in roots["rows"]) == 4732,
        "external root census",
    )
    audit = json.loads(AUDIT.read_text())
    require(
        audit["status"] == "PASS"
        and audit["rows"] == 48
        and audit["profiles"] == 69
        and audit["profile_visits"] == 672
        and audit["target_norm_root_count"] == 528
        and audit["candidate_root_count"] == 824
        and audit["source_point_count"] == audit["route_point_count"] == 672
        and audit["missing_free"] == 96
        and audit["missing_impossible"] == 48
        and audit["product_boundaries"] == 48
        and audit["checked"] == 480
        and audit["missing_z_roots"] == audit["d_lifts"] == 1440
        and audit["q_intersections"] == 1440
        and audit["common_q_roots"] == audit["q_candidate_count"] == 144
        and audit["lane_checks"] == audit["third_pair_nonzero"] == 288
        and audit["final_pair_solution_count"] == 0
        and audit["chart_b_paid"] == 48
        and audit["chart_c_paid"] == 96
        and audit["regularized_paid"] == 96,
        "direct replay terminal",
    )
    spec = importlib.util.spec_from_file_location("label_router", ROUTER)
    router = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(router)
    selected = [orbit for orbit in router.compile_orbits() if (3, 11) in orbit]
    require(
        selected == [[(3, 11), (3, 14), (4, 11), (4, 14)]],
        "four-label orbit transport",
    )
    print(
        "PASS cell-9 xi3 pairing-11 quadratic-resultant exclusion: "
        "rows=48 routes=672 z=1440 q=144 lanes=288 labels=4"
    )


if __name__ == "__main__":
    main()
