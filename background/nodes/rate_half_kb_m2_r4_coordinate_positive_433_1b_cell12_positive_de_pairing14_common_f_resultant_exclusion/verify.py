#!/usr/bin/env python3
"""Verify the cell-12 positive-DE pairing-14 packet."""

import ast
import collections
import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell12_positive_de_pairing14_template_adapter_modal.py"
RESULT = EXP / "rate_half_kb_positive_433_1b_cell12_positive_de_pairing14_template_adapter_result.json"
TEMPLATE = EXP / "rate_half_kb_positive_433_1b_cell4_positive_de_pairing14_common_f_resultant_modal.py"
TOWER = EXP / "rate_half_kb_positive_433_1b_cell12_four_basis_tower_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell12_compact_kernel_result.json"
ROOT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell12_de_pairing11_14_frobenius_roots_modal.py"
ROOT_RESULT = EXP / "rate_half_kb_positive_433_1b_cell12_de_pairing11_14_frobenius_roots_result.json"
AUDIT = EXP / "rate_half_kb_positive_433_1b_cell12_common_f_resultant_audit.py"
PINNED = {
    SCRIPT: "b5b0aec86aca8b8d2ac5da9fa0fbc8ecdf6a5a6eccc8c134629354dcda91decb",
    RESULT: "0d2eeef9c313023b1996b2a23b68c9f976f47ae0561f701c972a5458ee2ad8e8",
    TEMPLATE: "d46de7b84de40e9be7902d9c26e51df8b2e9fd99e7d208e78fc110338feb406a",
    ROOT_SCRIPT: "ecb93155c17cf700f53e2e49a8545261f5578cd30f3244d33e1bb37d3a55bb17",
    ROOT_RESULT: "27f54d3b36d9c22992bd6035cd5058e70da77cdf9c29ec9b9f4977daf77a7ead",
    AUDIT: "fb671d5f602fa274583d66c0da0f9ef1bfe2afa43dbf588b089c643fcd3f7c93",
}
P = 2130706433
MATCHING = ((0, 5), (1, 4), (2, 3))


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
        == "rate-half-kb-positive-433-1b-cell12-positive-de-pairing14-adapter-v1"
        and payload["field"] == P
        and payload["source_template_sha256"] == digest(TEMPLATE)
        and payload["source_tower_sha256"] == digest(TOWER)
        and payload["source_kernel_sha256"] == digest(KERNEL),
        "packet custody",
    )
    expected = set(itertools.product(
        itertools.product((-1, 1), repeat=2),
        itertools.product((-1, 1), repeat=2),
    ))
    seen = set()
    for row in payload["rows"]:
        key = (tuple(row["epsilon"]), tuple(row["sigma"]))
        require(key in expected and key not in seen, "Cartesian row")
        seen.add(key)
        require(row["status"] == "COMPLETE" and row["excluded"]
                and row["xi_index"] == 0 and row["pairing_index"] == 14
                and tuple(map(tuple, row["matching"])) == MATCHING
                and not row["witnesses"] and not row["unresolved"],
                "complete terminal")
    require(seen == expected and len(payload["rows"]) == 16, "16-row cover")
    totals = tuple(sum(row[key] for row in payload["rows"]) for key in (
        "target_root_count", "candidate_root_count", "source_point_count",
        "route_point_count", "uf_candidate_count", "colored_solution_count",
    ))
    require(totals == (120, 224, 304, 304, 64, 0), "exact totals")
    finite = collections.Counter(
        item["status"] for row in payload["rows"] for item in row["finite_rows"]
    )
    boundary = collections.Counter(
        item["stage"] for row in payload["rows"] for item in row["boundary_rows"]
    )
    endings = collections.Counter(
        item["status"] for row in payload["rows"]
        for finite in row["finite_rows"] for item in finite.get("uf_rows", [])
    )
    require(finite == {"CHECKED": 208, "MISSING_IMPOSSIBLE": 48,
                       "TARGET_PRODUCT_BOUNDARY": 48}
            and boundary == {"R_GUARD": 80, "T_GUARD": 64,
                             "CELL12_B_LEADING": 16}
            and endings == {"COLORED_PAIR_NONZERO": 64},
            "terminal partition")
    manifest = json.loads((NODE / "node.json").read_text())["node"]
    require(manifest["id"] == NODE.name and manifest["status"] == "PROVED",
            "node manifest")
    print("PASS cell-12 positive-DE pairing 14: rows=16 candidates=224 lifts=64")


if __name__ == "__main__":
    main()
