#!/usr/bin/env python3
"""Verify the cell-11 positive-DE pairing-14 packet."""

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
SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell11_positive_de_pairing14_template_adapter_modal.py"
RESULT = EXP / "rate_half_kb_positive_433_1b_cell11_positive_de_pairing14_template_adapter_result.json"
TEMPLATE = EXP / "rate_half_kb_positive_433_1b_cell4_positive_de_pairing14_common_f_resultant_modal.py"
TOWER = EXP / "rate_half_kb_positive_433_1b_cell11_four_basis_tower_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell11_compact_kernel_result.json"
ROOT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell11_positive_de_pairing14_frobenius_roots_modal.py"
ROOT_RESULT = EXP / "rate_half_kb_positive_433_1b_cell11_positive_de_pairing14_frobenius_roots_result.json"
AUDITOR = EXP / "rate_half_kb_positive_433_1b_cell11_positive_de_pairing14_common_f_audit.py"
AUDIT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell11_positive_de_pairing14_direct_audit_modal.py"
AUDIT_RESULT = EXP / "rate_half_kb_positive_433_1b_cell11_positive_de_pairing14_direct_audit_result.json"
ROUTER = EXP / "rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
PINNED = {
    SCRIPT: "4724540ee37409337b17d2ab18d93a5a6ee7ef8a56fb3847b9a281a195b7bd5f",
    RESULT: "daecccf91b43e41fe9628230ae0cfd62865c49297db47225042fa1b43d1ba6db",
    TEMPLATE: "d46de7b84de40e9be7902d9c26e51df8b2e9fd99e7d208e78fc110338feb406a",
    TOWER: "8be5facf7fe8e05f9a68fd740964b669e7a47ef2279efbcba504279860717e6a",
    KERNEL: "2ef59a5dd9e656f36fccc63f3c75aaee6889664312928ffe25d0d0816ed16236",
    ROOT_SCRIPT: "32ba180b7f67f21ecb5ec0182636f0f95c4cf3e04435cc872ba675342dcc8d17",
    ROOT_RESULT: "b3d572f9cd8a2877fb08f0b673a78a7731281d742fe470397fa237b580f53370",
    AUDITOR: "4ae6cae1cd554b55a02017be344ffb40daba3910f5b475f050aa0fc0dedd9986",
    AUDIT_SCRIPT: "f5dd2251366956e042e9d464409b743e000cb5c12300d7a4c078b3a568637f54",
    AUDIT_RESULT: "d437a8fa3788eb012474dc92ede701e49635c830202c3dbb1015d96a2ab36d6d",
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
        == "rate-half-kb-positive-433-1b-cell11-positive-de-pairing14-adapter-v1"
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
    require(totals == (136, 208, 208, 208, 0, 0), "exact totals")
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
    require(finite == {"CHECKED": 144, "MISSING_IMPOSSIBLE": 32,
                       "TARGET_PRODUCT_BOUNDARY": 32}
            and boundary == {"R_GUARD": 80, "T_GUARD": 32,
                             "CELL11_B_LEADING": 16,
                             "CELL11_C_LEADING": 16}
            and not endings,
            "terminal partition")

    roots = json.loads(ROOT_RESULT.read_text())
    require(roots["schema"]
            == "rate-half-kb-positive-433-1b-cell11-positive-de-pairing14-frobenius-roots-v1"
            and roots["source_primary_sha256"] == digest(RESULT)
            and len(roots["rows"]) == 37
            and sum(len(row["roots"]) for row in roots["rows"]) == 150
            and max(row["degree"] for row in roots["rows"]) == 1396,
            "external root census")
    audit = json.loads(AUDIT_RESULT.read_text())
    require(audit["schema"]
            == "rate-half-kb-positive-433-1b-cell11-positive-de-pairing14-direct-audit-v1"
            and audit["source_sha256"] == {
                "auditor": digest(AUDITOR), "primary": digest(RESULT),
                "roots": digest(ROOT_RESULT), "tower": digest(TOWER),
                "kernel": digest(KERNEL),
            }, "audit custody")
    require(audit["summary"] == {
        "candidate_root_count": 208, "checked": 144,
        "colored_nonzero": 0, "colored_solution_count": 0,
        "combined_profiles": 37, "leading_boundaries": 32,
        "missing_impossible": 32, "product_boundaries": 32,
        "profile_visits": 160, "route_point_count": 208, "rows": 16,
        "source_point_count": 208, "target_boundaries": 32,
        "target_root_count": 136, "uf_candidate_count": 0,
    }, "direct audit summary")

    spec = importlib.util.spec_from_file_location("label_router", ROUTER)
    router = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(router)
    selected = [orbit for orbit in router.compile_orbits() if (0, 14) in orbit]
    require(selected == [[(0, 14), (1, 14)]], "two-label orbit transport")
    manifest = json.loads((NODE / "node.json").read_text())["node"]
    require(manifest["id"] == NODE.name and manifest["status"] == "PROVED",
            "node manifest")
    print("PASS cell-11 positive-DE pairing 14: rows=16 candidates=208 labels=2")


if __name__ == "__main__":
    main()
