#!/usr/bin/env python3
"""Independent finite-field audit for the completion dimension ladder."""

from __future__ import annotations

import json
from itertools import combinations
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def rank_mod(matrix: list[list[int]], prime: int) -> int:
    work = [row[:] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    rank = 0
    for col in range(cols):
        pivot = next((row for row in range(rank, rows) if work[row][col] % prime), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][col], -1, prime)
        work[rank] = [(value * inverse) % prime for value in work[rank]]
        for row in range(rows):
            if row == rank:
                continue
            factor = work[row][col] % prime
            if factor:
                work[row] = [
                    (left - factor * right) % prime
                    for left, right in zip(work[row], work[rank])
                ]
        rank += 1
    return rank


def nullspace_mod(matrix: list[list[int]], prime: int) -> list[list[int]]:
    work = [row[:] for row in matrix]
    rows, cols = len(work), len(work[0])
    pivots: list[int] = []
    rank = 0
    for col in range(cols):
        pivot = next((row for row in range(rank, rows) if work[row][col] % prime), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][col], -1, prime)
        work[rank] = [(value * inverse) % prime for value in work[rank]]
        for row in range(rows):
            if row == rank:
                continue
            factor = work[row][col] % prime
            if factor:
                work[row] = [
                    (left - factor * right) % prime
                    for left, right in zip(work[row], work[rank])
                ]
        pivots.append(col)
        rank += 1
    basis: list[list[int]] = []
    for free in (col for col in range(cols) if col not in pivots):
        vector = [0] * cols
        vector[free] = 1
        for row, pivot in enumerate(pivots):
            vector[pivot] = -work[row][free] % prime
        basis.append(vector)
    return basis


def circuit_model(constraints: list[list[int]], prime: int) -> set[tuple[int, ...]]:
    basis = nullspace_mod(constraints, prime)
    require(len(basis) == 10, "toy correction dimension")
    columns = [
        [
            sum(coefficient * pow(point, degree, prime)
                for degree, coefficient in enumerate(polynomial)) % prime
            for polynomial in basis
        ]
        for point in range(14)
    ]
    require(all(any(column) for column in columns), "toy basepoint free")

    def subset_rank(subset: tuple[int, ...]) -> int:
        return rank_mod(
            [[columns[column][row] for column in subset] for row in range(10)],
            prime,
        )

    circuits: set[tuple[int, ...]] = set()
    for size in range(2, 6):
        for subset in combinations(range(14), size):
            if subset_rank(subset) != size - 1:
                continue
            if all(
                subset_rank(subset[:index] + subset[index + 1:]) == size - 1
                for index in range(size)
            ):
                circuits.add(subset)
    return circuits


def completion_maximum(circuits: set[tuple[int, ...]]) -> int:
    completions: dict[tuple[int, ...], set[int]] = {}
    for circuit in circuits:
        for index, point in enumerate(circuit):
            deletion = circuit[:index] + circuit[index + 1:]
            completions.setdefault(deletion, set()).add(point)
    return max(map(len, completions.values()))


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    endpoints: dict[str, dict[str, int]] = {}
    for kprime in (14, 21):
        q = kprime - 10
        m = 67472 + kprime
        structured = sum(
            comb(q + 4, support) * comb(m - support, 11 - support)
            for support in range(2, 6)
        )
        unstructured = sum(
            comb(m, support - 1) * (q - 1)
            * comb(m - support + 1 - (q - 1), 11 - support) // support
            for support in range(2, 6)
        )
        endpoints[str(kprime)] = {"structured": structured, "unstructured": unstructured}
    require(endpoints == p["endpoint_totals"], "independent endpoints")

    prime = 17
    evaluations = [
        [pow(point, degree, prime) for degree in range(14)]
        for point in range(14)
    ]
    structured_constraints = [
        [(left - right) % prime for left, right in zip(evaluations[point], evaluations[0])]
        for point in (1, 2, 3, 4)
    ]
    structured = circuit_model(structured_constraints, prime)
    require(len(structured) == 10, "structured circuit count")
    require(completion_maximum(structured) == 4, "structured four completions")
    require(all(set(circuit) <= {0, 1, 2, 3, 4} for circuit in structured), "structured carrier")

    dense = [
        sum(weight * evaluations[point][degree]
            for weight, point in zip((1, 1, 1, 1, 1, -5), range(5, 11))) % prime
        for degree in range(14)
    ]
    unstructured = circuit_model(structured_constraints[:3] + [dense], prime)
    require(len(unstructured) == 6, "unstructured circuit count")
    require(completion_maximum(unstructured) == 3, "unstructured three completions")
    print(
        "PASS sparse-circuit completion dimension ladder independent: "
        f"endpoints {len(endpoints)}, GF(17) circuits {len(structured)}/{len(unstructured)}, "
        "completion maxima 4/3"
    )


if __name__ == "__main__":
    main()
