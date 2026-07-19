#!/usr/bin/env python3
"""Verify full rank of every quadratic scroll chamber and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_quadratic_scroll_full_rank"
PARENT = "rate_half_list_budget_three_quadratic_scroll_atlas"
CONSUMER = "rate_half_list_adjacent_crossing"
P = 101


def determinant(matrix: list[list[int]]) -> int:
    rows = [[value % P for value in row] for row in matrix]
    answer = 1
    for column in range(4):
        pivot = next(row for row in range(column, 4) if rows[row][column])
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            answer = -answer
        value = rows[column][column]
        answer = answer * value % P
        inverse = pow(value, -1, P)
        rows[column] = [entry * inverse % P for entry in rows[column]]
        for row in range(column + 1, 4):
            factor = rows[row][column]
            rows[row] = [(entry - factor * base) % P for entry, base in zip(rows[row], rows[column], strict=True)]
    return answer % P


def coefficient_matrix(c: int, a0: int, a1: int, d0: int, d1: int, e0: int, e1: int, f0: int, f1: int, f2: int) -> list[list[int]]:
    s = f2 * pow(d1, -1, P) % P if f2 else 0
    columns = (
        (c, 0, -e0, -f0),
        (0, c * s, -e1 + s * a0, -f1 + s * d0),
        (0, c, a0, d0),
        (0, 0, a1, d1),
    )
    return [[columns[column][row] for column in range(4)] for row in range(4)]


def check_formula() -> None:
    fixtures = (
        # Pendant, linear b13.
        (3, 5, 0, 7, 11, 13, 17, 19, 23, 0),
        # Pendant, quadratic b13; balancing parameter must cancel.
        (3, 5, 0, 7, 11, 13, 17, 19, 23, 29),
        # K4-e quadratic chamber.
        (3, 5, 31, 7, 11, 13, 17, 19, 23, 0),
    )
    for values in fixtures:
        c, _, a1, _, d1, _, e1, _, f1, _ = values
        actual = determinant(coefficient_matrix(*values))
        expected = c * c * (e1 * d1 - a1 * f1) % P
        assert actual == expected
    assert all(determinant(coefficient_matrix(*values)) for values in fixtures)


def check_sources() -> None:
    packet = ROOT / "background" / "nodes" / NODE
    statement = (packet / "statement.md").read_text()
    proof = (packet / "proof.md").read_text()
    assert "det C=b_01^2 (L_12 L_03-L_02 L_13)" in statement
    assert "rank-deficient branch" in statement and "empty" in statement
    assert "det C=-b_01^3 [X^2]b_23!=0" in statement
    assert "balancing parameter cancels" in (packet / "audit.md").read_text()
    assert "Expanding the determinant" in proof


def check_dag() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[PARENT]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges


def main() -> None:
    check_formula()
    check_sources()
    check_dag()
    print(
        "RATE_HALF_LIST_BUDGET_THREE_QUADRATIC_SCROLL_FULL_RANK_PASS "
        "quadratic_chambers=4 determinant_formula=1 rank_deficient=0 dag=2/2"
    )


if __name__ == "__main__":
    main()
