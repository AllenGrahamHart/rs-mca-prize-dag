#!/usr/bin/env python3
"""Verify the cell-9 positive pairing-14 common-f exclusion."""

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
PRIMARY = EXP / "rate_half_kb_positive_433_1b_cell9_positive_de_pairing14_chart_result/manifest.json"
SUMMARY = EXP / "rate_half_kb_positive_433_1b_cell9_positive_de_pairing14_chart_scout_result.json"
ROOTS = EXP / "rate_half_kb_positive_433_1b_cell9_positive_de_pairing14_frobenius_roots_result.json"
AUDIT = EXP / "rate_half_kb_positive_433_1b_cell9_positive_de_pairing14_direct_audit_result.json"
ROUTER = EXP / "rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
HASHES = {
    PRIMARY: "2c71dd2914483f97fa776db8b2cc712e8ba76d4e5348351e8bd72e68eaf3a2c5",
    SUMMARY: "008d102db6bb8090029149e4143b2fe0a6927e3f72d03beceb005441168f29ad",
    ROOTS: "2ae6a6d9a80bb739d8a12a92b0a714f0a43f0069673ae5ede1c2a38071185117",
    AUDIT: "47c44a6d6d65042f9523be9ed50cc34f51d2e81ed0b54a49a634c5e0b51eb0d7",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    for path, expected in HASHES.items():
        require(hashlib.sha256(path.read_bytes()).hexdigest() == expected,
                f"hash: {path.name}")
    require(verify(PRIMARY) == {"shards": 3, "records": 96,
                                "bytes": 5226024}, "sharded custody")

    signs = tuple(itertools.product((-1, 1), repeat=2))
    expected = {
        (epsilon, sigma, 0, b_index, c_index)
        for epsilon in signs for sigma in signs
        for b_index in (2, 3) for c_index in (4, 5, 6)
    }
    seen = set()
    for row in iter_records(PRIMARY):
        key = (tuple(row["epsilon"]), tuple(row["sigma"]), row["xi_index"],
               row["b_row_index"], row["c_row_index"])
        require(key in expected and key not in seen, "primary Cartesian row")
        seen.add(key)
        require(row["status"] == "COMPLETE" and row["excluded"]
                and row["pairing_index"] == 14
                and tuple(map(tuple, row["matching"]))
                == ((0, 5), (1, 4), (2, 3))
                and (row["p_b_degree"], row["p_c_degree"]) == (2, 2)
                and row["common_f_resultant"]
                and not row["witnesses"] and not row["unresolved"]
                and not row["colored_solutions"], "primary terminal")
    require(seen == expected, "primary complete cover")

    summary = json.loads(SUMMARY.read_text())
    require(len(summary["rows"]) == 96
            and all(row["status"] == "COMPLETE" and row["excluded"]
                    and not row["witnesses"] and not row["unresolved"]
                    for row in summary["rows"]), "compact summary")
    roots = json.loads(ROOTS.read_text())
    require(roots["field"] == 2130706433 and len(roots["rows"]) == 57
            and sum(len(row["roots"]) for row in roots["rows"]) == 244
            and max(row["degree"] for row in roots["rows"]) == 1372,
            "external root census")
    audit = json.loads(AUDIT.read_text())
    require(audit["status"] == "PASS" and audit["rows"] == 96
            and audit["source_point_count"] == audit["route_point_count"]
            == 1152 and audit["uf_candidate_count"] == 384
            and audit["colored_nonzero"] == 384
            and audit["colored_solution_count"] == 0
            and audit["chart_b_paid"] == 96
            and audit["chart_c_paid"] == 192
            and audit["regularized_paid"] == 192, "direct replay terminal")

    spec = importlib.util.spec_from_file_location("label_router", ROUTER)
    router = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(router)
    selected = [orbit for orbit in router.compile_orbits()
                if (0, 14) in orbit]
    require(selected == [[(0, 14), (1, 14)]],
            "two-label orbit transport")
    print("PASS cell-9 positive pairing-14 common-f exclusion: rows=96 "
          "routes=1152 lifts=384 colored=384 labels=2")


if __name__ == "__main__":
    main()
