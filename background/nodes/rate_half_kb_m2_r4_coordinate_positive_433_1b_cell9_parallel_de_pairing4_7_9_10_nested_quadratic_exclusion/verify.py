#!/usr/bin/env python3
"""Verify the cell-9 pairing-4/7/9/10 nested-quadratic exclusion."""

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
PRIMARY = EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing4_chart_result/manifest.json"
SUMMARY = EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing4_chart_scout_result.json"
ROOTS = EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing4_frobenius_roots_result.json"
AUDIT = EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing4_direct_audit_result.json"
ROUTER = EXP / "rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
HASHES = {
    PRIMARY: "a80eaed4e083056ec86f50beffc98b6b56132bd5240b23a8cb86c458bcb894f8",
    SUMMARY: "ba58801d8ec1d18458456ac3e890811f6f8627c529f9d1ba576025182bb07c30",
    ROOTS: "cb282cb16fa653acfd9eae3de7badab2f6ab771b69ec0adea22a244c878c2895",
    AUDIT: "c73d3b2bd07f554c3d13926972bda7c6e7b301d489713d0fd9f3b8c6cf876211",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    for path, expected in HASHES.items():
        require(hashlib.sha256(path.read_bytes()).hexdigest() == expected,
                f"hash: {path.name}")
    require(verify(PRIMARY) == {"shards": 6, "records": 192,
                                "bytes": 69213912}, "sharded custody")

    signs = tuple(itertools.product((-1, 1), repeat=2))
    expected = {
        (epsilon, sigma, xi, b_index, c_index)
        for epsilon in signs for sigma in signs for xi in (0, 2)
        for b_index in (2, 3) for c_index in (4, 5, 6)
    }
    seen = set()
    for row in iter_records(PRIMARY):
        key = (tuple(row["epsilon"]), tuple(row["sigma"]), row["xi_index"],
               row["b_row_index"], row["c_row_index"])
        require(key in expected and key not in seen, "primary Cartesian row")
        seen.add(key)
        require(row["status"] == "COMPLETE" and row["excluded"]
                and row["pairing_index"] == 4
                and tuple(map(tuple, row["matching"]))
                == ((0, 2), (1, 4), (3, 5))
                and (row["p_u_degree"], row["p_f_degree"],
                     row["uf_eliminant_degree"], row["remainder_degree"])
                == (2, 2, 8, 1)
                and not row["witnesses"] and not row["unresolved"]
                and not row["colored_solutions"], "primary terminal")
    require(seen == expected, "primary complete cover")

    summary = json.loads(SUMMARY.read_text())
    require(len(summary["rows"]) == 192
            and all(row["status"] == "COMPLETE" and row["excluded"]
                    and not row["witnesses"] and not row["unresolved"]
                    for row in summary["rows"]), "compact summary")
    roots = json.loads(ROOTS.read_text())
    require(roots["field"] == 2130706433 and len(roots["rows"]) == 61
            and sum(len(row["roots"]) for row in roots["rows"]) == 308
            and max(row["degree"] for row in roots["rows"]) == 10944,
            "external root census")
    audit = json.loads(AUDIT.read_text())
    require(audit["status"] == "PASS" and audit["rows"] == 192
            and audit["source_point_count"] == audit["route_point_count"]
            == 4032 and audit["uf_candidate_count"] == 960
            and audit["uf_checked"] == 960
            and audit["colored_nonzero"] == 960
            and audit["colored_solution_count"] == 0
            and audit["chart_b_paid"] == 192
            and audit["chart_c_paid"] == 384
            and audit["regularized_paid"] == 384, "direct replay terminal")

    spec = importlib.util.spec_from_file_location("label_router", ROUTER)
    router = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(router)
    selected = [orbit for orbit in router.compile_orbits()
                if {(0, 4), (2, 4)} & set(orbit)]
    require(selected == [
        [(0, 4), (0, 7), (1, 4), (1, 7)],
        [(2, 4), (2, 7), (2, 9), (2, 10)],
    ], "eight-label orbit transport")
    print("PASS cell-9 pairing-4/7/9/10 exclusion: rows=192 routes=4032 "
          "uf=960 colored=960 orbits=2 labels=8")


if __name__ == "__main__":
    main()
