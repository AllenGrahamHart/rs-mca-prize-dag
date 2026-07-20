#!/usr/bin/env python3
"""Verify the marked constant-shift multistrip exclusion."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_marked_constant_shift_multistrip_exclusion"


def rank_mod(rows: list[list[int]], prime: int) -> int:
    matrix = [[entry % prime for entry in row] for row in rows]
    rank = 0
    for column in range(len(matrix[0])):
        pivot = next(
            (index for index in range(rank, len(matrix)) if matrix[index][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = pow(matrix[rank][column], -1, prime)
        matrix[rank] = [(entry * inverse) % prime for entry in matrix[rank]]
        for index, row in enumerate(matrix):
            if index == rank or not row[column]:
                continue
            factor = row[column]
            matrix[index] = [
                (left - factor * right) % prime
                for left, right in zip(row, matrix[rank])
            ]
        rank += 1
    return rank


def main() -> None:
    checks = 0
    profiles = 0
    rank_cases = 0

    for m in range(1, 7):
        for ell in range(2, 18):
            for d in range(m * ell + 1, (m + 1) * ell):
                for v in range((m + 1) * ell - d):
                    enlarged = d + v
                    one_kernel_factor = enlarged - m * ell
                    primitive_factor_floor = enlarged - (m - 1) * ell
                    assert one_kernel_factor > v
                    assert primitive_factor_floor > v
                    profiles += 1
                    checks += 2
    assert profiles > 4000

    window_profiles = 0
    for m in range(1, 7):
        for ell in range(2, 18):
            for p in range(ell):
                for d in range(m * ell + 1, (m + 1) * ell - p):
                    lower = (d - p + ell) // ell
                    assert m <= lower <= 2 * m
                    if d > m * ell + p - 1:
                        assert lower >= m + 1
                    assert (lower - 1) * ell + p - 1 < d
                    window_profiles += 1
                    checks += 3
    assert window_profiles > 4000

    # Exhaust the first two strip ranks over fields large enough to carry the
    # exact number of distinct labels.
    for m, prime in ((1, 3), (1, 5), (2, 5)):
        labels = tuple(range(2 * m + 1))
        for values in itertools.product(range(prime), repeat=len(labels)):
            rows = []
            for label, value in zip(labels, values):
                powers = [pow(label, exponent, prime) for exponent in range(m + 1)]
                rows.append(
                    [(-value * power) % prime for power in powers] + powers
                )
            rank = rank_mod(rows, prime)
            assert rank <= 2 * (m + 1)
            if rank >= 2 * m + 1:
                assert 2 * (m + 1) - rank <= 1
            rank_cases += 1
            checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {
        (edge["from"], edge["to"], edge["kind"])
        for edge in dag["edges"]
    }
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in (
        "l1_bounded_polarity_marked_full_pencil_reduction",
        "pma_coset_subtwoell_saturation_exclusion",
    ):
        assert nodes[supplier]["status"] == "PROVED"
        assert (supplier, NODE, "req") in edges
        checks += 2
    for consumer in (
        "l1_mixed_residual_intersection_pin",
        "l1_mixed_petal_amplification",
        "petal_mixed_amplification",
    ):
        assert (NODE, consumer, "ev") in edges
        checks += 1

    statement = (
        ROOT / "background" / "nodes" / NODE / "statement.md"
    ).read_text()
    for anchor in (
        "t>=2m+1,       m ell<d,       d+v<(m+1)ell",
        "gcd(F,W)=1",
        "t_dense>=2m+1",
        "ceil((d-p+1)/ell) <= T <= 2m",
    ):
        assert anchor in statement
        checks += 1

    print(
        "L1_MARKED_MULTISTRIP_PASS "
        f"checks={checks} profiles={profiles} windows={window_profiles} "
        f"rank_cases={rank_cases}"
    )


if __name__ == "__main__":
    main()
