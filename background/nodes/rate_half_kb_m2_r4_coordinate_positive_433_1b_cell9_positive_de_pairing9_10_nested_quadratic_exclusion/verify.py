#!/usr/bin/env python3
"""Verify the cell-9 positive pairing-9/10 exclusion."""

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
PRIMARY = EXP / "rate_half_kb_positive_433_1b_cell9_positive_de_pairing9_chart_result/manifest.json"
SUMMARY = EXP / "rate_half_kb_positive_433_1b_cell9_positive_de_pairing9_chart_scout_result.json"
ROOTS = EXP / "rate_half_kb_positive_433_1b_cell9_positive_de_pairing9_frobenius_roots_result.json"
AUDIT = EXP / "rate_half_kb_positive_433_1b_cell9_positive_de_pairing9_direct_audit_result.json"
ROUTER = EXP / "rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
HASHES = {
    PRIMARY: "d376fb5f9b827ab7eb4d8e1441cff90d9eb484a81aa7ccfab48ae5831f9e820d",
    SUMMARY: "fa3cf0c8cf25c7ee3fc1ebd31a3e4ec22941dccef15faa3dd6b7affaa8d45048",
    ROOTS: "7e8e32808a676ba07334236f3d552ffa0f5bc0987964f9ea08941ba19e1518a3",
    AUDIT: "6ffa9dcdfd15d847707b935e197cde8b61a54a4348208d4317c99dcaba91c3ee",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    for path, expected in HASHES.items():
        require(hashlib.sha256(path.read_bytes()).hexdigest() == expected,
                f"hash: {path.name}")
    require(verify(PRIMARY) == {"shards": 3, "records": 96,
                                "bytes": 33746580}, "sharded custody")

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
                and row["pairing_index"] == 9
                and tuple(map(tuple, row["matching"]))
                == ((0, 4), (1, 2), (3, 5))
                and (row["p_u_degree"], row["p_f_degree"],
                     row["uf_eliminant_degree"], row["remainder_degree"])
                == (2, 2, 8, 1)
                and not row["witnesses"] and not row["unresolved"]
                and not row["colored_solutions"], "primary terminal")
    require(seen == expected, "primary complete cover")

    summary = json.loads(SUMMARY.read_text())
    require(len(summary["rows"]) == 96
            and all(row["status"] == "COMPLETE" and row["excluded"]
                    and not row["witnesses"] and not row["unresolved"]
                    for row in summary["rows"]), "compact summary")
    roots = json.loads(ROOTS.read_text())
    require(roots["field"] == 2130706433 and len(roots["rows"]) == 53
            and sum(len(row["roots"]) for row in roots["rows"]) == 208
            and max(row["degree"] for row in roots["rows"]) == 10674,
            "external root census")
    audit = json.loads(AUDIT.read_text())
    require(audit["status"] == "PASS" and audit["rows"] == 96
            and audit["source_point_count"] == audit["route_point_count"]
            == 1728 and audit["uf_candidate_count"] == 384
            and audit["uf_checked"] == 384
            and audit["colored_nonzero"] == 384
            and audit["colored_solution_count"] == 0
            and audit["chart_b_paid"] == 96
            and audit["chart_c_paid"] == 192
            and audit["regularized_paid"] == 192, "direct replay terminal")

    spec = importlib.util.spec_from_file_location("label_router", ROUTER)
    router = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(router)
    selected = [orbit for orbit in router.compile_orbits()
                if (0, 9) in orbit]
    require(selected == [
        [(0, 9), (0, 10), (1, 9), (1, 10)],
    ], "four-label orbit transport")
    print("PASS cell-9 positive pairing-9/10 exclusion: rows=96 routes=1728 "
          "uf=384 colored=384 orbits=1 labels=4")


if __name__ == "__main__":
    main()
