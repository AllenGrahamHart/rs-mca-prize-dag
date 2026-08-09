#!/usr/bin/env python3
"""Verify the cell-9 endpoint compatibility decomposition."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
FILES = {
    "compat_script": EXP / "rate_half_kb_positive_433_1b_cell9_endpoint_compatibility_modal.py",
    "compat": EXP / "rate_half_kb_positive_433_1b_cell9_endpoint_compatibility_result.json",
    "replay_script": EXP / "rate_half_kb_positive_433_1b_cell9_endpoint_replay_modal.py",
    "replay": EXP / "rate_half_kb_positive_433_1b_cell9_endpoint_replay_result.json",
}
PINNED = {
    "compat_script": "1d2e647d24d273a88c9b326ddb4c5aa3af00d0e6fa13a1ed6851f906a2f65d67",
    "compat": "3020e03c035bbca3ed928c89fa7c15ad941a9ee328d88009e902d912e31f2bb8",
    "replay_script": "d9e2967066d5ca9909d0b64d0d84bd72bfaa8cefe74ffbba42f39b4111709f45",
    "replay": "f2afd55114515f9c337e935647cb4828359b0d1858f7bd4fdd23b3c642657a00",
}
STRUCTURE = EXP / "rate_half_kb_positive_433_1b_cell9_global_common_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell9_compact_kernel_result.json"
PRIME = 2130706433
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_global_five_relation_common_locus",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_global_common_kernel",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    for name, expected in PINNED.items():
        require(digest(FILES[name]) == expected, f"hash drift: {name}")
    compat = json.loads(FILES["compat"].read_text())
    replay = json.loads(FILES["replay"].read_text())
    require(compat["schema"] ==
            "rate-half-kb-positive-433-1b-cell9-endpoint-compatibility-v1"
            and compat["field"] == PRIME
            and compat["source_structure_sha256"] == digest(STRUCTURE)
            and compat["source_kernel_sha256"] == digest(KERNEL),
            "compatibility custody")
    expected = {
        (sign, endpoint)
        for sign in itertools.product((-1, 1), repeat=2)
        for endpoint in ("b", "c")
    }
    seen = set()
    for row in compat["rows"]:
        key = (tuple(row["epsilon"]), row["endpoint"])
        require(key in expected and key not in seen, "compatibility coverage")
        seen.add(key)
        endpoint = row["endpoint"]
        require(row["status"] == "COMPLETE" and row["base_dimension"] == 1
                and row["base_basis_size"] == 40
                and row["denominator_dimension"] == 0
                and row["denominator_basis_size"] == 31
                and not row["denominator_unit"]
                and row["indeterminate_dimension"] == 0
                and row["indeterminate_basis_size"] == 21
                and not row["indeterminate_unit"]
                and row["kernel_null_dimension"] == 0
                and row["kernel_null_basis_size"] == 21
                and not row["kernel_null_unit"]
                and row["dimension"] == 0 and not row["unit"]
                and row["basis_size"] == (38 if endpoint == "b" else 30)
                and len(row["compatibility_lex_basis"]) == 5
                and len(row["kernel_null_lex_basis"]) == 5
                and not row["stderr"], "compatibility exact ledger")
    require(seen == expected, "compatibility Cartesian cover")

    require(replay["schema"] ==
            "rate-half-kb-positive-433-1b-cell9-endpoint-replay-v1"
            and replay["field"] == PRIME
            and replay["source_compatibility_sha256"] == digest(FILES["compat"])
            and replay["source_kernel_sha256"] == digest(KERNEL),
            "replay custody")
    seen = set()
    null_sets = {}
    for row in replay["rows"]:
        key = (tuple(row["epsilon"]), row["endpoint"])
        require(key in expected and key not in seen, "replay coverage")
        seen.add(key)
        require(row["status"] == "COMPLETE"
                and row["compatibility_point_count"] == 6
                and row["generic_point_count"] == 4
                and row["kernel_null_point_count"] == 2
                and len(row["generic_points"]) == 4
                and len(row["kernel_null_points"]) == 2
                and row["all_guards_nonzero"], "replay point ledger")
        null_sets[key] = tuple(
            tuple(point[name] for name in ("r", "t", "b", "c"))
            for point in row["kernel_null_points"]
        )
    require(seen == expected, "replay Cartesian cover")
    for sign in itertools.product((-1, 1), repeat=2):
        require(null_sets[(sign, "b")] == null_sets[(sign, "c")],
                "endpoint base-locus mismatch")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(NODE.name in nodes and nodes[NODE.name]["status"] == "PROVED",
            "DAG node")
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    require(all((parent, NODE.name, "req") in edges for parent in PARENTS),
            "DAG parents")
    print("cell=9 endpoint_rows=8 deployed_points=48 generic=32 base=16")


if __name__ == "__main__":
    main()
