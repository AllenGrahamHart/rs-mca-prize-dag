#!/usr/bin/env python3
"""Check the collision-free cubic missing-pair orbit router."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_collision_free_value_router"
DEPENDENCIES = {
    "l1_mersenne_hnf_order_one_color_degree_barrier",
    "l1_mersenne_hnf_m8_order_one_conic_reduction",
}
CONSUMER = "l1_mixed_petal_amplification"


def distance(pair: tuple[int, int]) -> int:
    difference = (pair[1] - pair[0]) % 8
    return min(difference, 8 - difference)


def orbit(delta: int) -> set[tuple[int, int]]:
    return {
        tuple(sorted((shift, (shift + delta) % 8)))
        for shift in range(8)
    }


def main() -> None:
    all_pairs = set(itertools.combinations(range(8), 2))
    orbits = {delta: orbit(delta) for delta in range(1, 5)}
    assert {delta: len(values) for delta, values in orbits.items()} == {
        1: 8,
        2: 8,
        3: 8,
        4: 4,
    }
    assert set().union(*orbits.values()) == all_pairs
    assert all(distance(pair) == delta for delta, values in orbits.items() for pair in values)
    for left in range(1, 5):
        for right in range(left + 1, 5):
            assert orbits[left].isdisjoint(orbits[right])

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    for dependency in DEPENDENCIES:
        assert statuses[dependency] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert statuses[CONSUMER] == "TARGET"
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / f"background/nodes/{NODE}/statement.md").read_text()
    proof = (ROOT / f"background/nodes/{NODE}/proof.md").read_text()
    for anchor in ("(CFV1)", "(CFV2)", "(CFV3)"):
        assert anchor in statement
    for anchor in ("8+8+8+4=28", "collision-free", "scaled polynomial"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_COLLISION_FREE_VALUE_ROUTER_PASS orbits=4")


if __name__ == "__main__":
    main()
