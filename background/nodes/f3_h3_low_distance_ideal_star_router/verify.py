#!/usr/bin/env python3
"""Verify the H3 low-distance ideal-star router contract."""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_low_distance_ideal_star_router"
CONSUMER = "f3_h3_mobius_excess_half"
DEPENDENCIES = {
    "f3_h3_rich_fiber_norm_cutoff",
    "f3_h3_rich_fiber_ideal_batching",
    "f3_h3_distance_two_collision_2primary_exclusion",
}
CERTIFICATE = ROOT / "experiments/prize_resolution/h3_rich_norm_gcd_result.json"


def packing_check() -> tuple[int, int]:
    vertices = 7
    pairs = vertices * (vertices - 1) // 2
    centroid_upper = vertices * (vertices * 3)
    # Distance two is 2-primary and absent in the common odd-prime fiber.
    low_edges = (8 * pairs - centroid_upper + 3) // 4
    assert (pairs, centroid_upper, low_edges) == (21, 147, 6)

    edges = tuple(itertools.combinations(range(vertices), 2))
    minimum_max_degree = vertices
    checked = 0
    for chosen in itertools.combinations(edges, low_edges):
        degrees = [0] * vertices
        for left, right in chosen:
            degrees[left] += 1
            degrees[right] += 1
        minimum_max_degree = min(minimum_max_degree, max(degrees))
        checked += 1
    assert checked == 54_264
    assert minimum_max_degree == 2
    return low_edges, checked


def dag_check() -> tuple[int, int]:
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
    return len(DEPENDENCIES), 1


def text_check() -> None:
    base = ROOT / "background/nodes" / NODE
    statement = (base / "statement.md").read_text()
    proof = (base / "proof.md").read_text()
    assert "N(K_(E;F,G))" in statement
    assert "<= 6^(n/4)/4" in statement
    assert "168-4e<=147" in proof
    assert "matching on seven vertices has at most three" in proof


def boundary_evidence_check() -> int:
    data = json.loads(CERTIFICATE.read_text())
    order = int(data["order"])
    half = order // 2

    def vector(pair: list[int]) -> dict[int, int]:
        out: dict[int, int] = {}
        for exponent, coefficient in (
            ((pair[0] + pair[1]) % order, 1),
            (pair[0], -1),
            (pair[1], -1),
        ):
            if exponent >= half:
                exponent -= half
                coefficient = -coefficient
            out[exponent] = out.get(exponent, 0) + coefficient
        return {key: value for key, value in out.items() if value}

    def distance(left: dict[int, int], right: dict[int, int]) -> int:
        return sum(
            (left.get(key, 0) - right.get(key, 0)) ** 2
            for key in left.keys() | right.keys()
        )

    prime = int(data["prime"])
    targets = data["targets"]
    assert isinstance(targets, list) and len(targets) == 2
    for row in targets:
        pairs = row["pairs"]
        center = vector(pairs[0])
        assert all(distance(center, vector(pair)) == 6 for pair in pairs[1:])
        norms = [int(value) for value in row["norms"]]
        assert math.gcd(norms[0], norms[1]) == 4 * prime
    return len(targets)


def main() -> None:
    low_edges, graph_cases = packing_check()
    requirements, evidence = dag_check()
    text_check()
    boundary_targets = boundary_evidence_check()
    print(
        "F3_H3_LOW_DISTANCE_IDEAL_STAR_ROUTER_PASS "
        f"low_edges={low_edges} graph_cases={graph_cases} "
        f"dag={requirements}/{evidence} normalized_factor=4 "
        f"boundary_stars={boundary_targets}"
    )


if __name__ == "__main__":
    main()
