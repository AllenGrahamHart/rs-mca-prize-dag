#!/usr/bin/env python3
"""Verify the cell-5 parallel-DE pairing-11/14 packet."""

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
SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell5_de_pairing11_template_adapter_modal.py"
RESULT = EXP / "rate_half_kb_positive_433_1b_cell5_de_pairing11_template_adapter_result.json"
TEMPLATE = EXP / "rate_half_kb_positive_433_1b_cell4_de_pairing11_common_f_resultant_modal.py"
TOWER = EXP / "rate_half_kb_positive_433_1b_cell5_four_basis_tower_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell5_compact_kernel_result.json"
ROOT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell5_de_pairing11_frobenius_roots_modal.py"
ROOT_RESULT = EXP / "rate_half_kb_positive_433_1b_cell5_de_pairing11_frobenius_roots_result.json"
AUDITOR = EXP / "rate_half_kb_positive_433_1b_cell5_common_f_resultant_audit.py"
AUDIT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell5_de_pairing11_direct_audit_modal.py"
AUDIT_RESULT = EXP / "rate_half_kb_positive_433_1b_cell5_de_pairing11_direct_audit_result.json"
ROUTER = EXP / "rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
PINNED = {
    SCRIPT: "8008a5296154410df27066b13323d85597909fe3fb6f6673b87d744cb0c17c83",
    RESULT: "c84816b22008ba70a1f18c8164fdadf9c3461d57c3103c655ef654f2eb50bfe3",
    TEMPLATE: "3e3c5aa6b389ee572998bd46626b2df7956c475baaf4832378ef9ec4b6774664",
    ROOT_SCRIPT: "7541a302ed18a822ded0495306db2ec170b3769e1c5fca23cd4acc0dd8bf650e",
    ROOT_RESULT: "667d7e1408c100990c38fd1a60a3a94c995d5f74831fce6f33f97bcffee8196a",
    AUDITOR: "9440f4bba0e358d0939e963b3ca6c673a2e4393766fe98bb5da3a1f43e0cd6de",
    AUDIT_SCRIPT: "e709cf64168bfd41e9a136c2051c0b7bf5a309c897dcab01c1ae40e5948310cd",
    AUDIT_RESULT: "9ede68ace468d95dd9df68acdf53cf08de84c05e893d273659880e28118afb4e",
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
        == "rate-half-kb-positive-433-1b-cell5-de-pairing11-adapter-v1"
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
    require(totals == (264, 464, 576, 576, 0, 0), "exact totals")
    finite = collections.Counter(
        item["status"] for row in payload["rows"] for item in row["finite_rows"]
    )
    boundary = collections.Counter(
        item["stage"] for row in payload["rows"] for item in row["boundary_rows"]
    )
    require(finite == {"CHECKED": 448, "MISSING_IMPOSSIBLE": 64,
                       "TARGET_PRODUCT_BOUNDARY": 64}
            and boundary == {"R_GUARD": 160, "T_GUARD": 128},
            "terminal partition")

    roots = json.loads(ROOT_RESULT.read_text())
    require(roots["source_primary_sha256"] == {"pairing11": digest(RESULT)}
            and len(roots["rows"]) == 49
            and sum(len(row["roots"]) for row in roots["rows"]) == 236
            and max(row["degree"] for row in roots["rows"]) == 992,
            "external root census")
    audit = json.loads(AUDIT_RESULT.read_text())
    require(audit["source_sha256"] == {
        "auditor": digest(AUDITOR), "primary": digest(RESULT),
        "roots": digest(ROOT_RESULT), "tower": digest(TOWER),
        "kernel": digest(KERNEL),
    }, "audit custody")
    require(audit["summary"] == {
        "candidate_root_count": 464, "checked": 448,
        "colored_nonzero": 0, "colored_solution_count": 0,
        "combined_profiles": 49, "leading_boundaries": 0,
        "missing_impossible": 64, "product_boundaries": 64,
        "profile_visits": 320, "route_point_count": 576, "rows": 32,
        "source_point_count": 576, "target_boundaries": 112,
        "target_root_count": 264, "uf_candidate_count": 0,
    }, "direct audit summary")

    spec = importlib.util.spec_from_file_location("label_router", ROUTER)
    router = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(router)
    direct = {(0, 11), (2, 11)}
    selected = [orbit for orbit in router.compile_orbits() if direct & set(orbit)]
    require(selected == [[(0, 11), (1, 11)], [(2, 11), (2, 14)]],
            "four-label orbit transport")
    print("PASS cell-5 parallel-DE pairing 11/14: rows=32 candidates=464 labels=4")


if __name__ == "__main__":
    main()
