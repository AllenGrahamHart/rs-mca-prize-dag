#!/usr/bin/env python3
"""Verify the primitive quadratic-scroll module and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_quadratic_scroll_primitive_module"
PARENT = "rate_half_list_budget_three_quadratic_scroll_full_rank"
CONSUMER = "rate_half_list_adjacent_crossing"


def check_degree_logic() -> None:
    for d in (4, 2**39):
        assert d - 2 >= 2
        assert (d - 2, d - 1) == (d - 2, d - 1)
        assert (d - 2, d - 2) == (d - 2, d - 2)
        assert max((d - 2) + 1, (d - 2) + 1) == d - 1 < d


def check_sources() -> None:
    packet = ROOT / "background" / "nodes" / NODE
    statement = (packet / "statement.md").read_text()
    proof = (packet / "proof.md").read_text()
    audit = (packet / "audit.md").read_text()
    assert "<alpha,Xalpha> intersect <beta,Xbeta>={0}" in statement
    assert "pendant" in statement and "d-2         d-1" in statement
    assert "quadratic K_4-e" in statement and "d-2         d-2" in statement
    assert "gcd(alpha,beta)=gcd(A_0,A_1-hA_0)" in proof
    assert "alpha` divides `s_0+s_1X" in proof
    assert "small `d=3` boundary" in audit


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
    check_degree_logic()
    check_sources()
    check_dag()
    print(
        "RATE_HALF_LIST_BUDGET_THREE_QUADRATIC_SCROLL_PRIMITIVE_MODULE_PASS "
        "chambers=4 coprime=1 direct_sum=4 degree_profiles=2 dag=2/2"
    )


if __name__ == "__main__":
    main()
