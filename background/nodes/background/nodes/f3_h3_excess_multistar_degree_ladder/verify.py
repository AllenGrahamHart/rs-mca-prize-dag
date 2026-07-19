#!/usr/bin/env python3
"""Verify the H3 excess-to-multistar degree ladder."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_excess_multistar_degree_ladder"
DEPENDENCIES = {
    "f3_h3_rich_fiber_norm_cutoff",
    "f3_h3_weighted_multistar_router",
}
CONSUMER = "f3_h3_mobius_excess_half"


def ladder(m: int) -> int:
    weight = math.ceil(m * (m - 4) / 2)
    return math.ceil(2 * weight / m)


def arithmetic_check() -> None:
    for m in range(5, 80):
        expected = m - 4 if m % 2 == 0 else m - 3
        assert ladder(m) == expected
    assert [ladder(m) for m in (8, 9, 10, 11, 12)] == [4, 6, 6, 8, 8]

    for excess in range(1, 60):
        product = 18 + excess
        possible_d = [d for d in range(3) if (product - d) % 2 == 0]
        guaranteed = min((product - d) // 2 - 1 for d in possible_d)
        assert guaranteed == 7 + math.ceil(excess / 2)
        assert ladder(guaranteed) >= (4 if excess <= 2 else 6)

    weak = []
    for product in range(19, 80):
        for diagonal in range(3):
            if (product - diagonal) % 2:
                continue
            m_lower = (product - diagonal) // 2 - 1
            if ladder(m_lower) < 6:
                weak.append((product, diagonal))
    assert weak == [(19, 1), (20, 2)]


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
    }
    assert required <= {path.name for path in base.iterdir()}
    text = (base / "statement.md").read_text() + (base / "proof.md").read_text()
    for marker in ("7+ceil(e/2)", "(19,1) or (20,2)", "m Delta>=2W"):
        assert marker in text


def main() -> None:
    arithmetic_check()
    packet_check()
    print("F3_H3_EXCESS_MULTISTAR_DEGREE_LADDER_PASS weak=19/1,20/2")


if __name__ == "__main__":
    main()
