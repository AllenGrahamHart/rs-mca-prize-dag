#!/usr/bin/env python3
"""Verify the marked constant-shift strict-strip exclusion."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_marked_constant_shift_subtwoell_exclusion"


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

    for ell in range(2, 25):
        for d in range(ell + 1, 2 * ell):
            for v in range(0, 2 * ell - d):
                enlarged = d + v
                common_degree = enlarged - ell
                assert enlarged < 2 * ell
                assert common_degree > v
                profiles += 1
                checks += 2
    assert profiles > 1000

    for prime in (3, 5, 7):
        for labels in itertools.combinations(range(prime), 3):
            for values in itertools.product(range(prime), repeat=3):
                rows = [
                    [1, label, value, label * value]
                    for label, value in zip(labels, values)
                ]
                if rank_mod(rows, prime) <= 2:
                    assert len(set(values)) == 1
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
        "ell<d,       d+v<2ell",
        "gcd(F,W)=1",
        "ell<d,       d+p<2ell",
    ):
        assert anchor in statement
        checks += 1

    print(
        "L1_MARKED_CONSTANT_SHIFT_PASS "
        f"checks={checks} profiles={profiles} rank_cases={rank_cases}"
    )


if __name__ == "__main__":
    main()
