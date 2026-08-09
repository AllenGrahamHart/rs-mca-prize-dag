#!/usr/bin/env python3
"""Verify the cell-5 xi=3 pairings-1/2 reciprocal-linear packet."""

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
SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell5_xi3_pairings1_2_template_adapter_modal.py"
RESULT = EXP / "rate_half_kb_positive_433_1b_cell5_xi3_pairings1_2_template_adapter_result.json"
TEMPLATE = EXP / "rate_half_kb_positive_433_1b_cell4_xi3_pairings1_2_reciprocal_linear_modal.py"
TOWER = EXP / "rate_half_kb_positive_433_1b_cell5_four_basis_tower_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell5_compact_kernel_result.json"
ROOT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell5_xi3_pairings1_2_independent_roots_modal.py"
ROOT_RESULT = EXP / "rate_half_kb_positive_433_1b_cell5_xi3_pairings1_2_independent_roots_result.json"
AUDIT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell5_xi3_pairings1_2_direct_audit_modal.py"
AUDIT_RESULT = EXP / "rate_half_kb_positive_433_1b_cell5_xi3_pairings1_2_direct_audit_result.json"
ROUTER = EXP / "rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
PINNED = {
    SCRIPT: "70db812e881b14498735434e053dcc53fe6839899709f4ab60397d20ce749d18",
    RESULT: "b41b88eec0f8a7850e0a38c752598131741cb8b74f74311687daade8373fae67",
    TEMPLATE: "6175e9472f571b752273395050247db907e9bbb68065c7c0c8bdd0933e4ac2aa",
    TOWER: "68c18173d4133f66a85136b1ecc33235f7e979c26b6f96d8592030901a8a335c",
    KERNEL: "627a8df8bb8a2da4e11488658d1c2145b8c65ef7fbcef3f0f4f53f9d05ea752d",
    ROOT_SCRIPT: "848f85ee928109a29c06388371f7c53d2944800403f632a54cbb2e58676d04a8",
    ROOT_RESULT: "09aa13d48cbcd73a22edf2c5dd97474a001a7cfe9d2628eb4363a5204f0d67a0",
    AUDIT_SCRIPT: "6dd50238bd74a1923150d9563625c2a0a1903ed42c7c3c0ac1f04871e3789504",
    AUDIT_RESULT: "3ae08d4bae1ef7dd4e209b7e6eaeec8f2c0b92d0786c55676f6b0ba9311af7a3",
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
        == "rate-half-kb-positive-433-1b-cell5-xi3-pairings1-2-adapter-v1"
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
    require(pairing_totals(payload["rows"], 1) == (76, 180, 280, 280, 48, 0)
            and pairing_totals(payload["rows"], 2)
            == (112, 320, 432, 432, 16, 0), "per-pairing census")
    lane_counts = collections.Counter(
        row["pairing_index"]
        for row in payload["rows"] for _ in lanes(row)
    )
    require(lane_counts == {1: 192, 2: 32}
            and len(all_lanes) == 224
            and all(item["status"] == "THIRD_PAIR_NONZERO"
                    and item["final_pair_cut"] % P for item in all_lanes),
            "224 final lanes")
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
        (1, "CHECKED"): 220, (1, "MISSING_IMPOSSIBLE"): 24,
        (1, "TARGET_PRODUCT_BOUNDARY"): 24, (1, "EMPTY_Q_BRANCH"): 12,
        (2, "CHECKED"): 312, (2, "MISSING_IMPOSSIBLE"): 48,
        (2, "TARGET_PRODUCT_BOUNDARY"): 48, (2, "EMPTY_Q_BRANCH"): 24,
    } and boundaries == {
        (1, "R_GUARD"): 60, (1, "T_GUARD"): 48,
        (2, "R_GUARD"): 120, (2, "T_GUARD"): 96,
    } and no_lifts == {
        (1, "NO_B_ROOT"): 52, (2, "NO_B_ROOT"): 88,
    }, "per-pairing terminal partition")

    roots = json.loads(ROOT_RESULT.read_text())
    require(
        roots["schema"]
        == "rate-half-kb-positive-433-1b-cell5-xi3-pairings1-2-independent-roots-v1"
        and roots["source_primary_sha256"] == digest(RESULT)
        and len(roots["rows"]) == 129
        and sum(len(row["roots"]) for row in roots["rows"]) == 596
        and max(row["degree"] for row in roots["rows"]) == 508,
        "independent root census",
    )
    audit = json.loads(AUDIT_RESULT.read_text())
    require(
        audit["schema"]
        == "rate-half-kb-positive-433-1b-cell5-xi3-pairings1-2-direct-audit-v1"
        and audit["status"] == "PASS" and audit["profiles"] == 129
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
            "candidate_root_count": 180, "checked": 220,
            "common_z_roots": 48, "empty_q_branches": 12,
            "final_color_nonzero": 192, **common, "missing_impossible": 24,
            "no_lifts": 52, "product_boundaries": 24,
            "profile_visits": 192, "r_boundaries": 60,
            "route_point_count": 280, "rows": 12,
            "source_point_count": 280, "t_boundaries": 48,
            "target_boundaries": 24, "target_norm_root_count": 76,
            "z_candidate_count": 48, "z_lifts": 48,
        },
        "2": {
            "candidate_root_count": 320, "checked": 312,
            "common_z_roots": 16, "empty_q_branches": 24,
            "final_color_nonzero": 32, **common, "missing_impossible": 48,
            "no_lifts": 88, "product_boundaries": 48,
            "profile_visits": 384, "r_boundaries": 120,
            "route_point_count": 432, "rows": 24,
            "source_point_count": 432, "t_boundaries": 96,
            "target_boundaries": 48, "target_norm_root_count": 112,
            "z_candidate_count": 16, "z_lifts": 16,
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
    print("PASS cell-5 xi3 pairings 1/2: rows=36 candidates=500 labels=4")


if __name__ == "__main__":
    main()
