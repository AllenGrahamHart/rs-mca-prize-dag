#!/usr/bin/env python3
"""Verify the cell-9 xi3 pairing-2 reciprocal-linear exclusion."""

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
PRIMARY = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing2_chart_result/manifest.json"
SUMMARY = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing2_chart_scout_result.json"
ROOTS = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing2_frobenius_roots_result.json"
AUDIT = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing2_direct_audit_result.json"
ROUTER = EXP / "rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
HASHES = {
    PRIMARY: "06cb5414edb4fba9ea0a7f9cccf92052b987a5bbf9761d2095e8a3a40e1d1686",
    SUMMARY: "a555cd820d8484361844168ee7e6c3f06a6f5fce9f09a41061fc42b4e2f3d4bd",
    ROOTS: "c536f4033a05695395ad97fc0ed2ab316478062a1de9ed0a9e67aad973e60fc2",
    AUDIT: "d866198c6a36c316a22218dc2a3adeed871a56142abafe392b76d1371788fb27",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    for path, expected in HASHES.items():
        require(
            hashlib.sha256(path.read_bytes()).hexdigest() == expected,
            f"hash: {path.name}",
        )
    require(
        verify(PRIMARY) == {"shards": 5, "records": 144, "bytes": 9081212},
        "sharded custody",
    )

    signs = tuple(itertools.product((-1, 1), repeat=2))
    expected = {
        (epsilon, branch_index, sigma_c_anchor, b_index, c_index)
        for epsilon in signs
        for branch_index in range(3)
        for sigma_c_anchor in (-1, 1)
        for b_index in (2, 3)
        for c_index in (4, 5, 6)
    }
    seen = set()
    for row in iter_records(PRIMARY):
        key = (
            tuple(row["epsilon"]),
            row["branch_index"],
            row["sigma_c_anchor"],
            row["b_row_index"],
            row["c_row_index"],
        )
        require(key in expected and key not in seen, "primary Cartesian row")
        seen.add(key)
        require(
            row["status"] == "COMPLETE"
            and row["excluded"]
            and row["target_excluded"]
            and row["xi_index"] == 3
            and row["pairing_index"] == 2
            and row["sigma_c_anchor"] in (-1, 1)
            and row["target_lanes_covered"]
            == [[row["sigma_c_anchor"], -1], [row["sigma_c_anchor"], 1]]
            and row["remainder_degree"] == 1
            and (row["missing_cut_degree"], row["next_cut_degree"]) == (4, 2)
            and not row["witnesses"]
            and not row["unresolved"]
            and not row["final_pair_solutions"],
            "primary terminal",
        )
    require(seen == expected, "primary complete cover")

    summary = json.loads(SUMMARY.read_text())
    require(
        len(summary["rows"]) == 144
        and all(
            row["status"] == "COMPLETE"
            and row["excluded"]
            and not row["witnesses"]
            and not row["unresolved"]
            for row in summary["rows"]
        ),
        "compact summary",
    )
    roots = json.loads(ROOTS.read_text())
    require(
        roots["field"] == 2130706433
        and len(roots["rows"]) == 121
        and sum(len(row["roots"]) for row in roots["rows"]) == 716
        and max(row["degree"] for row in roots["rows"]) == 773,
        "external root census",
    )
    audit = json.loads(AUDIT.read_text())
    require(
        audit["status"] == "PASS"
        and audit["rows"] == 144
        and audit["profiles"] == 121
        and audit["profile_visits"] == 2304
        and audit["target_norm_root_count"] == 1584
        and audit["candidate_root_count"] == 2760
        and audit["source_point_count"] == audit["route_point_count"] == 2304
        and audit["missing_free"] == 288
        and audit["missing_impossible"] == 144
        and audit["product_boundaries"] == 144
        and audit["empty_q_branches"] == 144
        and audit["checked"] == 1584
        and audit["common_z_roots"] == 0
        and audit["z_candidate_count"] == audit["z_lifts"] == 0
        and audit["final_color_nonzero"] == 0
        and audit["final_pair_solution_count"] == 0
        and audit["chart_b_paid"] == 144
        and audit["chart_c_paid"] == 288
        and audit["regularized_paid"] == 288
        and audit["target_boundaries"] == 144
        and audit["no_lifts"] == 1920
        and audit["r_boundaries"] == audit["t_boundaries"] == 720,
        "direct replay terminal",
    )

    spec = importlib.util.spec_from_file_location("label_router", ROUTER)
    router = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(router)
    selected = [orbit for orbit in router.compile_orbits() if (3, 2) in orbit]
    require(selected == [[(3, 2), (4, 2)]], "two-label orbit transport")
    print(
        "PASS cell-9 xi3 pairing-2 reciprocal-linear exclusion: rows=144 "
        "routes=2304 common-z=0 labels=2"
    )


if __name__ == "__main__":
    main()
