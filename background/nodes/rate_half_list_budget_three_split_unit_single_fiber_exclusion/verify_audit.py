#!/usr/bin/env python3
"""Independent finite-field audit of the partial-fraction argument."""

from __future__ import annotations


P = 97
D = 8


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] % P == 0:
        poly.pop()
    return [value % P for value in poly]


def multiply(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] += a * b
    return trim(answer)


def quotient(dividend: list[int], divisor: list[int]) -> list[int]:
    remainder = trim(dividend[:])
    divisor = trim(divisor[:])
    answer = [0] * (len(remainder) - len(divisor) + 1)
    inverse = pow(divisor[-1], -1, P)
    while len(remainder) >= len(divisor) and remainder != [0]:
        shift = len(remainder) - len(divisor)
        factor = remainder[-1] * inverse % P
        answer[shift] = factor
        for index, value in enumerate(divisor):
            remainder[index + shift] -= factor * value
        remainder = trim(remainder)
    assert remainder == [0]
    return trim(answer)


def locator(roots: tuple[int, ...]) -> list[int]:
    answer = [1]
    for root in roots:
        answer = multiply(answer, [-root, 1])
    return answer


def fiber_quotient(roots: tuple[int, ...]) -> list[int]:
    tau = pow(roots[0], D, P)
    assert all(pow(root, D, P) == tau for root in roots)
    numerator = [-tau] + [0] * (D - 1) + [1]
    return quotient(numerator, locator(roots))


def rank(polynomials: list[list[int]]) -> int:
    width = max(map(len, polynomials))
    rows = [[poly[column] if column < len(poly) else 0 for column in range(width)] for poly in polynomials]
    pivot_row = 0
    for column in range(width):
        pivot = next((row for row in range(pivot_row, len(rows)) if rows[row][column] % P), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        inverse = pow(rows[pivot_row][column] % P, -1, P)
        rows[pivot_row] = [value * inverse % P for value in rows[pivot_row]]
        for row in range(len(rows)):
            if row == pivot_row:
                continue
            factor = rows[row][column] % P
            rows[row] = [(value - factor * base) % P for value, base in zip(rows[row], rows[pivot_row], strict=True)]
        pivot_row += 1
    return pivot_row


def main() -> None:
    fixtures = {
        "cycle": ((1,), (2,), (3,), (4,)),
        "k4e": ((1, -1), (2, -2), (3,), (4,)),
        "k4": ((1, -1), (2, -2), (3, -3), (4, -4)),
        "path": ((1,), (2,), (3,)),
        "triangle": ((1,), (2,), (3,), (4, -4)),
    }
    for groups in fixtures.values():
        normalized = tuple(tuple(root % P for root in group) for group in groups)
        polynomials = [fiber_quotient(group) for group in normalized]
        assert rank(polynomials) == len(polynomials)
        assert sum(map(len, normalized)) <= D
    print(
        "AUDIT_RATE_HALF_LIST_BUDGET_THREE_SPLIT_UNIT_SINGLE_FIBER_EXCLUSION_PASS "
        "fixtures=5 independent=5 partial_fraction_divisions=19"
    )


if __name__ == "__main__":
    main()
