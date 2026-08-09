#!/usr/bin/env python3
"""Verify the cell-9 pairing-11/14 common-f exclusion."""

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
PRIMARY = EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing11_chart_result/manifest.json"
SUMMARY = EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing11_chart_scout_result.json"
ROOTS = EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing11_frobenius_roots_result.json"
AUDIT = EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing11_direct_audit_result.json"
ROUTER = EXP / "rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
HASHES = {
    PRIMARY: "01ddc36f244f5a951cb0f2948d8099e261644d8d3cc1df8113d29c6d85d30fe4",
    SUMMARY: "f6c446c3175d8ef50cb666efb47c9c8e32248e16c7b4f3fb94363d21086995df",
    ROOTS: "5ed5be0505f3281466f007c8d22ce9c35e8ad62cea5c1caa4678f21d917ea29a",
    AUDIT: "3724358d263fe61f43cc0b3ed02a41af72b3be9239120868b8b16b14d32f3a6f",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    for path, expected in HASHES.items():
        require(hashlib.sha256(path.read_bytes()).hexdigest() == expected,
                f"hash: {path.name}")
    require(verify(PRIMARY) == {"shards": 6, "records": 192,
                                "bytes": 10567452}, "sharded custody")

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
                and row["pairing_index"] == 11
                and tuple(map(tuple, row["matching"]))
                == ((0, 4), (1, 5), (2, 3))
                and not row["witnesses"] and not row["unresolved"]
                and not row["colored_solutions"], "primary terminal")
    require(seen == expected, "primary complete cover")

    summary = json.loads(SUMMARY.read_text())
    require(len(summary["rows"]) == 192
            and all(row["status"] == "COMPLETE" and row["excluded"]
                    and not row["witnesses"] and not row["unresolved"]
                    for row in summary["rows"]), "compact summary")

    roots = json.loads(ROOTS.read_text())
    require(roots["field"] == 2130706433 and len(roots["rows"]) == 73
            and sum(len(row["roots"]) for row in roots["rows"]) == 364
            and max(row["degree"] for row in roots["rows"]) == 1396,
            "external root census")
    audit = json.loads(AUDIT.read_text())
    require(audit["status"] == "PASS" and audit["rows"] == 192
            and audit["source_point_count"] == 2496
            and audit["route_point_count"] == 2496
            and audit["uf_candidate_count"] == 1152
            and audit["colored_nonzero"] == 1152
            and audit["colored_solution_count"] == 0
            and audit["chart_b_paid"] == 192
            and audit["chart_c_paid"] == 384
            and audit["regularized_paid"] == 384, "direct replay terminal")

    spec = importlib.util.spec_from_file_location("label_router", ROUTER)
    router = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(router)
    selected = [orbit for orbit in router.compile_orbits()
                if {(0, 11), (2, 11)} & set(orbit)]
    require(selected == [[(0, 11), (1, 11)], [(2, 11), (2, 14)]],
            "four-label orbit transport")
    print("PASS cell-9 pairing-11/14 exclusion: rows=192 routes=2496 "
          "lifts=1152 orbits=2 labels=4")


if __name__ == "__main__":
    main()
