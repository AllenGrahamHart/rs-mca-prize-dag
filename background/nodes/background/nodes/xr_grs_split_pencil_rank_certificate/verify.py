#!/usr/bin/env python3
"""Replay the XR GRS split-pencil rank certificate."""

from __future__ import annotations

import copy
import itertools
import json
from pathlib import Path


HERE = Path(__file__).resolve()
REPO_ROOT = HERE.parents[3] if len(HERE.parents) > 3 else Path.cwd()
ROOT = REPO_ROOT if (REPO_ROOT / "dag.json").exists() else Path.cwd()
DAG = ROOT / "dag.json"
NODE = "xr_grs_split_pencil_rank_certificate"
DEPENDENCIES = (
    "xr_rank_five_divided_difference_clique_bridge",
    "xr_lowcore_u0_v1_grs_defect_reduction",
)
CONSUMERS = ("xr_highcore_collision_count", "xr_lowcore_spread_heart")
PRIME = 101


def inverse(value: int) -> int:
    return pow(value % PRIME, PRIME - 2, PRIME)


def divided_difference_row(subset: tuple[int, ...], domain: tuple[int, ...]) -> list[int]:
    row = [0] * len(domain)
    positions = {point: index for index, point in enumerate(domain)}
    for point in subset:
        denominator = 1
        for other in subset:
            if other != point:
                denominator = denominator * (point - other) % PRIME
        row[positions[point]] = inverse(denominator)
    return row


