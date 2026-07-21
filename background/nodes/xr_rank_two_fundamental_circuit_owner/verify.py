#!/usr/bin/env python3
"""Verify the XR rank-two fundamental-circuit owner."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_rank_two_fundamental_circuit_owner"
PARENT = "xr_trade_circuit_arity_segre_atlas"
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


def transpose(columns: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*columns)]


def segre_column(slope: int, parameter: int) -> list[int]:
    return [1, parameter % PRIME, slope % PRIME, slope * parameter % PRIME]


def scale_column(column: list[int], scalar: int) -> list[int]:
    return [(scalar * entry) % PRIME for entry in column]


def column_sum(columns: list[list[int]], coefficients: list[int]) -> list[int]:
    return [
        sum(coefficient * column[row] for coefficient, column in zip(coefficients, columns))
        % PRIME
        for row in range(4)
    ]


def lex_basis(columns: list[list[int]]) -> tuple[int, tuple[int, ...]]:
    q = rank_mod(transpose(columns))
    for indices in itertools.combinations(range(len(columns)), q):
        chosen = [columns[i] for i in indices]
        if rank_mod(transpose(chosen)) == q:
            return q, indices
    raise AssertionError("no column basis")


def basis_coordinates(basis: list[list[int]], target: list[int]) -> list[int]:
    q = len(basis)
    rows = [
        [basis[column][row] % PRIME for column in range(q)]
        + [target[row] % PRIME]
        for row in range(4)
    ]
    pivot_row = 0
    pivots: list[tuple[int, int]] = []
    for column in range(q):
        pivot = next(
            (i for i in range(pivot_row, len(rows)) if rows[i][column]),
            None,
        )
        if pivot is None:
            raise AssertionError("dependent anchor basis")
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        inverse = pow(rows[pivot_row][column], -1, PRIME)
        rows[pivot_row] = [
            (entry * inverse) % PRIME for entry in rows[pivot_row]
        ]
        for i in range(len(rows)):
            if i == pivot_row:
                continue
            factor = rows[i][column]
            if factor:
                rows[i] = [
                    (x - factor * y) % PRIME
                    for x, y in zip(rows[i], rows[pivot_row])
                ]
        pivots.append((column, pivot_row))
        pivot_row += 1
    assert all(any(row[column] for column in range(q)) or not row[-1] for row in rows)
    answer = [0] * q
    for column, row in pivots:
        answer[column] = rows[row][-1]
    return answer


def owners(
    columns: list[list[int]],
) -> tuple[int, tuple[int, ...], dict[int, list[int]]]:
    q, anchor_indices = lex_basis(columns)
    anchors = [columns[i] for i in anchor_indices]
    owner_vectors: dict[int, list[int]] = {}
    for e in range(len(columns)):
        if e in anchor_indices:
            continue
        beta = basis_coordinates(anchors, columns[e])
        vector = [0] * len(columns)
        vector[e] = 1
        for anchor, coefficient in zip(anchor_indices, beta):
            vector[anchor] = (-coefficient) % PRIME
        assert column_sum(columns, vector) == [0, 0, 0, 0]
        support = [i for i, coefficient in enumerate(vector) if coefficient]
        assert len(support) in (4, 5)
        owner_vectors[e] = vector
    assert rank_mod(list(owner_vectors.values())) == len(columns) - q
    return q, anchor_indices, owner_vectors


def add_vectors(vectors: list[list[int]], weights: list[int]) -> list[int]:
    return [
        sum(weight * vector[i] for weight, vector in zip(weights, vectors))
        % PRIME
        for i in range(len(vectors[0]))
    ]


def barycentric_weights(points: list[int]) -> list[int]:
    result = []
    for i, point in enumerate(points):
        denominator = 1
        for j, other in enumerate(points):
            if i != j:
                denominator = denominator * (point - other) % PRIME
        result.append(pow(denominator, -1, PRIME))
    return result


def rank_three_fixture() -> int:
    slopes = list(range(1, 8))
    raw = [segre_column(slope, slope) for slope in slopes]
    columns = [
        scale_column(column, weight)
        for column, weight in zip(raw, barycentric_weights(slopes))
    ]
    assert column_sum(columns, [1] * len(columns)) == [0, 0, 0, 0]
    q, anchors, owner_vectors = owners(columns)
    assert q == 3 and anchors == (0, 1, 2)
    assert all(sum(bool(value) for value in vector) == 4 for vector in owner_vectors.values())
    reconstructed = add_vectors(list(owner_vectors.values()), [1] * len(owner_vectors))
    assert reconstructed == [1] * len(columns)
    return len(owner_vectors)


def rank_four_fixture() -> tuple[int, int]:
    points = [(1, 1), (2, 2), (3, 3), (4, 16), (5, 5), (6, 36)]
    raw = [segre_column(slope, parameter) for slope, parameter in points]
    q, anchors, raw_owners = owners(raw)
    assert q == 4 and anchors == (0, 1, 2, 3)

    owner_list = list(raw_owners.values())
    full_relation = None
    for scalar in range(1, PRIME):
        candidate = add_vectors(owner_list, [1, scalar])
        if all(candidate):
            full_relation = candidate
            break
    assert full_relation is not None
    columns = [
        scale_column(column, coefficient)
        for column, coefficient in zip(raw, full_relation)
    ]
    assert column_sum(columns, [1] * len(columns)) == [0, 0, 0, 0]

    q, anchors, owner_vectors = owners(columns)
    assert q == 4 and anchors == (0, 1, 2, 3)
    arities = sorted(sum(bool(value) for value in vector) for vector in owner_vectors.values())
    assert arities == [4, 5]
    reconstructed = add_vectors(list(owner_vectors.values()), [1] * len(owner_vectors))
    assert reconstructed == [1] * len(columns)
    return arities[0], arities[1]


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
        "3<=q<=4",
        "lexicographicallyfirst",
        "exactlyfourorfiveblocks",
        "K=span{kappa^e:einI\\B}",
        "1_I=sum_(einI\\B)kappa^e",
        "atmostfouranchorblocks",
        "doesnotidentifythefirstMaxwellcore",
    ):
        assert marker in statement


def main() -> None:
    rank_three_owners = rank_three_fixture()
    four, five = rank_four_fixture()
    packet_check()
    print(
        "XR_RANK_TWO_FUNDAMENTAL_CIRCUIT_OWNER_PASS "
        f"q3_owners={rank_three_owners} q4_arities={four}+{five}"
    )


if __name__ == "__main__":
    main()
