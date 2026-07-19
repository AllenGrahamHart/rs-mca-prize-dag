#!/usr/bin/env python3
"""Verify the H3 low-distance exceptional-prime router and DAG wiring."""

from __future__ import annotations

import collections
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_low_distance_exceptional_prime_router"
PARENT = "f3_h3_rich_fiber_norm_cutoff"
CONSUMER = "f3_h3_mobius_excess_half"


def vector(order: int, pair: tuple[int, int]) -> dict[int, int]:
    half = order // 2
    out: collections.Counter[int] = collections.Counter()
    left, right = pair
    for exponent, coefficient in (
        ((left + right) % order, 1),
        (left, -1),
        (right, -1),
    ):
        if exponent >= half:
            exponent -= half
            coefficient = -coefficient
        out[exponent] += coefficient
    return {key: value for key, value in out.items() if value}


def distance(left: dict[int, int], right: dict[int, int]) -> int:
    return sum(
        (left.get(key, 0) - right.get(key, 0)) ** 2
        for key in left.keys() | right.keys()
    )


def dilate(order: int, pair: tuple[int, int], multiplier: int) -> tuple[int, int]:
    values = tuple(sorted((pair[0] * multiplier % order, pair[1] * multiplier % order)))
    assert values[0] != 0
    return values


def check_orbit_invariance() -> tuple[int, int]:
    comparisons = 0
    boundary = 0
    for order in (8, 16, 32):
        pairs = list(itertools.combinations_with_replacement(range(1, order), 2))
        vectors = {pair: vector(order, pair) for pair in pairs}
        for left, right in itertools.combinations(pairs, 2):
            base = distance(vectors[left], vectors[right])
            boundary += base == 6
            for multiplier in range(1, order, 2):
                moved_left = dilate(order, left, multiplier)
                moved_right = dilate(order, right, multiplier)
                assert distance(vectors[moved_left], vectors[moved_right]) == base
                comparisons += 1
    assert boundary > 0
    return comparisons, boundary


def check_packing_constants() -> None:
    unordered_representations = (19 + 1) // 2
    low_vectors = unordered_representations - 3
    pair_count = low_vectors * (low_vectors - 1) // 2
    assert unordered_representations == 10
    assert low_vectors == 7
    assert pair_count * 8 > low_vectors * (low_vectors * 3)
    assert pair_count * 6 <= low_vectors * (low_vectors * 3)


def check_orbit_growth_fence() -> int:
    official_lower_bounds = []
    for exponent in range(13, 42):
        order = 1 << exponent
        half = order // 2
        width = (half - 1) // 2
        family = width * (width - 1) // 2
        overlaps = 9 * width
        pair_pairs = family * (family - 1 - overlaps) // 2
        assert pair_pairs > 0
        orbit_lower_bound = (pair_pairs + half - 1) // half
        official_lower_bounds.append(orbit_lower_bound)
    assert official_lower_bounds[0] == 530_590_075
    assert all(left < right for left, right in zip(official_lower_bounds, official_lower_bounds[1:]))
    return official_lower_bounds[0]


def check_sources_and_dag() -> None:
    packet = ROOT / "background" / "nodes" / NODE
    statement = (packet / "statement.md").read_text()
    proof = (packet / "proof.md").read_text()
    audit = (packet / "audit.md").read_text()
    assert "||v_E-v_F||_2^2<=6" in statement
    assert "ceil(P(t)/2)>=10" in proof
    assert "Candidate prime factors" in audit

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[PARENT]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges


def main() -> None:
    comparisons, boundary = check_orbit_invariance()
    check_packing_constants()
    first_orbit_floor = check_orbit_growth_fence()
    check_sources_and_dag()
    print(
        "F3_H3_LOW_DISTANCE_EXCEPTIONAL_PRIME_ROUTER_PASS "
        f"orbit_distance_checks={comparisons} boundary6={boundary} "
        f"packing=10to7 n8192_orbit_floor={first_orbit_floor} "
        "candidate_union=finite dag=2/2"
    )


if __name__ == "__main__":
    main()
