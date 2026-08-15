#!/usr/bin/env python3
"""Independent determinant audit of the K'=11 circuit-shadow census."""

from __future__ import annotations

import hashlib
import json
from itertools import combinations
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "c6e5d380725fb05eee4fe901c8884eaae9806545c70024ef1a58af18e56e3e7f"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def evaluate(coefficients: list[int], point: int, prime: int) -> int:
    value = 0
    for coefficient in reversed(coefficients):
        value = (value * point + coefficient) % prime
    return value


def determinant(matrix: list[list[int]], prime: int) -> int:
    rows = [[value % prime for value in row] for row in matrix]
    value = 1
    for column in range(len(rows)):
        pivot = next((row for row in range(column, len(rows)) if rows[row][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            value = -value
        pivot_value = rows[column][column]
        value = value * pivot_value % prime
        inverse = pow(pivot_value, -1, prime)
        for row in range(column + 1, len(rows)):
            factor = rows[row][column] * inverse % prime
            for j in range(column, len(rows)):
                rows[row][j] = (rows[row][j] - factor * rows[column][j]) % prime
    return value % prime


def minor(matrix: list[list[int]], rows: tuple[int, ...], columns: tuple[int, ...]) -> list[list[int]]:
    return [[matrix[row][column] for column in columns] for row in rows]


def rank_at_least(matrix: list[list[int]], columns: tuple[int, ...], target: int, prime: int) -> bool:
    for rows in combinations(range(len(matrix)), target):
        for selected_columns in combinations(columns, target):
            if determinant(minor(matrix, rows, selected_columns), prime):
                return True
    return False


def make_matrix(circuit_size: int, prime: int) -> list[list[int]]:
    points = list(range(2, 13))
    weights = list(range(1, circuit_size + 1))
    moments = [
        sum(weight * pow(point, degree, prime) for weight, point in zip(weights, points)) % prime
        for degree in range(11)
    ]
    require(moments[0] != 0, f"audit pivot c={circuit_size}")
    inverse = pow(moments[0], -1, prime)
    polynomials = []
    for degree in range(1, 11):
        polynomial = [0] * 11
        polynomial[degree] = 1
        polynomial[0] = -moments[degree] * inverse % prime
        polynomials.append(polynomial)
    return [[evaluate(polynomial, point, prime) for point in points] for polynomial in polynomials]


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    prime = 103
    audited = []
    for c in p["circuit_sizes"]:
        matrix = make_matrix(c, prime)
        rank8 = 0
        rank9 = 0
        for omitted in combinations(range(11), 2):
            columns = tuple(index for index in range(11) if index not in omitted)
            if rank_at_least(matrix, columns, 9, prime):
                rank9 += 1
            else:
                require(rank_at_least(matrix, columns, 8, prime), f"audit rank-eight floor c={c}")
                rank8 += 1
        bases = 0
        for omitted in range(11):
            columns = tuple(index for index in range(11) if index != omitted)
            bases += determinant(minor(matrix, tuple(range(10)), columns), prime) != 0
        require(rank8 == comb(11 - c, 2), f"audit rank-eight c={c}")
        require(rank9 == 55 - rank8, f"audit rank-nine c={c}")
        require(bases == c, f"audit bases c={c}")
        audited.append((c, rank8, rank9, bases))

    proof = (HERE / "proof.md").read_text()
    for pin in (
        "I_B<=V'",
        "factors uniquely through",
        "unique circuit",
        "C(11-c,2)",
        "L_(C_B)*RS_{<11-c}",
        "eight-petal",
    ):
        require(pin in proof, f"proof pin {pin}")
    require(p["rank8_shadow_counts"] == [row[1] for row in audited], "contract rank-eight table")
    require(p["rank9_shadow_counts"] == [row[2] for row in audited], "contract rank-nine table")
    print(
        "RATE_HALF_MCA_RANK11_RANK8_CODIMENSION_ONE_CIRCUIT_SHADOW_CENSUS_AUDIT_PASS "
        f"toy=GF({prime}) circuit_sizes={len(audited)} determinants=independent proof_pins=6/6"
    )


if __name__ == "__main__":
    main()
