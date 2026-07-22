#!/usr/bin/env python3
"""Verify the general prize flat-nullity Maxwell compiler."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_prize_flat_nullity_maxwell_trade_space_compiler"
PARENTS = {
    "xr_rs_common_root_basis_charge",
    "xr_rs_flat_nullity_basis_charge",
    "xr_prize_flat_nullity_effective_core_floor",
    "xr_prize_flat_nullity_nonpersistent_root_cap",
    "xr_prize_u0_loop_defect_maxwell_rank_one_compiler",
}
CONSUMER = "xr_highcore_collision_count"


def rank(vectors: list[list[int]], prime: int) -> int:
    if not vectors:
        return 0
    matrix = [row[:] for row in vectors]
    rows = len(matrix)
    columns = len(matrix[0])
    pivot = 0
    for column in range(columns):
        choice = next(
            (row for row in range(pivot, rows) if matrix[row][column] % prime),
            None,
        )
        if choice is None:
            continue
        matrix[pivot], matrix[choice] = matrix[choice], matrix[pivot]
        inverse = pow(matrix[pivot][column] % prime, prime - 2, prime)
        matrix[pivot] = [value * inverse % prime for value in matrix[pivot]]
        for row in range(rows):
            if row == pivot:
                continue
            factor = matrix[row][column] % prime
            if factor:
                matrix[row] = [
                    (left - factor * right) % prime
                    for left, right in zip(matrix[row], matrix[pivot], strict=True)
                ]
        pivot += 1
        if pivot == rows:
            break
    return pivot


def official_density_check() -> int:
    n = 1 << 41
    budget = 8 * n**3
    checks = 0
    for rate, scale in ((4, 256), (8, 256), (16, 512)):
        k = n // rate
        h = n // scale + 1
        r = n - k
        # Hardest point because h>2: maximal allowed exceptional count v=k.
        assert h * (budget + 1 - k) > 2 * (r - k)
        assert h > 2
        checks += 2
    return checks


def dimension_check() -> int:
    checks = 0
    for a in range(1, 8):
        for h in range(1, 8):
            for u in range(0, 6):
                for v in range(0, 6):
                    for t in range(3, 9):
                        for e in range(h):
                            numerator = h * t + 2 * (a + u + v) - e
                            if numerator % 2:
                                continue
                            union = numerator // 2
                            rows = (h + u + v) * t
                            rank_cap = 2 * union - (2 * a + 1)
                            assert rows - rank_cap == (u + v) * (t - 2) + e + 1
                            checks += 1
    return checks


def circuit_owner_check() -> tuple[int, int]:
    prime = 101
    checks = 0
    mutations = 0

    # Non-MDS polynomial space W=<1,X^2>; points 1 and -1 form a 2-circuit.
    points = (1, 100)
    columns = [[1, 1], [1, 1]]
    assert rank(columns, prime) == 1
    b = [3, 3]
    q = [5, 5]
    assert rank(columns + [b], prime) == 1
    assert rank(columns + [q], prime) == 1
    checks += 3

    slopes = (1, 2, 4)
    alpha = (
        slopes[1] - slopes[2],
        slopes[2] - slopes[0],
        slopes[0] - slopes[1],
    )
    assert sum(alpha) % prime == 0
    assert sum(x * y for x, y in zip(slopes, alpha, strict=True)) % prime == 0
    relation = (1, -1)
    for coordinate in range(2):
        assert sum(a_i * relation[coordinate] for a_i in alpha) % prime == 0
        assert sum(
            slope * a_i * relation[coordinate]
            for slope, a_i in zip(slopes, alpha, strict=True)
        ) % prime == 0
        checks += 2

    broken_q = [5, 6]
    assert rank(columns + [broken_q], prime) == 2
    mutations += 1

    # In the u=0 MDS specialization every circuit has size a+1.
    mds_columns = [[1, 1, 1], [1, 2, 3]]
    assert rank(mds_columns, prime) == 2
    assert rank([[1, 1], [1, 2]], prime) == 2
    assert rank([[1, 1], [1, 3]], prime) == 2
    assert rank([[1, 1], [2, 3]], prime) == 2
    checks += 4
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
        "(u+v)(t-2)+e+1",
        "2<=|C|<=a+1",
        "b|CinW|C",
        "interiorandbothendpointchambers",
    ):
        assert marker in statement


def main() -> None:
    official = official_density_check()
    dimensions = dimension_check()
    circuits, mutations = circuit_owner_check()
    packet_check()
    print(
        "XR_PRIZE_FLAT_NULLITY_MAXWELL_TRADE_SPACE_COMPILER_PASS "
        f"official_checks={official} dimension_checks={dimensions} "
        f"circuit_checks={circuits} mutations={mutations}"
    )


if __name__ == "__main__":
    main()
