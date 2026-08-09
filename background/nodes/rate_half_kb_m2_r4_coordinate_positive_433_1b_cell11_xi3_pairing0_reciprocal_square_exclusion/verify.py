#!/usr/bin/env python3
"""Verify the cell-11 xi=3 pairing-0 reciprocal-square packet."""

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
SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell11_xi3_pairing0_template_adapter_modal.py"
RESULT = EXP / "rate_half_kb_positive_433_1b_cell11_xi3_pairing0_template_adapter_result.json"
TEMPLATE = EXP / "rate_half_kb_positive_433_1b_cell4_xi3_pairing0_reciprocal_square_modal.py"
TOWER = EXP / "rate_half_kb_positive_433_1b_cell11_four_basis_tower_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell11_compact_kernel_result.json"
ROOT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell11_xi3_pairing0_independent_roots_modal.py"
ROOT_RESULT = EXP / "rate_half_kb_positive_433_1b_cell11_xi3_pairing0_independent_roots_result.json"
AUDIT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell11_xi3_pairing0_direct_audit_modal.py"
AUDIT_RESULT = EXP / "rate_half_kb_positive_433_1b_cell11_xi3_pairing0_direct_audit_result.json"
ROUTER = EXP / "rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
PINNED = {
    SCRIPT: "d2b5fd32e0b342df7665645f7ba48dca3a392108e33a41fa2dd956a6126c974f",
    RESULT: "8992e513feaa1a4f398c85784c5686a0f1285b2f7a767361e42513edcc7359da",
    TEMPLATE: "be6e74f8713af6f26fe183a00e5bc50d0a89aa1fdd53c1c636525165a2f5ae68",
    TOWER: "8be5facf7fe8e05f9a68fd740964b669e7a47ef2279efbcba504279860717e6a",
    KERNEL: "2ef59a5dd9e656f36fccc63f3c75aaee6889664312928ffe25d0d0816ed16236",
    ROOT_SCRIPT: "843c56f385392e6d02d5ff3795f770945c2d6ad705b3e8bceed5ed9eb2fb9d89",
    ROOT_RESULT: "9bc381a37924cd38e291c13d24810d2643316b08ec239f01598c257d623eea77",
    AUDIT_SCRIPT: "ab8f98e14c8444fa8e0453469252f0a20a0fc1691640fbab3b73fa76b3daf27e",
    AUDIT_RESULT: "d93d514d13e454738aedba83c89f6c621d888b736b7a6283b2fc329f23f6124d",
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
        == "rate-half-kb-positive-433-1b-cell11-xi3-pairing0-adapter-v1"
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
    require(totals == (136, 300, 320, 320, 192, 0), "exact census totals")
    require(len(all_lanes) == 384
            and all(item["status"] == "THIRD_PAIR_NONZERO"
                    and item["final_pair_cut"] % P for item in all_lanes),
            "384 final lanes")
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
        "CHECKED": 176, "EMPTY_Q_BRANCH": 48,
        "MISSING_IMPOSSIBLE": 48, "TARGET_PRODUCT_BOUNDARY": 48,
    } and boundaries == {"R_GUARD": 120, "T_GUARD": 48,
                         "CELL11_B_LEADING": 24,
                         "CELL11_C_LEADING": 24}
      and no_lifts == {"NO_B_ROOT": 116}, "terminal partition")

    roots = json.loads(ROOT_RESULT.read_text())
    require(
        roots["schema"]
        == "rate-half-kb-positive-433-1b-cell11-xi3-pairing0-independent-roots-v1"
        and roots["source_primary_sha256"] == digest(RESULT)
        and len(roots["rows"]) == 89
        and sum(len(row["roots"]) for row in roots["rows"]) == 402
        and max(row["degree"] for row in roots["rows"]) == 756,
        "independent root census",
    )
    audit = json.loads(AUDIT_RESULT.read_text())
    require(audit == {
        "candidate_root_count": 300, "checked": 176,
        "common_y_roots": 96, "d_lifts": 192, "empty_q_branches": 48,
        "field": P, "final_pair_solution_count": 0,
        "leading_boundaries": 48, "missing_impossible": 48, "no_lifts": 116,
        "product_boundaries": 48, "profile_visits": 336,
        "profiles": 89, "r_boundaries": 120, "route_point_count": 320,
        "rows": 24,
        "schema": "rate-half-kb-positive-433-1b-cell11-xi3-pairing0-direct-audit-v1",
        "source_kernel_sha256": digest(KERNEL),
        "source_point_count": 320, "source_primary_sha256": digest(RESULT),
        "source_roots_sha256": digest(ROOT_RESULT),
        "source_template_sha256": digest(TEMPLATE),
        "source_tower_sha256": digest(TOWER), "status": "PASS",
        "t_boundaries": 48, "target_boundaries": 48,
        "target_norm_root_count": 136, "third_pair_nonzero": 384,
        "yd_candidate_count": 192,
    }, "independent direct replay")

    spec = importlib.util.spec_from_file_location("label_router", ROUTER)
    router = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(router)
    selected = [orbit for orbit in router.compile_orbits() if (3, 0) in orbit]
    require(selected == [[(3, 0), (4, 0)]], "two-label orbit transport")
    manifest = json.loads((NODE / "node.json").read_text())["node"]
    require(manifest["id"] == NODE.name and manifest["status"] == "PROVED",
            "node manifest")
    print("PASS cell-11 xi3 pairing 0: rows=24 candidates=300 labels=2")


if __name__ == "__main__":
    main()
