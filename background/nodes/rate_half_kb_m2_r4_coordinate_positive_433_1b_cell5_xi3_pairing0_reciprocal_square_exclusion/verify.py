#!/usr/bin/env python3
"""Verify the cell-5 xi=3 pairing-0 reciprocal-square packet."""

import ast
import collections
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell5_xi3_pairing0_template_adapter_modal.py"
RESULT = EXP / "rate_half_kb_positive_433_1b_cell5_xi3_pairing0_template_adapter_result.json"
TEMPLATE = EXP / "rate_half_kb_positive_433_1b_cell4_xi3_pairing0_reciprocal_square_modal.py"
TOWER = EXP / "rate_half_kb_positive_433_1b_cell5_four_basis_tower_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell5_compact_kernel_result.json"
ROOT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell5_xi3_pairing0_independent_roots_modal.py"
ROOT_RESULT = EXP / "rate_half_kb_positive_433_1b_cell5_xi3_pairing0_independent_roots_result.json"
AUDIT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell5_xi3_pairing0_direct_audit_modal.py"
AUDIT_RESULT = EXP / "rate_half_kb_positive_433_1b_cell5_xi3_pairing0_direct_audit_result.json"
ROUTER = EXP / "rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
PINNED = {
    SCRIPT: "f2d1507b8ce34e027f2fc43a329f6bf188e55c2323c6848fe62428ea2c9e3483",
    RESULT: "dd17c38b0a13afbefe5474e5f509ff39982e29f791abbfe1ff71051d7a652f88",
    TEMPLATE: "be6e74f8713af6f26fe183a00e5bc50d0a89aa1fdd53c1c636525165a2f5ae68",
    TOWER: "68c18173d4133f66a85136b1ecc33235f7e979c26b6f96d8592030901a8a335c",
    KERNEL: "627a8df8bb8a2da4e11488658d1c2145b8c65ef7fbcef3f0f4f53f9d05ea752d",
    ROOT_SCRIPT: "d77898d300e3c7620482fd62caafc2819ccabcd615e71de9231d14443771f8c6",
    ROOT_RESULT: "f25732afd5c55f40d853b8f0476366b861a1b3dfe8dba54e8499ccca17c7f99f",
    AUDIT_SCRIPT: "1892e54c7cdde0bc657ac1a08d4fc16b09fa002c1fe1783b7b6aa483ed0b9456",
    AUDIT_RESULT: "01768e946edabea06444fa42f278aab1638bc2d76f54dec8fa0ed4bce8e53fb7",
    ROUTER: "82df776b06b375e9bee6fcc77aead1ebca4594028fa2e51df6318422a9d2f9bb",
}
P = 2130706433


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def lanes(row):
    for finite in row["finite_rows"]:
        for y_row in finite.get("yd_rows", []):
            for d_row in y_row.get("d_rows", []):
                yield from d_row.get("lanes", [])


