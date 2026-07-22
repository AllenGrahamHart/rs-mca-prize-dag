#!/usr/bin/env python3
"""Verify the arbitrary-W rank-two received-pair router."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_prize_arbitrary_w_rank_two_received_pair_router"
PARENTS = {
    "xr_prize_arbitrary_w_rank_two_dual_plane_support_router",
    "xr_rank_two_received_pair_alternating_router",
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


def segre(gamma: int, beta: tuple[int, int]) -> tuple[int, ...]:
    c, d = beta
    return (c, d, gamma * c % PRIME, gamma * d % PRIME)


def interaction_check() -> tuple[int, int]:
    checks = 0
    mutations = 0

    # Four-block Mobius graph beta=[1:gamma], hyperplane x_2-x_3=0.
    slopes4 = (1, 2, 3, 4)
    columns4 = tuple(segre(gamma, (1, gamma)) for gamma in slopes4)
    theta = (0, 1, -1, 0)
    assert rank_columns(columns4) == 3
    assert all(sum(x * y for x, y in zip(theta, column, strict=True)) % PRIME == 0 for column in columns4)
    determinant = theta[0] * theta[3] - theta[1] * theta[2]
    assert determinant % PRIME != 0
    checks += 3

    broken = (1, 0, 0, 0)
    assert any(sum(x * y for x, y in zip(broken, column, strict=True)) % PRIME for column in columns4)
    mutations += 1

    # Five-block full Segre circuit has zero annihilator.
    slopes5 = (1, 2, 3, 4, 5)
    columns5 = tuple(segre(gamma, (1, gamma * gamma % PRIME)) for gamma in slopes5)
    assert rank_columns(columns5) == 4
    assert all(rank_columns(quad) == 4 for quad in combinations(columns5, 4))
    checks += 6
    return checks, mutations


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
        "theta=eta(A,B,C,D)",
        "AD-BC!=0",
        "perfect-pairingbranch",
        "augmented-orthogonal",
    ):
        assert marker in statement


def main() -> None:
    checks, mutations = interaction_check()
    packet_check()
    print(
        "XR_PRIZE_ARBITRARY_W_RANK_TWO_RECEIVED_PAIR_ROUTER_PASS "
        f"interaction_checks={checks} mutations={mutations}"
    )


if __name__ == "__main__":
    main()