def rank(matrix: list[list[int]]) -> int:
    work = [[entry % PRIME for entry in row] for row in matrix]
    pivot_row = 0
    for column in range(len(work[0])):
        pivot = next(
            (row for row in range(pivot_row, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = inverse(work[pivot_row][column])
        work[pivot_row] = [value * scale % PRIME for value in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row:
                continue
            scale = work[row][column]
            work[row] = [
                (left - scale * right) % PRIME
                for left, right in zip(work[row], work[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_row


def dot(row: list[int], vector: list[int]) -> int:
    return sum(left * right for left, right in zip(row, vector)) % PRIME


def finite_rank_fixture() -> tuple[int, int, int, int]:
    domain = tuple(range(1, 13))
    blocks = (
        (1, 2, 3, 4, 5, 6),
        (1, 2, 3, 4, 7, 8),
        (1, 2, 3, 4, 9, 10),
    )
    colors = (0, 7, 11)
    q = [pow(x, 4, PRIME) for x in domain]
    core = blocks[0][:4]
    core_q = {x: pow(x, 4, PRIME) for x in core}

    def interpolate(x: int) -> int:
        total = 0
        for point, value in core_q.items():
            numerator = 1
            denominator = 1
            for other in core_q:
                if other == point:
                    continue
                numerator = numerator * (x - other) % PRIME
                denominator = denominator * (point - other) % PRIME
            total += value * numerator * inverse(denominator)
        return total % PRIME

    direction = [(value - interpolate(x)) % PRIME for x, value in zip(domain, q)]
    u = [17 * value % PRIME for value in direction]
    for block, color in zip(blocks, colors):
        for x in block[4:]:
            u[domain.index(x)] = color * direction[domain.index(x)] % PRIME
    for x in core:
        u[domain.index(x)] = 0

    matrix = []
    parity_rows = 0
    for block, color in zip(blocks, colors):
        base = block[:4]
        for x in block[4:]:
            row = divided_difference_row(tuple(sorted(base + (x,))), domain)
            matrix.append(row + [(-color * value) % PRIME for value in row])
            parity_rows += 1
    if any(dot(row, u + q) for row in matrix):
        raise AssertionError("candidate pair not in kernel")
    corrupted = list(u)
    corrupted[domain.index(5)] = (corrupted[domain.index(5)] + 1) % PRIME
    corruptions_caught = int(any(dot(row, corrupted + q) for row in matrix))
    if corruptions_caught != 1:
        raise AssertionError("corrupted candidate remained in kernel")
    for degree_left in range(4):
        left = [pow(x, degree_left, PRIME) for x in domain]
        for degree_right in range(4):
            right = [pow(x, degree_right, PRIME) for x in domain]
            if any(dot(row, left + right) for row in matrix):
                raise AssertionError("cubic pair not in kernel")
    matrix_rank = rank(matrix)
    if matrix_rank > 2 * len(domain) - 9:
        raise AssertionError(matrix_rank)
    return parity_rows, matrix_rank, 2 * len(domain) - 9, corruptions_caught


def six_face_fixture() -> tuple[int, int, int]:
    points = (2, 5, 9, 14, 20, 27)
    q_values = {x: (pow(x, 5, PRIME) + 3 * pow(x, 4, PRIME)) % PRIME for x in points}
    u_values = {x: (7 * pow(x, 5, PRIME) + 11 * pow(x, 4, PRIME)) % PRIME for x in points}

    def dd(values: dict[int, int], subset: tuple[int, ...]) -> int:
        row = divided_difference_row(subset, points)
        return dot(row, [values[x] for x in points])

    q_faces = []
    u_faces = []
    colors = []
    for omitted in points:
        face = tuple(x for x in points if x != omitted)
        qdd = dd(q_values, face)
        udd = dd(u_values, face)
        if qdd == 0:
            raise AssertionError("zero denominator")
        q_faces.append(qdd)
        u_faces.append(udd)
        colors.append(udd * inverse(qdd) % PRIME)

    def affine(values: list[int]) -> bool:
        slope = (values[1] - values[0]) * inverse(points[1] - points[0]) % PRIME
        intercept = (values[0] - slope * points[0]) % PRIME
        return all(value == (intercept + slope * point) % PRIME for point, value in zip(points, values))

    if not affine(q_faces) or not affine(u_faces):
        raise AssertionError("facet divided differences are not affine")
    if len(set(colors)) != len(points):
        raise AssertionError(("nonconstant Mobius map not injective", colors))
    constant_values = {
        x: (7 * q_values[x] + 13 * pow(x, 3, PRIME)) % PRIME for x in points
    }
    constant_colors = []
    for omitted in points:
        face = tuple(x for x in points if x != omitted)
        constant_colors.append(dd(constant_values, face) * inverse(dd(q_values, face)) % PRIME)
    if set(constant_colors) != {7}:
        raise AssertionError(("constant Mobius branch failed", constant_colors))
    return len(points), len(set(colors)), len(set(constant_colors))


def official_arithmetic() -> list[int]:
    ranks = [2 * length - 8 for length in (772, 900, 964)]
    if ranks != [1536, 1792, 1920]:
        raise AssertionError(ranks)
    return ranks


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


def mutation_controls(dag: dict[str, object]) -> int:
    mutations = []
    changed = copy.deepcopy(dag)
    next(row for row in changed["nodes"] if row["id"] == NODE)["status"] = "TARGET"
    mutations.append(changed)
    changed = copy.deepcopy(dag)
    changed["edges"] = [
        row
        for row in changed["edges"]
        if not (row["from"] == DEPENDENCIES[0] and row["to"] == NODE)
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
    parity_rows, matrix_rank, rank_ceiling, corruptions = finite_rank_fixture()
    faces, colors, constant_colors = six_face_fixture()
    official = official_arithmetic()
    dag = json.loads(DAG.read_text())
    validate_dag(dag)
    mutations = mutation_controls(dag)
    print(
        "XR_GRS_SPLIT_PENCIL_RANK_CERTIFICATE_PASS "
        f"rank={parity_rows}:{matrix_rank}:{rank_ceiling}:{corruptions} "
        f"faces={faces}:{colors}:{constant_colors} "
        f"official={','.join(map(str, official))} "
        f"mutations={mutations}/{mutations}"
    )


if __name__ == "__main__":
    main()
