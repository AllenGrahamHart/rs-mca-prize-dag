#!/usr/bin/env python3
"""Verify the complete repeated-BC cell-11 outside exclusion assembly."""

import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell11_colored_deployed_off_guard_consistency_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell11_uncolored_deployed_off_guard_pair_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell11_selected_cofactor_deployed_boundary_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell11_missing_label_reconstruction_denominator_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell11_registered_guard_boundary_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell11_outside_label_sign_transport",
)
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"
RECORDS = ("BE", "CF", "DE+", "DE-", "DF+", "DF-", "EF")
DIRECT = ("BE", "CF", "DE+", "DF+", "EF")
TRANSPORT = {"DE-": "DE+", "DF-": "DF+"}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def pairings(values):
    values = tuple(values)
    if not values:
        yield ()
        return
    first = values[0]
    for index in range(1, len(values)):
        rest = values[1:index] + values[index + 1:]
        for tail in pairings(rest):
            yield ((first, values[index]),) + tail


MATCHINGS = tuple(pairings(range(6)))


def validate(records=RECORDS, common_towers=8, outside_signs=(-1, 1)):
    require(tuple(records) == RECORDS, "record partition")
    require(len(MATCHINGS) == len(set(MATCHINGS)) == 15, "matching census")
    paid = set(DIRECT) | set(TRANSPORT)
    require(paid == set(RECORDS), "missing-record coverage")
    require(all(source in DIRECT for source in TRANSPORT.values()),
            "transport source coverage")
    direct_labels = set(itertools.product(DIRECT, range(15)))
    transported_labels = set(itertools.product(TRANSPORT, range(15)))
    require(direct_labels.isdisjoint(transported_labels), "label overlap")
    require(len(direct_labels) == 75 and len(transported_labels) == 30,
            "representative arithmetic")
    labels = direct_labels | transported_labels
    require(labels == set(itertools.product(RECORDS, range(15)))
            and len(labels) == 105, "raw label coverage")
    formal_rows = common_towers * len(outside_signs)
    require(common_towers == 8 and tuple(outside_signs) == (-1, 1),
            "formal row coverage")
    require(formal_rows == 16 and formal_rows * len(labels) == 1680,
            "cell11 raw census")
    return formal_rows, len(labels)


def main():
    formal_rows, labels = validate()
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req")) for row in dag["edges"]}
    require(nodes[NODE.name]["status"] == "PROVED", "DAG status")
    for parent in PARENTS:
        require(nodes[parent]["status"] == "PROVED"
                and (parent, NODE.name, "req") in edges, "parent")
    require((NODE.name, CONSUMER, "ev") in edges, "consumer")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_CELL11_COMPLETE_OUTSIDE_VERIFY_PASS "
          f"formal_rows={formal_rows} labels_per_row={labels} raw_labels=1680")


if __name__ == "__main__":
    main()
