#!/usr/bin/env python3
"""Exact replay of the m=2 Layer-A saturation-count route fence."""

import json
from pathlib import Path


CERTIFICATE = Path(__file__).with_name("certificate.json")


def multiplicative_order(value: int, prime: int) -> int:
    current = 1
    for order in range(1, prime):
        current = current * value % prime
        if current == 1:
            return order
    raise AssertionError("nonzero field element has no order")


def matrix_rank(matrix: list[list[int]], prime: int) -> int:
    work = [row[:] for row in matrix]
    row = 0
    for column in range(len(work[0])):
        pivot = next(
            (index for index in range(row, len(work)) if work[index][column]),
            None,
        )
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        inverse = pow(work[row][column], prime - 2, prime)
        work[row] = [entry * inverse % prime for entry in work[row]]
        for index in range(len(work)):
            if index == row or not work[index][column]:
                continue
            scale = work[index][column]
            work[index] = [
                (left - scale * right) % prime
                for left, right in zip(work[index], work[row])
            ]
        row += 1
    return row


def main() -> None:
    payload = json.loads(CERTIFICATE.read_text())
    assert payload["schema"] == "rate-half-layer-a-saturation-fence-v1"
    prime = payload["field"]
    zeta = payload["zeta"]
    assert multiplicative_order(zeta, prime) == 32

    expected_w = [pow(zeta, 2 * index, prime) for index in range(13)]
    expected_h = [pow(zeta, 4 * index, prime) for index in range(8)]
    assert payload["W"] == expected_w
    assert payload["slopes"] == expected_h + [zeta]

    incidences = []
    for x in payload["W"]:
        roots = [
            gamma
            for gamma in payload["slopes"]
            if (gamma * gamma - pow(x, 4, prime)) % prime == 0
        ]
        assert len(roots) == 2
        assert set(roots) == {x * x % prime, -x * x % prime}
        incidences.extend((gamma, x) for gamma in roots)
    assert [list(pair) for pair in incidences] == payload["incidences"]
    assert len(incidences) == 26

    matrix = [
        [
            pow(gamma, degree_z, prime) * pow(x, degree_x, prime) % prime
            for degree_z in range(3)
            for degree_x in range(8)
        ]
        for gamma, x in incidences
    ]
    rank = matrix_rank(matrix, prime)
    assert rank == payload["rank"] == 20
    assert len(matrix[0]) - rank == payload["nullity"] == 4
    print("RATE_HALF_LAYER_A_SATURATION_COUNT_ROUTE_FENCE_PASS rank=20 nullity=4")


if __name__ == "__main__":
    main()
