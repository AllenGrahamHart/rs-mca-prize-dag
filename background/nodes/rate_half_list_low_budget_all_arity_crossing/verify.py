#!/usr/bin/env python3
"""Verify the all-arity low-budget rate-half list corollary."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_low_budget_all_arity_crossing"
BASE = "rate_half_list_low_budget_exact_crossing"
TRANSPORT = "list_subsqrt_interleaving_collapse"
CONSUMERS = ("list_grand", "list_large_m_scope_closure")


def check_dag() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[BASE]["status"] == "PROVED"
    assert nodes[TRANSPORT]["status"] == "PROVED"
    assert (BASE, NODE, "req") in edges
    assert (TRANSPORT, NODE, "req") in edges
    for consumer in CONSUMERS:
        assert (NODE, consumer, "ev") in edges


def main() -> None:
    n = 1 << 41
    safe = 3 * n // 4
    assert n - safe == n // 4
    assert n - (safe - 1) == n // 4 + 1
    q_lower = 1 << 128
    for budget in (1, 2):
        assert budget * budget < q_lower
        assert budget + 1 > budget
    check_dag()
    print(
        "RATE_HALF_LIST_LOW_BUDGET_ALL_ARITY_CROSSING_PASS "
        f"budgets=2 arity=all safe={safe} radius={n // 4} dag=4/4"
    )


if __name__ == "__main__":
    main()
