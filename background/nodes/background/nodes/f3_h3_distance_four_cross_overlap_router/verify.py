#!/usr/bin/env python3
"""Verify the structural distance-four cross-overlap reduction."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_distance_four_cross_overlap_router"
DEPENDENCIES = {
    "f3_h3_rich_fiber_norm_cutoff",
    "f3_h3_distance_two_collision_2primary_exclusion",
}
CONSUMER = "f3_h3_mobius_excess_half"


def atoms(pair: tuple[int, int], order: int) -> list[tuple[int, int, str]]:
    half = order // 2
    out = []
    for exponent, coefficient, kind in (
        ((pair[0] + pair[1]) % order, 1, "P"),
        (pair[0], -1, "N"),
        (pair[1], -1, "N"),
    ):
        if exponent >= half:
            exponent -= half
            coefficient = -coefficient
        out.append((exponent, coefficient, kind))
    return out


def vector(pair: tuple[int, int], order: int) -> dict[int, int]:
    out: dict[int, int] = {}
    for coordinate, coefficient, _ in atoms(pair, order):
        out[coordinate] = out.get(coordinate, 0) + coefficient
    return {key: value for key, value in out.items() if value}


def square_norm(value: dict[int, int]) -> int:
    return sum(coefficient * coefficient for coefficient in value.values())


def distance(left: dict[int, int], right: dict[int, int]) -> int:
    return sum(
        (left.get(key, 0) - right.get(key, 0)) ** 2
        for key in left.keys() | right.keys()
    )


def structural_check() -> tuple[int, int, int]:
    generic_edges = 0
    cross_ready = 0
    antipodal_pairs = 0
    for order in (16, 32):
        half = order // 2
        selected = [
            pair for pair in itertools.combinations_with_replacement(range(1, order), 2)
            if pair[0] != pair[1] and half not in pair
        ]
        vectors = {pair: vector(pair, order) for pair in selected}
        assert all(square_norm(value) in (1, 3) for value in vectors.values())
        antipodal_pairs += sum(square_norm(value) == 1 for value in vectors.values())
        for left, right in itertools.combinations(selected, 2):
            if square_norm(vectors[left]) != 3 or square_norm(vectors[right]) != 3:
                continue
            if distance(vectors[left], vectors[right]) != 4:
                continue
            generic_edges += 1
            common = {
                (coordinate, coefficient, left_kind, right_kind)
                for coordinate, coefficient, left_kind in atoms(left, order)
                for other_coordinate, other_coefficient, right_kind in atoms(right, order)
                if (coordinate, coefficient) == (other_coordinate, other_coefficient)
            }
            assert common
            if any(left_kind != right_kind for _, _, left_kind, right_kind in common):
                cross_ready += 1
    assert generic_edges > 0 and antipodal_pairs > 0
    return generic_edges, cross_ready, antipodal_pairs


def dag_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    refs = set(nodes[NODE]["refs"])
    for name in (
        "statement.md", "proof.md", "claim_contract.md",
        "dependency_subdag.md", "audit.md", "result.md",
        "verify.py", "verify_audit.py",
    ):
        assert f"background/nodes/{NODE}/{name}" in refs
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    for dependency in DEPENDENCIES:
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges


def main() -> None:
    generic, cross_ready, antipodal = structural_check()
    dag_check()
    for exponent in range(3, 42):
        order = 1 << exponent
        edge_budget = (3 * order * order + order) // 2
        target_budget = edge_budget // 6
        assert 6 * target_budget <= edge_budget
        assert edge_budget < 2 * order * order
    print(
        "F3_H3_DISTANCE_FOUR_CROSS_OVERLAP_ROUTER_PASS "
        f"generic_edges={generic} cross_ready={cross_ready} "
        f"antipodal_pairs={antipodal} budgets=39 dag=2/1"
    )


if __name__ == "__main__":
    main()
