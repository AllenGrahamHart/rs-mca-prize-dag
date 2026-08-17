#!/usr/bin/env python3
"""Check the floor-sensitive K'=72 rank-three-flat coupling arithmetic."""

from __future__ import annotations

import json
from math import comb


KPRIME = 72
M = 67472 + KPRIME
UNION = 36
PARALLEL = 29
OUTSIDE = M - UNION
COMPLETIONS = 31
TARGET = 20552964203529559475043545396584734873674935990


def choose(n: int, k: int) -> int:
    return comb(n, k) if 0 <= k <= n else 0


def independent_inside(size: int, parallel: int) -> int:
    ordinary = UNION - parallel
    return choose(ordinary, size) + parallel * choose(ordinary, size - 1)


def stratum_circuits(
    support: int,
    outside_points: int,
    parallel: int,
) -> int:
    if outside_points == 0:
        return independent_inside(support, parallel)
    return (
        independent_inside(support - outside_points, parallel)
        * choose(OUTSIDE, outside_points - 1)
        * COMPLETIONS
        // outside_points
    )


def selected_incidence(support: int, circuits: int) -> int:
    return circuits * choose(M - support, 11 - support)


def scenario(parallel: int) -> dict[str, int]:
    lower4 = sum(stratum_circuits(4, j, parallel) for j in range(4))
    lower5 = sum(stratum_circuits(5, j, parallel) for j in range(5))
    top4_independent = stratum_circuits(4, 4, parallel)
    top5_independent = stratum_circuits(5, 5, parallel)

    # The coupled envelope is increasing in C4 because one additional
    # support-four circuit loses at most ceil((N-34)/5) support-five
    # circuits, while its selected-incidence weight ratio is (m-4)/5.
    top4_coupled = top4_independent
    top5_coupled = (
        COMPLETIONS * choose(OUTSIDE, 4)
        - (OUTSIDE - 34) * top4_coupled
    ) // 5

    current_i4 = selected_incidence(4, lower4 + top4_independent)
    current_i5 = selected_incidence(5, lower5 + top5_independent)
    coupled_i4 = selected_incidence(4, lower4 + top4_coupled)
    coupled_i5 = selected_incidence(5, lower5 + top5_coupled)
    current_weighted = 21 * current_i4 + 15 * current_i5
    coupled_weighted = 21 * coupled_i4 + 15 * coupled_i5
    return {
        "parallel": parallel,
        "top4_independent": top4_independent,
        "top5_independent": top5_independent,
        "top5_coupled": top5_coupled,
        "current_i4": current_i4,
        "current_i5": current_i5,
        "current_weighted": current_weighted,
        "coupled_i4": coupled_i4,
        "coupled_i5": coupled_i5,
        "coupled_weighted": coupled_weighted,
        "target_margin": TARGET - coupled_weighted,
        "reduction": current_weighted - coupled_weighted,
    }

print(json.dumps({
    "m": M,
    "outside": OUTSIDE,
    "target": TARGET,
    "monotonicity_numerator": 3 * (
        (M - 4) - (OUTSIDE - 34)
    ),
    "plain": scenario(0),
    "parallel_refined": scenario(PARALLEL),
}, indent=2, sort_keys=True))
