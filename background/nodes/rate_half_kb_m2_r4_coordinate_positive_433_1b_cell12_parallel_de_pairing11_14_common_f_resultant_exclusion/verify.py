#!/usr/bin/env python3
"""Verify the cell-12 parallel-DE pairing-11/14 packet."""

import ast
import collections
import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell12_de_pairing11_template_adapter_modal.py"
RESULT = EXP / "rate_half_kb_positive_433_1b_cell12_de_pairing11_template_adapter_result.json"
TEMPLATE = EXP / "rate_half_kb_positive_433_1b_cell4_de_pairing11_common_f_resultant_modal.py"
TOWER = EXP / "rate_half_kb_positive_433_1b_cell12_four_basis_tower_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell12_compact_kernel_result.json"
ROOT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell12_de_pairing11_14_frobenius_roots_modal.py"
ROOT_RESULT = EXP / "rate_half_kb_positive_433_1b_cell12_de_pairing11_14_frobenius_roots_result.json"
AUDIT = EXP / "rate_half_kb_positive_433_1b_cell12_common_f_resultant_audit.py"
PINNED = {
    SCRIPT: "95b3dec780212cd34f29a17ae53f22370947ff123d37fd532d78a42c4f345bef",
    RESULT: "95feb8538e18220df5aa8e152510a3a48b624b8414afdabf216620aebbe6f8d4",
    TEMPLATE: "3e3c5aa6b389ee572998bd46626b2df7956c475baaf4832378ef9ec4b6774664",
    ROOT_SCRIPT: "ecb93155c17cf700f53e2e49a8545261f5578cd30f3244d33e1bb37d3a55bb17",
    ROOT_RESULT: "27f54d3b36d9c22992bd6035cd5058e70da77cdf9c29ec9b9f4977daf77a7ead",
    AUDIT: "fb671d5f602fa274583d66c0da0f9ef1bfe2afa43dbf588b089c643fcd3f7c93",
}
P = 2130706433
MATCHING = ((0, 4), (1, 5), (2, 3))


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    for path, expected in PINNED.items():
        require(digest(path) == expected, f"hash drift: {path.name}")
    source = SCRIPT.read_text()
    ast.parse(source)
    require("function.decorator_list = []" in source
            and 'node.name == "evaluate_case"' in source,
            "AST adapter boundary")
    payload = json.loads(RESULT.read_text())
    require(
        payload["schema"]
        == "rate-half-kb-positive-433-1b-cell12-de-pairing11-adapter-v1"
        and payload["field"] == P
        and payload["source_template_sha256"] == digest(TEMPLATE)
        and payload["source_tower_sha256"] == digest(TOWER)
        and payload["source_kernel_sha256"] == digest(KERNEL),
        "packet custody",
    )
    expected = set(itertools.product(
        itertools.product((-1, 1), repeat=2),
        itertools.product((-1, 1), repeat=2),
        (0, 2),
    ))
    seen = set()
    for row in payload["rows"]:
        key = (tuple(row["epsilon"]), tuple(row["sigma"]), row["xi_index"])
        require(key in expected and key not in seen, "Cartesian row")
        seen.add(key)
        require(row["status"] == "COMPLETE" and row["excluded"]
                and row["pairing_index"] == 11
                and tuple(map(tuple, row["matching"])) == MATCHING
                and not row["witnesses"] and not row["unresolved"],
                "complete terminal")
    require(seen == expected and len(payload["rows"]) == 32, "32-row cover")
    totals = tuple(sum(row[key] for row in payload["rows"]) for key in (
        "target_root_count", "candidate_root_count", "source_point_count",
        "route_point_count", "uf_candidate_count", "colored_solution_count",
    ))
    require(totals == (256, 464, 592, 592, 0, 0), "exact totals")
    finite = collections.Counter(
        item["status"] for row in payload["rows"] for item in row["finite_rows"]
    )
    boundary = collections.Counter(
        item["stage"] for row in payload["rows"] for item in row["boundary_rows"]
    )
    require(finite == {"CHECKED": 400, "MISSING_IMPOSSIBLE": 96,
                       "TARGET_PRODUCT_BOUNDARY": 96}
            and boundary == {"R_GUARD": 160, "T_GUARD": 128,
                             "CELL12_B_LEADING": 32}, "terminal partition")
    manifest = json.loads((NODE / "node.json").read_text())["node"]
    require(manifest["id"] == NODE.name and manifest["status"] == "PROVED",
            "node manifest")
    require("{(0,11),(1,11),(2,11),(2,14)}" in manifest["statement"],
            "four-label scope")
    print("PASS cell-12 parallel-DE pairing 11/14: rows=32 candidates=464")


if __name__ == "__main__":
    main()
