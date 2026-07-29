#!/usr/bin/env python3
"""Check the cubic three-color orbit router and DAG wiring."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_color_remainder_router"
DEPENDENCIES = {
    "l1_mersenne_hnf_m8_order_one_cubic_two_triple_exclusion",
    "l1_mersenne_hnf_m8_order_one_conic_reduction",
}
CONSUMER = "l1_mixed_petal_amplification"
REPRESENTATIVES = (
    (0, 1, 2),
    (0, 1, 3),
    (0, 1, 4),
    (0, 1, 5),
    (0, 1, 6),
    (0, 2, 4),
    (0, 2, 5),
)


def orbit(subset: tuple[int, int, int]) -> set[tuple[int, int, int]]:
    return {
        tuple(sorted((value + shift) % 8 for value in subset))
        for shift in range(8)
    }


def main() -> None:
    all_subsets = set(itertools.combinations(range(8), 3))
    orbits = [orbit(representative) for representative in REPRESENTATIVES]
    assert all(len(current) == 8 for current in orbits)
    assert sum(len(current) for current in orbits) == 56
    assert set().union(*orbits) == all_subsets
    for left_index, left in enumerate(orbits):
        for right in orbits[left_index + 1 :]:
            assert left.isdisjoint(right)

    profiles = {
        tuple(sorted(parts, reverse=True))
        for parts in itertools.product(range(1, 4), repeat=3)
        if sum(parts) == 6
    }
    assert profiles == {(3, 2, 1), (2, 2, 2)}

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
    for anchor in ("(TCR1)", "(TCR4)", "(TCR5)"):
        assert anchor in statement
    for anchor in ("56", "seven", "3+2+1", "2+2+2"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_THREE_COLOR_REMAINDER_ROUTER_PASS orbits=7")


if __name__ == "__main__":
    main()
