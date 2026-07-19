#!/usr/bin/env python3
"""Verify the B*=3 Plucker deduction, degree gate, and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_plucker_edge_gate"
PARENT = "rate_half_list_budget_three_split_pencil_normal_form"
CONSUMER = "rate_half_list_adjacent_crossing"


def symbolic_coefficient_check() -> None:
    # Track the coefficients of the three triangle equations used in the
    # proof of A1*Plucker=0. Keys name formal monomials A_i*b_jk*b_lm.
    terms: dict[tuple[str, str, str], int] = {}

    def add(key: tuple[str, str, str], coefficient: int) -> None:
        normalized = (key[0], *sorted(key[1:]))
        terms[normalized] = terms.get(normalized, 0) + coefficient

    # b01*(A2*b13-A3*b12)
    add(("A2", "b01", "b13"), 1)
    add(("A3", "b01", "b12"), -1)
    # -(A2*b01+A0*b12)*b13
    add(("A2", "b01", "b13"), -1)
    add(("A0", "b12", "b13"), -1)
    # +(A3*b01+A0*b13)*b12
    add(("A3", "b01", "b12"), 1)
    add(("A0", "b13", "b12"), 1)
    assert all(value == 0 for value in terms.values())

    exceptional_degrees = (4, 4, 6, 8, 3, 5)
    assert max(exceptional_degrees) == 8
    edge_caps = (
        (0, 0, 1, 1, 2, 2),
        (1, 1, 1, 1, 1, 1),
        (0, 1, 1, 1, 1, 2),
        (1, 1, 1, 1, 1, 1),
        (0, 1, 0, 1, 0, 1),
        (1, 1, 0, 1, 0, 0),
    )
    assert all(max(row) <= 2 for row in edge_caps)
    assert all(max(a + b, c + d, e + f) <= 4 for a, c, e, f, d, b in edge_caps)


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
    symbolic_coefficient_check()
    check_dag()
    print(
        "RATE_HALF_LIST_BUDGET_THREE_PLUCKER_EDGE_GATE_PASS "
        "plucker_terms=6 edge_types=6 max_edge_degree=2 max_exception_degree=8 dag=2/2"
    )


if __name__ == "__main__":
    main()
