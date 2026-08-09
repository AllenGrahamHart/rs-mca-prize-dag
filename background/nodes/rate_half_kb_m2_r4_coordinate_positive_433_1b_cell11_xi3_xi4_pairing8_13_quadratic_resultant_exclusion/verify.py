#!/usr/bin/env python3
"""Verify the cell-11 xi3/xi4 pairing-8/13 quadratic-resultant packet."""

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
SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell11_xi3_pairing8_template_adapter_modal.py"
RESULT = EXP / "rate_half_kb_positive_433_1b_cell11_xi3_pairing8_template_adapter_result.json"
TEMPLATE = EXP / "rate_half_kb_positive_433_1b_cell4_xi3_pairing8_quadratic_resultant_signfree_modal.py"
TOWER = EXP / "rate_half_kb_positive_433_1b_cell11_four_basis_tower_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell11_compact_kernel_result.json"
ROOT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell11_xi3_pairings7_8_11_independent_roots_modal.py"
ROOT_RESULT = EXP / "rate_half_kb_positive_433_1b_cell11_xi3_pairings7_8_11_independent_roots_result.json"
ROUTER = EXP / "rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
PINNED = {
    SCRIPT: "20f2a73552d10d9399d652639d8b75d24208595749de64353c31ed9743b508bc",
    RESULT: "2737ad15bea84898358cae29a777bf49416f53348b91f5c34c52cfbf2c186d4e",
    TEMPLATE: "58ed9e191436e0a629d2c7a263151d50d54910d226eee4c35c0bb55abf2a1b8b",
    TOWER: "8be5facf7fe8e05f9a68fd740964b669e7a47ef2279efbcba504279860717e6a",
    KERNEL: "2ef59a5dd9e656f36fccc63f3c75aaee6889664312928ffe25d0d0816ed16236",
    ROOT_SCRIPT: "2fedad39cf4ea45dfb5cdf41e4bf37a49a8f1c610f58e59194d1fd998a1a4cc8",
    ROOT_RESULT: "75d654ccdbbd5febf6fff48a273cfeb4c3d013bb39179c8d47d2e08306612656",
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
            for q_row in z_row.get("q_rows", []):
                yield from q_row.get("lanes", [])


def main():
    for path, expected_digest in PINNED.items():
        require(digest(path) == expected_digest, f"hash drift: {path.name}")
    source = SCRIPT.read_text()
    ast.parse(source)
    require(
        "function.decorator_list = []" in source
        and 'node.name == "evaluate_case"' in source
        and 'compile(module, REMOTE_TEMPLATE, "exec")' in source,
        "AST adapter boundary",
    )
    payload = json.loads(RESULT.read_text())
    require(
        payload["schema"]
        == "rate-half-kb-positive-433-1b-cell11-xi3-pairing8-adapter-v1"
        and payload["field"] == P
        and payload["source_template_sha256"] == digest(TEMPLATE)
        and payload["source_tower_sha256"] == digest(TOWER)
        and payload["source_kernel_sha256"] == digest(KERNEL),
        "primary packet custody",
    )
    expected = set(itertools.product(
        itertools.product((-1, 1), repeat=2), (-1, 1)
    ))
    seen = set()
    all_lanes = []
    row_censuses = {
        (-1, -1): (15, 20, 32, 16),
        (-1, 1): (7, 12, 4, 0),
        (1, -1): (15, 19, 32, 16),
        (1, 1): (7, 11, 4, 0),
    }
    for row in payload["rows"]:
        key = (tuple(row["epsilon"]), row["sigma_c"])
        require(key in expected and key not in seen, "source-sign coverage")
        seen.add(key)
        census = (
            row["target_norm_root_count"], row["candidate_root_count"],
            row["source_point_count"], row["q_candidate_count"],
        )
        require(
            row["status"] == "COMPLETE" and row["target_excluded"]
            and row["xi_index"] == 3 and row["pairing_index"] == 8
            and row["remainder_degree"] == 1
            and row["witness_count"] == 0 and not row["witnesses"]
            and census == row_censuses[(row["epsilon"][1], row["sigma_c"])]
            and row["route_point_count"] == row["source_point_count"]
            and row["z_candidate_count"] == row["q_candidate_count"]
            and row["final_pair_solution_count"] == 0
            and not row["final_pair_solutions"] and not row["unresolved"],
            "complete row terminal",
        )
        all_lanes.extend(lanes(row))
    require(seen == expected and len(payload["rows"]) == 8,
            "eight-row cover")
    totals = tuple(sum(row[key] for row in payload["rows"]) for key in (
        "target_norm_root_count", "candidate_root_count",
        "source_point_count", "route_point_count", "z_candidate_count",
        "q_candidate_count", "final_pair_solution_count",
    ))
    require(totals == (88, 124, 144, 144, 64, 64, 0),
            "exact census totals")
    require(
        len(all_lanes) == 128
        and all(lane["status"] == "THIRD_PAIR_NONZERO"
                and lane["final_pair_cut"] % P for lane in all_lanes),
        "final colored lanes",
    )
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
    require(
        statuses == {
    "CHECKED": 112,
    "MISSING_IMPOSSIBLE": 16,
    "TARGET_PRODUCT_BOUNDARY": 16
}
        and boundaries == {
            "R_GUARD": 40,
            "T_GUARD": 16,
            "CELL11_B_LEADING": 8,
            "CELL11_C_LEADING": 8,
        }
        and no_lifts == {"NO_B_ROOT": 68}
        and sum(len(row["target_boundary_rows"])
                for row in payload["rows"]) == 16,
        "terminal partition",
    )

    roots = json.loads(ROOT_RESULT.read_text())
    require(
        roots["schema"]
        == "rate-half-kb-positive-433-1b-cell11-xi3-pairings7-8-11-independent-roots-v1"
        and roots["field"] == P
        and roots["source_primary_sha256"]["8"] == digest(RESULT)
        and len(roots["rows"]) == 61
        and sum(len(row["roots"]) for row in roots["rows"]) == 302
        and max(row["degree"] for row in roots["rows"]) == 5192,
        "independent root census",
    )

    spec = importlib.util.spec_from_file_location("label_router", ROUTER)
    router = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(router)
    selected = [orbit for orbit in router.compile_orbits()
                if (3, 8) in orbit]
    require(selected == [[(3, 8), (3, 13), (4, 8), (4, 13)]],
            "four-label orbit transport")
    manifest = json.loads((NODE / "node.json").read_text())["node"]
    require(manifest["id"] == NODE.name and manifest["status"] == "PROVED",
            "node manifest")
    print("PASS cell-11 xi3/xi4 pairing 8/13: "
          "rows=8 candidates=124 lanes=128 labels=4")


if __name__ == "__main__":
    main()
