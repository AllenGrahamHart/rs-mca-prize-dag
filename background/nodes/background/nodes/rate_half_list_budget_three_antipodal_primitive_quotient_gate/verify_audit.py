#!/usr/bin/env python3
"""Audit every d=16 one-deletion-per-coset coefficient matrix."""

from __future__ import annotations

from itertools import product


PRIME = 97
ORDER = 16


def rank(matrix: list[list[int]]) -> int:
    rows = [[value % PRIME for value in row] for row in matrix]
    current = 0
    for column in range(len(rows[0])):
        pivot = next(
            (index for index in range(current, len(rows)) if rows[index][column]),
            None,
        )
        if pivot is None:
            continue
        rows[current], rows[pivot] = rows[pivot], rows[current]
        inverse = pow(rows[current][column], -1, PRIME)
        rows[current] = [value * inverse % PRIME for value in rows[current]]
        for index in range(len(rows)):
            if index == current or not rows[index][column]:
                continue
            factor = rows[index][column]
            rows[index] = [
                (left - factor * right) % PRIME
                for left, right in zip(rows[index], rows[current], strict=True)
            ]
        current += 1
    return current


def main() -> None:
    generator = next(
        value
        for value in range(2, PRIME)
        if pow(value, ORDER, PRIME) == 1 and pow(value, ORDER // 2, PRIME) != 1
    )
    subgroup = tuple(pow(generator, exponent, PRIME) for exponent in range(ORDER))
    cosets = tuple(
        tuple(subgroup[residue + 4 * step] for step in range(4))
        for residue in range(4)
    )

    checked = 0
    for deleted in product(*cosets):
        matrix = [[1, value, value**2, value**3] for value in deleted]
        assert rank(matrix) == 4
        checked += 1
    assert checked == 256
    print(
        "AUDIT_RATE_HALF_LIST_B3_ANTIPODAL_PRIMITIVE_QUOTIENT_GATE_PASS "
        "field=97 quotient_order=16 deletion_choices=256 rank=4"
    )


if __name__ == "__main__":
    main()
