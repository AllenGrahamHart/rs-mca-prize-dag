#!/usr/bin/env python3
"""Verify the cell-3 BC- uncolored generic-rank atlas."""

from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
LAUNCHER = "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_bcminus_uncolored_generic_rank_modal.py"
RESULT = "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_bcminus_uncolored_generic_rank_result.json"
HASHES = {
    LAUNCHER: "f441312e28e44ba924a0369930dc95593ef131b9e269a9c913d1d8a1ad55c4c5",
    RESULT: "5f0a1569a0bdbf61b5e066874ea9adc4b20d8602153d3804e3a0fcf94e0e50c9",
}
PARENT = "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell3_bcminus_genus_two_tower_locus"
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def validate(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-cell3-bcminus-uncolored-generic-rank-v1",
            "schema")
    require(payload["case_count"] == 360 and payload["complete_atlas"] is True,
            "coverage header")
    require(payload["status_counts"] == {"GENERIC_UNIT": 360}, "statuses")
    guards = payload["guard_atlas"]
    require(len(guards) == 47, "guard count")
    for digest, packed in guards.items():
        coefficients = [int(value) for value in packed.split(",")]
        actual = hashlib.sha256(json.dumps(
            coefficients, separators=(",", ":")
        ).encode()).hexdigest()
        require(actual == digest and coefficients[-1] == 1, "guard custody")
    expected = set(itertools.product(
        (-1, 1), (-1, 1), ("DE+", "DF+", "EF"), (-1, 1), range(15)
    ))
    actual = set()
    pairs = Counter()
    degrees = Counter()
    for row in payload["rows"]:
        case = (row["epsilon"][0], row["epsilon"][1],
                row["missing_record"], row["sigma_o"], row["pairing_index"])
        require(case in expected and case not in actual, "case")
        actual.add(case)
        require(row["status"] == "GENERIC_UNIT", "row status")
        selected = row["selected"]
        require(selected["size"] == selected["rank"] == 16, "full rank")
        pair = tuple(selected["equations"])
        require(pair == min(
            itertools.combinations(range(3), 2),
            key=lambda item: (row["equation_degrees"][item[0]]
                              +row["equation_degrees"][item[1]], item),
        ), "minimum-degree pair")
        require(row["guard_hashes"] and
                set(row["guard_hashes"]) <= set(guards), "row guards")
        pairs[pair] += 1
        degrees[tuple(row["equation_degrees"])] += 1
    require(actual == expected and len(payload["rows"]) == 360, "case coverage")
    require(pairs == Counter({(0, 1): 248, (0, 2): 64, (1, 2): 48}),
            "pair histogram")
    require(degrees == Counter({
        (2, 2, 4): 176, (2, 4, 2): 64, (0, 4, 4): 48,
        (4, 2, 2): 48, (4, 0, 4): 24,
    }), "degree histogram")


def main():
    for filename, digest in HASHES.items():
        require(hashlib.sha256((EXPERIMENTS / filename).read_bytes()).hexdigest()
                == digest, f"file custody {filename}")
    validate(json.loads((EXPERIMENTS / RESULT).read_text()))
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req"))
             for row in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    require(nodes[PARENT]["status"] == "PROVED" and
            (PARENT, NODE_ID, "req") in edges, "parent")
    require((NODE_ID, CONSUMER, "ev") in edges, "consumer")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_CELL3_BCMINUS_GENERIC_VERIFY_PASS cases=360 rank16=360 guards=47")


if __name__ == "__main__":
    main()
