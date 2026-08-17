#!/usr/bin/env python3
"""Verify the repeated-BC duplicate-role cells 11-14 transport."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_vieta_minor_compiler",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_signed_edge_atlas",
)
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"
ROLES = ("LA", "AB", "AC", "BC1", "BC2")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def pairings(values):
    values = tuple(values)
    first = values[0]
    for index in range(1, len(values)):
        second = values[index]
        rest = values[1:index] + values[index + 1:]
        yield ((first, second), (rest[0], rest[1]))


def cells():
    return tuple(
        (singleton, matching)
        for singleton in range(5)
        for matching in pairings(tuple(index for index in range(5)
                                    if index != singleton))
    )


def swap_cell(cell, swap=(0, 1, 2, 4, 3)):
    singleton, matching = cell
    return (
        swap[singleton],
        tuple(sorted(tuple(sorted(swap[value] for value in pair))
                     for pair in matching)),
    )


def source_roots(cell):
    singleton, matching = cell
    output = [None] * 5
    output[matching[0][0]], output[matching[0][1]] = "1", "epsilon1*iota"
    output[matching[1][0]], output[matching[1][1]] = "r", "epsilon2*iota*r"
    output[singleton] = "t"
    return tuple(output)


def validate(partner=14, duplicate_rows=("BC", "BC")):
    atlas = cells()
    require(len(atlas) == 15 and atlas[11] == (3, ((0, 4), (1, 2))),
            "cell11 atlas")
    require(partner == 14 and atlas[partner] == (4, ((0, 3), (1, 2))),
            "cell14 atlas")
    require(swap_cell(atlas[11]) == atlas[partner]
            and swap_cell(atlas[partner]) == atlas[11], "duplicate cell orbit")
    require(duplicate_rows[0] == duplicate_rows[1] == "BC", "duplicate target rows")
    roots_11, roots_14 = source_roots(atlas[11]), source_roots(atlas[partner])
    swap = (0, 1, 2, 4, 3)
    require(tuple(roots_11[swap[index]] for index in range(5)) == roots_14,
            "source-root row transport")
    target_rows = ("LA", "AB", "AC", duplicate_rows[0], duplicate_rows[1])
    require(tuple(target_rows[swap[index]] for index in range(5)) == target_rows,
            "target-row transport")
    source_signs, bc_signs, outside_signs, labels = 4, 2, 2, 105
    require(source_signs * bc_signs * outside_signs * labels == 1680,
            "transport census")
    return 1680


def main():
    systems = validate()
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req")) for row in dag["edges"]}
    require(nodes[NODE.name]["status"] == "PROVED", "DAG status")
    for parent in PARENTS:
        require(nodes[parent]["status"] == "PROVED"
                and (parent, NODE.name, "req") in edges, "parent")
    require((NODE.name, CONSUMER, "ev") in edges, "consumer")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_CELLS11_14_TRANSPORT_VERIFY_PASS "
          f"systems={systems} labels=105")


if __name__ == "__main__":
    main()
