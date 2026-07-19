#!/usr/bin/env python3
"""Audit the degree floor against the exact d=8 positive pencil."""

from __future__ import annotations


PRIME = 97
A_VALUES = (1, 8, 33, 79)
ROOTS = (50, 47, 96, 75)


def add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    return [
        ((left[index] if index < len(left) else 0)
         + (right[index] if index < len(right) else 0))
        % PRIME
        for index in range(size)
    ]


def multiply(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] = (answer[i + j] + a * b) % PRIME
    return answer


def derivative(poly: list[int]) -> list[int]:
    return [index * poly[index] % PRIME for index in range(1, len(poly))]


def from_roots(roots: tuple[int, ...]) -> list[int]:
    answer = [1]
    for root in roots:
        answer = multiply(answer, [(-root) % PRIME, 1])
    return answer


def scale(poly: list[int], scalar: int) -> list[int]:
    return [scalar * value % PRIME for value in poly]


def main() -> None:
    # The four boundary factors are G_i=Y-ROOTS[i]. Their differences span
    # the constant direction, so r=1 and v=0.
    r = 1
    v = 0
    lower = (r - 3) // 2
    assert len(set(ROOTS)) == 4
    assert v >= lower == -1

    parameters = tuple((ROOTS[0] - root) % PRIME for root in ROOTS)
    center = sum(parameters) * pow(4, -1, PRIME) % PRIME
    centered_u = [(-ROOTS[0] + center) % PRIME, 1]
    centered_parameters = tuple((value - center) % PRIME for value in parameters)
    assert sum(centered_parameters) % PRIME == 0
    e2 = sum(
        centered_parameters[i] * centered_parameters[j]
        for i in range(4)
        for j in range(i + 1, 4)
    ) % PRIME
    assert e2 != 0

    product_factors = [1]
    for parameter in centered_parameters:
        product_factors = multiply(product_factors, add(centered_u, [parameter]))
    deleted = tuple(value * value % PRIME for value in A_VALUES)
    domain_product = multiply(from_roots(deleted), product_factors)
    assert domain_product == [PRIME - 1] + [0] * 7 + [1]

    b_reverse = list(reversed(centered_u))
    e_reverse = list(reversed(from_roots(deleted)))
    h_poly = add(multiply(e_reverse, multiply(multiply(b_reverse, b_reverse), multiply(b_reverse, b_reverse))), [PRIME - 1])
    contact = 2 * (r - v)
    assert all(value == 0 for value in h_poly[:contact])

    k_poly = add(
        multiply(derivative(e_reverse), b_reverse),
        scale(multiply(e_reverse, derivative(b_reverse)), 4),
    )
    h_derivative = derivative(h_poly)
    b_cubed = multiply(multiply(b_reverse, b_reverse), b_reverse)
    assert h_derivative == multiply(b_cubed, k_poly)

    first_active_r = next(
        candidate
        for candidate in range(1, 64, 2)
        if ((candidate + 1) & candidate) == 0 and (candidate - 3) // 2 > 0
    )
    assert first_active_r == 7
    print(
        "AUDIT_RATE_HALF_LIST_B3_ANTIPODAL_PENCIL_DEGREE_FLOOR_PASS "
        "boundary_d=8 r=1 v=0 e2_nonzero=1 contact=2 "
        "derivative_factor=1 first_active_d=32"
    )


if __name__ == "__main__":
    main()
