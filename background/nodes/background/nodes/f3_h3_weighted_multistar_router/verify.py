#!/usr/bin/env python3
"""Verify the weighted H3 multistar theorem packet and arithmetic."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_weighted_multistar_router"
DEPENDENCIES = {
    "f3_h3_rich_fiber_norm_cutoff",
    "f3_h3_rich_fiber_ideal_batching",
    "f3_h3_distance_two_collision_2primary_exclusion",
}
CONSUMER = "f3_h3_mobius_excess_half"


def arithmetic_check() -> None:
    feasible = []
    for distance_four in range(22):
        for distance_six in range(22 - distance_four):
            lower_sum = (
                4 * distance_four
                + 6 * distance_six
                + 8 * (21 - distance_four - distance_six)
            )
            if lower_sum <= 147:
                weight = 2 * distance_four + distance_six
                assert weight >= 11
                feasible.append((distance_four, distance_six, weight))
    assert feasible
    assert min(weight for _, _, weight in feasible) == 11
    assert 2 * 11 > 7 * 3


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
        "statement.md",
        "proof.md",
        "claim_contract.md",
        "dependency_subdag.md",
        "audit.md",
        "result.md",
        "verify.py",
        "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    statement = (base / "statement.md").read_text()
    proof = (base / "proof.md").read_text()
    for marker in ("2a+b>=11", "weighted degree at least four", "fixed-root sieve"):
        assert marker in statement + proof


def main() -> None:
    arithmetic_check()
    packet_check()
    print("F3_H3_WEIGHTED_MULTISTAR_ROUTER_VERIFY_PASS min_weight=11 center_weight=4")


if __name__ == "__main__":
    main()
