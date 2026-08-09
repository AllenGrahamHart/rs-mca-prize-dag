#!/usr/bin/env python3
"""Verify the cell-5 xi3/xi4 pairing-5/12 exclusion packet."""

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
SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell5_xi3_pairing5_template_adapter_modal.py"
RESULT = EXP / "rate_half_kb_positive_433_1b_cell5_xi3_pairing5_template_adapter_result.json"
TEMPLATE = EXP / "rate_half_kb_positive_433_1b_cell4_xi3_pairing5_nested_signfree_modal.py"
TOWER = EXP / "rate_half_kb_positive_433_1b_cell5_four_basis_tower_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell5_compact_kernel_result.json"
ROOT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell5_xi3_pairings3_5_independent_roots_modal.py"
ROOT_RESULT = EXP / "rate_half_kb_positive_433_1b_cell5_xi3_pairings3_5_independent_roots_result.json"
AUDIT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell5_xi3_pairings3_5_direct_audit_modal.py"
AUDIT_RESULT = EXP / "rate_half_kb_positive_433_1b_cell5_xi3_pairings3_5_direct_audit_result.json"
ROUTER = EXP / "rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
PINNED = {
    SCRIPT: "43af240fe9fbb6b45a8536e84ebfd5ad447e28342d4c1ae9f287c6c59eb4862d",
    RESULT: "f2d421e6fa4b4111a45bc83375555a48cac8d82706b6611130ff726562093e12",
    TEMPLATE: "f1dd2096b7dfb7cf6a4a784ae04ef5a0fbd8b6e91f5bfa21bd584d990625f342",
    TOWER: "68c18173d4133f66a85136b1ecc33235f7e979c26b6f96d8592030901a8a335c",
    KERNEL: "627a8df8bb8a2da4e11488658d1c2145b8c65ef7fbcef3f0f4f53f9d05ea752d",
    ROOT_SCRIPT: "fd961b7740eb6993406e6a87652785987a87a99f493f57fd9d319d0877e6c52b",
    ROOT_RESULT: "c4e2d14ca8bec16eaed65c40191fc70a1844bf086754c8a124118fa6b9f2f0c3",
    AUDIT_SCRIPT: "f27f4078989f5565c55eaba4780bb4dacde6875fdb3bb844aa833f5a20079de4",
    AUDIT_RESULT: "9f5d1df26b08747ff134d2067021dfaf311625feed7ff4bf929ff863834f19f6",
    ROUTER: "82df776b06b375e9bee6fcc77aead1ebca4594028fa2e51df6318422a9d2f9bb",
}
PRIMARY_DIGESTS = {
    "3": "ac8903117be3e63fb5ddcec99a45dafe7b222b78cc65f41610cd3bba67ed771b",
    "4": "84834df5692e9c51f7ffa3939e4c22fdd58e6b691a875bde5962ccbeabc8181a",
    "5": "f2d421e6fa4b4111a45bc83375555a48cac8d82706b6611130ff726562093e12"
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
        == "rate-half-kb-positive-433-1b-cell5-xi3-pairing5-adapter-v1"
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
    require(totals == (48, 128, 208, 208, 0, 0, 0),
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
    "CHECKED": 176,
    "MISSING_IMPOSSIBLE": 16,
    "TARGET_PRODUCT_BOUNDARY": 16
}
            and boundaries == {
    "R_GUARD": 40,
    "T_GUARD": 32
}
            and no_lifts == {"NO_B_ROOT": 40}
            and sum(len(row["target_boundary_rows"])
                    for row in payload["rows"]) == 16,
            "terminal partition")
    all_lanes = [lane for row in payload["rows"] for lane in lanes(row)]
    require(len(all_lanes) == 0
            and all(lane["status"] == "THIRD_PAIR_NONZERO"
                    and lane["final_pair_cut"] % P for lane in all_lanes),
            "final colored lanes")

    roots = json.loads(ROOT_RESULT.read_text())
    require(
        roots["schema"]
        == "rate-half-kb-positive-433-1b-cell5-xi3-pairings3-5-independent-roots-v1"
        and roots["source_primary_sha256"] == PRIMARY_DIGESTS
        and roots["source_primary_sha256"][str(5)] == digest(RESULT)
        and len(roots["rows"]) == 69
        and sum(len(row["roots"]) for row in roots["rows"]) == 332
        and max(row["degree"] for row in roots["rows"]) == 4560,
        "independent root census",
    )
    audit = json.loads(AUDIT_RESULT.read_text())
    require(
        audit["schema"]
        == "rate-half-kb-positive-433-1b-cell5-xi3-pairings3-5-direct-audit-v1"
        and audit["status"] == "PASS" and audit["profiles"] == 69
        and audit["rows"] == 20
        and audit["source_primary_sha256"] == PRIMARY_DIGESTS
        and audit["source_primary_sha256"][str(5)] == digest(RESULT)
        and audit["source_roots_sha256"] == digest(ROOT_RESULT)
        and audit["source_template_sha256"] == TEMPLATE_DIGESTS
        and audit["source_template_sha256"][str(5)] == digest(TEMPLATE)
        and audit["source_tower_sha256"] == digest(TOWER)
        and audit["source_kernel_sha256"] == digest(KERNEL)
        and audit["pairing_totals"][str(5)] == {
    "candidate_root_count": 128,
    "checked": 176,
    "common_q_roots": 0,
    "common_z_roots": 0,
    "final_color_nonzero": 0,
    "final_pair_solution_count": 0,
    "missing_impossible": 16,
    "no_lifts": 40,
    "product_boundaries": 16,
    "profile_visits": 128,
    "q_candidate_count": 0,
    "q_intersections": 320,
    "q_lifts": 0,
    "r_boundaries": 40,
    "route_point_count": 208,
    "rows": 8,
    "source_point_count": 208,
    "t_boundaries": 32,
    "target_boundaries": 16,
    "target_norm_root_count": 48,
    "z_candidate_count": 0,
    "z_roots": 320
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
    print("PASS cell-5 xi3/xi4 pairing 5/12: "
          "rows=8 candidates=128 labels=4")


if __name__ == "__main__":
    main()
