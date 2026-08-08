#!/usr/bin/env python3
"""Verify complete exclusion of the two cell-12 endpoint roles."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
PRIME = 2130706433
FILES = {
    "pilot_script": EXP / "rate_half_kb_positive_433_1b_cell12_endpoint_compatibility_pilot_modal.py",
    "pilot": EXP / "rate_half_kb_positive_433_1b_cell12_endpoint_compatibility_pilot_result.json",
    "replay_script": EXP / "rate_half_kb_positive_433_1b_cell12_endpoint_compatibility_replay_modal.py",
    "replay": EXP / "rate_half_kb_positive_433_1b_cell12_endpoint_compatibility_replay_result.json",
    "primary_script": EXP / "rate_half_kb_positive_433_1b_cell12_endpoint_residual_census_modal.py",
    "primary": EXP / "rate_half_kb_positive_433_1b_cell12_endpoint_residual_census_result.json",
    "audit_script": EXP / "rate_half_kb_positive_433_1b_cell12_endpoint_residual_audit_modal.py",
    "audit": EXP / "rate_half_kb_positive_433_1b_cell12_endpoint_residual_audit_result.json",
}
PINNED = {
    "pilot_script": "74bffea50566f74a01cd6e70902ee3ea44931a27665fa5ca603efd5fa3480906",
    "pilot": "616dedceec0e7a5ceaa2720e2ea80937281bdc6fdc74f326577de4285d706b49",
    "replay_script": "2f5729eb3117a019530dd73211bf2ad25edb23c1285411ae7bd109634b707899",
    "replay": "9319f72a2312c5a326083e01f97d38585babc77a34ce591498f6efefe3028c4f",
    "primary_script": "3c4b2568929de41c1fecfa13f7670200396195590d27598dcf5d797177a3a546",
    "primary": "0f7965bda8301ba4dc87432e5fd3def2c0d02fb0572b3bbd5274a45210a3d0b8",
    "audit_script": "03651decde02593572f048a8246dad1de66e405d06649dd0c4bdd04021a798d4",
    "audit": "0d60d85be40d752f4bc2ca61115e528719938aa661216e92e8ce35c1a5c8cea8",
}
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell12_compact_kernel_result.json"
STRUCTURE = EXP / "rate_half_kb_positive_433_1b_cell12_complete_pivot_scout_result.json"
TOWER = EXP / "rate_half_kb_positive_433_1b_cell12_four_basis_tower_result.json"
SIGNS = tuple(itertools.product((-1, 1), repeat=2))


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name):
    return json.loads(FILES[name].read_text())


def verify_source(pilot, replay):
    require(pilot["schema"] == "rate-half-kb-positive-433-1b-cell12-endpoint-pilot-v1"
            and pilot["field"] == PRIME
            and pilot["source_structure_sha256"] == digest(STRUCTURE)
            and pilot["source_kernel_sha256"] == digest(KERNEL),
            "pilot custody")
    expected = {(sign, endpoint) for sign in SIGNS for endpoint in ("b", "c")}
    seen = set()
    for row in pilot["rows"]:
        key = (tuple(row["epsilon"]), row["endpoint"])
        require(key in expected and key not in seen, "pilot coverage")
        seen.add(key)
        endpoint = row["endpoint"]
        require(row["status"] == "COMPLETE" and row["dimension"] == 0
                and not row["unit"] and row["r_elimination_size"] == 1
                and row["cut_degree"] == 34
                and row["basis_size"] == (37 if endpoint == "b" else 30)
                and row["cut_terms"] == (1317 if endpoint == "b" else 1325),
                "pilot exact result")
    require(seen == expected, "pilot Cartesian cover")

    require(replay["schema"] == "rate-half-kb-positive-433-1b-cell12-endpoint-replay-v1"
            and replay["field"] == PRIME
            and replay["source_pilot_sha256"] == digest(FILES["pilot"])
            and replay["source_tower_sha256"] == digest(TOWER)
            and replay["source_kernel_sha256"] == digest(KERNEL),
            "replay custody")
    seen = set()
    totals = {"b": 0, "c": 0}
    for row in replay["rows"]:
        key = (tuple(row["epsilon"]), row["endpoint"])
        require(key in expected and key not in seen, "replay coverage")
        seen.add(key)
        endpoint = row["endpoint"]
        wanted = (29, 6, 14, 4) if endpoint == "b" else (21, 4, 8, 6)
        got = tuple(row[name] for name in (
            "eliminant_degree", "r_root_count", "lifted_point_count",
            "generic_point_count",
        ))
        require(row["status"] == "COMPLETE" and got == wanted
                and not row["route_boundary"] and not row["leading_boundary"]
                and len(row["generic_points"]) == wanted[-1],
                "replay exact result")
        totals[endpoint] += wanted[-1]
    require(seen == expected and totals == {"b": 16, "c": 24},
            "replay Cartesian totals")


def verify_targets(primary, audit):
    require(primary["schema"] == "rate-half-kb-positive-433-1b-cell12-endpoint-residual-v1"
            and primary["field"] == PRIME
            and primary["source_replay_sha256"] == digest(FILES["replay"])
            and primary["source_kernel_sha256"] == digest(KERNEL),
            "primary custody")
    require(audit["schema"] == "rate-half-kb-positive-433-1b-cell12-endpoint-residual-audit-v1"
            and audit["field"] == PRIME and audit["primary_complete"]
            and audit["source_replay_sha256"] == digest(FILES["replay"])
            and audit["source_kernel_sha256"] == digest(KERNEL)
            and audit["source_primary_sha256"] == digest(FILES["primary"]),
            "audit custody")
    expected = {
        (sign, endpoint, lane)
        for sign in SIGNS for endpoint in ("b", "c") for lane in SIGNS
    }
    primary_rows = {}
    for row in primary["rows"]:
        key = (tuple(row["epsilon"]), row["endpoint"], tuple(row["sigma"]))
        require(key in expected and key not in primary_rows, "primary coverage")
        count = 60 if row["endpoint"] == "b" else 90
        labels = {(item["point_index"], item["pairing_index"])
                  for item in row["rows"]}
        require(row["status"] == "COMPLETE" and row["systems"] == count
                and row["unit_systems"] == count
                and not row["nonunit_systems"] and len(labels) == count
                and all(item["unit"] and item["dimension"] == -1
                        and item["basis_size"] == 1 for item in row["rows"]),
                "primary unit ledger")
        primary_rows[key] = count
    require(set(primary_rows) == expected and sum(primary_rows.values()) == 2400,
            "primary Cartesian total")

    audit_rows = {}
    for row in audit["rows"]:
        key = (tuple(row["epsilon"]), row["endpoint"], tuple(row["sigma"]))
        require(key in primary_rows and key not in audit_rows, "audit coverage")
        count = primary_rows[key]
        require(row["status"] == "COMPLETE" and row["systems"] == count
                and row["unit_unrestricted"] == count
                and row["finite_unrestricted"] == 0
                and row["no_deployed_root"] == 0
                and row["target_boundary"] == 0
                and not row["witnesses"] and not row["unresolved"],
                "audit unit ledger")
        audit_rows[key] = count
    require(set(audit_rows) == expected and sum(audit_rows.values()) == 2400,
            "audit Cartesian total")


def main():
    for name, expected in PINNED.items():
        require(digest(FILES[name]) == expected, f"hash drift: {name}")
    manifest = json.loads((NODE / "node.json").read_text())
    require(manifest["node"]["id"] == NODE.name
            and manifest["node"]["status"] == "PROVED"
            and len(manifest["requires"]) == 6,
            "node manifest")
    pilot, replay, primary, audit = map(load, ("pilot", "replay", "primary", "audit"))
    verify_source(pilot, replay)
    verify_targets(primary, audit)
    print("PASS cell-12 endpoint roles: 40 source points, 2400/2400 unit systems")


if __name__ == "__main__":
    main()
