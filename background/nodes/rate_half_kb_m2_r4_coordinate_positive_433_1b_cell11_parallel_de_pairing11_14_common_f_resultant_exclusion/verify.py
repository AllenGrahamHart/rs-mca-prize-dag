#!/usr/bin/env python3
"""Verify the cell-11 parallel-DE pairing-11/14 packet."""

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
SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell11_de_pairing11_template_adapter_modal.py"
RESULT = EXP / "rate_half_kb_positive_433_1b_cell11_de_pairing11_template_adapter_result.json"
TEMPLATE = EXP / "rate_half_kb_positive_433_1b_cell4_de_pairing11_common_f_resultant_modal.py"
TOWER = EXP / "rate_half_kb_positive_433_1b_cell11_four_basis_tower_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell11_compact_kernel_result.json"
ROOT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell11_de_pairing11_frobenius_roots_modal.py"
ROOT_RESULT = EXP / "rate_half_kb_positive_433_1b_cell11_de_pairing11_frobenius_roots_result.json"
AUDITOR = EXP / "rate_half_kb_positive_433_1b_cell11_common_f_resultant_audit.py"
AUDIT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell11_de_pairing11_direct_audit_modal.py"
AUDIT_RESULT = EXP / "rate_half_kb_positive_433_1b_cell11_de_pairing11_direct_audit_result.json"
ROUTER = EXP / "rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
PINNED = {
    SCRIPT: "e404911a92f70dba6da29b735e702f7cdd8f2c204db09e25c683e1247aaf309c",
    RESULT: "5582966df3fdcdec3bb5582fe306248406dd67fa3c1824c67ddcd83fb995f6d5",
    TEMPLATE: "3e3c5aa6b389ee572998bd46626b2df7956c475baaf4832378ef9ec4b6774664",
    ROOT_SCRIPT: "6c9018871a8af16f2c765fb8d976f218d1831d1a09b548f3b4e2987747abf70d",
    ROOT_RESULT: "b8e5e90d5c1809331d608ede57f3fb2613353f41bc8ce1673b2f1c26ab3593b4",
    AUDITOR: "d0e72a9d1a2d351cd08b00a0697cb034dac13f6ccc9e6d85628f7bed07582ab7",
    AUDIT_SCRIPT: "b09ca3bb740efe124659dbf33ae33ccc31a452bc02d82518fd42e4b83e8a5e69",
    AUDIT_RESULT: "85a087ee11f419da04443442e4d4656a8ee55d1216d109f9cbaefe3c3d699094",
}
P = 2130706433
MATCHING = ((0, 4), (1, 5), (2, 3))


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
        == "rate-half-kb-positive-433-1b-cell11-de-pairing11-adapter-v1"
        and payload["field"] == P
        and payload["source_template_sha256"] == digest(TEMPLATE)
        and payload["source_tower_sha256"] == digest(TOWER)
        and payload["source_kernel_sha256"] == digest(KERNEL),
        "packet custody",
    )
    expected = set(itertools.product(
        itertools.product((-1, 1), repeat=2),
        itertools.product((-1, 1), repeat=2),
        (0, 2),
    ))
    seen = set()
    for row in payload["rows"]:
        key = (tuple(row["epsilon"]), tuple(row["sigma"]), row["xi_index"])
        require(key in expected and key not in seen, "Cartesian row")
        seen.add(key)
        require(row["status"] == "COMPLETE" and row["excluded"]
                and row["pairing_index"] == 11
                and tuple(map(tuple, row["matching"])) == MATCHING
                and not row["witnesses"] and not row["unresolved"],
                "complete terminal")
    require(seen == expected and len(payload["rows"]) == 32, "32-row cover")
    totals = tuple(sum(row[key] for row in payload["rows"]) for key in (
        "target_root_count", "candidate_root_count", "source_point_count",
        "route_point_count", "uf_candidate_count", "colored_solution_count",
    ))
    require(totals == (216, 360, 272, 272, 0, 0), "exact totals")
    finite = collections.Counter(
        item["status"] for row in payload["rows"] for item in row["finite_rows"]
    )
    boundary = collections.Counter(
        item["stage"] for row in payload["rows"] for item in row["boundary_rows"]
    )
    require(finite == {"CHECKED": 144, "MISSING_IMPOSSIBLE": 64,
                       "TARGET_PRODUCT_BOUNDARY": 64}
            and boundary == {"R_GUARD": 160, "T_GUARD": 64,
                             "CELL11_B_LEADING": 32,
                             "CELL11_C_LEADING": 32},
            "terminal partition")

    roots = json.loads(ROOT_RESULT.read_text())
    require(roots["source_primary_sha256"] == {"pairing11": digest(RESULT)}
            and len(roots["rows"]) == 53
            and sum(len(row["roots"]) for row in roots["rows"]) == 222
            and max(row["degree"] for row in roots["rows"]) == 1420,
            "external root census")
    audit = json.loads(AUDIT_RESULT.read_text())
    require(audit["source_sha256"] == {
        "auditor": digest(AUDITOR), "primary": digest(RESULT),
        "roots": digest(ROOT_RESULT), "tower": digest(TOWER),
        "kernel": digest(KERNEL),
    }, "audit custody")
    require(audit["summary"] == {
        "candidate_root_count": 360, "checked": 144,
        "colored_nonzero": 0, "colored_solution_count": 0,
        "combined_profiles": 53, "leading_boundaries": 64,
        "missing_impossible": 64, "product_boundaries": 64,
        "profile_visits": 320, "route_point_count": 272, "rows": 32,
        "source_point_count": 272, "target_boundaries": 64,
        "target_root_count": 216, "uf_candidate_count": 0,
    }, "direct audit summary")

    spec = importlib.util.spec_from_file_location("label_router", ROUTER)
    router = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(router)
    direct = {(0, 11), (2, 11)}
    selected = [orbit for orbit in router.compile_orbits() if direct & set(orbit)]
    require(selected == [[(0, 11), (1, 11)], [(2, 11), (2, 14)]],
            "four-label orbit transport")
    print("PASS cell-11 parallel-DE pairing 11/14: rows=32 candidates=360 labels=4")


if __name__ == "__main__":
    main()
