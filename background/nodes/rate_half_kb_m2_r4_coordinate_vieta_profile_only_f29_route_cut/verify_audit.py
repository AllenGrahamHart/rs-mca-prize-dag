#!/usr/bin/env python3
"""Independent determinant/evaluation audit of the F_29 route cut."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
P = 29


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def determinant(matrix: list[list[int]]) -> int:
    work = [[value % P for value in row] for row in matrix]
    result = 1
    for column in range(len(work)):
        pivot = next((row for row in range(column, len(work))
                      if work[row][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            result = -result
        value = work[column][column] % P
        result = result * value % P
        inverse = pow(value, P - 2, P)
        for row in range(column + 1, len(work)):
            multiple = work[row][column] * inverse % P
            for index in range(column, len(work)):
                work[row][index] = (
                    work[row][index] - multiple * work[column][index]
                ) % P
    return result % P


def poly_value(poly: list[int], value: int) -> int:
    return sum(coefficient * pow(value, degree, P)
               for degree, coefficient in enumerate(poly)) % P


def main() -> None:
    data = json.loads((NODE / "certificate.json").read_text())
    require(data["field"] == P, "field")
    bar = lambda edge: frozenset((-value) % P for value in edge)
    orbits = [
        (frozenset(first), frozenset(second))
        for first, second in [
            *data["k_orbits"], data["eta_orbit"],
            *[record["stars"] for record in data["right_records"]],
        ]
    ]
    require(all(bar(first) == second for first, second in orbits), "transport")
    stars = [edge for orbit in orbits for edge in orbit]
    multiplicities = Counter(stars)
    require(sum(value * (value - 1) // 2 for value in multiplicities.values()) == 2,
            "defect")
    degree = Counter(vertex for edge in stars for vertex in edge)
    require(sorted(degree.values()) == [4] * 12, "degree four")

    kappa = data["K"]
    products = (15, 6, 15, 14, 10)
    weighted_sums = (8, 2, 16, 10, 21)
    matrix: list[list[int]] = []
    for point, edge_product, weighted_sum in zip(kappa, products, weighted_sums):
        basis = [1, point, point * point % P]
        matrix.extend((
            [(-edge_product * value) % P for value in basis] + basis + [0, 0],
            [(weighted_sum * value) % P for value in basis]
            + [0, 0, 0, point, point * point % P],
        ))
    vector = [17, 9, 18, 28, 20, 3, 24, 1]
    require(all(sum(a * b for a, b in zip(row, vector)) % P == 0 for row in matrix),
            "kernel")
    minor = [[matrix[row][column] for column in range(7)] for row in range(7)]
    require(determinant(minor) == 28, "rank lower bound")
    require(all(poly_value(vector[:3], point) != 0 for point in kappa), "leading support")

    forced_c = data["forced_c"]
    require(forced_c == [9, 22, 1], "forced quadratic")
    require(poly_value(forced_c, 13) == poly_value(forced_c, 23) == 0, "forced roots")
    require({13, 23}.isdisjoint({2, 27, 3, 26, 5, 24}), "support failure")
    require(data["colored_rights"] == [3, 26], "colored right vertices")
    require([3 * 26 % P, -(3 + 26) % P, 1] == [20, 0, 1] != forced_c,
            "colored quadratic mismatch")

    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("not a deployed-field component" in statement, "scope guard")
    require("c_0(20)R_I(20)=8" in proof, "companion witness")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_VIETA_PROFILE_ONLY_F29_ROUTE_CUT_AUDIT_PASS "
        "defect=2 minor=28 roots=13,23"
    )


if __name__ == "__main__":
    main()
