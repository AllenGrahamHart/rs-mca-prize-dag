#!/usr/bin/env python3
"""Verify the residual transversal atlas and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_residual_transversal_atlas"
ATLAS = "rate_half_list_budget_three_split_fiber_atlas"
PLUCKER = "rate_half_list_budget_three_plucker_edge_gate"
PATH = "rate_half_list_budget_three_path_mobius_transversal"
CONSUMER = "rate_half_list_adjacent_crossing"

# name, multiplicity, member-degree offset, transversal cap, exceptional cap,
# first d for which member degree exceeds the residual cap.
PENCILS = (
    ("pendant", 1, -1, 2, 3, 7),
    ("K_4-e", 2, -1, 2, 4, 8),
    ("K_4", 4, -1, 2, 5, 9),
    ("triangle+singleton:d", 1, 0, 1, 2, 4),
    ("triangle+singleton:d-1", 3, -1, 1, 4, 7),
)

DENSE_BASE = (
    ("K_4-e", -2, 1, 1, 6, 11),
    ("K_4", -2, 1, 1, 8, 13),
)


def ratio(x: int, roots_n: tuple[int, ...], roots_d: tuple[int, ...], p: int) -> int:
    numerator = 1
    denominator = 1
    for root in roots_n:
        numerator = numerator * (x - root) % p
    for root in roots_d:
        denominator = denominator * (x - root) % p
    return numerator * pow(denominator, -1, p) % p


def check_transversal_fibers() -> None:
    p = 101
    mobius = [ratio(x, (2,), (3,), p) for x in range(p) if x != 3]
    assert len(mobius) == len(set(mobius)) == p - 1

    domain = [x for x in range(p) if x not in (5, 7)]
    cross_ratio = [ratio(x, (2, 3), (5, 7), p) for x in domain]
    multiplicities = {value: cross_ratio.count(value) for value in set(cross_ratio)}
    assert max(multiplicities.values()) <= 2


def check_caps() -> None:
    assert sum(row[1] for row in PENCILS) == 11
    assert sum(row[1] for row in PENCILS) + 2 == 13
    for _, _, offset, transversal, exceptional, threshold in PENCILS:
        cap = transversal + exceptional
        for d in range(2, 20):
            assert (d + offset > cap) == (d >= threshold)
    for _, offset, first_graph, second_graph, exceptional, threshold in DENSE_BASE:
        cap = first_graph + second_graph + exceptional
        for d in range(2, 20):
            assert (d + offset > cap) == (d >= threshold)
    assert 2**39 >= max(row[-1] for row in PENCILS + DENSE_BASE)


def check_sources() -> None:
    packet = ROOT / "background" / "nodes" / NODE
    statement = (packet / "statement.md").read_text()
    proof = (packet / "proof.md").read_text()
    assert "all thirteen" in statement
    assert "simultaneous coupling" in statement
    assert "b_13/(b_03 e_12)" in statement
    assert "d>=13" in statement
    assert "It cannot be constant" in proof


def check_dag() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    for parent in (ATLAS, PLUCKER, PATH):
        assert nodes[parent]["status"] == "PROVED"
        assert (parent, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges


def main() -> None:
    check_transversal_fibers()
    check_caps()
    check_sources()
    check_dag()
    print(
        "RATE_HALF_LIST_BUDGET_THREE_RESIDUAL_TRANSVERSAL_ATLAS_PASS "
        "new_exact_three=11 total_exact_three=13 dense_exact_two=2 "
        "max_threshold=13 dag=4/4"
    )


if __name__ == "__main__":
    main()
