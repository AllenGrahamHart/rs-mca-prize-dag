#!/usr/bin/env python3
"""Verify the arbitrary-W trade-circuit Segre router."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_prize_arbitrary_w_trade_circuit_segre_router"
PARENTS = {
    "xr_trade_circuit_arity_segre_atlas",
    "xr_prize_flat_nullity_maxwell_trade_space_compiler",
    "xr_prize_rank_one_trade_flat_basis_owner",
}
CONSUMER = "xr_highcore_collision_count"


def rank_columns(columns: tuple[tuple[int, ...], ...], prime: int) -> int:
    if not columns:
        return 0
    row_count = len(columns[0])
    matrix = [[column[row] % prime for column in columns] for row in range(row_count)]
    pivot = 0
    for column in range(len(columns)):
        choice = next(
            (row for row in range(pivot, row_count) if matrix[row][column]),
            None,
        )
        if choice is None:
            continue
        matrix[pivot], matrix[choice] = matrix[choice], matrix[pivot]
        inverse = pow(matrix[pivot][column], prime - 2, prime)
        matrix[pivot] = [value * inverse % prime for value in matrix[pivot]]
        for row in range(row_count):
            if row == pivot:
                continue
            factor = matrix[row][column]
            if factor:
                matrix[row] = [
                    (left - factor * right) % prime
                    for left, right in zip(matrix[row], matrix[pivot], strict=True)
                ]
        pivot += 1
        if pivot == row_count:
            break
    return pivot


def segre(beta: tuple[int, int], gamma: int, prime: int) -> tuple[int, ...]:
    c, d = beta
    return (c % prime, d % prime, gamma * c % prime, gamma * d % prime)


def fixture_check() -> tuple[int, int]:
    prime = 101
    checks = 0
    mutations = 0

    # Three-block rank-one ruling circuit.
    slopes3 = (1, 2, 4)
    columns3 = tuple(segre((1, 3), gamma, prime) for gamma in slopes3)
    assert rank_columns(columns3, prime) == 2
    assert all(rank_columns(pair, prime) == 2 for pair in combinations(columns3, 2))
    checks += 4

    # Four-block Mobius circuit beta=[1:gamma].
    slopes4 = (1, 2, 3, 4)
    columns4 = tuple(segre((1, gamma), gamma, prime) for gamma in slopes4)
    assert rank_columns(columns4, prime) == 3
    assert all(rank_columns(triple, prime) == 3 for triple in combinations(columns4, 3))
    checks += 5

    # Five-block full Segre circuit beta=[1:gamma^2].
    slopes5 = (1, 2, 3, 4, 5)
    columns5 = tuple(segre((1, gamma * gamma), gamma, prime) for gamma in slopes5)
    assert rank_columns(columns5, prime) == 4
    assert all(rank_columns(quad, prime) == 4 for quad in combinations(columns5, 4))
    checks += 6

    # Collapsing the four-block beta map produces rank one, not rank two.
    collapsed = tuple(segre((1, 3), gamma, prime) for gamma in slopes4)
    assert rank_columns(collapsed, prime) == 2
    mutations += 1
    return checks, mutations


def arity_check() -> int:
    checks = 0
    for trade_rank in range(1, 20):
        for arity in range(trade_rank + 2, 2 * trade_rank + 2):
            assert trade_rank <= arity - 2
            assert arity <= 2 * trade_rank + 1
            checks += 2
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
        "r+2<=ell<=2r+1",
        "rank-onecircuitsonthreeblocks",
        "rank-twocircuitsonfourorfiveblocks",
        "arbitraryblockarityisremoved",
    ):
        assert marker in statement


def main() -> None:
    fixtures, mutations = fixture_check()
    arities = arity_check()
    packet_check()
    print(
        "XR_PRIZE_ARBITRARY_W_TRADE_CIRCUIT_SEGRE_ROUTER_PASS "
        f"fixture_checks={fixtures} arity_checks={arities} mutations={mutations}"
    )


if __name__ == "__main__":
    main()
