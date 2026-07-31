#!/usr/bin/env python3
"""Independent exact checker for one F_29 coordinate Vieta witness."""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path


P = 29
K = (1, 28, 4, 25, 9)
J_PAIRS = ((2, 27), (3, 26), (5, 24))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def rank(matrix: list[list[int]]) -> int:
    work = [[value % P for value in row] for row in matrix]
    pivot_row = 0
    for column in range(len(work[0])):
        pivot = next((row for row in range(pivot_row, len(work))
                      if work[row][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        inverse = pow(work[pivot_row][column], P - 2, P)
        work[pivot_row] = [value * inverse % P for value in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row:
                continue
            multiple = work[row][column]
            if multiple:
                work[row] = [
                    (left - multiple * right) % P
                    for left, right in zip(work[row], work[pivot_row])
                ]
        pivot_row += 1
    return pivot_row


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--parity", choices=("positive", "negative"), required=True)
    args = parser.parse_args()
    payload = json.loads(args.certificate.read_text())
    record = payload[f"{args.parity}_witness"]
    require(record is not None, "missing witness")
    require(record["parity"] == args.parity, "parity")
    require(len(record["rows"]) == 5, "five rows")

    degrees = [0, 0, 0]
    star_edges = []
    matrix: list[list[int]] = []
    vector = [int(value) % P for value in record["kernel_vector"]]
    for kappa, row in zip(K, record["rows"]):
        require(row["kappa"] == kappa, "K order")
        edge = tuple(int(value) % P for value in row["edge"])
        require(edge[0] != edge[1], "distinct roots")
        product = edge[0] * edge[1] % P
        require(product == row["product"] % P, "Vieta product")
        root = row["sqrt_kappa"] % P
        require(root * root % P == kappa, "quotient lift")
        weighted_sum = root * sum(edge) % P
        require(weighted_sum == row["weighted_sum"] % P, "weighted sum")
        star_edges.extend((tuple(sorted(edge)), tuple(sorted((-value) % P for value in edge))))

        incident = set()
        for endpoint in edge:
            pair = next((index for index, values in enumerate(J_PAIRS)
                         if endpoint in values), None)
            require(pair is not None, "J endpoint")
            incident.add(pair)
        if len(incident) == 1:
            degrees[next(iter(incident))] += 2
        else:
            for pair in incident:
                degrees[pair] += 1

        if args.parity == "positive":
            basis2 = [1, kappa, kappa * kappa % P]
            matrix.extend((
                [(-product * value) % P for value in basis2]
                + basis2 + [0, 0],
                [(weighted_sum * value) % P for value in basis2]
                + [0, 0, 0, kappa, kappa * kappa % P],
            ))
        else:
            matrix.extend((
                [-product, -product * kappa, 1, kappa, 0, 0, 0],
                [weighted_sum, weighted_sum * kappa, 0, 0,
                 1, kappa, kappa * kappa % P],
            ))

    require(degrees == record["pair_degrees"], "degree replay")
    require(sorted(degrees) in ([2, 4, 4], [3, 3, 4]), "allowed profile")
    defect = sum(count * (count - 1) // 2
                 for count in Counter(star_edges).values())
    require(defect == record["defect"] and defect <= 3, "defect budget")
    expected_columns = 8 if args.parity == "positive" else 7
    require(len(vector) == expected_columns, "kernel dimension")
    require(all(sum(a * b for a, b in zip(row, vector)) % P == 0
                for row in matrix), "kernel equations")
    actual_rank = rank(matrix)
    require(actual_rank == record["rank"], "rank replay")
    require(actual_rank <= expected_columns - 1, "nonzero kernel")

    leading = vector[:3] if args.parity == "positive" else vector[:2]
    for kappa in K:
        value = sum(coefficient * pow(kappa, index, P)
                    for index, coefficient in enumerate(leading)) % P
        require(value != 0, "leading support")
    if args.parity == "positive":
        require(any(vector[6:8]), "positive odd part")
    else:
        require(any(vector[0:4]), "negative odd part")
    print(
        "KB_COORDINATE_VIETA_F29_WITNESS_PASS "
        f"parity={args.parity} rank={actual_rank} profile={degrees} defect={defect}"
    )


if __name__ == "__main__":
    main()
