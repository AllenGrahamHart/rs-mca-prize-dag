#!/usr/bin/env python3
"""Tiny replay of the full-column-rank Hankel branch."""

from __future__ import annotations

import json
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
Q = 5
R = 4
RADIUS = 1
D = tuple(range(Q))
ENDPOINTS = tuple(product((0, 1), repeat=R))


def hankel(moment: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    return tuple((moment[i], moment[i + 1]) for i in range(R - RADIUS))


def rank_two(matrix: tuple[tuple[int, int], ...]) -> bool:
    return any(
        (matrix[i][0] * matrix[j][1] - matrix[i][1] * matrix[j][0]) % Q
        for i in range(len(matrix))
        for j in range(i + 1, len(matrix))
    )


def has_split_locator(matrix: tuple[tuple[int, int], ...]) -> bool:
    return any(
        all((-x * left + right) % Q == 0 for left, right in matrix)
        for x in D
    )


def main() -> None:
    fullrank_rows = 0
    maximum_supported = 0
    maximizer = None

    for y0 in ENDPOINTS:
        for y1 in ENDPOINTS:
            matrices = tuple(
                hankel(tuple((a + gamma * b) % Q for a, b in zip(y0, y1)))
                for gamma in range(Q)
            )
            if not any(rank_two(matrix) for matrix in matrices):
                continue
            supported = sum(has_split_locator(matrix) for matrix in matrices)
            assert supported <= RADIUS + 1
            fullrank_rows += 1
            if supported > maximum_supported:
                maximum_supported = supported
                maximizer = (y0, y1)

    assert fullrank_rows == 246
    assert maximum_supported == 2
    assert maximizer == ((0, 1, 0, 1), (1, 0, 1, 0))

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_ca_hankel_fullrank_branch"]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (
        "rate_half_ca_hankel_split_pencil_equivalence",
        "rate_half_ca_hankel_fullrank_branch",
        "req",
    ) in edges
    assert (
        "rate_half_ca_hankel_fullrank_branch",
        "rate_half_band_closure",
        "ev",
    ) in edges

    print(
        "RATE_HALF_CA_HANKEL_FULLRANK_BRANCH_PASS "
        f"rows={fullrank_rows} maximum_supported={maximum_supported}"
    )


if __name__ == "__main__":
    main()
