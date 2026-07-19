#!/usr/bin/env python3
"""Audit the small-field rank-two locus without making it a theorem claim."""

from __future__ import annotations

from itertools import combinations


PRIME = 13


def multiply(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] = (answer[i + j] + a * b) % PRIME
    return answer


def matchings(values: tuple[int, ...]):
    if not values:
        yield ()
        return
    first = values[0]
    for index in range(1, len(values)):
        second = values[index]
        rest = values[1:index] + values[index + 1 :]
        for matching in matchings(rest):
            yield ((first, second),) + matching


def rank(matrix: list[list[int]]) -> int:
    rows = [row[:] for row in matrix]
    answer = 0
    for column in range(4):
        pivot = next(
            (row for row in range(answer, 4) if rows[row][column]), None
        )
        if pivot is None:
            continue
        rows[answer], rows[pivot] = rows[pivot], rows[answer]
        inverse = pow(rows[answer][column], PRIME - 2, PRIME)
        rows[answer] = [value * inverse % PRIME for value in rows[answer]]
        for row in range(4):
            if row != answer and rows[row][column]:
                factor = rows[row][column]
                rows[row] = [
                    (left - factor * right) % PRIME
                    for left, right in zip(rows[row], rows[answer], strict=True)
                ]
        answer += 1
    return answer


def residue_rank(pairs: tuple[tuple[int, int], ...]) -> int:
    denominators = [
        [left * right % PRIME, -(left + right) % PRIME, 1]
        for left, right in pairs
    ]
    columns = []
    for omitted in range(4):
        column = [1]
        for index, denominator in enumerate(denominators):
            if index != omitted:
                column = multiply(column, denominator)
        columns.append(column)
    best = 0
    for y_value in range(4):
        matrix = [
            [
                sum(
                    column[degree] * pow(y_value, (degree - residue) // 4, PRIME)
                    for degree in range(residue, len(column), 4)
                )
                % PRIME
                for column in columns
            ]
            for residue in range(4)
        ]
        best = max(best, rank(matrix))
    return best


def main() -> None:
    counts = {2: 0, 3: 0, 4: 0}
    nonantipodal_rank_two = 0
    for subset in combinations(range(1, PRIME), 8):
        for pairs in matchings(subset):
            value = residue_rank(pairs)
            counts[value] += 1
            if value == 2 and not all(
                (left + right) % PRIME == 0 for left, right in pairs
            ):
                nonantipodal_rank_two += 1
    assert counts == {2: 15, 3: 1_104, 4: 50_856}
    assert nonantipodal_rank_two == 0
    print(
        "AUDIT_RATE_HALF_LIST_B3_FIBER_FOUR_RANK_GATE_PASS "
        "pairings=51975 rank2=15 nonantipodal=0"
    )


if __name__ == "__main__":
    main()
