#!/usr/bin/env python3
"""Verify the cell-9 positive pairing-12/13 exclusion."""

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
PRIMARY = EXP / "rate_half_kb_positive_433_1b_cell9_positive_de_pairing12_chart_result/manifest.json"
SUMMARY = EXP / "rate_half_kb_positive_433_1b_cell9_positive_de_pairing12_chart_scout_result.json"
ROOTS = EXP / "rate_half_kb_positive_433_1b_cell9_positive_de_pairing12_frobenius_roots_result.json"
AUDIT = EXP / "rate_half_kb_positive_433_1b_cell9_positive_de_pairing12_direct_audit_result.json"
ROUTER = EXP / "rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
HASHES = {
    PRIMARY: "ae49719c0f3687979dafe1506876c8e397414f7b9121150dbd8b572b116b9cc4",
    SUMMARY: "9b297521ae831afe104cc9852309888723df139884fc1b0900d66ece06fd4344",
    ROOTS: "a93e2ec2239b10212dbfb025bf3216e22699933d4bbe4a94578d08268ace14d2",
    AUDIT: "1d129677315de816fcb5d836ae43738e67d9261e687009926d7720bde87aec55",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    for path, expected in HASHES.items():
        require(hashlib.sha256(path.read_bytes()).hexdigest() == expected,
                f"hash: {path.name}")
    require(verify(PRIMARY) == {"shards": 3, "records": 96,
                                "bytes": 33716536}, "sharded custody")

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
                and row["pairing_index"] == 12
                and tuple(map(tuple, row["matching"]))
                == ((0, 5), (1, 2), (3, 4))
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
            == 1728 and audit["uf_candidate_count"] == 192
            and audit["uf_checked"] == 192
            and audit["colored_nonzero"] == 192
            and audit["colored_solution_count"] == 0
            and audit["chart_b_paid"] == 96
            and audit["chart_c_paid"] == 192
            and audit["regularized_paid"] == 192, "direct replay terminal")

    spec = importlib.util.spec_from_file_location("label_router", ROUTER)
    router = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(router)
    selected = [orbit for orbit in router.compile_orbits()
                if (0, 12) in orbit]
    require(selected == [
        [(0, 12), (0, 13), (1, 12), (1, 13)],
    ], "four-label orbit transport")
    print("PASS cell-9 positive pairing-12/13 exclusion: rows=96 routes=1728 "
          "uf=192 colored=192 orbits=1 labels=4")


if __name__ == "__main__":
    main()
