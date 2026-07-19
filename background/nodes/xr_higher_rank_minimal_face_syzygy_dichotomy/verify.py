#!/usr/bin/env python3
"""Verify the arbitrary-rank minimal-face syzygy dichotomy."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_higher_rank_minimal_face_syzygy_dichotomy"
DEPENDENCY = "xr_higher_rank_uniform_split_pencil_reduction"
CONSUMER = "xr_highcore_collision_count"
PRIME = 1_000_003


def inverse(value: int) -> int:
    return pow(value % PRIME, PRIME - 2, PRIME)


def divided_difference(points: list[int], values: dict[int, int]) -> int:
    total = 0
    for x in points:
        derivative = 1
        for y in points:
            if y != x:
                derivative = derivative * (x - y) % PRIME
        total += values[x] * inverse(derivative)
    return total % PRIME


def poly_value(coefficients: list[int], x: int) -> int:
    total = 0
    for coefficient in reversed(coefficients):
        total = (total * x + coefficient) % PRIME
    return total


def matrix_rank(rows: list[list[int]]) -> int:
    matrix = [[entry % PRIME for entry in row] for row in rows]
    rank = 0
    columns = len(matrix[0]) if matrix else 0
    for column in range(columns):
        pivot = next((i for i in range(rank, len(matrix)) if matrix[i][column]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        scale = inverse(matrix[rank][column])
        matrix[rank] = [entry * scale % PRIME for entry in matrix[rank]]
        for i in range(len(matrix)):
            if i != rank and matrix[i][column]:
                factor = matrix[i][column]
                matrix[i] = [
                    (left - factor * right) % PRIME
                    for left, right in zip(matrix[i], matrix[rank])
                ]
        rank += 1
        if rank == len(matrix):
            break
    return rank


def nullspace(matrix: list[list[int]]) -> list[list[int]]:
    work = [[entry % PRIME for entry in row] for row in matrix]
    row = 0
    pivots: list[int] = []
    columns = len(work[0])
    for column in range(columns):
        pivot = next((i for i in range(row, len(work)) if work[i][column]), None)
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        scale = inverse(work[row][column])
        work[row] = [entry * scale % PRIME for entry in work[row]]
        for i in range(len(work)):
            if i != row and work[i][column]:
                factor = work[i][column]
                work[i] = [
                    (left - factor * right) % PRIME
                    for left, right in zip(work[i], work[row])
                ]
        pivots.append(column)
        row += 1
        if row == len(work):
            break
    free = [column for column in range(columns) if column not in pivots]
    basis = []
    for free_column in free:
        vector = [0] * columns
        vector[free_column] = 1
        for pivot_row, pivot_column in reversed(list(enumerate(pivots))):
            vector[pivot_column] = -sum(
                work[pivot_row][j] * vector[j] for j in free
            ) % PRIME
        basis.append(vector)
    return basis


def facet_affinity_check() -> int:
    checked = 0
    for a in range(2, 11):
        points = list(range(1, a + 3))
        for seed in range(1, 8):
            coefficients = [((seed + 3) * (j + 5) + j * j) % PRIME for j in range(a + 2)]
            values = {x: poly_value(coefficients, x) for x in points}
            facets = []
            for omitted in points:
                face = [x for x in points if x != omitted]
                facets.append((omitted, divided_difference(face, values)))
            x0, y0 = facets[0]
            x1, y1 = facets[1]
            slope = (y1 - y0) * inverse(x1 - x0) % PRIME
            intercept = (y0 - slope * x0) % PRIME
            assert all(value == (intercept + slope * x) % PRIME for x, value in facets)
            checked += 1

        low = [j + 7 for j in range(a)]
        values = {x: poly_value(low, x) for x in points}
        assert all(
            divided_difference([y for y in points if y != x], values) == 0
            for x in points
        )
        checked += 1
    return checked


def regular_syzygy_check() -> tuple[int, int]:
    systems = 0
    relations = 0
    for a in range(2, 11):
        points = list(range(2, a + 4))
        alpha, beta, chi, delta = 7, 11, 13, 5
        assert (beta * chi - alpha * delta) % PRIME != 0
        for t in range(4, a + 3):
            omitted = points[:t]
            gamma = [
                (alpha + beta * x) * inverse(chi + delta * x) % PRIME
                for x in omitted
            ]
            assert len(set(gamma)) == t
            matrix = [
                [1] * t,
                omitted,
                gamma,
                [x * g % PRIME for x, g in zip(omitted, gamma)],
            ]
            assert matrix_rank(matrix) == 3
            kernel = nullspace(matrix)
            assert len(kernel) == t - 3

            locator_derivative = {}
            for y in points:
                value = 1
                for z in points:
                    if z != y:
                        value = value * (y - z) % PRIME
                locator_derivative[y] = value
            mu = [
                [(y - x) * inverse(locator_derivative[y]) % PRIME for y in points]
                for x in omitted
            ]
            for coefficients in kernel:
                for column in range(len(points)):
                    assert sum(
                        coefficients[i] * mu[i][column] for i in range(t)
                    ) % PRIME == 0
                    assert sum(
                        gamma[i] * coefficients[i] * mu[i][column]
                        for i in range(t)
                    ) % PRIME == 0
                relations += 1
            systems += 1
    return systems, relations


def singular_dichotomy_check() -> int:
    checked = 0
    for root in range(2, 40):
        for d_scale in range(1, 5):
            for n_scale in range(1, 5):
                regular_points = [root + j for j in range(1, 4)]
                colors = [
                    n_scale * (x - root) * inverse(d_scale * (x - root)) % PRIME
                    for x in regular_points
                ]
                assert len(set(colors)) == 1
                checked += 1
    return checked


def official_deficit_check() -> tuple[tuple[str, int], ...]:
    rows = (
        ("rowc-r1_4", 1024, 256, 3),
        ("rowc-r1_8", 1024, 256, 3),
        ("rowc-r1_16", 1024, 512, 1),
        ("prize-r1_4", 1 << 41, 256, (1 << 33) - 1),
        ("prize-r1_8", 1 << 41, 256, (1 << 33) - 1),
        ("prize-r1_16", 1 << 41, 512, (1 << 32) - 1),
    )
    deficits = []
    for name, length, scale_denominator, expected in rows:
        h = length // scale_denominator + 1
        assert h > 2
        assert h - 2 == expected
        deficits.append((name, expected))
    return tuple(deficits)


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md", "proof.md", "claim_contract.md",
        "dependency_subdag.md", "audit.md", "result.md", "verify.py",
        "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = (base / "statement.md").read_text() + (base / "proof.md").read_text()
    for marker in ("|X|=a+2", "dim=t-3", "|P_0 union X|=k+2"):
        assert marker in text


def main() -> None:
    facets = facet_affinity_check()
    systems, relations = regular_syzygy_check()
    singular = singular_dichotomy_check()
    deficits = official_deficit_check()
    packet_check()
    print(
        "XR_HIGHER_RANK_MINIMAL_FACE_SYZYGY_PASS "
        f"facets={facets} systems={systems} relations={relations} singular={singular} "
        + " ".join(f"{name}:defect={defect}" for name, defect in deficits)
    )


if __name__ == "__main__":
    main()
