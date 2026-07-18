#!/usr/bin/env python3
"""Tiny exact checks for the two-sided Hankel minimal-index theorem."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def inv(value: int, prime: int) -> int:
    return pow(value % prime, prime - 2, prime)


def rref(
    matrix: list[list[int]], prime: int
) -> tuple[list[list[int]], tuple[int, ...]]:
    work = [[value % prime for value in row] for row in matrix]
    if not work:
        return work, ()
    rows, cols = len(work), len(work[0])
    pivots: list[int] = []
    row = 0
    for col in range(cols):
        pivot = next((i for i in range(row, rows) if work[i][col]), None)
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        scale = inv(work[row][col], prime)
        work[row] = [(scale * value) % prime for value in work[row]]
        for i in range(rows):
            if i == row or not work[i][col]:
                continue
            factor = work[i][col]
            work[i] = [
                (left - factor * right) % prime
                for left, right in zip(work[i], work[row])
            ]
        pivots.append(col)
        row += 1
        if row == rows:
            break
    return work, tuple(pivots)


def rank(matrix: list[list[int]], prime: int) -> int:
    return len(rref(matrix, prime)[1])


def nullspace(matrix: list[list[int]], prime: int) -> list[list[int]]:
    reduced, pivots = rref(matrix, prime)
    cols = len(matrix[0])
    free = [col for col in range(cols) if col not in pivots]
    basis: list[list[int]] = []
    for free_col in free:
        vector = [0] * cols
        vector[free_col] = 1
        for row, pivot in enumerate(pivots):
            vector[pivot] = (-reduced[row][free_col]) % prime
        basis.append(vector)
    return basis


def same_span(left: list[list[int]], right: list[list[int]], prime: int) -> bool:
    return (
        rank(left, prime)
        == rank(right, prime)
        == rank(left + right, prime)
    )


def shifts(generator: tuple[int, ...], width: int) -> list[list[int]]:
    count = width - len(generator) + 1
    return [
        [0] * offset + list(generator) + [0] * (count - offset - 1)
        for offset in range(count)
    ]


def hankel(sequence: tuple[int, ...], columns: int) -> list[list[int]]:
    rows = len(sequence) - columns + 1
    return [list(sequence[i : i + columns]) for i in range(rows)]


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    return [list(column) for column in zip(*matrix)]


def normalize(vector: tuple[int, ...], prime: int) -> tuple[int, ...]:
    first = next(value for value in vector if value % prime)
    scale = inv(first, prime)
    return tuple((scale * value) % prime for value in vector)


def check_principal_kernels() -> int:
    prime, length, radius = 3, 6, 2
    columns = radius + 1
    checked = 0
    for sequence in itertools.product(range(prime), repeat=length):
        matrix = hankel(sequence, columns)
        rho = rank(matrix, prime)
        if rho >= min(len(matrix), columns):
            continue
        right = nullspace(matrix, prime)
        left = nullspace(transpose(matrix), prime)
        candidates = {
            normalize(candidate, prime)
            for candidate in itertools.product(range(prime), repeat=rho + 1)
            if any(candidate)
        }
        witnesses = [
            candidate
            for candidate in candidates
            if same_span(right, shifts(candidate, columns), prime)
            and same_span(left, shifts(candidate, len(matrix)), prime)
        ]
        assert witnesses
        checked += 1
    # The remaining 648 sequences have full column rank and belong to the
    # already-closed maximal-minor branch.
    assert checked == 81
    return checked


def check_moving_family() -> int:
    prime = 101
    checked = 0
    for e in (1, 2, 3):
        rho = 3 * e
        length = 2 * rho + 2
        y0 = [0] * length
        y1 = [0] * length
        y0[3 * e + 2] = 1
        y1[3 * e - 1] = 1
        for gamma in (0, 2, 7):
            sequence = tuple(
                (left + gamma * right) % prime for left, right in zip(y0, y1)
            )
            matrix = hankel(sequence, rho + 1)
            q = [0] * (rho + 1)
            for j in range(e + 1):
                q[3 * j] = pow(-gamma, j, prime)
            assert all(
                sum(value * coefficient for value, coefficient in zip(row, q))
                % prime
                == 0
                for row in matrix
            )
            assert rank(matrix, prime) == rho
            checked += 1

    # The first member is the sharp route fence R=8, r=3: its endpoint
    # kernels are distinct, so the generic kernel genuinely moves.
    m0 = hankel(tuple([0, 0, 0, 0, 0, 1, 0, 0]), 4)
    m1 = hankel(tuple([0, 0, 1, 0, 0, 0, 0, 0]), 4)
    assert rank(m0, prime) == rank(m1, prime) == 3
    assert rank(nullspace(m0, prime) + nullspace(m1, prime), prime) == 2
    return checked


def check_official_arithmetic() -> int:
    n_domain = 1 << 41
    redundancy = 1 << 40

    # A >= 9 follows from the coarse inequality; A=7 is the exact parity
    # edge, and A=5 is the load-bearing final included profile.
    for a in (9, 11, 101):
        rho = (redundancy + 1 - a) // 2
        assert a * (rho + a) >= 2 * n_domain

    a = 7
    rho = redundancy // 2 - 3
    assert 4 * rho - n_domain + 21 == 9

    a = 5
    rho = redundancy // 2 - 2
    s = (rho - 6) // 2
    d = rho - s
    assert (n_domain - s) // d == 6
    assert rho - a + (n_domain - s) // d == rho + 1

    # Mutations at the two terminal profiles remain deliberately unproved.
    assert redundancy + 1 - 2 * (redundancy // 2 - 1) == 3
    assert redundancy + 1 - 2 * (redundancy // 2) == 1
    return 7


def main() -> None:
    principal = check_principal_kernels()
    moving = check_moving_family()
    arithmetic = check_official_arithmetic()

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    node_id = "rate_half_ca_hankel_minimal_index_budget"
    assert nodes[node_id]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    for dependency in (
        "rate_half_ca_hankel_split_pencil_equivalence",
        "rate_half_ca_hankel_fullrank_branch",
        "rate_half_ca_hankel_fixed_kernel_branch",
        "rate_half_quadratic_exact_range",
    ):
        assert (dependency, node_id, "req") in edges
    assert (node_id, "rate_half_band_closure", "ev") in edges

    print(
        "RATE_HALF_CA_HANKEL_MINIMAL_INDEX_BUDGET_PASS "
        f"principal={principal} moving={moving} arithmetic={arithmetic}"
    )


if __name__ == "__main__":
    main()
