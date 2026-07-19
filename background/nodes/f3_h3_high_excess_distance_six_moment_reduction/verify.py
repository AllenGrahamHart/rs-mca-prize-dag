#!/usr/bin/env python3
"""Verify the H3 high-excess distance-six moment reduction."""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_high_excess_distance_six_moment_reduction"
DEPENDENCIES = {
    "f3_h3_distance_four_fiber_degree_cap",
    "f3_h3_excess_budget_degree_tradeoff",
}
CONSUMER = "f3_h3_mobius_excess_half"


def lower_distance_six(excess: int) -> tuple[int, int, int, int]:
    small = 7 + math.ceil(excess / 2)
    weight = math.ceil(small * (small - 2) / 2)
    distance_four = 2 * (small - 1)
    return small, weight, distance_four, weight - 2 * distance_four


def arithmetic_check() -> None:
    ratios = []
    for excess in range(15, 10_000):
        small, weight, distance_four, distance_six = lower_distance_six(excess)
        assert distance_six > 0
        ratios.append((Fraction(excess, distance_six), excess, small, weight, distance_four))
    assert max(ratios) == (Fraction(8, 21), 16, 15, 98, 28)
    assert Fraction(21 * 62, 136) == Fraction(651, 68)
    assert Fraction(651, 68) < Fraction(9574, 1000)


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
    for marker in ("P(t)-18 <=(8/21)N_6(t)", "136 M_6,33", "651/68"):
        assert marker in text


def main() -> None:
    arithmetic_check()
    packet_check()
    print("F3_H3_HIGH_EXCESS_DISTANCE_SIX_MOMENT_PASS ratio=8/21 excess=16")


if __name__ == "__main__":
    main()
