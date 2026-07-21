#!/usr/bin/env python3
"""Verify the XR four-anchor quadric-centroid atlas."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_rank_two_four_anchor_quadric_centroid_atlas"
PARENT = "xr_rank_two_fundamental_circuit_owner"
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


def solve_square(columns: list[list[int]], target: list[int]) -> list[int]:
    size = len(columns)
    rows = [
        [columns[column][row] % PRIME for column in range(size)]
        + [target[row] % PRIME]
        for row in range(size)
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


def segre_column(slope: int, parameter: int) -> list[int]:
    return [1, parameter % PRIME, slope % PRIME, slope * parameter % PRIME]


def scale_column(column: list[int], scalar: int) -> list[int]:
    return [(scalar * entry) % PRIME for entry in column]


def add_vectors(vectors: list[list[int]], weights: list[int]) -> list[int]:
    return [
        sum(weight * vector[i] for weight, vector in zip(weights, vectors))
        % PRIME
        for i in range(len(vectors[0]))
    ]


def column_sum(columns: list[list[int]], coefficients: list[int]) -> list[int]:
    return [
        sum(coefficient * column[row] for coefficient, column in zip(coefficients, columns))
        % PRIME
        for row in range(4)
    ]


def barycentric_weights(points: list[int]) -> list[int]:
    weights = []
    for i, point in enumerate(points):
        denominator = 1
        for j, other in enumerate(points):
            if i != j:
                denominator = denominator * (point - other) % PRIME
        weights.append(pow(denominator, -1, PRIME))
    return weights


def scaled_slope_parameter(column: list[int]) -> tuple[int, int, int, int]:
    c, d, gamma_c, gamma_d = column
    if c:
        slope = gamma_c * pow(c, -1, PRIME) % PRIME
    else:
        slope = gamma_d * pow(d, -1, PRIME) % PRIME
    assert gamma_c == slope * c % PRIME
    assert gamma_d == slope * d % PRIME
    return c, d, slope, (c * gamma_d - d * gamma_c) % PRIME


def atlas_check(columns: list[list[int]], expected_arities: list[int]) -> int:
    assert column_sum(columns, [1] * len(columns)) == [0, 0, 0, 0]
    anchors = columns[:4]
    assert rank_mod([list(row) for row in zip(*anchors)]) == 4
    anchor_data = [scaled_slope_parameter(column) for column in anchors]
    coefficients: dict[tuple[int, int], int] = {}
    for i in range(4):
        c_i, d_i, gamma_i, determinant_i = anchor_data[i]
        assert determinant_i == 0
        for j in range(i + 1, 4):
            c_j, d_j, gamma_j, _ = anchor_data[j]
            coefficient = (gamma_j - gamma_i) * (c_i * d_j - d_i * c_j) % PRIME
            assert coefficient
            coefficients[(i, j)] = coefficient

    hessian = [[0] * 4 for _ in range(4)]
    for (i, j), coefficient in coefficients.items():
        hessian[i][j] = coefficient
        hessian[j][i] = coefficient
    assert rank_mod(hessian) == 4

    betas = []
    arities = []
    for e in range(4, len(columns)):
        beta = solve_square(anchors, columns[e])
        image = [
            sum(beta[i] * anchors[i][row] for i in range(4)) % PRIME
            for row in range(4)
        ]
        assert image == columns[e]
        determinant = (image[0] * image[3] - image[1] * image[2]) % PRIME
        quadric = sum(
            coefficient * beta[i] * beta[j]
            for (i, j), coefficient in coefficients.items()
        ) % PRIME
        assert determinant == quadric == 0
        support = sum(bool(value) for value in beta)
        assert support in (3, 4)
        arities.append(support + 1)

        owner = [(-value) % PRIME for value in beta] + [0] * (len(columns) - 4)
        owner[e] = 1
        assert column_sum(columns, owner) == [0, 0, 0, 0]
        betas.append(beta)

    assert sorted(arities) == sorted(expected_arities)
    assert [sum(beta[i] for beta in betas) % PRIME for i in range(4)] == [PRIME - 1] * 4
    return len(betas)


def mixed_fixture() -> int:
    points = [(1, 1), (2, 2), (3, 3), (4, 16), (5, 5), (6, 36)]
    raw = [segre_column(slope, parameter) for slope, parameter in points]
    anchors = raw[:4]
    raw_owners = []
    for e in range(4, 6):
        beta = solve_square(anchors, raw[e])
        vector = [(-value) % PRIME for value in beta] + [0, 0]
        vector[e] = 1
        assert column_sum(raw, vector) == [0, 0, 0, 0]
        raw_owners.append(vector)
    relation = None
    for scalar in range(1, PRIME):
        candidate = add_vectors(raw_owners, [1, scalar])
        if all(candidate):
            relation = candidate
            break
    assert relation is not None
    columns = [
        scale_column(column, coefficient)
        for column, coefficient in zip(raw, relation)
    ]
    return atlas_check(columns, [4, 5])


def all_five_fixture() -> int:
    slopes = list(range(1, 9))
    raw = [segre_column(slope, slope * slope) for slope in slopes]
    columns = [
        scale_column(column, weight)
        for column, weight in zip(raw, barycentric_weights(slopes))
    ]
    return atlas_check(columns, [5, 5, 5, 5])


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[PARENT]["status"] == "PROVED"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "p_ij=(gamma_j-gamma_i)(c_id_j-d_ic_j)",
        "Q_B(beta)=sum_(i<j)p_ijbeta_ibeta_j",
        "smoothsplitprojectivequadric",
        "|supp(beta_e)|in{3,4}",
        "kappa^e_i=-beta_(e,i)",
        "sum_(enotinB)beta_e=(-1,-1,-1,-1)",
        "completecoefficient-levelatlas",
        "doesnotcountsuchquadricpointconfigurations",
    ):
        assert marker in statement


def main() -> None:
    mixed = mixed_fixture()
    all_five = all_five_fixture()
    packet_check()
    print(
        "XR_RANK_TWO_FOUR_ANCHOR_QUADRIC_CENTROID_ATLAS_PASS "
        f"mixed={mixed} all_five={all_five}"
    )


if __name__ == "__main__":
    main()
