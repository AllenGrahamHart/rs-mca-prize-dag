#!/usr/bin/env python3
"""Verify the repeated-BC cell-3 BC- genus-two tower locus."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
FILES = {
    "projection_launcher": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_bcminus_curve_probe_modal.py",
        "c4e252dc949cbfcd91893d022e72144a19cbb5cc3b1bd54c49409c7276e494f5",
    ),
    "projection_result": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_bcminus_curve_probe_result.json",
        "bcd1b16ff4a1271837f6efd9e507feeaee0fbeeb0ee90dea2236f0301251b3f8",
    ),
    "tower_launcher": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_bcminus_tower_certificate_modal.py",
        "8fcb4a8cbe0b9463c600cd33e6406d2ba255b808c3f81d568d573dd18531a0dd",
    ),
    "tower_result": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_bcminus_tower_certificate_result.json",
        "61b807172ce3e7d11e3ee9462897f62654ba31921b88572460c3d57648d281be",
    ),
}
SOURCE_SHA256 = "713122da1efabb83a8c10598591240e6e7abb1069c1d105f6bea973de6a9d554"
PARENT = "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cells3_6_compact_locus"
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"
PROJECTION = (
    "b**3*c**3 + b**2*c**4 + 3*b**2*c**3 - 2*b**2*c**2 "
    "- 2*b**2*c - b**2 - b*c**4 - 2*b*c**3 - 2*b*c**2 + 3*b*c + b + c"
)
PROJECTION_ELIMINATION = (
    "c4b2+c3b3-c4b+3c3b2-2c3b-2c2b2-2c2b-2cb2+3cb-b2+c+b"
)
RELATIONS = {
    (-1, -1): "b*c*r**2 - 16711679*b*c - 16711678*b*r + 16711678*c*r - r**2 + 16711679",
    (-1, 1): "-b*c*r**2 - 16711679*b*c + 16711680*b*r - 16711680*c*r + r**2 + 16711679",
    (1, -1): "-b*c*r**2 + 16711679*b*c - 16711678*b*r + 16711678*c*r + r**2 - 16711679",
    (1, 1): "b*c*r**2 + 16711679*b*c + 16711680*b*r - 16711680*c*r - r**2 - 16711679",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def validate_projection(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-cell3-bcminus-curve-probe-v1",
            "projection schema")
    require(payload["source_sha256"] == SOURCE_SHA256, "projection source")
    require(payload["status_counts"] == {"COMPLETE": 4}, "projection completion")
    expected = set(itertools.product((-1, 1), repeat=2))
    actual = set()
    for row in payload["rows"]:
        epsilon = tuple(row["epsilon"])
        require(epsilon in expected and epsilon not in actual, "projection case")
        actual.add(epsilon)
        require(row["status"] == "COMPLETE" and row["full_dimension"] == 1,
                "projection row")
        require(row["removed_gcd"] == {
            "degree": 2, "expression": "r**2", "terms": 1,
        }, "projection gcd")
        output = "".join(row["elimination_output"].split())
        require(output == "DIM=3SIZE=1"+PROJECTION_ELIMINATION,
                "projection polynomial")
    require(actual == expected and len(payload["rows"]) == 4,
            "projection coverage")


def validate_tower(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-cell3-bcminus-tower-v1",
            "tower schema")
    require(payload["source_sha256"] == SOURCE_SHA256, "tower source")
    require(payload["status_counts"] == {"COMPLETE": 4}, "tower completion")
    expected = set(itertools.product((-1, 1), repeat=2))
    actual = set()
    for row in payload["rows"]:
        epsilon = tuple(row["epsilon"])
        require(epsilon in expected and epsilon not in actual, "tower case")
        actual.add(epsilon)
        require(row["status"] == "COMPLETE", "tower row")
        require(row["substitution"] == {
            "t": f"{epsilon[0]*epsilon[1]}*r^2",
        }, "tower substitution")
        require(row["removed_gcd"] == "r**2", "tower gcd")
        require(row["projection"] == PROJECTION, "tower projection")
        require(row["r_relation"] == RELATIONS[epsilon], "tower relation")
        require(row["original_dimension"] == 1 and
                row["tower_dimension"] == 1, "tower dimensions")
        require(set(row["remainders"]) == {
            "primitive_0_mod_tower", "primitive_1_mod_tower",
            "primitive_2_mod_tower", "projection_mod_original",
            "r_relation_mod_original",
        } and all(value == "0" for value in row["remainders"].values()),
                "bidirectional containments")
    require(actual == expected and len(payload["rows"]) == 4, "tower coverage")
    prime = 2130706433
    require((-((1 << 32)*13)) % prime == 1694498843,
            "degree-six discriminant residue")


def main():
    for filename, expected in FILES.values():
        require(hashlib.sha256((EXPERIMENTS / filename).read_bytes()).hexdigest()
                == expected, f"file custody {filename}")
    validate_projection(json.loads(
        (EXPERIMENTS / FILES["projection_result"][0]).read_text()))
    validate_tower(json.loads(
        (EXPERIMENTS / FILES["tower_result"][0]).read_text()))
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req"))
             for row in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    require(nodes[PARENT]["status"] == "PROVED" and
            (PARENT, NODE_ID, "req") in edges, "parent")
    require((NODE_ID, CONSUMER, "ev") in edges, "consumer")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_CELL3_BCMINUS_TOWER_VERIFY_PASS rows=4 containments=20 genus=2")


if __name__ == "__main__":
    main()
