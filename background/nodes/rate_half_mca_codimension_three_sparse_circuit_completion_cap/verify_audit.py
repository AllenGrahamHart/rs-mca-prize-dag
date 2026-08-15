#!/usr/bin/env python3
"""Independent finite-field audit of the circuit-completion dichotomy."""

from __future__ import annotations

import hashlib
import itertools
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "87d1bd00338c62a01640e593eec40d0cec20c8e8cbde2c138b482958a458c7e5"


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
    rows = len(work)
    cols = len(work[0])
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
    free = [col for col in range(cols) if col not in pivots]
    basis = []
    for free_col in free:
        vector = [0] * cols
        vector[free_col] = 1
        for row, pivot_col in enumerate(pivots):
            vector[pivot_col] = -work[row][free_col] % prime
        basis.append(vector)
    return basis


def evaluation(point: int, prime: int) -> list[int]:
    return [pow(point, degree, prime) for degree in range(13)]


def projected_columns(constraints: list[list[int]], prime: int) -> list[list[int]]:
    basis = nullspace_mod(constraints, prime)
    assert len(basis) == 10
    return [
        [sum(coefficient * pow(point, degree, prime)
             for degree, coefficient in enumerate(polynomial)) % prime
         for polynomial in basis]
        for point in range(13)
    ]


def subset_rank(columns: list[list[int]], subset: tuple[int, ...], prime: int) -> int:
    return rank_mod([[columns[col][row] for col in subset] for row in range(10)], prime)


def circuits(columns: list[list[int]], prime: int) -> set[tuple[int, ...]]:
    found: set[tuple[int, ...]] = set()
    for size in range(2, 6):
        for subset in itertools.combinations(range(13), size):
            if subset_rank(columns, subset, prime) != size - 1:
                continue
            if all(subset_rank(columns, subset[:i] + subset[i + 1:], prime) == size - 1
                   for i in range(size)):
                found.add(subset)
    return found


def completion_map(found: set[tuple[int, ...]]) -> dict[tuple[int, ...], set[int]]:
    result: dict[tuple[int, ...], set[int]] = {}
    for circuit in found:
        for index, point in enumerate(circuit):
            base = circuit[:index] + circuit[index + 1:]
            result.setdefault(base, set()).add(point)
    return result


def low_full_rank_count(columns: list[list[int]], prime: int) -> int:
    count = 0
    for subset in itertools.combinations(range(13), 11):
        if subset_rank(columns, subset, prime) != 10:
            continue
        matrix = [[columns[col][row] for col in subset] for row in range(10)]
        relation = nullspace_mod(matrix, prime)
        assert len(relation) == 1
        if sum(value != 0 for value in relation[0]) <= 5:
            count += 1
    return count


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    parameters = json.loads(CONTRACT.read_text())["parameters"]
    prime = 17
    evaluations = [evaluation(point, prime) for point in range(13)]

    structured_constraints = [
        [(left - right) % prime for left, right in zip(evaluations[point], evaluations[0])]
        for point in (1, 2, 3)
    ]
    structured_columns = projected_columns(structured_constraints, prime)
    assert all(any(value for value in column) for column in structured_columns)
    structured_circuits = circuits(structured_columns, prime)
    structured_completions = completion_map(structured_circuits)
    assert structured_completions[(0,)] == {1, 2, 3}
    assert all(set(circuit) <= {0, 1, 2, 3} for circuit in structured_circuits)

    dense_weights = [1, 1, 1, 1, 1, -5]
    dense_constraint = [
        sum(weight * evaluations[point][degree]
            for weight, point in zip(dense_weights, range(4, 10))) % prime
        for degree in range(13)
    ]
    unstructured_constraints = structured_constraints[:2] + [dense_constraint]
    unstructured_columns = projected_columns(unstructured_constraints, prime)
    assert all(any(value for value in column) for column in unstructured_columns)
    unstructured_circuits = circuits(unstructured_columns, prime)
    unstructured_completions = completion_map(unstructured_circuits)
    assert max(map(len, unstructured_completions.values())) == 2

    m = parameters["official_support_size"]
    structured_cap = sum(comb(7, support) * comb(m - support, 11 - support)
                         for support in range(2, 6))
    terms = {
        str(support): 2 * comb(m, support - 1) * comb(m - support - 1, 11 - support) // support
        for support in range(2, 6)
    }
    assert structured_cap == parameters["structured_carrier_cap"]
    assert terms == parameters["unstructured_support_terms"]
    assert sum(terms.values()) == parameters["per_record_sparse_incidence_cap"]
    assert low_full_rank_count(structured_columns, prime) <= sum(
        comb(7, support) * comb(13 - support, 11 - support)
        for support in range(2, 6)
    )
    assert low_full_rank_count(unstructured_columns, prime) <= sum(
        2 * comb(13, support - 1) * comb(12 - support, 11 - support) // support
        for support in range(2, 6)
    )

    print(
        "PASS codimension-three sparse circuit audit: "
        f"structured circuits {len(structured_circuits)}, "
        f"unstructured circuits {len(unstructured_circuits)}, "
        f"max completions {max(map(len, unstructured_completions.values()))}"
    )


if __name__ == "__main__":
    main()
