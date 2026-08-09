#!/usr/bin/env python3
"""Verify the cell-9 pairing-3/6 nested-quadratic exclusion."""

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
PRIMARY = EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing3_chart_result/manifest.json"
SUMMARY = EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing3_chart_scout_result.json"
ROOTS = EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing3_frobenius_roots_result.json"
AUDIT = EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing3_direct_audit_result.json"
ROUTER = EXP / "rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
HASHES = {
    PRIMARY: "62ce86664ea56bc29fa11c6d978ea496745b3f34c1c8665477a62f214456a527",
    SUMMARY: "01b3bdd1989a42ca1b98449c25e2a9488e9c86263878e19c75b8e21b52bd7c4e",
    ROOTS: "0aa79f4256d31aa6665061241af79a9f9588e3088946fc54e0af7132dee0a79e",
    AUDIT: "330c4783d6bc345c412ecfc371d224d841f9920d7efd798a3bc594c7c87a2622",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    for path, expected in HASHES.items():
        require(hashlib.sha256(path.read_bytes()).hexdigest() == expected,
                f"hash: {path.name}")
    require(verify(PRIMARY) == {"shards": 6, "records": 192,
                                "bytes": 31504272}, "sharded custody")

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
                and row["pairing_index"] == 3
                and tuple(map(tuple, row["matching"]))
                == ((0, 2), (1, 3), (4, 5))
                and (row["p_u_degree"], row["p_v_degree"],
                     row["nested_quartic_degree"], row["remainder_degree"])
                == (2, 2, 4, 1)
                and not row["witnesses"] and not row["unresolved"]
                and not row["colored_solutions"], "primary terminal")
    require(seen == expected, "primary complete cover")

    summary = json.loads(SUMMARY.read_text())
    require(len(summary["rows"]) == 192
            and all(row["status"] == "COMPLETE" and row["excluded"]
                    and not row["witnesses"] and not row["unresolved"]
                    for row in summary["rows"]), "compact summary")
    roots = json.loads(ROOTS.read_text())
    require(roots["field"] == 2130706433 and len(roots["rows"]) == 69
            and sum(len(row["roots"]) for row in roots["rows"]) == 360
            and max(row["degree"] for row in roots["rows"]) == 4816,
            "external root census")
    audit = json.loads(AUDIT.read_text())
    require(audit["status"] == "PASS" and audit["rows"] == 192
            and audit["source_point_count"] == audit["route_point_count"]
            == 2784 and audit["uv_candidate_count"] == 384
            and audit["uv_checked"] == 384 and audit["f_rows"] == 768
            and audit["colored_nonzero"] == 768
            and audit["colored_solution_count"] == 0
            and audit["chart_b_paid"] == 192
            and audit["chart_c_paid"] == 384
            and audit["regularized_paid"] == 384, "direct replay terminal")

    spec = importlib.util.spec_from_file_location("label_router", ROUTER)
    router = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(router)
    selected = [orbit for orbit in router.compile_orbits()
                if {(0, 3), (2, 3)} & set(orbit)]
    require(selected == [
        [(0, 3), (0, 6), (1, 3), (1, 6)],
        [(2, 3), (2, 6)],
    ], "six-label orbit transport")
    print("PASS cell-9 pairing-3/6 exclusion: rows=192 routes=2784 "
          "uv=384 f=768 orbits=2 labels=6")


if __name__ == "__main__":
    main()
