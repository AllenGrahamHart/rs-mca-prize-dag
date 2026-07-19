#!/usr/bin/env python3
"""Verify the H3 antipodal-tail split and DAG wiring."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_antipodal_tail_distance_six_split"
DEPENDENCIES = {
    "f3_h3_high_excess_distance_six_moment_reduction",
    "f3_h3_distance_four_fiber_degree_cap",
    "f3_h3_low_distance_quotient_incidence_router",
}
CONSUMER = "f3_h3_mobius_excess_half"
PRIME = 1_000_003


def minimum_small_vectors(excess: int) -> int:
    return 7 + (excess + 1) // 2


def free_distance_six_floor(size: int) -> int:
    centroid = (size * (size - 4) + 1) // 2
    distance_four = size
    return centroid - 2 * distance_four


def antipodal_distance_six_floor(size: int) -> int:
    centroid = (size * (size - 2) + 1) // 2
    distance_four = 2 * (size - 1)
    return centroid - 2 * distance_four


def arithmetic_check() -> None:
    interfaces = {
        6: (Fraction(8, 17), Fraction(4, 5)),
        10: (Fraction(4, 11), Fraction(1, 2)),
        14: (Fraction(16, 53), Fraction(8, 21)),
    }
    for cutoff, (free_ratio, antipodal_ratio) in interfaces.items():
        for excess in range(cutoff + 1, 513):
            minimum = minimum_small_vectors(excess)
            for size in range(minimum, minimum + 40):
                assert Fraction(excess, free_distance_six_floor(size)) <= free_ratio
                assert Fraction(excess, antipodal_distance_six_floor(size)) <= antipodal_ratio
    assert Fraction(53 * 62, 272) == Fraction(1643, 136)
    assert Fraction(1643, 136) < Fraction(12081, 1000)
    assert Fraction(53, 42) < Fraction(53, 27)
    assert Fraction(136 * 42, 1113) == Fraction(272, 53)
    assert Fraction(136 * 53, 1113) == Fraction(136, 21)
    assert Fraction(1113, 136 * 42) == Fraction(53, 272)
    assert Fraction(198, 8) == Fraction(99, 4)
    assert Fraction(130 * 11, 68) == Fraction(715, 34)
    assert Fraction(4, 5) / Fraction(8, 17) == Fraction(17, 10)
    assert Fraction(1, 2) / Fraction(4, 11) == Fraction(11, 8)


def identity_check() -> None:
    x, u, a, z = 2, 3, 5, 7
    square = x * x % PRIME
    target = (1 - square) % PRIME
    v = (square - u) * pow(1 - u, PRIME - 2, PRIME) % PRIME
    b = (square - a) * pow(1 - a, PRIME - 2, PRIME) % PRIME
    w = (square + (1 - square) * z) % PRIME
    assert (1 - u) * (1 - v) % PRIME == target
    assert (1 - a) * (1 - b) % PRIME == target
    assert (1 - w) % PRIME == target * (1 - z) % PRIME


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert all((dependency, NODE, "req") in edges for dependency in DEPENDENCIES)
    assert (NODE, CONSUMER, "ev") in edges
    packet = (
        ROOT / "background" / "nodes" / NODE / "statement.md"
    ).read_text()
    for marker in (
        "P(t)-18 <=(16/53)N_6(t)",
        "136(42M_6,33^0+53M_6,33^A)<=1113B_n",
        "(53/42)M_6,33^A",
        "4(10M_6,25^0+17M_6,25^A)<=5B_(n,6)",
        "17(8M_6,29^0+11M_6,29^A)<=22B_(n,10)",
    ):
        assert marker in packet


def main() -> None:
    arithmetic_check()
    identity_check()
    packet_check()
    print(
        "F3_H3_ANTIPODAL_TAIL_DISTANCE_SIX_SPLIT_PASS "
        "ratio=16/53 weighted_antipodal_cost=53/42 memberships=2+3"
    )


if __name__ == "__main__":
    main()
