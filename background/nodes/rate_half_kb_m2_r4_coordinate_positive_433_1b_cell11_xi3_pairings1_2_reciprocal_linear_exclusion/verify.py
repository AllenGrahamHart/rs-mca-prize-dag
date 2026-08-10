#!/usr/bin/env python3
"""Verify the cell-11 xi=3 pairings-1/2 reciprocal-linear packet."""

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
SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell11_xi3_pairings1_2_template_adapter_modal.py"
RESULT = EXP / "rate_half_kb_positive_433_1b_cell11_xi3_pairings1_2_template_adapter_result.json"
TEMPLATE = EXP / "rate_half_kb_positive_433_1b_cell4_xi3_pairings1_2_reciprocal_linear_modal.py"
TOWER = EXP / "rate_half_kb_positive_433_1b_cell11_four_basis_tower_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell11_compact_kernel_result.json"
ROOT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell11_xi3_pairings1_2_independent_roots_modal.py"
ROOT_RESULT = EXP / "rate_half_kb_positive_433_1b_cell11_xi3_pairings1_2_independent_roots_result.json"
AUDIT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell11_xi3_pairings1_2_direct_audit_modal.py"
AUDIT_RESULT = EXP / "rate_half_kb_positive_433_1b_cell11_xi3_pairings1_2_direct_audit_result.json"
ROUTER = EXP / "rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
PINNED = {
    SCRIPT: "3f181f16c8530f8966a31909839f1f35466910c91a733e1ab2628e430e840663",
    RESULT: "0a537719ab6b287cf028e6a0e465fff318f62b735bdb774e54ccc453474c3c95",
    TEMPLATE: "6175e9472f571b752273395050247db907e9bbb68065c7c0c8bdd0933e4ac2aa",
    TOWER: "8be5facf7fe8e05f9a68fd740964b669e7a47ef2279efbcba504279860717e6a",
    KERNEL: "2ef59a5dd9e656f36fccc63f3c75aaee6889664312928ffe25d0d0816ed16236",
    ROOT_SCRIPT: "b515b754c745518f3daf742e4f51525f5a141669d6d9a8d4b6113a0c365e2212",
    ROOT_RESULT: "0b3fa65eaf573e76007496a2987fd97d5bf91911dcef90103d0443146f8b961a",
    AUDIT_SCRIPT: "3947060b0f1209daa4320da1c228b39d7220d115738fa679216e0fada2d8611c",
    AUDIT_RESULT: "de8a709056403533aff30ea2b99daf65e361b7f765354ed9277a542e06c653e5",
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
        for z_row in finite.get("z_rows", []):
            yield from z_row.get("lanes", [])


def pairing_totals(rows, pairing):
    selected = [row for row in rows if row["pairing_index"] == pairing]
    return tuple(sum(row[key] for row in selected) for key in (
        "target_norm_root_count", "candidate_root_count",
        "source_point_count", "route_point_count", "z_candidate_count",
        "final_pair_solution_count",
    ))


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
        == "rate-half-kb-positive-433-1b-cell11-xi3-pairings1-2-adapter-v1"
        and payload["field"] == P
        and payload["source_template_sha256"] == digest(TEMPLATE)
        and payload["source_tower_sha256"] == digest(TOWER)
        and payload["source_kernel_sha256"] == digest(KERNEL),
        "packet custody",
    )
    signs = tuple(itertools.product((-1, 1), repeat=2))
    expected = {
        (*epsilon, branch, 0, 1)
        for epsilon in signs for branch in range(3)
    } | {
        (*epsilon, branch, sigma_c, 2)
        for epsilon in signs for branch in range(3) for sigma_c in (-1, 1)
    }
    seen = set()
    all_lanes = []
    for row in payload["rows"]:
        key = (*row["epsilon"], row["branch_index"],
               row["sigma_c_anchor"], row["pairing_index"])
        require(key in expected and key not in seen, "branch coverage")
        seen.add(key)
        require(row["status"] == "COMPLETE" and row["target_excluded"]
                and row["xi_index"] == 3 and row["pairing_index"] in (1, 2)
                and row["remainder_degree"] == 1
                and row["witness_count"] == 0 and not row["witnesses"]
                and row["final_pair_solution_count"] == 0
                and not row["final_pair_solutions"] and not row["unresolved"],
                "complete branch terminal")
        all_lanes.extend(lanes(row))
    require(seen == expected and len(payload["rows"]) == 36, "36-row cover")
    require(pairing_totals(payload["rows"], 1) == (72, 162, 176, 176, 16, 0)
            and pairing_totals(payload["rows"], 2)
            == (144, 324, 352, 352, 32, 0), "per-pairing census")
    lane_counts = collections.Counter(
        row["pairing_index"]
        for row in payload["rows"] for _ in lanes(row)
    )
    require(lane_counts == {1: 64, 2: 64}
            and len(all_lanes) == 128
            and all(item["status"] == "THIRD_PAIR_NONZERO"
                    and item["final_pair_cut"] % P for item in all_lanes),
            "128 final lanes")
    statuses = collections.Counter(
        (row["pairing_index"], item["status"])
        for row in payload["rows"] for item in row["finite_rows"]
    )
    boundaries = collections.Counter(
        (row["pairing_index"], item["stage"])
        for row in payload["rows"] for item in row["boundary_rows"]
    )
    no_lifts = collections.Counter(
        (row["pairing_index"], item["stage"])
        for row in payload["rows"] for item in row["no_lift_rows"]
    )
    require(statuses == {
        (1, "CHECKED"): 104, (1, "MISSING_IMPOSSIBLE"): 24,
        (1, "TARGET_PRODUCT_BOUNDARY"): 24, (1, "EMPTY_Q_BRANCH"): 24,
        (2, "CHECKED"): 208, (2, "MISSING_IMPOSSIBLE"): 48,
        (2, "TARGET_PRODUCT_BOUNDARY"): 48, (2, "EMPTY_Q_BRANCH"): 48,
    } and boundaries == {
        (1, "R_GUARD"): 60, (1, "T_GUARD"): 24,
        (1, "CELL11_B_LEADING"): 12, (1, "CELL11_C_LEADING"): 12,
        (2, "R_GUARD"): 120, (2, "T_GUARD"): 48,
        (2, "CELL11_B_LEADING"): 24, (2, "CELL11_C_LEADING"): 24,
    } and no_lifts == {
        (1, "NO_B_ROOT"): 74, (2, "NO_B_ROOT"): 148,
    }, "per-pairing terminal partition")

    roots = json.loads(ROOT_RESULT.read_text())
    require(
        roots["schema"]
        == "rate-half-kb-positive-433-1b-cell11-xi3-pairings1-2-independent-roots-v1"
        and roots["source_primary_sha256"] == digest(RESULT)
        and len(roots["rows"]) == 125
        and sum(len(row["roots"]) for row in roots["rows"]) == 610
        and max(row["degree"] for row in roots["rows"]) == 712,
        "independent root census",
    )
    audit = json.loads(AUDIT_RESULT.read_text())
    require(
        audit["schema"]
        == "rate-half-kb-positive-433-1b-cell11-xi3-pairings1-2-direct-audit-v1"
        and audit["status"] == "PASS" and audit["profiles"] == 125
        and audit["source_primary_sha256"] == digest(RESULT)
        and audit["source_roots_sha256"] == digest(ROOT_RESULT)
        and audit["source_template_sha256"] == digest(TEMPLATE)
        and audit["source_tower_sha256"] == digest(TOWER)
        and audit["source_kernel_sha256"] == digest(KERNEL),
        "direct replay custody",
    )
    common = {
        "final_pair_solution_count": 0,
    }
    expected_pairings = {
        "1": {
            "candidate_root_count": 162, "checked": 104,
            "common_z_roots": 16, "empty_q_branches": 24,
            "final_color_nonzero": 64, **common, "leading_boundaries": 24,
            "missing_impossible": 24, "no_lifts": 74, "product_boundaries": 24,
            "profile_visits": 192, "r_boundaries": 60,
            "route_point_count": 176, "rows": 12,
            "source_point_count": 176, "t_boundaries": 24,
            "target_boundaries": 24, "target_norm_root_count": 72,
            "z_candidate_count": 16, "z_lifts": 16,
        },
        "2": {
            "candidate_root_count": 324, "checked": 208,
            "common_z_roots": 32, "empty_q_branches": 48,
            "final_color_nonzero": 64, **common, "leading_boundaries": 48,
            "missing_impossible": 48, "no_lifts": 148, "product_boundaries": 48,
            "profile_visits": 384, "r_boundaries": 120,
            "route_point_count": 352, "rows": 24,
            "source_point_count": 352, "t_boundaries": 48,
            "target_boundaries": 48, "target_norm_root_count": 144,
            "z_candidate_count": 32, "z_lifts": 32,
        },
    }
    require(audit["pairing_totals"] == expected_pairings,
            "per-pairing direct replay")

    spec = importlib.util.spec_from_file_location("label_router", ROUTER)
    router = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(router)
    selected = [orbit for orbit in router.compile_orbits()
                if {(3, 1), (3, 2)} & set(orbit)]
    require(selected == [[(3, 1), (4, 1)], [(3, 2), (4, 2)]],
            "four-label orbit transport")
    manifest = json.loads((NODE / "node.json").read_text())["node"]
    require(manifest["id"] == NODE.name and manifest["status"] == "PROVED",
            "node manifest")
    print("PASS cell-11 xi3 pairings 1/2: rows=36 candidates=486 labels=4")


if __name__ == "__main__":
    main()
