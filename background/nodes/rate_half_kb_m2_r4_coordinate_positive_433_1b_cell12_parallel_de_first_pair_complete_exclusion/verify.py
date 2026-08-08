#!/usr/bin/env python3
"""Verify the cell-12 parallel-DE first-pair exclusion packet."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
P = 2130706433
NAMES = (
    "parallel_de_four_basis_norm",
    "parallel_de_four_basis_replay",
    "parallel_de_first_pair_residual",
    "parallel_de_first_pair_audit",
)
FILES = {}
for stem in NAMES:
    prefix = f"rate_half_kb_positive_433_1b_cell12_{stem}"
    FILES[f"{stem}_script"] = EXP / f"{prefix}_modal.py"
    FILES[stem] = EXP / f"{prefix}_result.json"
PINNED = {
    "parallel_de_four_basis_norm_script": "b82fce616ce7ed5ae07f1c6a0112cf760e62881366b0f594b7b448d1bc38273d",
    "parallel_de_four_basis_norm": "44f0e750ba1b80367df8cff37884aed20dc5b03b4abf53dc77a065a4522108c3",
    "parallel_de_four_basis_replay_script": "d1a7f7dd92e3fa29b663c8f15af53929affa653f91e9b00ea70d43b12a9c4fcf",
    "parallel_de_four_basis_replay": "d8b2f7136103c234e5843288ffa31be7ea621e4f7bdb8c4155feaa696faee0ee",
    "parallel_de_first_pair_residual_script": "3e628852d9b8d7d0a26cc786b68be041983854a7dfcb2376500033b1c2a02d99",
    "parallel_de_first_pair_residual": "8e246ef55d1af90ed710bbd44c7aa456317e69582783a38738c5e479d9860197",
    "parallel_de_first_pair_audit_script": "22aada196e2b05600061de84c5323331df6d1859f4c94a3f464bb17cb2adbe1c",
    "parallel_de_first_pair_audit": "a4924f9280c54ffce2720c7c7ffd2e26a37c2a149a94cc56f46d24ef99d73f3f",
}
TOWER = EXP / "rate_half_kb_positive_433_1b_cell12_four_basis_tower_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell12_compact_kernel_result.json"
SIGNS = tuple(itertools.product((-1, 1), repeat=2))


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name):
    return json.loads(FILES[name].read_text())


def main():
    for name, expected in PINNED.items():
        require(digest(FILES[name]) == expected, f"hash drift: {name}")
    norm = load("parallel_de_four_basis_norm")
    require(norm["schema"] == "rate-half-kb-positive-433-1b-cell12-parallel-de-four-basis-v1"
            and norm["field"] == P
            and norm["source_tower_sha256"] == digest(TOWER)
            and norm["source_kernel_sha256"] == digest(KERNEL), "norm custody")
    expected_source = {(sign, kind) for sign in SIGNS
                       for kind in ("opposite", "equal_negative")}
    norm_rows = {}
    for row in norm["rows"]:
        key = (tuple(row["epsilon"]), row["cut_kind"])
        require(key in expected_source and key not in norm_rows, "norm coverage")
        kind = row["cut_kind"]
        require(row["status"] == "COMPLETE"
                and row["target_norm"]["numerator"]["degree"] ==
                (350 if kind == "opposite" else 362)
                and row["target_root_count"] == (8 if kind == "opposite" else 7)
                and len(row["candidate_roots"]) == (15 if kind == "opposite" else 14),
                "norm profile")
        norm_rows[key] = row
    require(set(norm_rows) == expected_source, "norm Cartesian cover")

    replay = load("parallel_de_four_basis_replay")
    require(replay["schema"] == "rate-half-kb-positive-433-1b-cell12-parallel-de-replay-v1"
            and replay["source_norm_sha256"] == digest(FILES["parallel_de_four_basis_norm"])
            and replay["source_tower_sha256"] == digest(TOWER)
            and replay["source_kernel_sha256"] == digest(KERNEL), "replay custody")
    replay_rows = {}
    for row in replay["rows"]:
        key = (tuple(row["epsilon"]), row["cut_kind"])
        require(key in norm_rows and key not in replay_rows
                and row["status"] == "COMPLETE" and not row["unresolved"],
                "replay coverage")
        wanted = 2 if row["cut_kind"] == "opposite" else 0
        require(len(row["witnesses"]) == wanted
                and row["excluded_generic"] == (wanted == 0), "source terminal")
        replay_rows[key] = row
    require(set(replay_rows) == expected_source
            and sum(len(row["witnesses"]) for row in replay_rows.values()) == 8,
            "source replay totals")

    expected_targets = {(source, lane) for source in SIGNS for lane in SIGNS}
    primary = load("parallel_de_first_pair_residual")
    require(primary["schema"] == "rate-half-kb-positive-433-1b-cell12-parallel-de-residual-v1"
            and primary["source_replay_sha256"] == digest(FILES["parallel_de_four_basis_replay"])
            and primary["source_kernel_sha256"] == digest(KERNEL), "primary custody")
    primary_rows = {}
    for row in primary["rows"]:
        key = (tuple(row["epsilon"]), tuple(row["sigma"]))
        labels = {(item["point_index"], item["pairing_index"])
                  for item in row["rows"]}
        require(key in expected_targets and key not in primary_rows
                and row["status"] == "COMPLETE" and row["systems"] == 6
                and row["unit_systems"] == 6 and not row["nonunit_systems"]
                and labels == set(itertools.product(range(2), range(3)))
                and all(item["unit"] and item["dimension"] == -1
                        and item["basis_size"] == 1 for item in row["rows"]),
                "primary unit ledger")
        primary_rows[key] = row
    require(set(primary_rows) == expected_targets, "primary Cartesian cover")

    audit = load("parallel_de_first_pair_audit")
    require(audit["schema"] == "rate-half-kb-positive-433-1b-cell12-parallel-de-audit-v1"
            and audit["primary_complete"]
            and audit["source_replay_sha256"] == digest(FILES["parallel_de_four_basis_replay"])
            and audit["source_kernel_sha256"] == digest(KERNEL)
            and audit["source_primary_sha256"] == digest(FILES["parallel_de_first_pair_residual"]),
            "audit custody")
    audit_keys = set()
    for row in audit["rows"]:
        key = (tuple(row["epsilon"]), tuple(row["sigma"]))
        require(key in expected_targets and key not in audit_keys
                and row["status"] == "COMPLETE" and row["systems"] == 6
                and row["unit_systems"] == 6 and row["finite_systems"] == 0
                and not row["witnesses"] and not row["unresolved"],
                "audit unit ledger")
        audit_keys.add(key)
    require(audit_keys == expected_targets, "audit Cartesian cover")
    manifest = json.loads((NODE / "node.json").read_text())
    require(manifest["node"]["status"] == "PROVED"
            and manifest["node"]["id"] == NODE.name, "node manifest")
    print("PASS cell-12 parallel-DE first pair: 9 labels, 96/96 unit systems")


if __name__ == "__main__":
    main()
