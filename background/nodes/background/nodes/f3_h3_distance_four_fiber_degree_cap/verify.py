#!/usr/bin/env python3
"""Verify the H3 distance-four fiber-degree cap."""

from __future__ import annotations

import collections
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_distance_four_fiber_degree_cap"
DEPENDENCY = "f3_h3_distance_four_cross_overlap_router"
CONSUMER = "f3_h3_mobius_excess_half"


def order_root(prime: int, order: int) -> int:
    for base in range(2, prime):
        root = pow(base, (prime - 1) // order, prime)
        if pow(root, order // 2, prime) == prime - 1:
            return root
    raise AssertionError((prime, order))


def vector(pair: tuple[int, int], order: int) -> dict[int, int]:
    out: collections.Counter[int] = collections.Counter()
    half = order // 2
    for exponent, coefficient in (
        ((pair[0] + pair[1]) % order, 1),
        (pair[0], -1),
        (pair[1], -1),
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


def finite_check() -> tuple[int, int, int]:
    checked = 0
    maximum_generic_degree = 0
    maximum_total_degree = 0
    for order, prime in ((32, 97), (64, 193)):
        root = order_root(prime, order)
        powers = [pow(root, exponent, prime) for exponent in range(order)]
        pairs = list(itertools.combinations_with_replacement(range(1, order), 2))
        vectors = {pair: vector(pair, order) for pair in pairs}
        small = [pair for pair in pairs if sum(value * value for value in vectors[pair].values()) <= 3]
        fibers: dict[int, list[tuple[int, int]]] = collections.defaultdict(list)
        for pair in small:
            target = (1 - powers[pair[0]]) * (1 - powers[pair[1]]) % prime
            fibers[target].append(pair)
        for fiber in fibers.values():
            adjacency = {pair: [] for pair in fiber}
            edges = []
            for left, right in itertools.combinations(fiber, 2):
                if distance(vectors[left], vectors[right]) == 4:
                    adjacency[left].append(right)
                    adjacency[right].append(left)
                    edges.append((left, right))
            antipodal = [pair for pair in fiber if sum(value * value for value in vectors[pair].values()) == 1]
            assert len(antipodal) <= 1
            generic = [pair for pair in fiber if pair not in antipodal]
            assert all(sum(value * value for value in vectors[pair].values()) == 3 for pair in generic)
            for pair in generic:
                generic_degree = sum(neighbor in generic for neighbor in adjacency[pair])
                maximum_generic_degree = max(maximum_generic_degree, generic_degree)
                maximum_total_degree = max(maximum_total_degree, len(adjacency[pair]))
                assert generic_degree <= 3
                assert len(adjacency[pair]) <= 4

            indegree = {pair: 0 for pair in generic}
            generic_edge_count = 0
            for left, right in edges:
                if left not in indegree or right not in indegree:
                    continue
                orientations = []
                for source, head in ((left, right), (right, left)):
                    head_product = powers[head[0]] * powers[head[1]] % prime
                    if any(
                        head_product == -powers[exponent] % prime
                        for exponent in source
                    ):
                        orientations.append((source, head))
                assert orientations
                _, head = min(orientations)
                indegree[head] += 1
                assert indegree[head] <= 1
                generic_edge_count += 1

            assert generic_edge_count <= len(generic)
            bound = len(generic) + len(antipodal) * len(generic)
            assert len(edges) <= bound
            checked += 1
    assert maximum_generic_degree == 3
    assert maximum_total_degree == 4
    return checked, maximum_generic_degree, maximum_total_degree


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md", "proof.md", "claim_contract.md",
        "dependency_subdag.md", "audit.md", "result.md", "verify.py",
        "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = (base / "statement.md").read_text() + (base / "proof.md").read_text()
    for marker in (
        "squared norm one",
        "squared norm three",
        "orientation of indegree at most",
        "N_4(t) <= g+ag",
        "N_4(t) <= 2(m-1)",
    ):
        assert marker in text


def main() -> None:
    fibers, generic_degree, total_degree = finite_check()
    packet_check()
    print(
        "F3_H3_DISTANCE_FOUR_FIBER_DEGREE_CAP_PASS "
        f"fibers={fibers} generic_degree={generic_degree} total_degree={total_degree}"
    )


if __name__ == "__main__":
    main()
