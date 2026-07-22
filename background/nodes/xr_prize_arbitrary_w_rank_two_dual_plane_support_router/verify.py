#!/usr/bin/env python3
"""Verify the arbitrary-W rank-two dual-plane support router."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_prize_arbitrary_w_rank_two_dual_plane_support_router"
PARENTS = {
    "xr_prize_arbitrary_w_trade_circuit_segre_router",
    "xr_prize_rank_one_trade_flat_basis_owner",
}
CONSUMER = "xr_highcore_collision_count"
PRIME = 101


def rank_columns(columns: tuple[tuple[int, ...], ...]) -> int:
    if not columns:
        return 0
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


def segre(gamma: int, ratio: int) -> tuple[int, ...]:
    return (1, ratio, gamma, gamma * ratio % PRIME)


def plane_fixture() -> tuple[int, int]:
    # Dual to the constant code: both vectors sum to zero and have no common
    # zero, so [F:G] is defined on the whole support union.
    f = (1, 1, 1, -1, -1, -1, 0)
    g = (1, 2, 3, 4, 5, 6, 80)
    assert sum(f) % PRIME == 0
    assert sum(g) % PRIME == 0
    assert all((left % PRIME) or (right % PRIME) for left, right in zip(f, g, strict=True))

    checks = 3
    mutations = 0
    for betas in (
        ((1, 1), (1, 2), (1, 3), (1, 4)),
        ((1, 3), (1, 3), (1, 1), (1, 1), (1, 2)),
    ):
        zero_sets = []
        for c, d in betas:
            zero_sets.append(
                {index for index, (fx, gx) in enumerate(zip(f, g, strict=True)) if (c * fx + d * gx) % PRIME == 0}
            )
        for left_index, right_index in combinations(range(len(betas)), 2):
            if betas[left_index] == betas[right_index]:
                assert zero_sets[left_index] == zero_sets[right_index]
            else:
                assert zero_sets[left_index].isdisjoint(zero_sets[right_index])
            checks += 1

    slopes = (1, 2, 3, 4, 5)
    ratios = (3, 3, 1, 1, 2)
    columns = tuple(segre(gamma, ratio) for gamma, ratio in zip(slopes, ratios, strict=True))
    assert rank_columns(columns) == 4
    assert all(rank_columns(quad) == 4 for quad in combinations(columns, 4))
    assert max(ratios.count(value) for value in set(ratios)) == 2
    checks += 7

    broken = ratios[:3] + (3, 3)
    assert max(broken.count(value) for value in set(broken)) >= 3
    mutations += 1
    return checks, mutations


def locator_fixture() -> int:
    support = (1, 3, 5, 7)
    values = (2, 4, 8, 16)
    checks = 0
    recovered = []
    for x, value in zip(support, values, strict=True):
        derivative = 1
        for y in support:
            if x != y:
                derivative = derivative * (x - y) % PRIME
        recovered.append(value * derivative % PRIME)
    assert all(value for value in recovered)
    checks += len(recovered)
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
        "L=<F,G>subset(W|X)^perp",
        "multiplicityatmosttwo",
        "b|SinW|S",
        "one dual plane plus its projective fibers".replace(" ", ""),
    ):
        assert marker in statement


def main() -> None:
    planes, mutations = plane_fixture()
    locators = locator_fixture()
    packet_check()
    print(
        "XR_PRIZE_ARBITRARY_W_RANK_TWO_DUAL_PLANE_SUPPORT_ROUTER_PASS "
        f"plane_checks={planes} locator_checks={locators} mutations={mutations}"
    )


if __name__ == "__main__":
    main()
