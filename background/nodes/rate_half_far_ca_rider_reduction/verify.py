#!/usr/bin/env python3
"""Tiny exhaustive replay of the far-CA rider reduction."""

from __future__ import annotations

import json
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def agreement(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return sum(x == y for x, y in zip(left, right, strict=True))


def replay(prime: int, code: tuple[tuple[int, ...], ...], r: int) -> tuple[int, int]:
    n = len(code[0])
    a = n - r
    words = tuple(product(range(prime), repeat=n))
    checked_far = 0
    max_bad = 0

    for first in words:
        for second in words:
            joint = max(
                sum(x == cx and y == cy for x, y, cx, cy in zip(first, second, c1, c2, strict=True))
                for c1 in code
                for c2 in code
            )
            if joint >= a:
                continue
            checked_far += 1

            bad = 0
            for slope in range(prime):
                line = tuple((x + slope * y) % prime for x, y in zip(first, second, strict=True))
                bad += max(agreement(line, candidate) for candidate in code) >= a
            max_bad = max(max_bad, bad)

            pair_list = sum(
                sum(x == cx and y == cy for x, y, cx, cy in zip(first, second, c1, c2, strict=True))
                >= n - 2 * r
                for c1 in code
                for c2 in code
            )
            assert bad <= 1 + (r + 1) * pair_list

            if bad >= 2:
                for word in (first, second):
                    distance = n - max(agreement(word, candidate) for candidate in code)
                    assert distance <= 2 * r

    assert checked_far > 0
    return checked_far, max_bad


def main() -> None:
    row1 = replay(2, ((0, 0, 0), (1, 1, 1)), 1)
    row2 = replay(3, ((0, 0, 0), (1, 1, 1), (2, 2, 2)), 1)

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_far_ca_rider_reduction"]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (
        "rate_half_far_ca_rider_reduction",
        "rate_half_band_closure",
        "ev",
    ) in edges

    print(f"RATE_HALF_FAR_CA_RIDER_REDUCTION_PASS rows={row1},{row2}")


if __name__ == "__main__":
    main()
