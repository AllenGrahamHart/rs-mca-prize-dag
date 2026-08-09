#!/usr/bin/env python3
"""Verify the cell-11 parallel-DE first-pair exclusion packet."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
P = 2130706433
PREFIX = "rate_half_kb_positive_433_1b_cell11_"
FILES = {
    "norm_script": EXP / f"{PREFIX}parallel_de_four_basis_norm_modal.py",
    "norm": EXP / f"{PREFIX}parallel_de_four_basis_norm_result.json",
    "replay_script": EXP / f"{PREFIX}parallel_de_four_basis_replay_modal.py",
    "replay": EXP / f"{PREFIX}parallel_de_four_basis_replay_result.json",
    "audit_script": EXP / f"{PREFIX}parallel_de_norm_frobenius_audit_modal.py",
    "audit": EXP / f"{PREFIX}parallel_de_norm_frobenius_audit_result.json",
}
PINNED = {
    "norm_script": "46e3027a75a367b79907023e0b61d35458ad32e12164d6bd2bfc0e93f7ce2d19",
    "norm": "fe4eca817b4066455982d2bf5848f9d387945e6a18c4c4d3b68451445120dfed",
    "replay_script": "9278aa1b75aa930e19f9cb0242c70abd7bedab1b3e5dcf5f0f125a1eaf762623",
    "replay": "113fe9632739a9918da66d583c8eb63fc1419d1c765028be9255ea154324dab7",
    "audit_script": "bd8bce7655ba5925df22d418835a5fcaccb7640d79aad7f9e28ef95e71f3565b",
    "audit": "75f99608b32f34908319bf46277a2d69fb2f246c40597f861c0393bb4270e342",
}
TOWER = EXP / f"{PREFIX}four_basis_tower_result.json"
KERNEL = EXP / f"{PREFIX}compact_kernel_result.json"
SIGNS = tuple(itertools.product((-1, 1), repeat=2))
KINDS = ("opposite", "equal_negative")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name):
    return json.loads(FILES[name].read_text())


def validate():
    for name, expected in PINNED.items():
        require(digest(FILES[name]) == expected, f"hash drift: {name}")

    expected_rows = {(sign, kind) for sign in SIGNS for kind in KINDS}
    norm = load("norm")
    require(
        norm["schema"] == "rate-half-kb-positive-433-1b-cell11-parallel-de-four-basis-v1"
        and norm["field"] == P
        and norm["source_tower_sha256"] == digest(TOWER)
        and norm["source_kernel_sha256"] == digest(KERNEL),
        "norm custody",
    )
    norm_rows = {}
    for row in norm["rows"]:
        key = (tuple(row["epsilon"]), row["cut_kind"])
        require(key in expected_rows and key not in norm_rows, "norm coverage")
        kind = row["cut_kind"]
        require(
            row["status"] == "COMPLETE"
            and row["target_norm"]["numerator"]["degree"]
            == (400 if kind == "opposite" else 408)
            and row["target_root_count"] == (7 if kind == "opposite" else 4)
            and len(row["candidate_roots"]) == (11 if kind == "opposite" else 9)
            and row["guard_root_count"] == 9,
            "norm profile",
        )
        require(row["candidate_roots"] == sorted(set(row["candidate_roots"])),
                "candidate normalization")
        norm_rows[key] = row
    require(set(norm_rows) == expected_rows, "norm Cartesian cover")

    replay = load("replay")
    require(
        replay["schema"] == "rate-half-kb-positive-433-1b-cell11-parallel-de-replay-v1"
        and replay["field"] == P
        and replay["source_norm_sha256"] == digest(FILES["norm"])
        and replay["source_tower_sha256"] == digest(TOWER)
        and replay["source_kernel_sha256"] == digest(KERNEL),
        "replay custody",
    )
    replay_rows = {}
    terminal_counts = {"route": 0, "leading": 0, "no_lift": 0, "finite": 0}
    finite_statuses = {}
    for row in replay["rows"]:
        key = (tuple(row["epsilon"]), row["cut_kind"])
        require(
            key in norm_rows
            and key not in replay_rows
            and row["status"] == "COMPLETE"
            and row["candidate_root_count"] == len(norm_rows[key]["candidate_roots"])
            and not row["witnesses"]
            and not row["unresolved"]
            and row["excluded_generic"],
            "replay coverage",
        )
        wanted_no_lift = 7 if row["cut_kind"] == "opposite" else 3
        require(
            len(row["route_boundary"]) == 7
            and len(row["leading_boundary"]) == 1
            and len(row["no_lift"]) == wanted_no_lift
            and len(row["finite_rows"]) == 4
            and all(item["stage"] == "B_LEADING" for item in row["leading_boundary"])
            and 7 + 1 + wanted_no_lift + 4
            == row["candidate_root_count"] + (8 if row["cut_kind"] == "opposite" else 6),
            "replay terminal ledger",
        )
        terminal_counts["route"] += len(row["route_boundary"])
        terminal_counts["leading"] += len(row["leading_boundary"])
        terminal_counts["no_lift"] += len(row["no_lift"])
        terminal_counts["finite"] += len(row["finite_rows"])
        for item in row["finite_rows"]:
            finite_statuses[item["status"]] = finite_statuses.get(item["status"], 0) + 1
        replay_rows[key] = row
    require(
        set(replay_rows) == expected_rows
        and terminal_counts == {"route": 56, "leading": 8, "no_lift": 40, "finite": 32}
        and finite_statuses == {"MISSING_IMPOSSIBLE": 16, "NONZERO": 16},
        "replay totals",
    )

    audit = load("audit")
    require(
        audit["schema"]
        == "rate-half-kb-positive-433-1b-cell11-parallel-de-norm-frobenius-audit-v1"
        and audit["field"] == P
        and audit["complete"]
        and audit["source_norm_sha256"] == digest(FILES["norm"]),
        "audit custody",
    )
    audit_rows = {}
    for row in audit["rows"]:
        key = (tuple(row["epsilon"]), row["cut_kind"])
        source = norm_rows.get(key)
        require(
            source is not None
            and key not in audit_rows
            and row["status"] == "COMPLETE"
            and row["profile_visits"] == 9
            and row["unique_profiles"] == 7
            and row["target_roots"] == source["target_roots"]
            and len(row["guard_roots"]) == source["guard_root_count"] == 9
            and row["candidate_roots"]
            == sorted(set(row["target_roots"]) | set(row["guard_roots"]))
            and row["candidate_roots"] == source["candidate_roots"],
            "independent Frobenius row",
        )
        audit_rows[key] = row
    require(set(audit_rows) == expected_rows, "audit Cartesian cover")

    manifest = json.loads((NODE / "node.json").read_text())
    requires = {edge["from"] for edge in manifest["requires"]}
    require(
        manifest["node"]["status"] == "PROVED"
        and manifest["node"]["id"] == NODE.name
        and {
            "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell11_quadratic_four_basis_common_locus",
            "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell11_global_common_kernel",
            "rate_half_kb_m2_r4_coordinate_positive_433_1b_universal_generic_outside_label_orbit_quotient",
            "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas",
            "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
        } == requires
        and manifest["evidence_for"] == [{"to": "rate_half_band_closure"}],
        "node manifest",
    )
    return norm, replay, audit


def main():
    validate()
    print("PASS cell-11 parallel-DE first pair: labels=9 roots=80 witnesses=0")


if __name__ == "__main__":
    main()
