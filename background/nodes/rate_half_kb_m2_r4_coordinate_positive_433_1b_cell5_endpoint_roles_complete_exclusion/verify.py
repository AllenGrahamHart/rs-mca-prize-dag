#!/usr/bin/env python3
"""Verify complete exclusion of the two cell-5 endpoint roles."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
PRIME = 2130706433
FILES = {
    "pilot_script": EXP / "rate_half_kb_positive_433_1b_cell5_endpoint_compatibility_pilot_modal.py",
    "pilot": EXP / "rate_half_kb_positive_433_1b_cell5_endpoint_compatibility_pilot_result.json",
    "replay_script": EXP / "rate_half_kb_positive_433_1b_cell5_endpoint_compatibility_replay_modal.py",
    "replay": EXP / "rate_half_kb_positive_433_1b_cell5_endpoint_compatibility_replay_result.json",
    "root_script": EXP / "rate_half_kb_positive_433_1b_cell5_endpoint_eliminant_rootlessness_modal.py",
    "root": EXP / "rate_half_kb_positive_433_1b_cell5_endpoint_eliminant_rootlessness_result.json",
}
PINNED = {
    "pilot_script": "acc5bf043cec867a32b8024598e258fdf96b12ccf9b4b98b09acba111f3c9fdd",
    "pilot": "2aa299a33d85a14eec78a0722ec9c82d137327acdfdc7ef8a370243ea9f21030",
    "replay_script": "adafb45423f22aed9416aa7bbd3ed05de6f8b0813e704e3cfcdfa92ba106df43",
    "replay": "3d18b5cedbd2fbd6250c75dcb258c4381445b2eb19f52a25edf50faa03ca24da",
    "root_script": "6e52637612bb4e751318fab7268055bfde83c24c1fb117541d28b2d4fbae745e",
    "root": "f9690150ce1312c43e50eccfef21d84328329a70d1125f656bbefe796e945d9d",
}
STRUCTURE = EXP / "rate_half_kb_positive_433_1b_cell5_complete_pivot_scout_result.json"
TOWER = EXP / "rate_half_kb_positive_433_1b_cell5_four_basis_tower_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell5_compact_kernel_result.json"
SIGNS = tuple(itertools.product((-1, 1), repeat=2))


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name):
    return json.loads(FILES[name].read_text())


def validate(pilot, replay, root, kernel):
    expected = {(sign, endpoint) for sign in SIGNS for endpoint in ("b", "c")}
    require(
        pilot["schema"] == "rate-half-kb-positive-433-1b-cell5-endpoint-pilot-v1"
        and pilot["field"] == PRIME
        and pilot["source_structure_sha256"] == digest(STRUCTURE)
        and pilot["source_kernel_sha256"] == digest(KERNEL),
        "pilot custody",
    )
    pilot_rows = {}
    for row in pilot["rows"]:
        key = (tuple(row["epsilon"]), row["endpoint"])
        require(key in expected and key not in pilot_rows, "pilot coverage")
        endpoint = row["endpoint"]
        exact = (
            (28, 1233, 16) if endpoint == "b" else (21, 1777, 11)
        )
        require(
            row["status"] == "COMPLETE"
            and row["dimension"] == 0
            and not row["unit"]
            and row["r_elimination_dimension"] == 4
            and row["r_elimination_size"] == 1
            and row["cut_degree"] == 38
            and (row["basis_size"], row["cut_terms"]) == exact[:2],
            "pilot exact result",
        )
        pilot_rows[key] = (row, exact[2])
    require(set(pilot_rows) == expected, "pilot Cartesian cover")

    require(
        replay["schema"] == "rate-half-kb-positive-433-1b-cell5-endpoint-replay-v1"
        and replay["field"] == PRIME
        and replay["source_pilot_sha256"] == digest(FILES["pilot"])
        and replay["source_tower_sha256"] == digest(TOWER)
        and replay["source_kernel_sha256"] == digest(KERNEL),
        "replay custody",
    )
    replay_rows = {}
    for row in replay["rows"]:
        key = (tuple(row["epsilon"]), row["endpoint"])
        require(key in pilot_rows and key not in replay_rows, "replay coverage")
        degree = pilot_rows[key][1]
        require(
            row["status"] == "COMPLETE"
            and row["eliminant_degree"] == degree
            and row["r_root_count"] == 0
            and row["lifted_point_count"] == 0
            and row["generic_point_count"] == 0
            and not row["r_roots"]
            and not row["generic_points"]
            and not row["route_boundary"]
            and not row["leading_boundary"]
            and not row["no_lift"],
            "replay rootless result",
        )
        replay_rows[key] = row
    require(set(replay_rows) == expected, "replay Cartesian cover")

    require(
        root["schema"] == (
            "rate-half-kb-positive-433-1b-cell5-endpoint-"
            "eliminant-rootlessness-v1"
        )
        and root["field"] == PRIME
        and root["source_pilot_sha256"] == digest(FILES["pilot"])
        and root["complete"],
        "root audit custody",
    )
    root_rows = {}
    for row in root["rows"]:
        key = (tuple(row["epsilon"]), row["endpoint"])
        require(key in pilot_rows and key not in root_rows, "root audit coverage")
        pilot_row, degree = pilot_rows[key]
        require(
            row["degree"] == degree
            and row["eliminant_sha256"]
            == hashlib.sha256(pilot_row["r_elimination"].encode()).hexdigest()
            and row["root_gcd"] == [1]
            and row["root_count"] == 0,
            "independent Frobenius rootlessness",
        )
        root_rows[key] = row
    require(set(root_rows) == expected, "root audit Cartesian cover")

    kernel_signatures = {
        tuple(item["sha256"] for item in row["kernel"])
        for row in kernel["rows"]
    }
    require(
        {tuple(row["epsilon"]) for row in kernel["rows"]} == set(SIGNS)
        and len(kernel_signatures) == 1,
        "sign-independent common kernel",
    )
    return {"pilot": len(pilot_rows), "replay": len(replay_rows), "roots": 0}


def main():
    for name, expected in PINNED.items():
        require(digest(FILES[name]) == expected, f"hash drift: {name}")
    manifest = json.loads((NODE / "node.json").read_text())
    require(
        manifest["node"]["id"] == NODE.name
        and manifest["node"]["status"] == "PROVED"
        and len(manifest["requires"]) == 3,
        "node manifest",
    )
    result = validate(load("pilot"), load("replay"), load("root"), json.loads(KERNEL.read_text()))
    print(
        "PASS cell-5 endpoint roles: "
        f"eliminants={result['pilot']} independent-root-count={result['roots']} "
        "labels=30"
    )


if __name__ == "__main__":
    main()
