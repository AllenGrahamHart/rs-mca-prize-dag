#!/usr/bin/env python3
"""Verify the uncolored repeated-BC generic function-field rank atlas."""

from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
LAUNCHER = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_"
    "bcplus_uncolored_generic_rank_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_"
    "bcplus_uncolored_generic_rank_result.json"
)
LAUNCHER_SHA256 = "c120f1a82da25b06a259ec6e5e1e1cf42e62b0c1f93c132715ce69c208898d34"
RESULT_SHA256 = "084af4aebeaaa536558c1e71252a2ed6c3e19ac21f00160eb136ee70dc8a65fe"
PARENT = "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell3_bcplus_torus_locus"
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell3_bcplus_uncolored_guard_root_atlas"
GLOBAL_RECORDS = ("BE", "CF", "DE+", "DE-", "DF+", "DF-", "EF")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def pairings(values):
    values = tuple(values)
    if not values:
        return ((),)
    output = []
    for index in range(1, len(values)):
        for tail in pairings(values[1:index]+values[index+1:]):
            output.append(((values[0], values[index]),)+tail)
    return tuple(output)


MATCHINGS = pairings(range(6))


def case_key(row):
    return (tuple(row["epsilon"]), row["missing_record"],
            row["sigma_o"], row["pairing_index"])


def validate(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-cell3-bcplus-uncolored-generic-rank-v1",
            "schema")
    require(payload["case_count"] == 360 and payload["complete_atlas"] is True
            and payload["status_counts"] == {"GENERIC_UNIT": 360},
            "global status")
    expected = set(itertools.product(
        itertools.product((-1, 1), repeat=2),
        ("DE+", "DF+", "EF"), (-1, 1), range(15),
    ))
    rows = {case_key(row): row for row in payload["rows"]}
    require(len(rows) == len(payload["rows"]) == 360
            and set(rows) == expected, "case cover")

    atlas = {}
    for digest, text in payload["guard_atlas"].items():
        coefficients = [int(value) for value in text.split(",")]
        require(coefficients and coefficients[-1] != 0, "guard degree")
        computed = hashlib.sha256(json.dumps(
            coefficients, separators=(",", ":")
        ).encode()).hexdigest()
        require(computed == digest, "guard digest")
        atlas[digest] = coefficients
    require(len(atlas) == 54, "guard atlas size")

    equation_degrees = Counter()
    rank_profile = Counter()
    used_guards = set()
    for key in sorted(rows):
        row = rows[key]
        _, missing_record, _, pairing_index = key
        residual = tuple(name for name in GLOBAL_RECORDS
                         if name != missing_record)
        expected_matching = [
            [residual[left], residual[right]]
            for left, right in MATCHINGS[pairing_index]
        ]
        require(row["status"] == "GENERIC_UNIT"
                and tuple(row["residual_records"]) == residual
                and row["matching"] == expected_matching,
                "case semantics")
        selected = row["selected"]
        require(selected is not None
                and selected["equations"] == [0, 1]
                and selected["rank"] == selected["size"]
                and selected["size"] in (16, 24)
                and 368 <= selected["residual_determinant_degree"] <= 720,
                "full-rank certificate")
        require(row["pair_rows"] == [selected], "selected pair custody")
        require(len(row["guard_hashes"]) == 5
                and row["guard_hashes"] == sorted(set(row["guard_hashes"]))
                and set(row["guard_hashes"]) <= set(atlas),
                "case guard cover")
        equation_degrees[tuple(row["equation_degrees"])] += 1
        rank_profile[(selected["size"], selected["rank"])] += 1
        used_guards.update(row["guard_hashes"])

    require(used_guards == set(atlas), "unused guard")
    require(equation_degrees == {
        (0, 4, 4): 48,
        (2, 2, 4): 176,
        (2, 4, 2): 64,
        (4, 0, 4): 24,
        (4, 2, 2): 48,
    }, "equation-degree census")
    require(rank_profile == {(16, 16): 248, (24, 24): 112},
            "rank census")


def main():
    require(hashlib.sha256(LAUNCHER.read_bytes()).hexdigest() ==
            LAUNCHER_SHA256, "launcher custody")
    require(hashlib.sha256(RESULT.read_bytes()).hexdigest() ==
            RESULT_SHA256, "result custody")
    validate(json.loads(RESULT.read_text()))
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req"))
             for row in dag["edges"]}
    require(nodes[NODE.name]["status"] == "PROVED", "DAG status")
    require(nodes[PARENT]["status"] == "PROVED"
            and (PARENT, NODE.name, "req") in edges, "parent")
    require((NODE.name, CONSUMER, "req") in edges, "consumer")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_BCPLUS_UNCOLORED_GENERIC_RANK_VERIFY_PASS cases=360 guards=54 ranks=248x16+112x24")


if __name__ == "__main__":
    main()
