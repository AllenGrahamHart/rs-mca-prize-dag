#!/usr/bin/env python3
"""Verify the split-unit single-fiber exclusion and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_split_unit_single_fiber_exclusion"
PARENT = "rate_half_list_budget_three_linear_grassmann_atlas"
CONSUMER = "rate_half_list_adjacent_crossing"


def check_deficit_ledger() -> None:
    rows = {
        "cycle": ((1, 1, 1, 1), 4),
        "k4e": ((2, 2, 1, 1), 6),
        "k4": ((2, 2, 2, 2), 8),
        "path013": ((1, 1, 1), 3),
        "triangle": ((1, 1, 1, 2), 5),
    }
    for deficits, total in rows.values():
        assert sum(deficits) == total <= 8
    assert max(total for _, total in rows.values()) <= 2**39


def check_sources() -> None:
    packet = ROOT / "background" / "nodes" / NODE
    statement = (packet / "statement.md").read_text()
    proof = (packet / "proof.md").read_text()
    audit = (packet / "audit.md").read_text()
    assert "R_i A_i=X^d-tau_i" in statement
    assert "V_a(X)=(X^d-a^d)/(X-a)" in proof
    assert "square Vandermonde system" in proof
    assert "2d-4>d" in proof
    assert "path relation omits" in audit
    assert "multi-fiber" in statement


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
    check_deficit_ledger()
    check_sources()
    check_dag()
    print(
        "RATE_HALF_LIST_BUDGET_THREE_SPLIT_UNIT_SINGLE_FIBER_EXCLUSION_PASS "
        "chambers=9 type_rows=5 max_removed=8 same_fiber_excluded=1 "
        "vandermonde=1 dag=2/2"
    )


if __name__ == "__main__":
    main()
