#!/usr/bin/env python3
"""Exhaustive syndrome replay of the post-quadratic MDS route fence."""

from __future__ import annotations

import json
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
Q = 5
COLUMNS = tuple((1, x) for x in range(4))
VECTORS = tuple(product(range(Q), repeat=2))


def add_slope(y0: tuple[int, int], y1: tuple[int, int], slope: int) -> tuple[int, int]:
    return tuple((a + slope * b) % Q for a, b in zip(y0, y1))


def span(column: tuple[int, int]) -> set[tuple[int, int]]:
    return {tuple((a * value) % Q for value in column) for a in range(Q)}


def main() -> None:
    spans = tuple(span(column) for column in COLUMNS)
    close = set().union(*spans)
    y0 = (0, 1)
    y1 = (1, 4)

    assert not any(y0 in line and y1 in line for line in spans)
    expected = {
        0: (0, 1),
        1: (1, 0),
        2: (2, 4),
        3: (3, 3),
        4: (4, 2),
    }
    assert {slope: add_slope(y0, y1, slope) for slope in range(Q)} == expected
    assert expected[0] not in close
    assert all(expected[slope] in close for slope in range(1, Q))

    maximum = 0
    histogram: dict[int, int] = {}
    for left in VECTORS:
        for right in VECTORS:
            if any(left in line and right in line for line in spans):
                continue
            bad = sum(add_slope(left, right, slope) in close for slope in range(Q))
            histogram[bad] = histogram.get(bad, 0) + 1
            maximum = max(maximum, bad)

    assert maximum == 4
    assert histogram == {0: 8, 1: 40, 3: 320, 4: 160}
    assert (4 - 1) ** 2 - 4 * (2 + 1) == -3

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_postquadratic_mds_extension_fence"]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (
        "rate_half_postquadratic_mds_extension_fence",
        "rate_half_band_closure",
        "ev",
    ) in edges

    print(
        "RATE_HALF_POSTQUADRATIC_MDS_EXTENSION_FENCE_PASS "
        f"maximum={maximum} histogram={histogram}"
    )


if __name__ == "__main__":
    main()
