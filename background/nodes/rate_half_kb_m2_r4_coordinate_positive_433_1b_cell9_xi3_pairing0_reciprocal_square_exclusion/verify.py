#!/usr/bin/env python3
"""Verify the cell-9 xi3 pairing-0 reciprocal-square exclusion."""

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
PRIMARY = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing0_chart_result/manifest.json"
SUMMARY = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing0_chart_scout_result.json"
ROOTS = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing0_frobenius_roots_result.json"
AUDIT = EXP / "rate_half_kb_positive_433_1b_cell9_xi3_pairing0_direct_audit_result.json"
ROUTER = EXP / "rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
HASHES = {
    PRIMARY: "01863298143d3ede7eec333159dbf894d3ba98819820e46eb3d0d5a2849bf6d4",
    SUMMARY: "104b881c9e2e6e57ceeeb77316766704f065b39791d4370443931166cd7afb3c",
    ROOTS: "271d1b8ec0b86609662b240fb92cf641c38756b94e5a8828a8601905606d62a1",
    AUDIT: "aac3a5ddf8b7533207c71b88db3da8f3ee52dce55e4cf58021127db34392307f",
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
        verify(PRIMARY) == {"shards": 5, "records": 144, "bytes": 7360458},
        "sharded custody",
    )

    signs = tuple(itertools.product((-1, 1), repeat=2))
    expected = {
        (epsilon, branch_index, sigma_o, b_index, c_index)
        for epsilon in signs
        for branch_index in range(3)
        for sigma_o in (-1, 1)
        for b_index in (2, 3)
        for c_index in (4, 5, 6)
    }
    seen = set()
    for row in iter_records(PRIMARY):
        key = (
            tuple(row["epsilon"]),
            row["branch_index"],
            row["sigma_o"],
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
            and row["pairing_index"] == 0
            and (row["missing_cut_degree"], row["outside_cut_degree"])
            == (2, 2)
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
        and len(roots["rows"]) == 113
        and sum(len(row["roots"]) for row in roots["rows"]) == 644
        and max(row["degree"] for row in roots["rows"]) == 764,
        "external root census",
    )
    audit = json.loads(AUDIT.read_text())
    require(
        audit["status"] == "PASS"
        and audit["rows"] == 144
        and audit["source_point_count"] == audit["route_point_count"] == 1968
        and audit["checked"] == 1248
        and audit["common_y_roots"] == 288
        and audit["yd_candidate_count"] == audit["d_lifts"] == 576
        and audit["third_pair_nonzero"] == 1152
        and audit["final_pair_solution_count"] == 0
        and audit["chart_b_paid"] == 144
        and audit["chart_c_paid"] == 288
        and audit["regularized_paid"] == 288,
        "direct replay terminal",
    )

    spec = importlib.util.spec_from_file_location("label_router", ROUTER)
    router = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(router)
    selected = [orbit for orbit in router.compile_orbits() if (3, 0) in orbit]
    require(selected == [[(3, 0), (4, 0)]], "two-label orbit transport")
    print(
        "PASS cell-9 xi3 pairing-0 reciprocal-square exclusion: rows=144 "
        "routes=1968 lifts=576 colored=1152 labels=2"
    )


if __name__ == "__main__":
    main()
