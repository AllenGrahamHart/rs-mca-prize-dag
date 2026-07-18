#!/usr/bin/env python3
"""Verify the budget-three incidence types and exact intersection fixture."""

from __future__ import annotations

import json
from itertools import permutations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_intersection_reduction"
CONSUMER = "rate_half_list_adjacent_crossing"
EDGES = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
PERMUTATIONS = tuple(permutations(range(4)))


def compositions(total: int, parts: int, prefix: tuple[int, ...] = ()):
    if parts == 1:
        yield prefix + (total,)
        return
    for value in range(total + 1):
        yield from compositions(total - value, parts - 1, prefix + (value,))


def canonical(singletons: tuple[int, ...], edge_counts: tuple[int, ...]):
    edge_map = {edge: edge_counts[index] for index, edge in enumerate(EDGES)}
    images = []
    for permutation in PERMUTATIONS:
        mapped_singletons = tuple(singletons[permutation[i]] for i in range(4))
        mapped_edges = tuple(
            edge_map[tuple(sorted((permutation[a], permutation[b])))] for a, b in EDGES
        )
        images.append((mapped_singletons, mapped_edges))
    return min(images)


def incidence_types() -> dict[tuple[int, int, int, int], set[tuple]]:
    raw_patterns = (
        (0, 0, 4, 0),
        (0, 0, 5, 1),
        (0, 0, 6, 2),
        (0, 1, 2, 0),
        (0, 1, 3, 1),
        (0, 2, 0, 0),
    )
    quarter = 20
    answer = {}
    for pattern in raw_patterns:
        n0, n1, n2, n4 = pattern
        triples = 4 * quarter - n0 - n1 - n2 - n4
        types = set()
        for singletons in compositions(n1, 4):
            for edge_counts in compositions(n2, 6):
                edge_degrees = tuple(
                    singletons[i]
                    + sum(
                        edge_counts[j]
                        for j, edge in enumerate(EDGES)
                        if i in edge
                    )
                    for i in range(4)
                )
                omitted = tuple(
                    triples + edge_degrees[i] + n4 - (3 * quarter - 1)
                    for i in range(4)
                )
                if min(omitted) < 0 or sum(omitted) != triples:
                    continue
                if any(
                    triples
                    - omitted[a]
                    - omitted[b]
                    + edge_counts[j]
                    + n4
                    > 2 * quarter - 1
                    for j, (a, b) in enumerate(EDGES)
                ):
                    continue
                types.add(canonical(singletons, edge_counts))
        answer[pattern] = types
    return answer


def evaluate(poly: tuple[int, ...], x: int, prime: int) -> int:
    value = 0
    for coefficient in poly[::-1]:
        value = (value * x + coefficient) % prime
    return value


def rank(matrix: list[list[int]], prime: int) -> int:
    work = [row[:] for row in matrix]
    pivot_row = 0
    for column in range(len(work[0])):
        selected = next(
            (row for row in range(pivot_row, len(work)) if work[row][column] % prime),
            None,
        )
        if selected is None:
            continue
        work[pivot_row], work[selected] = work[selected], work[pivot_row]
        inverse = pow(work[pivot_row][column], -1, prime)
        work[pivot_row] = [entry * inverse % prime for entry in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row or not work[row][column]:
                continue
            multiplier = work[row][column]
            work[row] = [
                (left - multiplier * right) % prime
                for left, right in zip(work[row], work[pivot_row], strict=True)
            ]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_row


def intersection_matrix(
    domain: tuple[int, ...], supports: tuple[tuple[int, ...], ...], dimension: int, prime: int
) -> list[list[int]]:
    rows = []
    for coordinate, x in enumerate(domain):
        members = tuple(i for i, support in enumerate(supports) if coordinate in support)
        if len(members) <= 1:
            continue
        powers = tuple(pow(x, degree, prime) for degree in range(dimension))
        if 0 in members:
            base = 0
        else:
            base = members[0]
        for member in members:
            if member == base:
                continue
            row = [0] * (3 * dimension)
            if member:
                offset = (member - 1) * dimension
                row[offset : offset + dimension] = powers
            if base:
                offset = (base - 1) * dimension
                row[offset : offset + dimension] = [(-value) % prime for value in powers]
            rows.append(row)
    return rows


def toy_fixture() -> tuple[int, tuple[int, ...], tuple[int, int, int, int]]:
    prime = 17
    domain = (1, 9, 13, 15, 16, 8, 4, 2)
    polys = (
        (0, 0, 0, 0),
        (11, 2, 8, 7),
        (8, 5, 13, 2),
        (15, 13, 15, 13),
    )
    received = (11, 0, 0, 0, 4, 0, 0, 1)
    words = tuple(tuple(evaluate(poly, x, prime) for x in domain) for poly in polys)
    supports = tuple(
        tuple(index for index, (left, right) in enumerate(zip(word, received, strict=True)) if left == right)
        for word in words
    )
    agreements = tuple(len(support) for support in supports)
    assert agreements == (5, 5, 5, 5)
    assert len(set(words)) == 4
    assert all(len(set(supports[i]) & set(supports[j])) <= 3 for i, j in EDGES)
    degrees = tuple(sum(index in support for support in supports) for index in range(8))
    pattern = tuple(degrees.count(value) for value in (0, 1, 2, 4))
    assert pattern == (0, 1, 2, 0)

    matrix = intersection_matrix(domain, supports, 4, prime)
    coefficient_vector = [entry for poly in polys[1:] for entry in poly]
    assert len(matrix) == len(coefficient_vector) == 12
    assert all(
        sum(left * right for left, right in zip(row, coefficient_vector, strict=True)) % prime == 0
        for row in matrix
    )
    matrix_rank = rank(matrix, prime)
    assert matrix_rank == 11
    mutated = coefficient_vector[:]
    mutated[0] = (mutated[0] + 1) % prime
    assert any(
        sum(left * right for left, right in zip(row, mutated, strict=True)) % prime
        for row in matrix
    )
    return matrix_rank, agreements, pattern


def check_dag() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (NODE, CONSUMER, "ev") in edges


def main() -> None:
    types = incidence_types()
    zero_singletons = (0, 0, 0, 0)
    expected = {
        (0, 0, 4, 0): {
            (zero_singletons, (0, 0, 1, 1, 1, 1)),
            (zero_singletons, (0, 1, 1, 1, 1, 0)),
        },
        (0, 0, 5, 1): {(zero_singletons, (0, 1, 1, 1, 1, 1))},
        (0, 0, 6, 2): {(zero_singletons, (1, 1, 1, 1, 1, 1))},
        (0, 1, 2, 0): {((0, 0, 0, 1), (0, 1, 0, 1, 0, 0))},
        (0, 1, 3, 1): {((0, 0, 0, 1), (1, 1, 0, 1, 0, 0))},
        (0, 2, 0, 0): set(),
    }
    assert types == expected
    assert sum(map(len, types.values())) == 6
    matrix_rank, agreements, pattern = toy_fixture()
    check_dag()
    print(
        "RATE_HALF_LIST_BUDGET_THREE_INTERSECTION_REDUCTION_PASS "
        f"incidence_types=6 toy_rank={matrix_rank}/12 agreements={agreements} "
        f"pattern={pattern} dag=1/1"
    )


if __name__ == "__main__":
    main()
