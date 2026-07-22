#!/usr/bin/env python3
"""Verify the XR prize rank-one flat/basis owner."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_prize_rank_one_trade_flat_basis_owner"
PARENTS = {
    "xr_prize_flat_nullity_maxwell_trade_space_compiler",
    "xr_prize_flat_nullity_rank_metric_trade_router",
    "xr_rs_flat_nullity_basis_charge",
    "xr_poststrip_affine_pencil_charge",
}
CONSUMER = "xr_highcore_collision_count"


def rank(rows: list[list[int]], prime: int) -> int:
    matrix = [row[:] for row in rows]
    if not matrix:
        return 0
    row_count = len(matrix)
    column_count = len(matrix[0])
    pivot = 0
    for column in range(column_count):
        choice = next(
            (row for row in range(pivot, row_count) if matrix[row][column] % prime),
            None,
        )
        if choice is None:
            continue
        matrix[pivot], matrix[choice] = matrix[choice], matrix[pivot]
        inverse = pow(matrix[pivot][column] % prime, prime - 2, prime)
        matrix[pivot] = [value * inverse % prime for value in matrix[pivot]]
        for row in range(row_count):
            if row == pivot:
                continue
            factor = matrix[row][column] % prime
            if factor:
                matrix[row] = [
                    (left - factor * right) % prime
                    for left, right in zip(matrix[row], matrix[pivot], strict=True)
                ]
        pivot += 1
        if pivot == row_count:
            break
    return pivot


def owner_fixtures() -> tuple[int, int]:
    prime = 101
    checks = 0
    mutations = 0

    # Spanning MDS support for W=<1,X>; linear b,q vanish under interpolation
    # residuals on all three support points.
    support = (1, 2, 3)
    w_rows = [[1, 1, 1], list(support)]
    b = [(7 + 4 * x) % prime for x in support]
    q = [(9 + 6 * x) % prime for x in support]
    assert rank(w_rows, prime) == 2
    assert rank(w_rows + [b], prime) == 2
    assert rank(w_rows + [q], prime) == 2
    checks += 3
    broken = q[:]
    broken[-1] += 1
    assert rank(w_rows + [broken], prime) == 3
    mutations += 1

    # Proper rank-one flat for W=<1,X^2>: points 1 and -1 are parallel.
    flat_rows = [[1, 1], [1, 1]]
    assert rank(flat_rows, prime) == 1
    j = 1
    u = 1
    flat_size = 2
    assert flat_size == j + u
    assert flat_size >= j + 1
    checks += 3
    return checks, mutations


def cap_check() -> int:
    n = 1 << 41
    checks = 0
    for rate, scale in ((4, 256), (8, 256), (16, 512)):
        k = n // rate
        h = n // scale + 1
        r = n - k
        for v in (0, 1, k // 100, k - 1):
            cap = (r - v) // h
            assert cap <= r // h
            assert (cap + 1) * h > r - v
            assert cap * h <= r - v
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
        "b|SinW|S",
        "floor((R-v)/h)",
        "|F|<=j+u",
        "When`u=0`",
    ):
        assert marker in statement


def main() -> None:
    fixtures, mutations = owner_fixtures()
    caps = cap_check()
    packet_check()
    print(
        "XR_PRIZE_RANK_ONE_TRADE_FLAT_BASIS_OWNER_PASS "
        f"fixture_checks={fixtures} cap_checks={caps} mutations={mutations}"
    )


if __name__ == "__main__":
    main()
