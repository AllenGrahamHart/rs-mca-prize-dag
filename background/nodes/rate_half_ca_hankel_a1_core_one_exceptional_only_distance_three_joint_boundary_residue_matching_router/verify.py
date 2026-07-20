#!/usr/bin/env python3
"""Verify the joint boundary/residue label involution."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


NODE = (
    "rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_"
    "joint_boundary_residue_matching_router"
)
DEPS = {
    "rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_"
    "matching_free_boundary_power_router",
    "rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_"
    "dual_row_product_power_router",
}


def involution(label: tuple[int, int], prime: int, mu: int, order: int) -> tuple[int, int]:
    y, residue = label
    return (-y % prime, (mu - residue) % order)


def invariant(labels: list[tuple[int, int]], prime: int, mu: int, order: int) -> bool:
    counts = Counter(labels)
    return all(
        count == counts[involution(label, prime, mu, order)]
        for label, count in counts.items()
    )


def main() -> None:
    # A nontrivial quotient-group fixture: 449-1 is divisible by 7.
    prime = 449
    quotient_order = 7
    mu = 5
    seeds = [(11, 0), (23, 2), (71, 6)]
    labels = []
    for seed in seeds:
        labels.extend([seed, involution(seed, prime, mu, quotient_order)])

    assert invariant(labels, prime, mu, quotient_order)
    assert all(
        involution(involution(label, prime, mu, quotient_order), prime, mu, quotient_order)
        == label
        for label in labels
    )
    assert all(involution(label, prime, mu, quotient_order) != label for label in labels)

    residue_product = sum(residue for _, residue in labels) % quotient_order
    assert residue_product == len(seeds) * mu % quotient_order

    mutated = labels.copy()
    y, residue = mutated[-1]
    mutated[-1] = (y, (residue + 1) % quotient_order)
    assert not invariant(mutated, prime, mu, quotient_order)
    assert sum(residue for _, residue in mutated) % quotient_order != residue_product

    # When the r-th power map is surjective, only central symmetry remains.
    trivial = [(5, 0), (-5 % 17, 0)]
    assert invariant(trivial, 17, 0, 1)

    root = Path(__file__).resolve().parents[3]
    dag = json.loads((root / "dag.json").read_text())
    node = next(item for item in dag["nodes"] if item["id"] == NODE)
    assert node["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    for dep in DEPS:
        assert (dep, NODE, "req") in edges
    assert (NODE, "rate_half_band_closure", "ev") in edges

    print(
        "RATE_HALF_DISTANCE_THREE_JOINT_BOUNDARY_RESIDUE_MATCHING_PASS "
        f"labels={len(labels)} quotient_order={quotient_order} mutations=2"
    )


if __name__ == "__main__":
    main()
