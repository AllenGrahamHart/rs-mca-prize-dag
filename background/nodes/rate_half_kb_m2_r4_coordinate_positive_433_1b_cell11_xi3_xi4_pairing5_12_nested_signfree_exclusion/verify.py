#!/usr/bin/env python3
"""Verify the cell-11 xi3/xi4 pairing-5/12 exclusion packet."""

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
SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell11_xi3_pairing5_template_adapter_modal.py"
RESULT = EXP / "rate_half_kb_positive_433_1b_cell11_xi3_pairing5_template_adapter_result.json"
TEMPLATE = EXP / "rate_half_kb_positive_433_1b_cell4_xi3_pairing5_nested_signfree_modal.py"
TOWER = EXP / "rate_half_kb_positive_433_1b_cell11_four_basis_tower_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell11_compact_kernel_result.json"
ROOT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell11_xi3_pairings3_5_independent_roots_modal.py"
ROOT_RESULT = EXP / "rate_half_kb_positive_433_1b_cell11_xi3_pairings3_5_independent_roots_result.json"
AUDIT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell11_xi3_pairings3_5_direct_audit_modal.py"
AUDIT_RESULT = EXP / "rate_half_kb_positive_433_1b_cell11_xi3_pairings3_5_direct_audit_result.json"
ROUTER = EXP / "rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
PINNED = {
    SCRIPT: "6099b10f1dc70fb177dae3902b18cc50e1c4f8a2a73990f12fab52a083710016",
    RESULT: "4b82b4a69068972487bd9065e6bdd2b5989094b2229e7165f1f623173de73c71",
    TEMPLATE: "f1dd2096b7dfb7cf6a4a784ae04ef5a0fbd8b6e91f5bfa21bd584d990625f342",
    TOWER: "8be5facf7fe8e05f9a68fd740964b669e7a47ef2279efbcba504279860717e6a",
    KERNEL: "2ef59a5dd9e656f36fccc63f3c75aaee6889664312928ffe25d0d0816ed16236",
    ROOT_SCRIPT: "a38f3d55d4ede520ade1bf0f1a61ccc29870a3db10f369c9141d946b4ce5760a",
    ROOT_RESULT: "c8a7b8218c5a06793cabb0da9226bb7f2c1ed8544fce73a178eeb3a85cf7f53c",
    AUDIT_SCRIPT: "e6b4e2b087bdebaa62a96d2d6e4a59542a6297aba536ec8cc85a4b7ca947e5ff",
    AUDIT_RESULT: "3c7f900f90da88500bb516b42158306a3642a88bbd0c6b3d79a20252554183a9",
    ROUTER: "82df776b06b375e9bee6fcc77aead1ebca4594028fa2e51df6318422a9d2f9bb",
}
PRIMARY_DIGESTS = {
    "3": "d5f1909d5635efe83299ab48759fd212500888817e9b0aad8abcc21a7cd1eb74",
    "4": "0d54dc3a2ae985f4e24ebb87d917f7794a7ef6a2064352d8605477e6b2715e44",
    "5": "4b82b4a69068972487bd9065e6bdd2b5989094b2229e7165f1f623173de73c71"
}
TEMPLATE_DIGESTS = {
    "3": "ed1133214b5126f59279ccc75b91f4a572ef9cb62d6b24d8c84df8377da4ce5c",
    "4": "0992beedc8d85e1d7e510d40dadccd72d01e8b38325d9e6fe56c741ab50711fd",
    "5": "f1dd2096b7dfb7cf6a4a784ae04ef5a0fbd8b6e91f5bfa21bd584d990625f342"
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
            for q_row in z_row.get("q_rows", []):
                yield from q_row.get("lanes", [])


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
        == "rate-half-kb-positive-433-1b-cell11-xi3-pairing5-adapter-v1"
        and payload["field"] == P
        and payload["source_template_sha256"] == digest(TEMPLATE)
        and payload["source_tower_sha256"] == digest(TOWER)
        and payload["source_kernel_sha256"] == digest(KERNEL),
        "primary packet custody",
    )
    signs = tuple(itertools.product((-1, 1), repeat=2))
    expected = {(epsilon, sigma) for epsilon in signs for sigma in (-1, 1)}
    seen = {(tuple(row["epsilon"]), row["sigma_c"]) for row in payload["rows"]}
    require(seen == expected and len(payload["rows"]) == 8,
            "exact row cover")
    for row in payload["rows"]:
        require(
            row["status"] == "COMPLETE" and row["target_excluded"]
            and row["xi_index"] == 3 and row["pairing_index"] == 5
            and row["remainder_degree"] == 1
            and row["witness_count"] == 0 and not row["witnesses"]
            and row["final_pair_solution_count"] == 0
            and not row["final_pair_solutions"] and not row["unresolved"],
            "complete row terminal",
        )
    totals = tuple(sum(row[key] for row in payload["rows"]) for key in (
        "target_norm_root_count", "candidate_root_count",
        "source_point_count", "route_point_count", "z_candidate_count",
        "q_candidate_count", "final_pair_solution_count",
    ))
    require(totals == (56, 140, 240, 240, 16, 16, 0),
            "primary census")
    statuses = collections.Counter(
        item["status"] for row in payload["rows"]
        for item in row["finite_rows"]
    )
    boundaries = collections.Counter(
        item["stage"] for row in payload["rows"]
        for item in row["boundary_rows"]
    )
    no_lifts = collections.Counter(
        item["stage"] for row in payload["rows"]
        for item in row["no_lift_rows"]
    )
    require(statuses == {
    "CHECKED": 208,
    "MISSING_IMPOSSIBLE": 16,
    "TARGET_PRODUCT_BOUNDARY": 16
}
            and boundaries == {
    "R_GUARD": 40,
    "T_GUARD": 16,
    "CELL11_B_LEADING": 8,
    "CELL11_C_LEADING": 8
}
            and no_lifts == {"NO_B_ROOT": 52}
            and sum(len(row["target_boundary_rows"])
                    for row in payload["rows"]) == 16,
            "terminal partition")
    all_lanes = [lane for row in payload["rows"] for lane in lanes(row)]
    require(len(all_lanes) == 32
            and all(lane["status"] == "THIRD_PAIR_NONZERO"
                    and lane["final_pair_cut"] % P for lane in all_lanes),
            "final colored lanes")

    roots = json.loads(ROOT_RESULT.read_text())
    require(
        roots["schema"]
        == "rate-half-kb-positive-433-1b-cell11-xi3-pairings3-5-independent-roots-v1"
        and roots["source_primary_sha256"] == PRIMARY_DIGESTS
        and roots["source_primary_sha256"][str(5)] == digest(RESULT)
        and len(roots["rows"]) == 73
        and sum(len(row["roots"]) for row in roots["rows"]) == 370
        and max(row["degree"] for row in roots["rows"]) == 6510,
        "independent root census",
    )
    audit = json.loads(AUDIT_RESULT.read_text())
    require(
        audit["schema"]
        == "rate-half-kb-positive-433-1b-cell11-xi3-pairings3-5-direct-audit-v1"
        and audit["status"] == "PASS" and audit["profiles"] == 73
        and audit["rows"] == 20
        and audit["source_primary_sha256"] == PRIMARY_DIGESTS
        and audit["source_primary_sha256"][str(5)] == digest(RESULT)
        and audit["source_roots_sha256"] == digest(ROOT_RESULT)
        and audit["source_template_sha256"] == TEMPLATE_DIGESTS
        and audit["source_template_sha256"][str(5)] == digest(TEMPLATE)
        and audit["source_tower_sha256"] == digest(TOWER)
        and audit["source_kernel_sha256"] == digest(KERNEL)
        and audit["pairing_totals"][str(5)] == {
    "candidate_root_count": 140,
    "checked": 208,
    "common_q_roots": 16,
    "common_z_roots": 0,
    "final_color_nonzero": 32,
    "final_pair_solution_count": 0,
    "leading_boundaries": 16,
    "missing_impossible": 16,
    "no_lifts": 52,
    "product_boundaries": 16,
    "profile_visits": 128,
    "q_candidate_count": 16,
    "q_intersections": 448,
    "q_lifts": 16,
    "r_boundaries": 40,
    "route_point_count": 240,
    "rows": 8,
    "source_point_count": 240,
    "t_boundaries": 16,
    "target_boundaries": 16,
    "target_norm_root_count": 56,
    "z_candidate_count": 16,
    "z_roots": 448
},
        "pairing-specific direct replay",
    )

    spec = importlib.util.spec_from_file_location("label_router", ROUTER)
    router = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(router)
    selected = [orbit for orbit in router.compile_orbits()
                if (3, 5) in orbit]
    require(selected == [[(3, 5), (3, 12), (4, 5), (4, 12)]],
            "four-label orbit transport")
    manifest = json.loads((NODE / "node.json").read_text())["node"]
    require(manifest["id"] == NODE.name and manifest["status"] == "PROVED",
            "node manifest")
    print("PASS cell-11 xi3/xi4 pairing 5/12: "
          "rows=8 candidates=140 labels=4")


if __name__ == "__main__":
    main()
