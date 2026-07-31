#!/usr/bin/env python3
"""Exact F_29 product-rank census on the banked abstract fixture."""

import itertools


PRIME = 29
PAIR_REPRESENTATIVES = (1, 4, 5, 6, 7, 9, 13)


def rank_mod(rows: list[list[int]]) -> int:
    matrix = [[value % PRIME for value in row] for row in rows]
    pivot_row = 0
    for column in range(6):
        pivot = next(
            (row for row in range(pivot_row, len(matrix)) if matrix[row][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        inverse = pow(matrix[pivot_row][column], -1, PRIME)
        matrix[pivot_row] = [value * inverse % PRIME for value in matrix[pivot_row]]
        for row in range(pivot_row + 1, len(matrix)):
            scale = matrix[row][column]
            if scale:
                matrix[row] = [
                    (left - scale * right) % PRIME
                    for left, right in zip(matrix[row], matrix[pivot_row])
                ]
        pivot_row += 1
    return pivot_row


def product_data(values: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    a, b, c, d, e, f = values
    return (
        (a, d * e), (-a, d * f), (b, -d * f),
        (-b, e * f), (c, -e * f), (-c, a * b),
        (d, a * c), (-d, -a * c), (e, b * c),
        (-e, -b * c), (f, a * d), (-f, b * e),
    )


def product_rows(values: tuple[int, ...]) -> list[list[int]]:
    rows = []
    for kappa, product in product_data(values):
        kappa %= PRIME
        product %= PRIME
        rows.append([
            -product % PRIME,
            -product * kappa % PRIME,
            -product * kappa * kappa % PRIME,
            1,
            kappa,
            kappa * kappa % PRIME,
        ])
    return rows


def main() -> None:
    tested = 0
    separator_survivors = 0
    complete_survivors = 0
    first = None
    for values in itertools.permutations(PAIR_REPRESENTATIVES, 6):
        tested += 1
        rows = product_rows(values)
        if rank_mod(rows[:6]) > 5:
            continue
        separator_survivors += 1
        if first is None:
            first = values
        if rank_mod(rows) <= 5:
            complete_survivors += 1

    expected = (5040, 140, 0, (1, 4, 6, 9, 7, 5))
    actual = (tested, separator_survivors, complete_survivors, first)
    if actual != expected:
        raise RuntimeError(f"fixture census mismatch: {actual}")

    rows = product_rows(first)
    if rank_mod(rows[:6]) != 5 or rank_mod(rows) != 6:
        raise RuntimeError("first witness ranks")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_COMPLETE_FIBER_FIXTURE_CENSUS_PASS "
        "tested=5040 separator_survivors=140 complete_survivors=0 "
        "first=1,4,6,9,7,5 ranks=5/6"
    )


if __name__ == "__main__":
    main()
