#!/usr/bin/env python3
"""Replay the XR split-pencil rank-two support atlas."""

from __future__ import annotations

import copy
import itertools
import json
from pathlib import Path


HERE = Path(__file__).resolve()
REPO_ROOT = HERE.parents[3] if len(HERE.parents) > 3 else Path.cwd()
ROOT = REPO_ROOT if (REPO_ROOT / "dag.json").exists() else Path.cwd()
DAG = ROOT / "dag.json"
NODE = "xr_split_pencil_trade_rank_two_support_atlas"
DEPENDENCY = "xr_split_pencil_trade_rank_two_localization"
CONSUMERS = ("xr_highcore_collision_count", "xr_lowcore_spread_heart")

EXPECTED = {
    (4, 6, (1, 1, 1, 1)),
    (4, 7, (1, 2, 2, 2)),
    (4, 8, (2, 2, 2, 2)),
    (5, 6, (1, 1, 1, 1, 1)),
    (6, 6, (1, 1, 1, 1, 1, 1)),
}


def enumerate_profiles(pair_cap: int) -> set[tuple[int, int, tuple[int, ...]]]:
    found: set[tuple[int, int, tuple[int, ...]]] = set()
    for t in range(4, 21):
        upper = pair_cap * t // (t - 2)
        for active in range(6, upper + 1):
            choices = range(1, active - 4)
            for zeros in itertools.combinations_with_replacement(choices, t):
                if sum(zeros) > active:
                    continue
                if zeros[0] + zeros[1] < active - pair_cap:
                    continue
                found.add((t, active, zeros))
    return found


def inv(value: int, prime: int) -> int:
    return pow(value % prime, prime - 2, prime)


def matrix_rank(matrix: list[list[int]], prime: int) -> int:
    rows = [row[:] for row in matrix]
    rank = 0
    width = len(rows[0])
    for col in range(width):
        pivot = next((r for r in range(rank, len(rows)) if rows[r][col] % prime), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = inv(rows[rank][col], prime)
        rows[rank] = [(scale * value) % prime for value in rows[rank]]
        for r in range(len(rows)):
            if r == rank or rows[r][col] % prime == 0:
                continue
            factor = rows[r][col] % prime
            rows[r] = [
                (left - factor * right) % prime
                for left, right in zip(rows[r], rows[rank])
            ]
        rank += 1
        if rank == len(rows):
            break
    return rank


def witness(active: int, rows: int, prime: int = 101) -> tuple[int, tuple[int, ...]]:
    if active == 6:
        domain = list(range(6))
        exponent = 1
        parameters = list(range(rows))
    elif active == 7:
        domain = [0, 1, -1, 2, -2, 3, -3]
        exponent = 2
        parameters = [0, 1, 4, 9]
    elif active == 8:
        domain = [1, -1, 2, -2, 3, -3, 4, -4]
        exponent = 2
        parameters = [1, 4, 9, 16]
    else:
        raise AssertionError(active)

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

    matrix = []
    for coefficient, parameter in zip(barycentric, parameters):
        matrix.append(
            [
                coefficient
                * (pow(value, exponent, prime) - parameter)
                * inv(denominator, prime)
                % prime
                for value, denominator in zip(domain, denominators)
            ]
        )

    if matrix_rank(matrix, prime) != 2:
        raise AssertionError("witness rank")
    for row in matrix:
        for degree in range(4):
            if sum(value * pow(x, degree, prime) for value, x in zip(row, domain)) % prime:
                raise AssertionError("row is not dual GRS4")
    for column in zip(*matrix):
        if sum(column) % prime:
            raise AssertionError("first trade identity")
        if sum(parameter * value for parameter, value in zip(parameters, column)) % prime:
            raise AssertionError("second trade identity")

    supports = [{j for j, value in enumerate(row) if value % prime} for row in matrix]
    if min(map(len, supports)) < 5:
        raise AssertionError("row distance")
    if max(len(left & right) for left, right in itertools.combinations(supports, 2)) > 4:
        raise AssertionError("pair cap")
    zeros = tuple(sorted(active - len(support) for support in supports))
    if (rows, active, zeros) not in EXPECTED:
        raise AssertionError((rows, active, zeros))
    return matrix_rank(matrix, prime), zeros


def validate_dag(data: dict[str, object]) -> None:
    nodes = {row["id"]: row for row in data["nodes"]}
    if nodes.get(NODE, {}).get("status") != "PROVED":
        raise AssertionError("node status")
    edges = {(row["from"], row["to"], row["kind"]) for row in data["edges"]}
    if (DEPENDENCY, NODE, "req") not in edges:
        raise AssertionError("dependency edge")
    for consumer in CONSUMERS:
        if (NODE, consumer, "ev") not in edges:
            raise AssertionError(("consumer edge", consumer))


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
    if any(enumerate_profiles(cap) for cap in (1, 2, 3)):
        raise AssertionError("pair-cap-three exclusion")
    profiles = enumerate_profiles(4)
    if profiles != EXPECTED:
        raise AssertionError((profiles, EXPECTED))
    witnesses = [witness(active, rows) for rows, active, _ in sorted(EXPECTED)]
    dag = json.loads(DAG.read_text())
    validate_dag(dag)
    mutations = mutation_controls(dag)
    print(
        "XR_SPLIT_PENCIL_TRADE_RANK_TWO_SUPPORT_ATLAS_PASS "
        f"profiles={len(profiles)} witnesses={len(witnesses)} "
        f"mutations={mutations}/{mutations}"
    )


if __name__ == "__main__":
    main()
