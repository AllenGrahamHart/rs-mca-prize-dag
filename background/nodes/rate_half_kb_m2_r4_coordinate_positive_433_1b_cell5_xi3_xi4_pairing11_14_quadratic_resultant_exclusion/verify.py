#!/usr/bin/env python3
"""Verify the cell-5 xi3/xi4 pairing-11/14 quadratic-resultant packet."""

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
SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell5_xi3_pairing11_template_adapter_modal.py"
RESULT = EXP / "rate_half_kb_positive_433_1b_cell5_xi3_pairing11_template_adapter_result.json"
TEMPLATE = EXP / "rate_half_kb_positive_433_1b_cell4_xi3_pairing11_quadratic_resultant_signfree_modal.py"
TOWER = EXP / "rate_half_kb_positive_433_1b_cell5_four_basis_tower_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell5_compact_kernel_result.json"
ROOT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell5_xi3_pairing11_independent_roots_modal.py"
ROOT_RESULT = EXP / "rate_half_kb_positive_433_1b_cell5_xi3_pairing11_independent_roots_result.json"
ROUTER = EXP / "rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
PINNED = {
    SCRIPT: "68067987abd18a78440b8aae0361d002b79e35190b53088330695c93a5a2bade",
    RESULT: "fb6261257eed36849179d0ca4f0c2dd1b4504c64a425716428dac5ea605de0d4",
    TEMPLATE: "8f2fe8ca53863b2220ae60558b3f8d64269eec0f3952138679f2bc3a7069698b",
    TOWER: "68c18173d4133f66a85136b1ecc33235f7e979c26b6f96d8592030901a8a335c",
    KERNEL: "627a8df8bb8a2da4e11488658d1c2145b8c65ef7fbcef3f0f4f53f9d05ea752d",
    ROOT_SCRIPT: "cb0ac6ebdf651388e42e92c10d2c5720587a80f49b1b13280bdca0ea7be3fd10",
    ROOT_RESULT: "87ca88f19a75e66e152a1ff9d43500e499c332ca42b03c05db19db424141413b",
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
        == "rate-half-kb-positive-433-1b-cell5-xi3-pairing11-adapter-v1"
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
        -1: (8,15,16,4),
        1: (5,12,14,2),
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
            and row["xi_index"] == 3 and row["pairing_index"] == 11
            and row["remainder_degree"] == 1
            and row["witness_count"] == 0 and not row["witnesses"]
            and census == row_censuses[row["sigma_c"]]
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
    require(totals == (52, 108, 120, 120, 24, 24, 0), "exact census totals")
    require(
        len(all_lanes) == 48
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
    "CHECKED": 88,
    "MISSING_IMPOSSIBLE": 16,
    "TARGET_PRODUCT_BOUNDARY": 16
}
        and boundaries == {"R_GUARD": 40, "T_GUARD": 32}
        and no_lifts == {"NO_B_ROOT": 44}
        and sum(len(row["target_boundary_rows"])
                for row in payload["rows"]) == 16,
        "terminal partition",
    )

    roots = json.loads(ROOT_RESULT.read_text())
    require(
        roots["schema"]
        == "rate-half-kb-positive-433-1b-cell5-xi3-pairing11-independent-roots-v1"
        and roots["field"] == P
        and roots["source_primary_sha256"] == digest(RESULT)
        and len(roots["rows"]) == 45
        and sum(len(row["roots"]) for row in roots["rows"]) == 172
        and max(row["degree"] for row in roots["rows"]) == 3432,
        "independent root census",
    )

    spec = importlib.util.spec_from_file_location("label_router", ROUTER)
    router = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(router)
    selected = [orbit for orbit in router.compile_orbits()
                if (3, 11) in orbit]
    require(selected == [[(3, 11), (3, 14), (4, 11), (4, 14)]],
            "four-label orbit transport")
    manifest = json.loads((NODE / "node.json").read_text())["node"]
    require(manifest["id"] == NODE.name and manifest["status"] == "PROVED",
            "node manifest")
    print("PASS cell-5 xi3/xi4 pairing 11/14: "
          "rows=8 candidates=108 lanes=48 labels=4")


if __name__ == "__main__":
    main()
