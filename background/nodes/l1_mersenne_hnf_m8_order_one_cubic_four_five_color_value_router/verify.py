#!/usr/bin/env python3
"""Check four/five-color cubic profile and orbit counts."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_four_five_color_value_router"
DEPENDENCIES = {
    "l1_mersenne_hnf_order_one_color_degree_barrier",
    "l1_mersenne_hnf_m8_order_one_conic_reduction",
}
CONSUMER = "l1_mixed_petal_amplification"


def translate_set(values: frozenset[int], shift: int) -> frozenset[int]:
    return frozenset((value + shift) % 8 for value in values)


def orbit(configuration: tuple[frozenset[int], frozenset[int]]) -> set[tuple[frozenset[int], frozenset[int]]]:
    repeated, missing = configuration
    return {
        (translate_set(repeated, shift), translate_set(missing, shift))
        for shift in range(8)
    }


def main() -> None:
    five_color = {
        (frozenset({repeated}), frozenset(missing))
        for repeated in range(8)
        for missing in itertools.combinations([value for value in range(8) if value != repeated], 3)
    }
    triple_color = {
        (frozenset({triple}), frozenset(missing))
        for triple in range(8)
        for missing in itertools.combinations([value for value in range(8) if value != triple], 4)
    }
    two_double = {
        (frozenset(repeated), frozenset(missing))
        for repeated in itertools.combinations(range(8), 2)
        for missing in itertools.combinations([value for value in range(8) if value not in repeated], 4)
    }
    assert (len(five_color), len(triple_color), len(two_double)) == (280, 280, 420)

    def orbit_count(configurations: set[tuple[frozenset[int], frozenset[int]]]) -> int:
        remaining = set(configurations)
        count = 0
        while remaining:
            current = next(iter(remaining))
            remaining.difference_update(orbit(current))
            count += 1
        return count

    assert orbit_count(five_color) == 35
    assert orbit_count(triple_color) == 35
    assert orbit_count(two_double) == 54

    profiles = {
        tuple(sorted(parts, reverse=True))
        for length in (4, 5)
        for parts in itertools.product(range(1, 4), repeat=length)
        if sum(parts) == 6
    }
    assert profiles == {(2, 1, 1, 1, 1), (3, 1, 1, 1), (2, 2, 1, 1)}

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
    for anchor in ("(FFV1)", "(FFV2)", "(FFV3)", "124"):
        assert anchor in statement
    for anchor in ("420", "12", "54", "Burnside"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_FOUR_FIVE_COLOR_VALUE_ROUTER_PASS packets=124")


if __name__ == "__main__":
    main()
