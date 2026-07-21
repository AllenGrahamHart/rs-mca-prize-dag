#!/usr/bin/env python3
"""Verify the XR three-anchor dual-GRS3 factorization."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_rank_two_three_anchor_grs3_factorization"
PARENTS = {
    "xr_rank_two_fundamental_circuit_owner",
    "xr_higher_rank_uniform_split_pencil_reduction",
}
CONSUMER = "xr_highcore_collision_count"
PRIME = 1009


def rank_mod(matrix: list[list[int]]) -> int:
    rows = [[entry % PRIME for entry in row] for row in matrix]
    rank = 0
    columns = len(rows[0]) if rows else 0
    for column in range(columns):
        pivot = next(
            (i for i in range(rank, len(rows)) if rows[i][column]), None
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, PRIME)
        rows[rank] = [(entry * inverse) % PRIME for entry in rows[rank]]
        for i in range(len(rows)):
            if i == rank:
                continue
            factor = rows[i][column]
            if factor:
                rows[i] = [
                    (x - factor * y) % PRIME
                    for x, y in zip(rows[i], rows[rank])
                ]
        rank += 1
    return rank


def evaluate(coefficients: list[int], point: int) -> int:
    value = 0
    for coefficient in reversed(coefficients):
        value = (value * point + coefficient) % PRIME
    return value


def locator_derivative(points: list[int], i: int) -> int:
    product = 1
    for j, point in enumerate(points):
        if i != j:
            product = product * (points[i] - point) % PRIME
    return product


def solve_square(matrix: list[list[int]], target: list[int]) -> list[int]:
    size = len(matrix)
    rows = [
        [entry % PRIME for entry in matrix[i]] + [target[i] % PRIME]
        for i in range(size)
    ]
    for column in range(size):
        pivot = next(i for i in range(column, size) if rows[i][column])
        rows[column], rows[pivot] = rows[pivot], rows[column]
        inverse = pow(rows[column][column], -1, PRIME)
        rows[column] = [(entry * inverse) % PRIME for entry in rows[column]]
        for i in range(size):
            if i == column:
                continue
            factor = rows[i][column]
            if factor:
                rows[i] = [
                    (x - factor * y) % PRIME
                    for x, y in zip(rows[i], rows[column])
                ]
    return [rows[i][-1] for i in range(size)]


def full_support_polynomial(points: list[int], degree_bound: int) -> list[int]:
    tail = [0] + [index + 1 for index in range(1, degree_bound)]
    for constant in range(1, PRIME):
        coefficients = tail[:]
        coefficients[0] = constant
        if all(evaluate(coefficients, point) for point in points):
            return coefficients
    raise AssertionError("failed to find root-avoiding H")


def grs3_fixture(t: int) -> tuple[list[int], list[int], list[int]]:
    slopes = list(range(1, t + 1))
    degree_bound = t - 3
    h_coefficients = full_support_polynomial(slopes, degree_bound)
    scales = [
        evaluate(h_coefficients, slope)
        * pow(locator_derivative(slopes, i), -1, PRIME)
        % PRIME
        for i, slope in enumerate(slopes)
    ]
    assert all(scales)
    assert [
        sum(scale * pow(slope, moment, PRIME) for scale, slope in zip(scales, slopes))
        % PRIME
        for moment in range(3)
    ] == [0, 0, 0]

    values = [
        scale * locator_derivative(slopes, i) % PRIME
        for i, scale in enumerate(scales)
    ]
    interpolation = [
        [pow(slopes[row], column, PRIME) for column in range(degree_bound)]
        for row in range(degree_bound)
    ]
    recovered = solve_square(interpolation, values[:degree_bound])
    assert recovered == h_coefficients
    assert all(evaluate(recovered, slope) == value for slope, value in zip(slopes, values))
    return slopes, scales, h_coefficients


def owner_formula(slopes: list[int], scales: list[int]) -> int:
    columns = [
        [scale, scale * slope % PRIME, scale * slope % PRIME, scale * slope * slope % PRIME]
        for scale, slope in zip(scales, slopes)
    ]
    assert rank_mod([list(row) for row in zip(*columns)]) == 3
    anchors = (0, 1, 2)
    owners = []
    for e in range(3, len(slopes)):
        support = anchors + (e,)
        derivatives = {
            i: locator_derivative([slopes[j] for j in support], support.index(i))
            for i in support
        }
        vector = [0] * len(slopes)
        numerator = scales[e] * derivatives[e] % PRIME
        for i in support:
            vector[i] = numerator * pow(scales[i] * derivatives[i] % PRIME, -1, PRIME) % PRIME
        assert vector[e] == 1
        assert all(
            sum(vector[i] * columns[i][row] for i in support) % PRIME == 0
            for row in range(4)
        )
        owners.append(vector)
    assert [sum(vector[i] for vector in owners) % PRIME for i in range(len(slopes))] == [1] * len(slopes)
    return len(owners)


def polynomial_pencil_check(slopes: list[int], scales: list[int]) -> None:
    p = [3, 5, 7, 11]
    q = [13, 17, 19, 23]
    rows = [
        [scale * (p[j] + slope * q[j]) % PRIME for j in range(len(p))]
        for scale, slope in zip(scales, slopes)
    ]
    assert [sum(row[j] for row in rows) % PRIME for j in range(len(p))] == [0] * len(p)
    assert [
        sum(slope * row[j] for slope, row in zip(slopes, rows)) % PRIME
        for j in range(len(p))
    ] == [0] * len(p)


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for parent in PARENTS:
        assert nodes[parent]["status"] == "PROVED"
        assert (parent, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "lambda_i(x)=s_i(P(x)+gamma_iQ(x))/Lambda'_X(x)",
        "sum_is_i=sum_is_igamma_i=sum_is_igamma_i^2=0",
        "degH<t-3",
        "s_i=H(gamma_i)/L'_Gamma(gamma_i)",
        "full-supportwordofthedual`GRS_3`code",
        "s_eL'_C(gamma_e)/(s_iL'_C(gamma_i))",
        "notpartoftheminimum-facequotient",
    ):
        assert marker in statement


def main() -> None:
    fixtures = 0
    owners = 0
    for t in range(4, 14):
        slopes, scales, _ = grs3_fixture(t)
        polynomial_pencil_check(slopes, scales)
        owners += owner_formula(slopes, scales)
        fixtures += 1
    packet_check()
    print(
        "XR_RANK_TWO_THREE_ANCHOR_GRS3_FACTORIZATION_PASS "
        f"fixtures={fixtures} owners={owners}"
    )


if __name__ == "__main__":
    main()
