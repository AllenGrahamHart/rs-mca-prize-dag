#!/usr/bin/env python3
"""Verify the cell-9 pairing-5/8/12/13 nested-quadratic exclusion."""

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
PRIMARY = EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing5_chart_result/manifest.json"
SUMMARY = EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing5_chart_scout_result.json"
ROOTS = EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing5_frobenius_roots_result.json"
AUDIT = EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing5_direct_audit_result.json"
RECOVERY = EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing5_chart_result_recovery_175_176_177/manifest.json"
RECOVERY_SUMMARY = EXP / "rate_half_kb_positive_433_1b_cell9_de_pairing5_chart_scout_result_recovery_175_176_177.json"
ROUTER = EXP / "rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
HASHES = {
    PRIMARY: "d1c73b4e56eb12bf12fa1896325d181c456dcc5f2b3c89042cac1765875264ac",
    SUMMARY: "dc0bbfebfb60c9e1f0a6ae48c84c93868dc7c7e6b91e6161e27e0faf56b967b3",
    ROOTS: "26ace83c367ee2391f7940beb8d457f567d086a1eba49eeacce76db425ae920a",
    AUDIT: "32e2fd8972f2fc1232adbe397d5fc4a4e480d989085875c8af1dc6c435af61ea",
    RECOVERY: "c44dcdeede73a9befd45e8c7f44302f8bfcf5439e1ff7f37423d1151f3c9dfcc",
    RECOVERY_SUMMARY: "66cccd38020592fc007cc7b153fe8e30d15bf0d01ea3514176daf2061b1cbd35",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    for path, expected in HASHES.items():
        require(hashlib.sha256(path.read_bytes()).hexdigest() == expected,
                f"hash: {path.name}")
    require(verify(PRIMARY) == {"shards": 6, "records": 192,
                                "bytes": 68182568}, "sharded custody")
    require(verify(RECOVERY)["records"] == 3, "recovery custody")

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
                and row["pairing_index"] == 5
                and tuple(map(tuple, row["matching"]))
                == ((0, 2), (1, 5), (3, 4))
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
            and sum(len(row["roots"]) for row in roots["rows"]) == 264
            and max(row["degree"] for row in roots["rows"]) == 10864,
            "external root census")
    audit = json.loads(AUDIT.read_text())
    require(audit["status"] == "PASS" and audit["rows"] == 192
            and audit["source_point_count"] == audit["route_point_count"]
            == 3072 and audit["uf_candidate_count"] == 576
            and audit["uf_checked"] == 576
            and audit["colored_nonzero"] == 576
            and audit["colored_solution_count"] == 0
            and audit["chart_b_paid"] == 192
            and audit["chart_c_paid"] == 384
            and audit["regularized_paid"] == 384, "direct replay terminal")

    spec = importlib.util.spec_from_file_location("label_router", ROUTER)
    router = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(router)
    selected = [orbit for orbit in router.compile_orbits()
                if {(0, 5), (2, 5)} & set(orbit)]
    require(selected == [
        [(0, 5), (0, 8), (1, 5), (1, 8)],
        [(2, 5), (2, 8), (2, 12), (2, 13)],
    ], "eight-label orbit transport")
    print("PASS cell-9 pairing-5/8/12/13 exclusion: rows=192 routes=3072 "
          "uf=576 colored=576 orbits=2 labels=8")


if __name__ == "__main__":
    main()
