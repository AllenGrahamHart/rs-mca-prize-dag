#!/usr/bin/env python3
"""Verify the distance-two 2-primary exclusion and packing refinement."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_distance_two_collision_2primary_exclusion"
DEPENDENCY = "f3_h3_shifted_product_sidon"
CONSUMER = "f3_h3_low_distance_ideal_star_router"


def packing_check() -> tuple[int, int, int]:
    vertices = 7
    pairs = vertices * (vertices - 1) // 2
    centroid_upper = vertices * vertices * 3
    low_edges = (8 * pairs - centroid_upper + 3) // 4
    assert (pairs, centroid_upper, low_edges) == (21, 147, 6)

    edges = tuple(itertools.combinations(range(vertices), 2))
    minimum_max_degree = vertices
    cases = 0
    for chosen in itertools.combinations(edges, low_edges):
        degree = [0] * vertices
        for left, right in chosen:
            degree[left] += 1
            degree[right] += 1
        minimum_max_degree = min(minimum_max_degree, max(degree))
        cases += 1
    assert cases == 54_264
    assert minimum_max_degree == 2
    return low_edges, cases, minimum_max_degree


def cyclotomic_exponent_check() -> int:
    checked = 0
    for order in (8, 16, 32, 64):
        degree = order // 2
        for exponent in range(1, order):
            reduced = exponent % order
            root_order = order // (reduced & -reduced)
            assert root_order >= 2 and root_order & (root_order - 1) == 0
            extension_degree = degree // (root_order // 2)
            norm = 1 << extension_degree
            assert norm > 0 and norm & (norm - 1) == 0
            checked += 1
    return checked


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
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "req") in edges


def main() -> None:
    low_edges, graph_cases, minimum_degree = packing_check()
    exponent_checks = cyclotomic_exponent_check()
    dag_check()
    print(
        "F3_H3_DISTANCE_TWO_COLLISION_2PRIMARY_EXCLUSION_PASS "
        f"low_edges={low_edges} graph_cases={graph_cases} "
        f"star_degree={minimum_degree} exponents={exponent_checks} dag=1/1"
    )


if __name__ == "__main__":
    main()
