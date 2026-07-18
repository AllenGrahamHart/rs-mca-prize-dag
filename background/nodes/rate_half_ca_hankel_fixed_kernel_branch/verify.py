#!/usr/bin/env python3
"""Tiny replay of the fixed-kernel Hankel branch."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
Q = 5
R = 4
RADIUS = 1
DOMAIN = (0, 1, 2, 3)


def scale(vector: tuple[int, ...], scalar: int) -> tuple[int, ...]:
    return tuple((scalar * value) % Q for value in vector)


def add_scaled(
    left: tuple[int, ...], right: tuple[int, ...], scalar: int
) -> tuple[int, ...]:
    return tuple((a + scalar * b) % Q for a, b in zip(left, right))


def hankel(moment: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    return tuple((moment[i], moment[i + 1]) for i in range(R - RADIUS))


def matrix_rank(matrix: tuple[tuple[int, int], ...]) -> int:
    if all(row == (0, 0) for row in matrix):
        return 0
    if any(
        (matrix[i][0] * matrix[j][1] - matrix[i][1] * matrix[j][0]) % Q
        for i in range(len(matrix))
        for j in range(i + 1, len(matrix))
    ):
        return 2
    return 1


def has_split_locator(matrix: tuple[tuple[int, int], ...]) -> bool:
    return any(
        all((-x * left + right) % Q == 0 for left, right in matrix)
        for x in DOMAIN
    )


def common_split(y0: tuple[int, ...], y1: tuple[int, ...]) -> bool:
    m0, m1 = hankel(y0), hankel(y1)
    return any(
        all((-x * left + right) % Q == 0 for left, right in m0 + m1)
        for x in DOMAIN
    )


def fixed_kernel_generators() -> tuple[tuple[str, tuple[int, ...]], ...]:
    geometric = tuple(
        (f"root-{x}", tuple(pow(x, i, Q) for i in range(R)))
        for x in range(Q)
    )
    # This is the projective row direction (0,1); its right kernel is the
    # degree-zero coefficient line, so it contains no monic linear locator.
    return geometric + (("boundary", (0, 0, 0, 1)),)


def main() -> None:
    presentations = 0
    far_presentations = 0
    histogram: Counter[int] = Counter()

    for _name, generator in fixed_kernel_generators():
        for c0 in range(Q):
            for c1 in range(Q):
                if c0 == c1 == 0:
                    continue
                y0, y1 = scale(generator, c0), scale(generator, c1)
                matrices = tuple(
                    hankel(add_scaled(y0, y1, gamma)) for gamma in range(Q)
                )

                # These six projective row directions exhaust rank-one
                # fixed-kernel Hankel pencils of this shape.
                assert max(map(matrix_rank, matrices)) == 1
                presentations += 1

                if common_split(y0, y1):
                    continue
                far_presentations += 1

                supported = tuple(
                    gamma
                    for gamma, matrix in enumerate(matrices)
                    if has_split_locator(matrix)
                )
                rank_drops = tuple(
                    gamma
                    for gamma, matrix in enumerate(matrices)
                    if matrix_rank(matrix) == 0
                )
                assert set(supported).issubset(rank_drops)
                assert len(supported) <= 1
                histogram[len(supported)] += 1

    assert presentations == 144
    assert far_presentations == 48
    assert histogram == Counter({1: 40, 0: 8})

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_ca_hankel_fixed_kernel_branch"]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (
        "rate_half_ca_hankel_split_pencil_equivalence",
        "rate_half_ca_hankel_fixed_kernel_branch",
        "req",
    ) in edges
    assert (
        "rate_half_ca_hankel_fixed_kernel_branch",
        "rate_half_band_closure",
        "ev",
    ) in edges

    print(
        "RATE_HALF_CA_HANKEL_FIXED_KERNEL_BRANCH_PASS "
        f"presentations={presentations} far={far_presentations} "
        f"histogram={dict(sorted(histogram.items()))}"
    )


if __name__ == "__main__":
    main()
