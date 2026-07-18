#!/usr/bin/env python3
"""Replay the XR nonlocal rank-two rational-fiber dictionary."""

from __future__ import annotations

import copy
import itertools
import json
from pathlib import Path


HERE = Path(__file__).resolve()
REPO_ROOT = HERE.parents[3] if len(HERE.parents) > 3 else Path.cwd()
ROOT = REPO_ROOT if (REPO_ROOT / "dag.json").exists() else Path.cwd()
DAG = ROOT / "dag.json"
NODE = "xr_split_pencil_nonlocal_rank_two_rational_fibers"
DEPENDENCIES = {
    "xr_split_pencil_trade_rank_two_support_atlas",
    "xr_split_pencil_six_face_syzygy_quotient",
}
CONSUMERS = ("xr_highcore_collision_count", "xr_lowcore_spread_heart")


def inv(value: int, prime: int) -> int:
    return pow(value % prime, prime - 2, prime)


def rank(matrix: list[list[int]], prime: int) -> int:
    rows = [[value % prime for value in row] for row in matrix]
    pivot_row = 0
    width = len(rows[0])
    for col in range(width):
        pivot = next((r for r in range(pivot_row, len(rows)) if rows[r][col]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        scale = inv(rows[pivot_row][col], prime)
        rows[pivot_row] = [(scale * value) % prime for value in rows[pivot_row]]
        for r in range(len(rows)):
            if r == pivot_row or rows[r][col] == 0:
                continue
            factor = rows[r][col]
            rows[r] = [
                (left - factor * right) % prime
                for left, right in zip(rows[r], rows[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


def build_trade(
    prime: int,
    domain: list[int],
    parameters: list[int],
    exponent: int,
    slope_labels: list[int] | None = None,
) -> tuple[tuple[int, ...], int]:
    slopes = parameters if slope_labels is None else slope_labels
    barycentric = []
    for i, value in enumerate(parameters):
        product = 1
        for j, other in enumerate(parameters):
            if i != j:
                product = product * (value - other) % prime
        barycentric.append(inv(product, prime))

    denominators = []
    for i, value in enumerate(domain):
        product = 1
        for j, other in enumerate(domain):
            if i != j:
                product = product * (value - other) % prime
        denominators.append(product)

    matrix = [
        [
            coefficient
            * (pow(x, exponent, prime) - parameter)
            * inv(denominator, prime)
            % prime
            for x, denominator in zip(domain, denominators)
        ]
        for coefficient, parameter in zip(barycentric, parameters)
    ]
    if rank(matrix, prime) != 2:
        raise AssertionError("trade rank")
    for row in matrix:
        for degree in range(4):
            if sum(value * pow(x, degree, prime) for value, x in zip(row, domain)) % prime:
                raise AssertionError("dual cubic row")
    for column in zip(*matrix):
        if sum(column) % prime:
            raise AssertionError("first trade identity")
        if sum(parameter * value for parameter, value in zip(slopes, column)) % prime:
            raise AssertionError("second trade identity")

    supports = [{j for j, value in enumerate(row) if value % prime} for row in matrix]
    if max(len(a & b) for a, b in itertools.combinations(supports, 2)) > 4:
        raise AssertionError("pair cap")
    zeros = tuple(sorted(len(domain) - len(support) for support in supports))
    return zeros, rank(matrix, prime)


def quadratic_witnesses() -> list[tuple[tuple[int, ...], int]]:
    seven = build_trade(101, [0, 1, -1, 2, -2, 3, -3], [0, 1, 4, 9], 2)
    eight = build_trade(101, [1, -1, 2, -2, 3, -3, 4, -4], [1, 4, 9, 16], 2)
    if seven[0] != (1, 2, 2, 2) or eight[0] != (2, 2, 2, 2):
        raise AssertionError((seven, eight))
    return [seven, eight]


def cubic_witness() -> tuple[tuple[int, ...], int]:
    prime = 103
    fibers: dict[int, list[int]] = {}
    for value in range(1, prime):
        fibers.setdefault(pow(value, 3, prime), []).append(value)
    groups = [(image, roots) for image, roots in sorted(fibers.items()) if len(roots) == 3]
    if len(groups) < 4:
        raise AssertionError("cube fibers")
    chosen = groups[:4]
    domain = [root for _, roots in chosen for root in roots[:2]]
    parameters = [image for image, _ in chosen]
    result = build_trade(prime, domain, parameters, 3)
    if result[0] != (2, 2, 2, 2):
        raise AssertionError(result)
    return result


def mutation_control() -> bool:
    prime = 101
    domain = [1, -1, 2, -2, 3, -3, 4, -4]
    parameters = [1, 4, 9, 16]
    try:
        build_trade(prime, domain, parameters, 2, [1, 4, 9, 17])
    except AssertionError:
        return True
    raise AssertionError("fiber-label mutation survived")


def validate_dag(data: dict[str, object]) -> None:
    nodes = {row["id"]: row for row in data["nodes"]}
    if nodes.get(NODE, {}).get("status") != "PROVED":
        raise AssertionError("node status")
    edges = {(row["from"], row["to"], row["kind"]) for row in data["edges"]}
    for dependency in DEPENDENCIES:
        if (dependency, NODE, "req") not in edges:
            raise AssertionError(("dependency edge", dependency))
    for consumer in CONSUMERS:
        if (NODE, consumer, "ev") not in edges:
            raise AssertionError(("consumer edge", consumer))


def dag_mutation_controls(dag: dict[str, object]) -> int:
    mutations = []
    changed = copy.deepcopy(dag)
    next(row for row in changed["nodes"] if row["id"] == NODE)["status"] = "TARGET"
    mutations.append(changed)
    for dependency in DEPENDENCIES:
        changed = copy.deepcopy(dag)
        changed["edges"] = [
            row
            for row in changed["edges"]
            if not (row["from"] == dependency and row["to"] == NODE)
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
    quadratic = quadratic_witnesses()
    cubic = cubic_witness()
    fiber_mutation = mutation_control()
    dag = json.loads(DAG.read_text())
    validate_dag(dag)
    mutations = dag_mutation_controls(dag)
    print(
        "XR_SPLIT_PENCIL_NONLOCAL_RANK_TWO_RATIONAL_FIBERS_PASS "
        f"quadratic={len(quadratic)} cubic={cubic[1]} "
        f"fiber_mutation={int(fiber_mutation)} dag_mutations={mutations}/{mutations}"
    )


if __name__ == "__main__":
    main()
