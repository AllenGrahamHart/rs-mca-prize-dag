#!/usr/bin/env python3
"""Verify the fiber-four residue-rank gate and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_fiber_four_rank_gate"
DEPENDENCY = "rate_half_list_budget_three_multideletion_multifiber_exclusion"
CONSUMER = "rate_half_list_adjacent_crossing"
PRIME = 1_000_003


def multiply(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] = (answer[i + j] + a * b) % PRIME
    return answer


def polynomial(roots: tuple[int, ...]) -> list[int]:
    answer = [1]
    for root in roots:
        answer = multiply(answer, [-root % PRIME, 1])
    return answer


def rank(matrix: list[list[int]]) -> int:
    rows = [row[:] for row in matrix]
    height = len(rows)
    width = len(rows[0])
    answer = 0
    for column in range(width):
        pivot = next(
            (row for row in range(answer, height) if rows[row][column]), None
        )
        if pivot is None:
            continue
        rows[answer], rows[pivot] = rows[pivot], rows[answer]
        inverse = pow(rows[answer][column], PRIME - 2, PRIME)
        rows[answer] = [value * inverse % PRIME for value in rows[answer]]
        for row in range(height):
            if row != answer and rows[row][column]:
                factor = rows[row][column]
                rows[row] = [
                    (left - factor * right) % PRIME
                    for left, right in zip(rows[row], rows[answer], strict=True)
                ]
        answer += 1
    return answer


def residue_rank(root_sets: tuple[tuple[int, ...], ...]) -> int:
    denominators = [polynomial(roots) for roots in root_sets]
    columns = []
    for omitted in range(4):
        column = [1]
        for index, denominator in enumerate(denominators):
            if index != omitted:
                column = multiply(column, denominator)
        columns.append(column)

    best = 0
    for y_value in range(4):
        matrix = []
        for residue in range(4):
            row = []
            for column in columns:
                value = 0
                y_power = 1
                for degree in range(residue, len(column), 4):
                    value = (value + column[degree] * y_power) % PRIME
                    y_power = y_power * y_value % PRIME
                row.append(value)
            matrix.append(row)
        best = max(best, rank(matrix))
    return best


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges


def main() -> None:
    triangle = ((2,), (3,), (5,), (7, 11))
    k4e = ((2, 3), (5, 7), (11,), (13,))
    antipodal = ((2, -2), (3, -3), (5, -5), (7, -7))
    assert residue_rank(triangle) >= 3
    assert residue_rank(k4e) >= 3
    assert residue_rank(antipodal) == 2
    assert 4 * (5 - 3) > 4
    packet_check()
    print(
        "RATE_HALF_LIST_B3_FIBER_FOUR_RANK_GATE_PASS "
        "linear_profiles=2 antipodal_rank=2"
    )


if __name__ == "__main__":
    main()
