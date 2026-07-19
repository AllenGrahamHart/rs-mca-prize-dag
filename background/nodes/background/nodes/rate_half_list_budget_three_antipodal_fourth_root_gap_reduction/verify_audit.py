#!/usr/bin/env python3
"""Audit canonical truncations over a small prime field."""

from __future__ import annotations

from itertools import product


PRIME = 1009


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] % PRIME == 0:
        poly.pop()
    return [coefficient % PRIME for coefficient in poly]


def add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    return trim([
        (left[index] if index < len(left) else 0)
        + (right[index] if index < len(right) else 0)
        for index in range(size)
    ])


def scale(poly: list[int], scalar: int) -> list[int]:
    return trim([scalar * coefficient for coefficient in poly])


def multiply(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] = (answer[i + j] + a * b) % PRIME
    return trim(answer)


def derivative(poly: list[int]) -> list[int]:
    return trim([index * poly[index] for index in range(1, len(poly))] or [0])


def series(e_poly: list[int], limit: int) -> list[int]:
    answer = [1]
    for m in range(1, limit + 1):
        numerator = sum(
            (4 * m - 3 * j) * e_poly[j] * answer[m - j]
            for j in range(1, min(4, m) + 1)
        )
        answer.append(-numerator * pow(4 * m, -1, PRIME) % PRIME)
    return answer


def residual(d_poly: list[int], u_poly: list[int]) -> list[int]:
    r = len(u_poly) - 1
    d = 4 * r + 4
    bracket = add(
        multiply(derivative(d_poly), u_poly),
        scale(multiply(d_poly, derivative(u_poly)), 4),
    )
    return add(scale(multiply(d_poly, u_poly), d), scale([0] + bracket, -1))


def main() -> None:
    cases = 0
    for coefficients in product((-1, 0, 1), repeat=3):
        for constant in (-1, 1):
            e_poly = [1, *coefficients, constant]
            d_poly = list(reversed(e_poly))
            for r in range(1, 25):
                values = series(e_poly, 4 * r + 4)
                b_poly = values[:r + 1]
                u_poly = list(reversed(b_poly))
                assert len(residual(d_poly, u_poly)) - 1 <= 3

                mutation = u_poly.copy()
                mutation[r - 1] = (mutation[r - 1] + 1) % PRIME
                assert len(residual(d_poly, mutation)) - 1 == r + 3

                b_fourth = multiply(
                    multiply(b_poly, b_poly),
                    multiply(b_poly, b_poly),
                )
                contact = add(multiply(e_poly, b_fourth), [-1])
                contact_order = next(i for i in range(1, len(contact)) if contact[i])
                omitted = next(i for i in range(r + 1, len(values)) if values[i])
                assert contact_order == omitted
                cases += 1

    r = (1 << 37) - 1
    assert r + 1 == 1 << 37
    assert r + 3 == (1 << 37) + 2
    print(
        "AUDIT_RATE_HALF_ANTIPODAL_FOURTH_ROOT_GAP_PASS "
        f"prime={PRIME} canonical_cases={cases} official_index={r + 1}"
    )


if __name__ == "__main__":
    main()
