#!/usr/bin/env python3
"""Verify the cell-9 xi3 pairing-5 nested sign-free exclusion."""

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
PRIMARY = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing5_chart_result/manifest.json"
SUMMARY = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing5_chart_scout_result.json"
ROOTS = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing5_frobenius_roots_result.json"
AUDIT = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing5_direct_audit_result.json"
ROUTER = EXP / "rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
HASHES = {
    PRIMARY: "6b9bc2761d4a4a1f1634c336074fd29ff3bd8a53f96a59fb43ef92ca00970f31",
    SUMMARY: "6611f793000b3530c846dbc741d583116d24cec148db8e08904efaa1ea81685d",
    ROOTS: "b8b579c6b313a0eb7ef3d763cc4a0bfddc33b36ad709ae511a6e71baa1d3a360",
    AUDIT: "354004fc817dbb82202327e7b01ffebae884d3552daf4e2888fe5b7eb8fc2b27",
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
        verify(PRIMARY) == {"shards": 2, "records": 48, "bytes": 11705340},
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
        require(
            row["status"] == "COMPLETE"
            and row["excluded"]
            and row["target_excluded"]
            and row["xi_index"] == 3
            and row["pairing_index"] == 5
            and row["missing_cut_degree"] == 2
            and row["antipodal_u_degree"] == 2
            and row["second_target_z_degree"] == 8
            and row["z_sign_free_degree"] == 3
            and row["remainder_z_degree"] == 3
            and row["remainder_u_z_degrees"] == [4, 4]
            and row["remainder_degree"] == 1
            and row["z_candidate_count"] == len(row["z_candidates"]) == 6
            and row["q_candidate_count"] == len(row["q_candidates"]) == 6
            and len(lane_rows) == 12
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
        and routes == 1152
        and z_candidates == q_candidates == 288
        and lanes == 576,
        "primary complete cover",
    )

    summary = json.loads(SUMMARY.read_text())
    require(
        len(summary["rows"]) == 48
        and all(
            row["status"] == "COMPLETE"
            and row["excluded"]
            and row["z_candidate_count"] == row["q_candidate_count"] == 6
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
        and sum(len(row["roots"]) for row in roots["rows"]) == 328
        and max(row["degree"] for row in roots["rows"]) == 6236,
        "external root census",
    )
    audit = json.loads(AUDIT.read_text())
    require(
        audit["status"] == "PASS"
        and audit["rows"] == 48
        and audit["profiles"] == 69
        and audit["profile_visits"] == 768
        and audit["target_norm_root_count"] == 576
        and audit["candidate_root_count"] == 1016
        and audit["source_point_count"] == audit["route_point_count"] == 1152
        and audit["missing_free"] == 96
        and audit["missing_impossible"] == 48
        and audit["product_boundaries"] == 48
        and audit["checked"] == 960
        and audit["missing_z_roots"] == audit["d_lifts"] == 2976
        and audit["q_intersections"] == 2976
        and audit["common_q_roots"] == audit["q_candidate_count"] == 288
        and audit["lane_checks"] == audit["third_pair_nonzero"] == 576
        and audit["final_pair_solution_count"] == 0
        and audit["chart_b_paid"] == 48
        and audit["chart_c_paid"] == 96
        and audit["regularized_paid"] == 96,
        "direct replay terminal",
    )
    spec = importlib.util.spec_from_file_location("label_router", ROUTER)
    router = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(router)
    selected = [orbit for orbit in router.compile_orbits() if (3, 5) in orbit]
    require(
        selected == [[(3, 5), (3, 12), (4, 5), (4, 12)]],
        "four-label orbit transport",
    )
    print(
        "PASS cell-9 xi3 pairing-5 nested sign-free exclusion: "
        "rows=48 routes=1152 z=2976 q=288 lanes=576 labels=4"
    )


if __name__ == "__main__":
    main()
