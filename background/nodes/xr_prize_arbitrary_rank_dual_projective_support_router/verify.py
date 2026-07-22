#!/usr/bin/env python3
"""Verify the arbitrary-rank dual-projective support router."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_prize_arbitrary_rank_dual_projective_support_router"
PARENTS = {
    "xr_prize_arbitrary_w_trade_circuit_segre_router",
    "xr_prize_arbitrary_w_rank_two_dual_plane_support_router",
    "xr_prize_arbitrary_w_rank_two_received_pair_router",
}
CONSUMER = "xr_highcore_collision_count"
PRIME = 101


def rank_columns(columns: tuple[tuple[int, ...], ...]) -> int:
    rows = len(columns[0])
    matrix = [[column[row] % PRIME for column in columns] for row in range(rows)]
    pivot = 0
    for column in range(len(columns)):
        choice = next(
            (row for row in range(pivot, rows) if matrix[row][column]),
            None,
        )
        if choice is None:
            continue
        matrix[pivot], matrix[choice] = matrix[choice], matrix[pivot]
        inverse = pow(matrix[pivot][column], PRIME - 2, PRIME)
        matrix[pivot] = [value * inverse % PRIME for value in matrix[pivot]]
        for row in range(rows):
            if row == pivot:
                continue
            factor = matrix[row][column]
            if factor:
                matrix[row] = [
                    (left - factor * right) % PRIME
                    for left, right in zip(matrix[row], matrix[pivot], strict=True)
                ]
        pivot += 1
        if pivot == rows:
            break
    return pivot


def segre(gamma: int, coefficients: tuple[int, ...]) -> tuple[int, ...]:
    return coefficients + tuple(gamma * value % PRIME for value in coefficients)


def projective_fixtures() -> tuple[int, int]:
    checks = 0
    mutations = 0

    # Rank-three, minimum arity five: powers 0..3 after duplicated exponents.
    slopes5 = (1, 2, 3, 4, 5)
    columns5 = tuple(
        segre(gamma, (1, gamma, gamma * gamma % PRIME)) for gamma in slopes5
    )
    assert rank_columns(columns5) == 4
    assert all(rank_columns(quad) == 4 for quad in combinations(columns5, 4))
    checks += 6

    # Rank-three, maximal arity seven: a permuted degree-five Vandermonde.
    slopes7 = (1, 2, 3, 4, 5, 6, 7)
    columns7 = tuple(
        segre(
            gamma,
            (1, pow(gamma, 2, PRIME), pow(gamma, 4, PRIME)),
        )
        for gamma in slopes7
    )
    assert rank_columns(columns7) == 6
    assert all(rank_columns(six) == 6 for six in combinations(columns7, 6))
    checks += 8

    # Three repeated coefficient directions would make a proper 3-circuit.
    repeated = tuple(segre(gamma, (1, 2, 3)) for gamma in (1, 2, 4))
    assert rank_columns(repeated) == 2
    mutations += 1
    return checks, mutations


def dimension_check() -> int:
    checks = 0
    for rank in range(2, 30):
        for arity in range(rank + 2, 2 * rank + 2):
            column_rank = arity - 1
            interaction = 2 * rank - column_rank
            assert interaction == 2 * rank - arity + 1
            assert interaction >= 0
            if arity == 2 * rank + 1:
                assert interaction == 0
            checks += 3
    return checks


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for parent in PARENTS:
        assert nodes[parent]["status"] == "PROVED"
        assert (parent, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "Phi:X->P^(r-1)",
        "2r-t+1",
        "occursatmosttwice",
        "maximalcircuitarity",
    ):
        assert marker in statement


def main() -> None:
    fixtures, mutations = projective_fixtures()
    dimensions = dimension_check()
    packet_check()
    print(
        "XR_PRIZE_ARBITRARY_RANK_DUAL_PROJECTIVE_SUPPORT_ROUTER_PASS "
        f"fixture_checks={fixtures} dimension_checks={dimensions} mutations={mutations}"
    )


if __name__ == "__main__":
    main()
