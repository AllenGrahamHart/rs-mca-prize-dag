#!/usr/bin/env python3
"""Verify the H3 excess-budget/degree tradeoff packet."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_excess_budget_degree_tradeoff"
DEPENDENCIES = {
    "f3_h3_quotient_block_identity",
    "f3_h3_excess_multistar_degree_ladder",
}
CONSUMER = "f3_h3_mobius_excess_half"
PARETO = {0: (300, 4), 2: (266, 6), 6: (198, 8), 10: (130, 10), 14: (62, 12)}


def ladder(m: int) -> int:
    return m - 4 if m % 2 == 0 else m - 3


def degree(cutoff: int) -> int:
    return ladder(7 + math.ceil((cutoff + 1) / 2))


def arithmetic_check() -> None:
    for cutoff, (coefficient, expected_degree) in PARETO.items():
        assert 300 - 17 * cutoff == coefficient
        assert degree(cutoff) == expected_degree
    changes = []
    previous = None
    for cutoff in range(18):
        current = degree(cutoff)
        if current != previous:
            changes.append(cutoff)
            previous = current
    assert changes == list(PARETO)

    for n in (8, 32, 8192):
        for cutoff in range(18):
            exact = 300 * n * n - 17 * cutoff * (n - 1) * (n - 2)
            conservative = (300 - 17 * cutoff) * n * n
            assert exact == conservative + 51 * cutoff * n - 34 * cutoff
            assert exact >= conservative


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    for dependency in DEPENDENCIES:
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md", "proof.md", "claim_contract.md",
        "dependency_subdag.md", "audit.md", "result.md", "verify.py",
        "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = (base / "statement.md").read_text() + (base / "proof.md").read_text()
    for marker in ("B_E(n)=300n^2-17E(n-1)(n-2)", "E=0,2,6,10,14", "51E n-34E"):
        assert marker in text


def main() -> None:
    arithmetic_check()
    packet_check()
    print("F3_H3_EXCESS_BUDGET_DEGREE_TRADEOFF_PASS pareto=0,2,6,10,14")


if __name__ == "__main__":
    main()
