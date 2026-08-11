#!/usr/bin/env python3
"""Independent Cramer-rule and minor audit of the m=1 rank fence."""

import json
from pathlib import Path


P = 17
Y0 = (1, 10, 16, 2, 14, 0, 3, 11)
Y1 = (0, 14, 9, 7, 13, 12, 15, 0)
SUPPORTS = {
    0: (1, 2, 5),
    1: (3, 7, 11),
    2: (9, 12, 13),
    4: (4, 6, 16),
    15: (8, 10, 15),
}


def det(matrix: list[list[int]]) -> int:
    if len(matrix) == 1:
        return matrix[0][0] % P
    total = 0
    for column, value in enumerate(matrix[0]):
        minor = [row[:column] + row[column + 1 :] for row in matrix[1:]]
        total += (-1 if column % 2 else 1) * value * det(minor)
    return total % P


def cramer_word(support: tuple[int, ...], target: tuple[int, ...]) -> list[int]:
    base = [[pow(x, moment, P) for x in support] for moment in range(3)]
    denominator = det(base)
    assert denominator
    values = []
    for column in range(3):
        replaced = [row[:] for row in base]
        for row in range(3):
            replaced[row][column] = target[row]
        values.append(det(replaced) * pow(denominator, P - 2, P) % P)
    word = [0] * 16
    for x, value in zip(support, values):
        word[x - 1] = value
    for moment in range(8):
        assert sum(word[x - 1] * pow(x, moment, P) for x in range(1, 17)) % P == target[moment]
    return word


def build_matrix(first: int, second: int, words: dict[int, list[int]]):
    gap_inverse = pow(second - first, P - 2, P)
    c1 = [(b - a) * gap_inverse % P for a, b in zip(words[first], words[second])]
    c0 = [(a - first * b) % P for a, b in zip(words[first], c1)]
    support = tuple(sorted(set(SUPPORTS[first]) | set(SUPPORTS[second])))
    owners = {x: slope for slope, points in SUPPORTS.items() for x in points}
    matrix = []
    kernel = []
    coefficients = {}
    for x in support:
        owner = owners[x]
        q1 = (4 * x * x + 12 * x) % P
        q0 = (x**3 + 9 * x * x + 7) % P
        assert q1 and (q0 + owner * q1) % P == 0
        kernel.append(q1)
        coefficients[x] = (
            -owner * c0[x - 1] % P,
            (c0[x - 1] - owner * c1[x - 1]) % P,
            c1[x - 1],
        )
    for moment in range(5):
        for degree in range(3):
            matrix.append(
                [coefficients[x][degree] * pow(x, moment, P) % P for x in support]
            )
    assert all(sum(a * b for a, b in zip(row, kernel)) % P == 0 for row in matrix)
    return matrix, support


def main() -> None:
    payload = json.loads(Path(__file__).with_name("certificate.json").read_text())
    words = {}
    for slope, support in SUPPORTS.items():
        target = tuple((a + slope * b) % P for a, b in zip(Y0, Y1))
        words[slope] = cramer_word(support, target)

    for record in payload["pairs"]:
        matrix, support = build_matrix(*record["slopes"], words)
        assert list(support) == record["support"]
        columns = [index for index in range(6) if index != record["omitted_column"]]
        minor = [[matrix[row][column] for column in columns] for row in record["rows"]]
        assert det(minor) == record["determinant"] != 0

    q0_14 = (14**3 + 9 * 14**2 + 7) % P
    q1_14 = (4 * 14**2 + 12 * 14) % P
    assert q0_14 and not q1_14
    print("RATE_HALF_BIVARIATE_ROW_SURPLUS_ROUTE_FENCE_AUDIT_PASS pairs=10")


if __name__ == "__main__":
    main()
