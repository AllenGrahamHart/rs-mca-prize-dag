#!/usr/bin/env python3
"""Verify the maximal-row budget-three field-degree collapse."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_maximal_field_degree_collapse"
PARENT = "rules_freeze"
CONSUMER = "rate_half_list_adjacent_crossing"
TWO_128 = 1 << 128


def v2(value: int) -> int:
    answer = 0
    while value % 2 == 0:
        value //= 2
        answer += 1
    return answer


def check_arithmetic() -> None:
    cubic = 5 * (1 << 41) + 1
    assert 3 * TWO_128 <= cubic**3 < 4 * TWO_128
    assert cubic == 10_995_116_277_761
    assert cubic % 7 == 0 and cubic > 7

    assert (4 * (1 << 41) + 1) ** 3 < 3 * TWO_128
    assert (6 * (1 << 41) + 1) ** 3 > 4 * TWO_128
    assert max(v2(e) for e in range(4, 130)) == 7
    assert 33 * 4 > 130


def check_sources() -> None:
    packet = ROOT / "background" / "nodes" / NODE
    statement = (packet / "statement.md").read_text()
    proof = (packet / "proof.md").read_text()
    audit = (packet / "audit.md").read_text()
    assert "e` is either one or two" in statement
    assert "p=+/-1 mod 2^40" in statement
    assert "5*2^41+1=10995116277761=0 mod 7" in proof
    assert "restricted to `n=2^41`" in audit


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
    check_arithmetic()
    check_sources()
    check_dag()
    print(
        "RATE_HALF_LIST_BUDGET_THREE_MAXIMAL_FIELD_DEGREE_COLLAPSE_PASS "
        "degrees=1,2 cubic_candidates=1 cubic_composite=1 dag=2/2"
    )


if __name__ == "__main__":
    main()
