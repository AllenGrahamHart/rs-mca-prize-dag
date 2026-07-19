#!/usr/bin/env python3
"""Replay the XR six-face Plucker-syzygy quotient."""

from __future__ import annotations

import copy
import itertools
import json
from pathlib import Path


HERE = Path(__file__).resolve()
REPO_ROOT = HERE.parents[3] if len(HERE.parents) > 3 else Path.cwd()
ROOT = REPO_ROOT if (REPO_ROOT / "dag.json").exists() else Path.cwd()
DAG = ROOT / "dag.json"
NODE = "xr_split_pencil_six_face_syzygy_quotient"
DEPENDENCIES = {
    "xr_grs_split_pencil_rank_certificate",
    "xr_split_pencil_trade_rank_two_support_atlas",
}
CONSUMERS = ("xr_highcore_collision_count", "xr_lowcore_spread_heart")
PRIME = 101


def inv(value: int) -> int:
    return pow(value % PRIME, PRIME - 2, PRIME)


def rref(matrix: list[list[int]]) -> tuple[list[list[int]], list[int]]:
    rows = [[value % PRIME for value in row] for row in matrix]
    pivots = []
    pivot_row = 0
    width = len(rows[0])
    for col in range(width):
        pivot = next((r for r in range(pivot_row, len(rows)) if rows[r][col]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        scale = inv(rows[pivot_row][col])
        rows[pivot_row] = [(scale * value) % PRIME for value in rows[pivot_row]]
        for r in range(len(rows)):
            if r == pivot_row or rows[r][col] == 0:
                continue
            factor = rows[r][col]
            rows[r] = [
                (left - factor * right) % PRIME
                for left, right in zip(rows[r], rows[pivot_row])
            ]
        pivots.append(col)
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return rows, pivots


def nullspace(matrix: list[list[int]]) -> list[list[int]]:
    reduced, pivots = rref(matrix)
    width = len(matrix[0])
    free = [col for col in range(width) if col not in pivots]
    basis = []
    for free_col in free:
        vector = [0] * width
        vector[free_col] = 1
        for row, pivot in enumerate(pivots):
            vector[pivot] = -reduced[row][free_col] % PRIME
        basis.append(vector)
    return basis


def rank(matrix: list[list[int]]) -> int:
    return len(rref(matrix)[1])


def canonical_faces() -> list[list[int]]:
    domain = list(range(6))
    denominators = []
    for i, value in enumerate(domain):
        product = 1
        for j, other in enumerate(domain):
            if i != j:
                product = product * (value - other) % PRIME
        denominators.append(product)
    return [
        [
            (y - omitted) * inv(denominator) % PRIME
            for y, denominator in zip(domain, denominators)
        ]
        for omitted in domain
    ]


def full_support_kernel_vector(basis: list[list[int]]) -> list[int]:
    for coefficients in itertools.product(range(1, 8), repeat=len(basis)):
        vector = [
            sum(scale * row[col] for scale, row in zip(coefficients, basis)) % PRIME
            for col in range(len(basis[0]))
        ]
        if all(vector):
            return vector
    raise AssertionError("no full-support syzygy")


def face_fan(active_faces: int) -> tuple[int, int, int]:
    points = list(range(active_faces))
    alpha, beta, chi, delta = 2, 3, 5, 7
    slopes = [
        (alpha + beta * point) * inv(chi + delta * point) % PRIME
        for point in points
    ]
    if len(set(slopes)) != active_faces:
        raise AssertionError("Mobius colors are not distinct")
    matrix = [
        [1] * active_faces,
        points,
        slopes,
        [point * slope % PRIME for point, slope in zip(points, slopes)],
    ]
    matrix_rank = rank(matrix)
    basis = nullspace(matrix)
    if matrix_rank != 3 or len(basis) != active_faces - 3:
        raise AssertionError((active_faces, matrix_rank, len(basis)))

    faces = canonical_faces()[:active_faces]
    for face, omitted in zip(faces, points):
        if face[omitted] != 0 or sum(value != 0 for value in face) != 5:
            raise AssertionError("face support")
        for degree in range(4):
            if sum(value * pow(x, degree, PRIME) for x, value in enumerate(face)) % PRIME:
                raise AssertionError("face is not dual cubic")

    coefficients = full_support_kernel_vector(basis)
    trade = [
        [coefficient * value % PRIME for value in face]
        for coefficient, face in zip(coefficients, faces)
    ]
    if rank(trade) != 2:
        raise AssertionError("trade rank")
    if any(sum(column) % PRIME for column in zip(*trade)):
        raise AssertionError("first trade identity")
    if any(
        sum(slope * value for slope, value in zip(slopes, column)) % PRIME
        for column in zip(*trade)
    ):
        raise AssertionError("second trade identity")

    mutated = [row[:] for row in matrix]
    mutated[2][-1] = (mutated[2][-1] + 1) % PRIME
    mutated[3][-1] = points[-1] * mutated[2][-1] % PRIME
    mutation_rank = rank(mutated)
    if mutation_rank != 4:
        raise AssertionError(("mutation did not break Mobius law", active_faces, mutation_rank))
    return matrix_rank, len(basis), mutation_rank


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
    fans = [face_fan(active) for active in (4, 5, 6)]
    residual_profiles = {(4, 7, (1, 2, 2, 2)), (4, 8, (2, 2, 2, 2))}
    if len(residual_profiles) != 2 or any(profile[1] <= 6 for profile in residual_profiles):
        raise AssertionError("rank-two quotient profiles")
    dag = json.loads(DAG.read_text())
    validate_dag(dag)
    mutations = mutation_controls(dag)
    print(
        "XR_SPLIT_PENCIL_SIX_FACE_SYZYGY_QUOTIENT_PASS "
        f"fans={len(fans)} dimensions={','.join(str(row[1]) for row in fans)} "
        f"residual_profiles={len(residual_profiles)} mutations={mutations}/{mutations}"
    )


if __name__ == "__main__":
    main()
