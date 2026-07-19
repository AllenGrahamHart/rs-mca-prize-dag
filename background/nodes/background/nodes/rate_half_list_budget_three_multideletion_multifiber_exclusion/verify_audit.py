#!/usr/bin/env python3
"""Audit the rational-series independence criterion."""

from __future__ import annotations


PRIME = 1_000_003
PROFILES = (
    (1, 1, 1, 1),
    (1, 1, 1),
    (2, 2, 1, 1),
    (2, 2, 2, 2),
    (1, 1, 1, 2),
)


def multiply(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] = (answer[i + j] + a * b) % PRIME
    return answer


def denominator(roots: list[int]) -> list[int]:
    answer = [1]
    for root in roots:
        answer = multiply(answer, [1, -root % PRIME])
    return answer


def matrix_rank(columns: list[list[int]]) -> int:
    height = max(len(column) for column in columns)
    rows = [
        [column[i] if i < len(column) else 0 for column in columns]
        for i in range(height)
    ]
    answer = 0
    for column in range(len(columns)):
        pivot = next((i for i in range(answer, height) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[answer], rows[pivot] = rows[pivot], rows[answer]
        inverse = pow(rows[answer][column], PRIME - 2, PRIME)
        rows[answer] = [entry * inverse % PRIME for entry in rows[answer]]
        for row in range(height):
            if row != answer and rows[row][column]:
                factor = rows[row][column]
                rows[row] = [
                    (left - factor * right) % PRIME
                    for left, right in zip(rows[row], rows[answer], strict=True)
                ]
        answer += 1
    return answer


def main() -> None:
    checked = 0
    for deletions in PROFILES:
        minimum = min(deletions)
        total = sum(deletions)
        roots_by_index = []
        cursor = 2
        for size in deletions:
            roots_by_index.append(list(range(cursor, cursor + size)))
            cursor += size
        denominators = [denominator(roots) for roots in roots_by_index]
        common = [1]
        for value in denominators:
            common = multiply(common, value)
        numerators = []
        for i, size in enumerate(deletions):
            value = [1]
            for j, other in enumerate(denominators):
                if i != j:
                    value = multiply(value, other)
            value = [0] * (size - minimum) + value
            assert len(value) - 1 <= total - minimum
            numerators.append(value)
        assert matrix_rank(numerators) == len(deletions)
        checked += 1

    print(
        "AUDIT_RATE_HALF_LIST_B3_MULTIDELETION_MULTIFIBER_EXCLUSION_PASS "
        f"rational_profiles={checked}"
    )


if __name__ == "__main__":
    main()
