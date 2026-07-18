#!/usr/bin/env python3
"""Tiny exhaustive replay of the split-locator Hankel equivalence."""

from __future__ import annotations

import json
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
Q = 5
D = tuple(range(4))
R = 2
RADIUS = 1
VECTORS = tuple(product(range(Q), repeat=R))


def split_locators() -> tuple[tuple[int, int], ...]:
    # X-x has coefficient vector (-x,1).
    return tuple(((-x) % Q, 1) for x in D)


def annihilates(moment: tuple[int, int], locator: tuple[int, int]) -> bool:
    return sum(a * b for a, b in zip(moment, locator)) % Q == 0


def span(column: tuple[int, int]) -> set[tuple[int, int]]:
    return {tuple((a * value) % Q for value in column) for a in range(Q)}


def main() -> None:
    columns = tuple((1, x) for x in D)
    spans = tuple(span(column) for column in columns)
    close = set().union(*spans)
    locators = split_locators()

    for moment in VECTORS:
        by_distance = moment in close
        by_hankel = any(annihilates(moment, locator) for locator in locators)
        assert by_distance == by_hankel

    pair_rows = 0
    slope_rows = 0
    for y0 in VECTORS:
        for y1 in VECTORS:
            common_support = any(y0 in line and y1 in line for line in spans)
            common_locator = any(
                annihilates(y0, locator) and annihilates(y1, locator)
                for locator in locators
            )
            assert common_support == common_locator
            pair_rows += 1

            if common_support:
                continue
            for gamma in range(Q):
                moment = tuple((a + gamma * b) % Q for a, b in zip(y0, y1))
                by_distance = moment in close
                by_pencil = any(
                    annihilates(moment, locator) for locator in locators
                )
                assert by_distance == by_pencil
                slope_rows += 1

    # Explicit route-fence pencil: four supported slopes and no common locator.
    y0 = (0, 1)
    y1 = (1, 4)
    assert not any(
        annihilates(y0, locator) and annihilates(y1, locator)
        for locator in locators
    )
    supported = {
        gamma
        for gamma in range(Q)
        if any(
            annihilates(
                tuple((a + gamma * b) % Q for a, b in zip(y0, y1)),
                locator,
            )
            for locator in locators
        )
    }
    assert supported == {1, 2, 3, 4}

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_ca_hankel_split_pencil_equivalence"]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (
        "rate_half_ca_hankel_split_pencil_equivalence",
        "rate_half_band_closure",
        "ev",
    ) in edges

    print(
        "RATE_HALF_CA_HANKEL_SPLIT_PENCIL_EQUIVALENCE_PASS "
        f"moments={len(VECTORS)} pairs={pair_rows} slope_rows={slope_rows}"
    )


if __name__ == "__main__":
    main()
