#!/usr/bin/env python3
"""Verify the cell-3 BC- colored function-field norm atlas."""

from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
LAUNCHER = (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_"
    "bcminus_colored_norm_modal.py"
)
RESULT = (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_"
    "bcminus_colored_norm_result.json"
)
LAUNCHER_SHA256 = "2d0d3442e2333e673849ec0df44021d49601abdd51cceb95f873bdb2102f72a1"
RESULT_SHA256 = "323507a457f1fa34a0e1f9ad77cdfae34ee8ff21c56551ebf32234ce7d64d687"
PARENT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_"
    "cell3_bcminus_genus_two_tower_locus"
)
CONSUMER = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_"
    "cell3_bcminus_colored_missing_exclusion"
)
PRIME = 2130706433


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def validate(payload):
    require(
        payload["schema"] ==
        "rate-half-kb-positive-433-1b-o0b-cell3-bcminus-colored-norm-v1",
        "schema",
    )
    require(payload["case_count"] == 8, "case count")
    require(payload["status_counts"] == {"COMPLETE": 8}, "status census")
    rows = {
        (tuple(row["epsilon"]), row["missing_record"]): row
        for row in payload["rows"]
    }
    expected = set(itertools.product(
        itertools.product((-1, 1), repeat=2), ("BE", "CF")
    ))
    require(set(rows) == expected and len(payload["rows"]) == 8,
            "case coverage")
    guards = None
    degree_rows = []
    for (epsilon, missing_record), row in sorted(rows.items()):
        require(row["status"] == "COMPLETE", "row completion")
        require(row["epsilon"] == list(epsilon), "epsilon echo")
        require(row["known_coordinate"] ==
                ("b" if missing_record == "BE" else "c"),
                "known coordinate")
        numerator = row["cut_norm_numerator"]
        denominator = row["cut_norm_denominator"]
        expected_degrees = (92, 104) if missing_record == "BE" else (100, 112)
        require((len(numerator) - 1, len(denominator) - 1) == expected_degrees,
                "norm degree")
        for polynomial in (numerator, denominator):
            require(polynomial[-1] == 1, "monic normalization")
            require(all(isinstance(value, int) and 0 <= value < PRIME
                        for value in polynomial), "coefficient range")
        row_guards = row["construction_guards"]
        require(len(row_guards) == 4, "guard count")
        for digest, coefficients in row_guards.items():
            encoded = json.dumps(coefficients, separators=(",", ":")).encode()
            require(hashlib.sha256(encoded).hexdigest() == digest,
                    "guard identity")
            require(coefficients[-1] == 1, "guard normalization")
        if guards is None:
            guards = row_guards
        require(row_guards == guards, "common guard atlas")
        degree_rows.append((missing_record, *expected_degrees))
    require(Counter(degree_rows) == Counter({
        ("BE", 92, 104): 4, ("CF", 100, 112): 4,
    }), "degree census")


def main():
    require(hashlib.sha256((EXPERIMENTS / LAUNCHER).read_bytes()).hexdigest()
            == LAUNCHER_SHA256, "launcher custody")
    require(hashlib.sha256((EXPERIMENTS / RESULT).read_bytes()).hexdigest()
            == RESULT_SHA256, "result custody")
    validate(json.loads((EXPERIMENTS / RESULT).read_text()))
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req"))
             for row in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    require(nodes[PARENT]["status"] == "PROVED" and
            (PARENT, NODE_ID, "req") in edges, "parent edge")
    require((NODE_ID, CONSUMER, "ev") in edges, "consumer edge")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_CELL3_BCMINUS_COLORED_NORM_VERIFY_PASS rows=8 guards=4 degrees=92,100")


if __name__ == "__main__":
    main()
