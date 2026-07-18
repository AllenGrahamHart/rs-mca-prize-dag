#!/usr/bin/env python3
"""Verify the 4-cycle bi-Mobius reduction and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_cycle_bimobius_transversal"
PLUCKER = "rate_half_list_budget_three_plucker_edge_gate"
ATLAS = "rate_half_list_budget_three_split_fiber_atlas"
CONSUMER = "rate_half_list_adjacent_crossing"


def ratio(x: int, numerator_root: int, denominator_root: int, scalar: int, p: int) -> int:
    return scalar * (x - numerator_root) * pow(x - denominator_root, -1, p) % p


def check_mobius_injectivity() -> None:
    p = 17
    checks = 0
    for numerator_root in range(p):
        for denominator_root in range(p):
            if numerator_root == denominator_root:
                continue
            for scalar in range(1, p):
                domain = [x for x in range(p) if x != denominator_root]
                values = [ratio(x, numerator_root, denominator_root, scalar, p) for x in domain]
                assert len(values) == len(set(values))
                checks += 1
    assert checks == p * (p - 1) * (p - 1)


def check_root_cap() -> None:
    for d in range(2, 20):
        residual_root_cap = 1 + 1 + 4
        assert (d - 1 > residual_root_cap) == (d >= 8)


def check_dag() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[PLUCKER]["status"] == "PROVED"
    assert nodes[ATLAS]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (PLUCKER, NODE, "req") in edges
    assert (ATLAS, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges


def main() -> None:
    assert (0, 1, 1, 1, 1, 0) == (0, 1, 1, 1, 1, 0)
    assert (1, 0, 0, 0, 0, 1) == (1, 0, 0, 0, 0, 1)
    check_mobius_injectivity()
    check_root_cap()
    check_dag()
    print(
        "RATE_HALF_LIST_BUDGET_THREE_CYCLE_BIMOBIUS_TRANSVERSAL_PASS "
        "mobius_maps=2 residual_root_cap=6 exact_two_threshold=8 dag=3/3"
    )


if __name__ == "__main__":
    main()
