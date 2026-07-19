#!/usr/bin/env python3
"""Independent finite-field audit of coprimality and directness."""

from __future__ import annotations


P = 101


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] % P == 0:
        poly.pop()
    return [value % P for value in poly]


def add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    return trim([(left[i] if i < len(left) else 0) + (right[i] if i < len(right) else 0) for i in range(size)])


def multiply(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] += a * b
    return trim(answer)


def divide_remainder(dividend: list[int], divisor: list[int]) -> list[int]:
    remainder = trim(dividend[:])
    divisor = trim(divisor[:])
    inverse = pow(divisor[-1], -1, P)
    while len(remainder) >= len(divisor) and remainder != [0]:
        shift = len(remainder) - len(divisor)
        factor = remainder[-1] * inverse % P
        for index, value in enumerate(divisor):
            remainder[index + shift] -= factor * value
        remainder = trim(remainder)
    return remainder


def gcd(left: list[int], right: list[int]) -> list[int]:
    while trim(right[:]) != [0]:
        left, right = right, divide_remainder(left, right)
    left = trim(left)
    inverse = pow(left[-1], -1, P)
    return [value * inverse % P for value in left]


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
    x = [0, 1]
    alpha = [1, 2, 1]
    for beta in ([2, 0, 3, 1], [3, 1, 1]):
        assert gcd(alpha, beta) == [1]
        shifted_beta = add(beta, multiply([7], multiply(x, alpha)))
        assert gcd(alpha, shifted_beta) == [1]
        assert rank([alpha, multiply(x, alpha), beta, multiply(x, beta)]) == 4

    # A degree-at-least-two alpha cannot divide a nonzero affine polynomial.
    for affine in ([1], [1, 1], [0, 1]):
        assert divide_remainder(affine, alpha) != [0]
    print(
        "AUDIT_RATE_HALF_LIST_BUDGET_THREE_QUADRATIC_SCROLL_PRIMITIVE_MODULE_PASS "
        "gcd_invariance=2 direct_sum=2 affine_divisibility=3"
    )


if __name__ == "__main__":
    main()
