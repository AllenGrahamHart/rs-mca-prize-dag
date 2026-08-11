#!/usr/bin/env python3
"""Independent kernel-basis and fixed-minor audit of the Layer-A fence."""

import json
from pathlib import Path


def determinant(matrix: list[list[int]], prime: int) -> int:
    work = [row[:] for row in matrix]
    result = 1
    for column in range(len(work)):
        pivot = next(
            index
            for index in range(column, len(work))
            if work[index][column] % prime
        )
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            result = -result
        value = work[column][column] % prime
        result = result * value % prime
        inverse = pow(value, prime - 2, prime)
        for row in range(column + 1, len(work)):
            scale = work[row][column] * inverse % prime
            for entry in range(column, len(work)):
                work[row][entry] = (
                    work[row][entry] - scale * work[column][entry]
                ) % prime
    return result % prime


def main() -> None:
    payload = json.loads(Path(__file__).with_name("certificate.json").read_text())
    prime = payload["field"]
    incidences = [tuple(pair) for pair in payload["incidences"]]
    matrix = [
        [
            pow(gamma, degree_z, prime) * pow(x, degree_x, prime) % prime
            for degree_z in range(3)
            for degree_x in range(8)
        ]
        for gamma, x in incidences
    ]

    kernel = []
    for shift in range(4):
        vector = [0] * 24
        vector[16 + shift] = 1
        vector[4 + shift] = -1 % prime
        kernel.append(vector)
    for vector in kernel:
        assert all(
            sum(left * right for left, right in zip(row, vector)) % prime == 0
            for row in matrix
        )

    minor = [
        [matrix[row][column] for column in payload["minor_columns"]]
        for row in payload["minor_rows"]
    ]
    assert len(minor) == len(minor[0]) == 20
    assert determinant(minor, prime) == payload["minor_determinant"] == 45
    print("RATE_HALF_LAYER_A_SATURATION_COUNT_ROUTE_FENCE_AUDIT_PASS det=45")


if __name__ == "__main__":
    main()
