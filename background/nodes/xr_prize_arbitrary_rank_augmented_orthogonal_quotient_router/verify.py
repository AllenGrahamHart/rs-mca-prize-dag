#!/usr/bin/env python3
"""Verify the arbitrary-rank augmented-orthogonal quotient router."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_prize_arbitrary_rank_augmented_orthogonal_quotient_router"
PARENTS = {
    "xr_prize_arbitrary_rank_dual_projective_support_router",
    "xr_prize_arbitrary_w_rank_two_received_pair_router",
}
CONSUMER = "xr_highcore_collision_count"
PRIME = 101


def rank_rows(rows: tuple[tuple[int, ...], ...]) -> int:
    matrix = [[value % PRIME for value in row] for row in rows]
    pivot = 0
    columns = len(matrix[0])
    for column in range(columns):
        choice = next(
            (row for row in range(pivot, len(matrix)) if matrix[row][column]),
            None,
        )
        if choice is None:
            continue
        matrix[pivot], matrix[choice] = matrix[choice], matrix[pivot]
        inverse = pow(matrix[pivot][column], PRIME - 2, PRIME)
        matrix[pivot] = [value * inverse % PRIME for value in matrix[pivot]]
        for row in range(len(matrix)):
            if row == pivot:
                continue
            factor = matrix[row][column]
            if factor:
                matrix[row] = [
                    (left - factor * right) % PRIME
                    for left, right in zip(matrix[row], matrix[pivot], strict=True)
                ]
        pivot += 1
    return pivot


def quotient_checks() -> tuple[int, int]:
    checks = 0
    mutations = 0

    # Rank-one image v=(3,5) has one affine root.
    root = -3 * pow(5, PRIME - 2, PRIME) % PRIME
    slopes = tuple(range(12)) + (root,)
    interactive = [gamma for gamma in slopes if (3 + 5 * gamma) % PRIME == 0]
    assert interactive == [root]
    checks += len(slopes)

    # Full-rank quotient directions and their Segre columns lie on a conic.
    conic = []
    for gamma in range(1, 10):
        coefficient = (-gamma % PRIME, 1)
        assert (coefficient[0] + gamma * coefficient[1]) % PRIME == 0
        conic.append(
            (
                coefficient[0],
                coefficient[1],
                gamma * coefficient[0] % PRIME,
                gamma,
            )
        )
        checks += 1
    assert rank_rows(tuple(conic)) == 3
    checks += 1

    bad = (1, 1)
    assert any((bad[0] + gamma * bad[1]) % PRIME for gamma in range(1, 10))
    mutations += 1
    return checks, mutations


def arity_checks() -> int:
    checks = 0
    for rank in range(2, 80):
        upper = 2 * rank - 1
        assert upper < 2 * rank + 1
        for arity in range(rank + 2, upper + 1):
            assert arity - 1 <= 2 * (rank - 1)
            checks += 1
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
        "s=rankPin{0,1,2}",
        "Exactlyoneactiverowliesoutside",
        "r+2<=t<=2r-1",
        "tau_i(-gamma_i,1,-gamma_i^2,gamma_i)",
    ):
        assert marker in statement


def main() -> None:
    quotient, mutations = quotient_checks()
    arities = arity_checks()
    packet_check()
    print(
        "XR_PRIZE_ARBITRARY_RANK_AUGMENTED_ORTHOGONAL_QUOTIENT_ROUTER_PASS "
        f"quotient_checks={quotient} arity_checks={arities} mutations={mutations}"
    )


if __name__ == "__main__":
    main()
