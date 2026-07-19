#!/usr/bin/env python3
"""Replay the XR collision-direction star configuration."""

from __future__ import annotations

import copy
import itertools
import json
from math import comb, prod
from pathlib import Path


HERE = Path(__file__).resolve()
REPO_ROOT = HERE.parents[3] if len(HERE.parents) > 3 else Path.cwd()
ROOT = REPO_ROOT if (REPO_ROOT / "dag.json").exists() else Path.cwd()
DAG = ROOT / "dag.json"
NODE = "xr_rank_five_direction_star_configuration"
DEPENDENCY = "xr_rank_five_divided_difference_clique_bridge"
CONSUMER = "xr_highcore_collision_count"
PRIME = 101


def inverse(value: int) -> int:
    return pow(value % PRIME, PRIME - 2, PRIME)


def interpolate_coefficients(points: tuple[int, ...]) -> tuple[int, ...]:
    matrix = [
        [pow(x, degree, PRIME) for degree in range(4)] + [pow(x, 4, PRIME)]
        for x in points
    ]
    for column in range(4):
        pivot = next(row for row in range(column, 4) if matrix[row][column])
        matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
        scale = inverse(matrix[column][column])
        matrix[column] = [value * scale % PRIME for value in matrix[column]]
        for row in range(4):
            if row == column:
                continue
            scale = matrix[row][column]
            matrix[row] = [
                (left - scale * right) % PRIME
                for left, right in zip(matrix[row], matrix[column])
            ]
    return tuple(matrix[row][4] for row in range(4))


def monomial_exponents(max_degree: int) -> list[tuple[int, ...]]:
    return [
        exponents
        for exponents in itertools.product(range(max_degree + 1), repeat=4)
        if sum(exponents) <= max_degree
    ]


def rank(matrix: list[list[int]]) -> int:
    work = [row[:] for row in matrix]
    rows = len(work)
    columns = len(work[0])
    pivot_row = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(pivot_row, rows) if work[row][column]), None
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = inverse(work[pivot_row][column])
        work[pivot_row] = [value * scale % PRIME for value in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row:
                continue
            scale = work[row][column]
            work[row] = [
                (left - scale * right) % PRIME
                for left, right in zip(work[row], work[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def finite_fixture() -> tuple[int, int, list[int]]:
    domain = tuple(range(1, 8))
    vertices = [
        interpolate_coefficients(points)
        for points in itertools.combinations(domain, 4)
    ]
    exponents = monomial_exponents(3)
    evaluation = [
        [
            prod(
                pow(coordinate, exponent, PRIME)
                for coordinate, exponent in zip(vertex, powers)
            )
            % PRIME
            for powers in exponents
        ]
        for vertex in vertices
    ]
    matrix_rank = rank(evaluation)
    if len(vertices) != 35 or len(exponents) != 35 or matrix_rank != 35:
        raise AssertionError((len(vertices), len(exponents), matrix_rank))

    sharp_weights = []
    for degree in range(4):
        chosen = set(domain[:degree])
        weight = sum(
            chosen.isdisjoint(points)
            for points in itertools.combinations(domain, 4)
        )
        sharp_weights.append(weight)
        if weight != comb(7 - degree, 4):
            raise AssertionError((degree, weight))
    return len(vertices), matrix_rank, sharp_weights


def official_arithmetic() -> list[int]:
    rows = ((9, 1), (9, 3), (7, 4))
    degrees = []
    for size, complement in rows:
        degree = max(
            d for d in range(size - 3) if comb(size - d, 4) > complement
        )
        degrees.append(degree)
    if degrees != [4, 4, 2]:
        raise AssertionError(degrees)
    return degrees


def validate_dag(data: dict[str, object]) -> None:
    nodes = {row["id"]: row for row in data["nodes"]}
    if nodes.get(NODE, {}).get("status") != "PROVED":
        raise AssertionError("node status")
    edges = {(row["from"], row["to"], row["kind"]) for row in data["edges"]}
    if (DEPENDENCY, NODE, "req") not in edges:
        raise AssertionError("dependency edge")
    if (NODE, CONSUMER, "ev") not in edges:
        raise AssertionError("consumer edge")


def mutation_controls(dag: dict[str, object]) -> int:
    mutations = []
    changed = copy.deepcopy(dag)
    next(row for row in changed["nodes"] if row["id"] == NODE)["status"] = "TARGET"
    mutations.append(changed)
    changed = copy.deepcopy(dag)
    changed["edges"] = [
        row
        for row in changed["edges"]
        if not (row["from"] == DEPENDENCY and row["to"] == NODE)
    ]
    mutations.append(changed)
    caught = 0
    for mutation in mutations:
        try:
            validate_dag(mutation)
        except AssertionError:
            caught += 1
    if caught != len(mutations):
        raise AssertionError((caught, len(mutations)))
    return caught


def main() -> None:
    vertices, matrix_rank, weights = finite_fixture()
    degrees = official_arithmetic()
    dag = json.loads(DAG.read_text())
    validate_dag(dag)
    mutations = mutation_controls(dag)
    print(
        "XR_RANK_FIVE_DIRECTION_STAR_CONFIGURATION_PASS "
        f"fixture={vertices}:{matrix_rank} "
        f"weights={','.join(map(str, weights))} "
        f"degrees={','.join(map(str, degrees))} "
        f"mutations={mutations}/{mutations}"
    )


if __name__ == "__main__":
    main()
