#!/usr/bin/env python3
"""Audit the two-window formula on the exact characteristic-193 packet."""

from __future__ import annotations


PRIME = 193
ORDER = 64
ZETA = 125
EXPONENTS = (0, 1, 3, 62)


def multiply(left: list[int], right: list[int], limit: int | None = None) -> list[int]:
    size = len(left) + len(right) - 1
    if limit is not None:
        size = min(size, limit)
    answer = [0] * size
    for i, value in enumerate(left):
        for j, other in enumerate(right):
            if i + j >= size:
                break
            answer[i + j] = (answer[i + j] + value * other) % PRIME
    return answer


def inverse(poly: list[int], limit: int) -> list[int]:
    answer = [pow(poly[0], -1, PRIME)]
    for degree in range(1, limit):
        total = sum(
            poly[index] * answer[degree - index]
            for index in range(1, min(degree, len(poly) - 1) + 1)
        )
        answer.append(-total * answer[0] % PRIME)
    return answer


def square_root_one(poly: list[int], limit: int) -> list[int]:
    answer = [1]
    inverse_two = pow(2, -1, PRIME)
    for degree in range(1, limit):
        cross = sum(answer[index] * answer[degree - index] for index in range(1, degree))
        answer.append((poly[degree] - cross) * inverse_two % PRIME)
    return answer


def divide_exact(numerator: list[int], denominator: list[int]) -> list[int]:
    remainder = numerator[:]
    quotient = [0] * (len(numerator) - len(denominator) + 1)
    inverse_lead = pow(denominator[-1], -1, PRIME)
    for offset in range(len(quotient) - 1, -1, -1):
        coefficient = remainder[offset + len(denominator) - 1] * inverse_lead % PRIME
        quotient[offset] = coefficient
        for index, value in enumerate(denominator):
            remainder[offset + index] = (
                remainder[offset + index] - coefficient * value
            ) % PRIME
    assert all(value == 0 for value in remainder[: len(denominator) - 1])
    return quotient


def fourth_root_inverse(e_poly: list[int], limit: int) -> list[int]:
    answer = [1]
    for degree in range(1, limit):
        numerator = sum(
            (4 * degree - 3 * index) * e_poly[index] * answer[degree - index]
            for index in range(1, min(4, degree) + 1)
        )
        answer.append(-numerator * pow(4 * degree, -1, PRIME) % PRIME)
    return answer


def main() -> None:
    assert pow(ZETA, ORDER, PRIME) == 1
    assert pow(ZETA, ORDER // 2, PRIME) != 1
    e_poly = [1]
    for exponent in EXPONENTS:
        root = pow(ZETA, exponent, PRIME)
        e_poly = multiply(e_poly, [1, -root % PRIME])

    h = 9
    r = 15
    coefficients = fourth_root_inverse(e_poly, 3 * h)
    assert coefficients[2 * h - 2 : 2 * h + 1] == [0, 0, 94]
    c = coefficients[2 * h]
    direct = multiply(coefficients[:h], coefficients[2 * h : 3 * h], h)
    direct = [value * pow(c, -1, PRIME) % PRIME for value in direct]

    numerator = [1] + [0] * (ORDER - 1) + [PRIME - 1]
    quotient = divide_exact(numerator, e_poly)
    b_poly = coefficients[: r + 1]
    b2 = multiply(b_poly, b_poly)
    b4 = multiply(b2, b2)
    residual = [
        ((quotient[index] if index < len(quotient) else 0)
         - (b4[index] if index < len(b4) else 0))
        % PRIME
        for index in range(max(len(quotient), len(b4)))
    ]
    rbar = residual[2 * h :]
    alpha = rbar[0]
    original = multiply(rbar, inverse(b2, h), h)
    original = [value * pow(alpha, -1, PRIME) % PRIME for value in original]
    assert original == direct

    root = square_root_one(direct, h)
    assert root[h - 2 : h] == [102, 24]
    mutation = direct.copy()
    mutation[h - 2] = (mutation[h - 2] + 2) % PRIME
    mutated_root = square_root_one(mutation, h)
    assert mutated_root[h - 2] == (root[h - 2] + 1) % PRIME
    print(
        "AUDIT_RATE_HALF_ANTIPODAL_GENERIC_TWO_WINDOW_SQUARE_PASS "
        "prime=193 order=64 primary=0,0,94 secondary=102,24 mutation=1"
    )


if __name__ == "__main__":
    main()