def main():
    for path, expected_digest in PINNED.items():
        require(digest(path) == expected_digest, f"hash drift: {path.name}")
    source = SCRIPT.read_text()
    ast.parse(source)
    require("function.decorator_list = []" in source
            and 'node.name == "evaluate_case"' in source,
            "AST adapter boundary")
    payload = json.loads(RESULT.read_text())
    require(
        payload["schema"]
        == "rate-half-kb-positive-433-1b-cell5-xi3-pairing0-adapter-v1"
        and payload["field"] == P
        and payload["source_template_sha256"] == digest(TEMPLATE)
        and payload["source_tower_sha256"] == digest(TOWER)
        and payload["source_kernel_sha256"] == digest(KERNEL),
        "packet custody",
    )
    expected = set(itertools.product(
        itertools.product((-1, 1), repeat=2), range(3), (-1, 1)
    ))
    seen = set()
    all_lanes = []
    for row in payload["rows"]:
        key = (tuple(row["epsilon"]), row["branch_index"], row["sigma_o"])
        require(key in expected and key not in seen, "branch coverage")
        seen.add(key)
        require(row["status"] == "COMPLETE" and row["target_excluded"]
                and row["xi_index"] == 3 and row["pairing_index"] == 0
                and row["witness_count"] == 0 and not row["witnesses"]
                and row["final_pair_solution_count"] == 0
                and not row["final_pair_solutions"] and not row["unresolved"],
                "complete branch terminal")
        all_lanes.extend(lanes(row))
    require(seen == expected and len(payload["rows"]) == 24, "24-row cover")
    totals = tuple(sum(row[key] for row in payload["rows"]) for key in (
        "target_norm_root_count", "candidate_root_count",
        "source_point_count", "route_point_count", "yd_candidate_count",
        "final_pair_solution_count",
    ))
    require(totals == (132, 324, 416, 416, 160, 0), "exact census totals")
    require(len(all_lanes) == 320
            and all(item["status"] == "THIRD_PAIR_NONZERO"
                    and item["final_pair_cut"] % P for item in all_lanes),
            "320 final lanes")
    statuses = collections.Counter(
        item["status"] for row in payload["rows"] for item in row["finite_rows"]
    )
    boundaries = collections.Counter(
        item["stage"] for row in payload["rows"] for item in row["boundary_rows"]
    )
    no_lifts = collections.Counter(
        item["stage"] for row in payload["rows"] for item in row["no_lift_rows"]
    )
    require(statuses == {
        "CHECKED": 296, "EMPTY_Q_BRANCH": 24,
        "MISSING_IMPOSSIBLE": 48, "TARGET_PRODUCT_BOUNDARY": 48,
    } and boundaries == {"R_GUARD": 120, "T_GUARD": 96}
      and no_lifts == {"NO_B_ROOT": 104}, "terminal partition")

    roots = json.loads(ROOT_RESULT.read_text())
    require(
        roots["schema"]
        == "rate-half-kb-positive-433-1b-cell5-xi3-pairing0-independent-roots-v1"
        and roots["source_primary_sha256"] == digest(RESULT)
        and len(roots["rows"]) == 93
        and sum(len(row["roots"]) for row in roots["rows"]) == 392
        and max(row["degree"] for row in roots["rows"]) == 548,
        "independent root census",
    )
    audit = json.loads(AUDIT_RESULT.read_text())
    require(audit == {
        "candidate_root_count": 324, "checked": 296,
        "common_y_roots": 80, "d_lifts": 160, "empty_q_branches": 24,
        "field": P, "final_pair_solution_count": 0,
        "missing_impossible": 48, "no_lifts": 104,
        "product_boundaries": 48, "profile_visits": 336,
        "profiles": 93, "r_boundaries": 120, "route_point_count": 416,
        "rows": 24,
        "schema": "rate-half-kb-positive-433-1b-cell5-xi3-pairing0-direct-audit-v1",
        "source_kernel_sha256": digest(KERNEL),
        "source_point_count": 416, "source_primary_sha256": digest(RESULT),
        "source_roots_sha256": digest(ROOT_RESULT),
        "source_template_sha256": digest(TEMPLATE),
        "source_tower_sha256": digest(TOWER), "status": "PASS",
        "t_boundaries": 96, "target_boundaries": 48,
        "target_norm_root_count": 132, "third_pair_nonzero": 320,
        "yd_candidate_count": 160,
    }, "independent direct replay")

    spec = importlib.util.spec_from_file_location("label_router", ROUTER)
    router = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(router)
    selected = [orbit for orbit in router.compile_orbits() if (3, 0) in orbit]
    require(selected == [[(3, 0), (4, 0)]], "two-label orbit transport")
    manifest = json.loads((NODE / "node.json").read_text())["node"]
    require(manifest["id"] == NODE.name and manifest["status"] == "PROVED",
            "node manifest")
    print("PASS cell-5 xi3 pairing 0: rows=24 candidates=324 labels=2")


if __name__ == "__main__":
    main()
