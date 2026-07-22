#!/usr/bin/env python3
"""Exact swap-pencil fence for the abstract quadric divisor route."""

from __future__ import annotations


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def add(left: list[int], right: list[int], prime: int) -> list[int]:
    size = max(len(left), len(right))
    out = [0] * size
    for index in range(size):
        out[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % prime
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def scale(poly: list[int], scalar: int, prime: int) -> list[int]:
    return [scalar * coefficient % prime for coefficient in poly]


def multiply(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % prime
    return out


def locator(roots: list[int], prime: int) -> list[int]:
    out = [1]
    for root in roots:
        out = multiply(out, [(-root) % prime, 1], prime)
    return out


def inverse(value: int, prime: int) -> int:
    require(value % prime != 0, "attempted to invert zero")
    return pow(value, prime - 2, prime)


def exact_divide(dividend: list[int], divisor: list[int], prime: int) -> list[int]:
    require(len(dividend) >= len(divisor), "negative quotient degree")
    remainder = dividend[:]
    quotient = [0] * (len(dividend) - len(divisor) + 1)
    inverse_leading = inverse(divisor[-1], prime)
    for shift in range(len(quotient) - 1, -1, -1):
        coefficient = remainder[shift + len(divisor) - 1] * inverse_leading % prime
        quotient[shift] = coefficient
        for index, value in enumerate(divisor):
            remainder[shift + index] = (
                remainder[shift + index] - coefficient * value
            ) % prime
    require(not any(remainder[: len(divisor) - 1]), "division has nonzero remainder")
    return quotient


def rank(matrix: list[list[int]], prime: int) -> int:
    work = [row[:] for row in matrix]
    row = 0
    for column in range(len(work[0])):
        pivot = next((index for index in range(row, len(work)) if work[index][column]), None)
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        factor = inverse(work[row][column], prime)
        work[row] = [value * factor % prime for value in work[row]]
        for index in range(len(work)):
            if index == row or work[index][column] == 0:
                continue
            factor = work[index][column]
            work[index] = [
                (value - factor * pivot_value) % prime
                for value, pivot_value in zip(work[index], work[row], strict=True)
            ]
        row += 1
        if row == len(work):
            break
    return row


def main() -> None:
    prime = 97
    e = 4
    base_roots = [1, 2, 3, 4]
    outside_roots = list(range(10, 10 + 2 * e))
    k_zero = locator(base_roots, prime)
    p_z = multiply(k_zero, locator(outside_roots, prime), prime)
    directions = [
        locator([root for root in base_roots if root != removed], prime)
        for removed in base_roots[:3]
    ]

    width = len(k_zero)
    basis = [poly + [0] * (width - len(poly)) for poly in [k_zero, *directions]]
    require(rank(basis, prime) == 4, "swap-pencil space is not four-dimensional")

    divisors = {tuple(k_zero)}
    for index, removed in enumerate(base_roots[:3]):
        for replacement in outside_roots:
            divisor = multiply(directions[index], [(-replacement) % prime, 1], prime)
            linear_form = add(
                k_zero,
                scale(directions[index], removed - replacement, prime),
                prime,
            )
            require(divisor == linear_form, "swap-pencil coordinate identity failed")
            require(multiply(divisor, exact_divide(p_z, divisor, prime), prime) == p_z, "not a divisor")

            direction_coordinates = [0, 0, 0]
            direction_coordinates[index] = (removed - replacement) % prime
            b_1, b_2, b_3 = direction_coordinates
            cone_value = (b_1 * b_2 + b_2 * b_3 + b_3 * b_1) % prime
            require(cone_value == 0, "swap divisor left the quadric cone")
            divisors.add(tuple(divisor))

    require(len(divisors) == 6 * e + 1, "wrong number of distinct swap divisors")
    require(len(divisors) > 3 * e - 3, "fence does not beat the proposed threshold")
    require(2 % prime != 0, "direction conic is singular in this characteristic")
    cone_matrix_scaled_by_two = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    require(rank(cone_matrix_scaled_by_two, prime) == 3, "quadric cone has wrong rank")

    for b_1 in range(4):
        for b_2 in range(4):
            for b_3 in range(4):
                source = (b_1 * b_2 + b_2 * b_3 + b_3 * b_1) % prime
                a_coordinate = (b_1 + b_2) % prime
                b_coordinate = 2 * b_2 % prime
                c_coordinate = (b_2 + b_3) % prime
                target = (4 * a_coordinate * c_coordinate - b_coordinate**2) % prime
                require(target == 4 * source % prime, "trace-cone coordinate change failed")

    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_DISTANCE_THREE_"
        "ABSTRACT_QUADRIC_DIVISOR_ROUTE_FENCE_PASS "
        f"e={e} divisors={len(divisors)} threshold={3 * e - 3}"
    )


if __name__ == "__main__":
    main()
