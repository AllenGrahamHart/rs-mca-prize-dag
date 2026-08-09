#!/usr/bin/env python3
"""Verify the cell-5 positive-DE pairing-14 packet."""

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
SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell5_positive_de_pairing14_template_adapter_modal.py"
RESULT = EXP / "rate_half_kb_positive_433_1b_cell5_positive_de_pairing14_template_adapter_result.json"
TEMPLATE = EXP / "rate_half_kb_positive_433_1b_cell4_positive_de_pairing14_common_f_resultant_modal.py"
TOWER = EXP / "rate_half_kb_positive_433_1b_cell5_four_basis_tower_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell5_compact_kernel_result.json"
ROOT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell5_positive_de_pairing14_frobenius_roots_modal.py"
ROOT_RESULT = EXP / "rate_half_kb_positive_433_1b_cell5_positive_de_pairing14_frobenius_roots_result.json"
AUDITOR = EXP / "rate_half_kb_positive_433_1b_cell5_positive_de_pairing14_common_f_audit.py"
AUDIT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell5_positive_de_pairing14_direct_audit_modal.py"
AUDIT_RESULT = EXP / "rate_half_kb_positive_433_1b_cell5_positive_de_pairing14_direct_audit_result.json"
ROUTER = EXP / "rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
PINNED = {
    SCRIPT: "2502ae191c14ee6e635a2455c076c0cf5671c3b93dab063d428988467f180f78",
    RESULT: "0bba2a8ec0b3a2aaca1b7cd07eeb81bc57c2f5498e6a5a8bac1c32d1e622b66c",
    TEMPLATE: "d46de7b84de40e9be7902d9c26e51df8b2e9fd99e7d208e78fc110338feb406a",
    TOWER: "68c18173d4133f66a85136b1ecc33235f7e979c26b6f96d8592030901a8a335c",
    KERNEL: "627a8df8bb8a2da4e11488658d1c2145b8c65ef7fbcef3f0f4f53f9d05ea752d",
    ROOT_SCRIPT: "7c63ee2bba7c7e84b5ec2e06fba0a2332ac552becef3bf171b6c4439a16894d7",
    ROOT_RESULT: "58674cf6db3c3c70bc99cbf22e3dfa98abe6f8065411b82b3351a86ef20c83ca",
    AUDITOR: "6605096118d3fb32c62cef8be973259cf146b36831fd2745e60a8afc16b87d1b",
    AUDIT_SCRIPT: "69f37a04c32d95f7e6bd49083453a75cd25953bd82ad5fd1a2f1e78e252baab0",
    AUDIT_RESULT: "d42a4ac17ee63afd5b3e2cf68f32e550e760e7858cc10c455a01b092ef5b30e3",
    ROUTER: "82df776b06b375e9bee6fcc77aead1ebca4594028fa2e51df6318422a9d2f9bb",
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
        == "rate-half-kb-positive-433-1b-cell5-positive-de-pairing14-adapter-v1"
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
    require(totals == (96, 208, 240, 240, 192, 0), "exact totals")
    finite = collections.Counter(
        item["status"] for row in payload["rows"] for item in row["finite_rows"]
    )
    boundary = collections.Counter(
        item["stage"] for row in payload["rows"] for item in row["boundary_rows"]
    )
    endings = collections.Counter(
        item["status"] for row in payload["rows"]
        for finite_row in row["finite_rows"]
        for item in finite_row.get("uf_rows", [])
    )
    require(finite == {"CHECKED": 176, "MISSING_IMPOSSIBLE": 32,
                       "TARGET_PRODUCT_BOUNDARY": 32}
            and boundary == {"R_GUARD": 80, "T_GUARD": 64}
            and endings == {"COLORED_PAIR_NONZERO": 192},
            "terminal partition")

    roots = json.loads(ROOT_RESULT.read_text())
    require(roots["schema"]
            == "rate-half-kb-positive-433-1b-cell5-positive-de-pairing14-frobenius-roots-v1"
            and roots["source_primary_sha256"] == digest(RESULT)
            and len(roots["rows"]) == 37
            and sum(len(row["roots"]) for row in roots["rows"]) == 136
            and max(row["degree"] for row in roots["rows"]) == 984,
            "external root census")
    audit = json.loads(AUDIT_RESULT.read_text())
    require(audit["schema"]
            == "rate-half-kb-positive-433-1b-cell5-positive-de-pairing14-direct-audit-v1"
            and audit["source_sha256"] == {
                "auditor": digest(AUDITOR), "primary": digest(RESULT),
                "roots": digest(ROOT_RESULT), "tower": digest(TOWER),
                "kernel": digest(KERNEL),
            }, "audit custody")
    require(audit["summary"] == {
        "candidate_root_count": 208, "checked": 176,
        "colored_nonzero": 192, "colored_solution_count": 0,
        "combined_profiles": 37, "leading_boundaries": 0,
        "missing_impossible": 32, "product_boundaries": 32,
        "profile_visits": 160, "route_point_count": 240, "rows": 16,
        "source_point_count": 240, "target_boundaries": 32,
        "target_root_count": 96, "uf_candidate_count": 192,
    }, "direct audit summary")

    spec = importlib.util.spec_from_file_location("label_router", ROUTER)
    router = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(router)
    selected = [orbit for orbit in router.compile_orbits() if (0, 14) in orbit]
    require(selected == [[(0, 14), (1, 14)]], "two-label orbit transport")
    manifest = json.loads((NODE / "node.json").read_text())["node"]
    require(manifest["id"] == NODE.name and manifest["status"] == "PROVED",
            "node manifest")
    print("PASS cell-5 positive-DE pairing 14: rows=16 candidates=208 labels=2")


if __name__ == "__main__":
    main()
