#!/usr/bin/env python3
"""Verify the H3 high-excess low-distance moment reduction."""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_high_excess_low_distance_moment_reduction"
DEPENDENCIES = {
    "f3_h3_excess_multistar_degree_ladder",
    "f3_h3_excess_budget_degree_tradeoff",
}
CONSUMER = "f3_h3_mobius_excess_half"


def minimum_weight(excess: int) -> int:
    small = 7 + math.ceil(excess / 2)
    return math.ceil(small * (small - 4) / 2)


def arithmetic_check() -> None:
    ratios = [(Fraction(excess, minimum_weight(excess)), excess) for excess in range(15, 10_000)]
    ratio, excess = max(ratios)
    assert (ratio, excess, minimum_weight(excess)) == (Fraction(16, 83), 16, 83)
    assert Fraction(83 * 62, 272) == Fraction(2573, 136)
    assert Fraction(2573, 136) < 19
    for n in (32, 8192, 1 << 41):
        budget = 300 * n * n - 238 * (n - 1) * (n - 2)
        assert budget > 62 * n * n
        assert 83 * budget // 272 >= 0


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
    for marker in ("P(t)-18 <= (16/83) W(t)", "272 M_33", "2573/136"):
        assert marker in text


def main() -> None:
    arithmetic_check()
    packet_check()
    print("F3_H3_HIGH_EXCESS_LOW_DISTANCE_MOMENT_PASS ratio=16/83 excess=16")


if __name__ == "__main__":
    main()
