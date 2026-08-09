#!/usr/bin/env python3
"""Verify the cell-9 xi3 pairing-1 reciprocal-linear exclusion."""

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
PRIMARY = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing1_chart_result/manifest.json"
SUMMARY = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing1_chart_scout_result.json"
ROOTS = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing1_frobenius_roots_result.json"
AUDIT = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing1_direct_audit_result.json"
ROUTER = EXP / "rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
HASHES = {
    PRIMARY: "6eefc83cb14689bd3ce0d008f89c77b82625c9483b2338ef511f944ee02372df",
    SUMMARY: "90c2f9e9f3661289d626f0e77e380ade0c5168ad4d572465adcc89b48c23cc4e",
    ROOTS: "d335c08721b42473a7098570e05b449f2cb346629904823b9f42756afb07234c",
    AUDIT: "aea7420a7db60855594a050186a8cccd4573bba93d84a0ea4ce4d41063d3ed5c",
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
        verify(PRIMARY) == {"shards": 3, "records": 72, "bytes": 4687224},
        "sharded custody",
    )

    signs = tuple(itertools.product((-1, 1), repeat=2))
    expected = {
        (epsilon, branch_index, b_index, c_index)
        for epsilon in signs
        for branch_index in range(3)
        for b_index in (2, 3)
        for c_index in (4, 5, 6)
    }
    seen = set()
    for row in iter_records(PRIMARY):
        key = (
            tuple(row["epsilon"]),
            row["branch_index"],
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
            and row["pairing_index"] == 1
            and row["sigma_c_anchor"] == 0
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
        len(summary["rows"]) == 72
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
        and sum(len(row["roots"]) for row in roots["rows"]) == 708
        and max(row["degree"] for row in roots["rows"]) == 768,
        "external root census",
    )
    audit = json.loads(AUDIT.read_text())
    require(
        audit["status"] == "PASS"
        and audit["rows"] == 72
        and audit["source_point_count"] == audit["route_point_count"] == 1296
        and audit["checked"] == 936
        and audit["common_z_roots"] == 144
        and audit["z_candidate_count"] == audit["z_lifts"] == 144
        and audit["final_color_nonzero"] == 576
        and audit["final_pair_solution_count"] == 0
        and audit["chart_b_paid"] == 72
        and audit["chart_c_paid"] == 144
        and audit["regularized_paid"] == 144,
        "direct replay terminal",
    )

    spec = importlib.util.spec_from_file_location("label_router", ROUTER)
    router = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(router)
    selected = [orbit for orbit in router.compile_orbits() if (3, 1) in orbit]
    require(selected == [[(3, 1), (4, 1)]], "two-label orbit transport")
    print(
        "PASS cell-9 xi3 pairing-1 reciprocal-linear exclusion: rows=72 "
        "routes=1296 lifts=144 colored=576 labels=2"
    )


if __name__ == "__main__":
    main()
