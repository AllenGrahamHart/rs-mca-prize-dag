#!/usr/bin/env python3
"""Verify deployed-field roots of all uncolored generic-rank guards."""

from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
LAUNCHER = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_"
    "bcplus_uncolored_guard_roots_modal.py"
)
SOURCE = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_"
    "bcplus_uncolored_generic_rank_result.json"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_"
    "bcplus_uncolored_guard_roots_result.json"
)
LAUNCHER_SHA256 = "2b6b2671707a3f45d09e10d92fc9a0efd2ba25a8ae8226bebec3a661aacb65fb"
SOURCE_SHA256 = "084af4aebeaaa536558c1e71252a2ed6c3e19ac21f00160eb136ee70dc8a65fe"
RESULT_SHA256 = "719e586402513ac950c59a588b0aab0e35bdb4e7073f301e460cbceec3b3ad98"
PARENT = "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell3_bcplus_uncolored_generic_rank_atlas"
CONSUMERS = {
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell3_bcplus_uncolored_de_residual_pairing_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell3_bcplus_uncolored_df_residual_pairing_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell3_bcplus_uncolored_ef_residual_pairing_exclusion",
}
PRIME = 2130706433


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def trim(value):
    value = [item % PRIME for item in value]
    while len(value) > 1 and value[-1] == 0:
        value.pop()
    return value or [0]


def multiply(left, right):
    output = [0]*(len(left)+len(right)-1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            output[left_index+right_index] = (
                output[left_index+right_index]+left_value*right_value
            ) % PRIME
    return trim(output)


def divide(dividend, divisor):
    dividend, divisor = trim(dividend), trim(divisor)
    require(divisor != [0], "zero polynomial divisor")
    work = dividend[:]
    quotient = [0]*max(1, len(dividend)-len(divisor)+1)
    inverse = pow(divisor[-1], -1, PRIME)
    while work != [0] and len(work) >= len(divisor):
        shift = len(work)-len(divisor)
        coefficient = work[-1]*inverse % PRIME
        quotient[shift] = coefficient
        for index, value in enumerate(divisor):
            work[shift+index] = (
                work[shift+index]-coefficient*value
            ) % PRIME
        work = trim(work)
    return trim(quotient), work


def root_polynomial(roots):
    output = [1]
    for root in roots:
        output = multiply(output, [-root, 1])
    return output


def evaluate(polynomial, value):
    output = 0
    for coefficient in reversed(polynomial):
        output = (output*value+coefficient) % PRIME
    return output


def validate(source, payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-cell3-bcplus-uncolored-guard-roots-v1",
            "schema")
    require(payload["source_sha256"] == SOURCE_SHA256, "source link")
    require(payload["guard_count"] == 54
            and payload["status_counts"] == {"COMPLETE": 54},
            "global status")
    atlas = {
        digest: [int(value) for value in text.split(",")]
        for digest, text in source["guard_atlas"].items()
    }
    rows = {row["sha256"]: row for row in payload["rows"]}
    require(len(rows) == len(payload["rows"]) == 54
            and set(rows) == set(atlas), "guard cover")

    incidence = defaultdict(list)
    degree_histogram = Counter()
    for digest in sorted(rows):
        row, polynomial = rows[digest], atlas[digest]
        roots = row["roots"]
        require(row["status"] == "COMPLETE"
                and row["degree"] == len(polynomial)-1
                and roots == sorted(set(roots)), "guard row")
        field_part = root_polynomial(roots)
        require(row["field_part_degree"] == len(roots)
                and row["field_part_coefficients"] == field_part,
                "field-part certificate")
        _, remainder = divide(polynomial, field_part)
        require(remainder == [0]
                and all(evaluate(polynomial, root) == 0 for root in roots),
                "root divisibility")
        degree_histogram[len(roots)] += 1
        for root in roots:
            incidence[root].append(digest)

    require(degree_histogram == {0: 29, 1: 1, 2: 16, 3: 1, 4: 5, 11: 2},
            "field-part degree census")
    require(payload["root_union"] == sorted(incidence)
            and payload["root_incidence"] == {
                str(root): sorted(digests)
                for root, digests in sorted(incidence.items())
            }, "root incidence")
    require(len(incidence) == 67
            and sum(map(len, incidence.values())) == 78,
            "root census")


def main():
    require(hashlib.sha256(LAUNCHER.read_bytes()).hexdigest() ==
            LAUNCHER_SHA256, "launcher custody")
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest() ==
            SOURCE_SHA256, "source custody")
    require(hashlib.sha256(RESULT.read_bytes()).hexdigest() ==
            RESULT_SHA256, "result custody")
    validate(json.loads(SOURCE.read_text()), json.loads(RESULT.read_text()))
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req"))
             for row in dag["edges"]}
    require(nodes[NODE.name]["status"] == "PROVED", "DAG status")
    require(nodes[PARENT]["status"] == "PROVED"
            and (PARENT, NODE.name, "req") in edges, "parent")
    require(all((NODE.name, consumer, "req") in edges
                for consumer in CONSUMERS), "consumers")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_BCPLUS_UNCOLORED_GUARD_ROOT_VERIFY_PASS guards=54 roots=67 incidences=78")


if __name__ == "__main__":
    main()
