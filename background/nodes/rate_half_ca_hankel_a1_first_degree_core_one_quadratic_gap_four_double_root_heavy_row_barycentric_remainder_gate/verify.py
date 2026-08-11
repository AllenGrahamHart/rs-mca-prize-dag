#!/usr/bin/env python3
"""Exact finite-field replay of the heavy-row barycentric remainder gate."""


P = 101


def trim(poly: list[int]) -> list[int]:
    result = [value % P for value in poly]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    return trim([
        (left[index] if index < len(left) else 0)
        + (right[index] if index < len(right) else 0)
        for index in range(size)
    ])


def scale(value: int, poly: list[int]) -> list[int]:
    return trim([value * entry for entry in poly])


def multiply(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] = (result[i + j] + a * b) % P
    return trim(result)


def divide(dividend: list[int], divisor: list[int]) -> tuple[list[int], list[int]]:
    remainder = trim(dividend)
    quotient = [0] * max(1, len(remainder) - len(divisor) + 1)
    inverse = pow(divisor[-1], P - 2, P)
    while len(remainder) >= len(divisor) and remainder != [0]:
        shift = len(remainder) - len(divisor)
        coefficient = remainder[-1] * inverse % P
        quotient[shift] = coefficient
        subtraction = [0] * shift + scale(coefficient, divisor)
        remainder = add(remainder, scale(-1, subtraction))
    return trim(quotient), trim(remainder)


def lagrange_weight(points: list[int], target: int, point: int) -> int:
    numerator = 1
    denominator = 1
    for other in points:
        numerator = numerator * (target - other) % P
        if other != point:
            denominator = denominator * (point - other) % P
    denominator = denominator * (target - point) % P
    return numerator * pow(denominator, P - 2, P) % P


def main() -> None:
    points = [1, 2, 3, 4, 5]
    target = 6
    weights = [lagrange_weight(points, target, point) for point in points]
    assert weights == [1, 96, 10, 91, 5]

    h = multiply([-7, 1], [-7, 1])
    t_form = [3, 1]
    correction = [2, 5, 9]
    heavy_row = multiply(h, t_form)
    rows = [
        add(heavy_row, scale(point - target, correction))
        for point in points
    ]
    assert all(len(row) == 4 and row[-1] == 1 for row in rows)

    extrapolated = [0]
    for weight, row in zip(weights, rows):
        extrapolated = add(extrapolated, scale(weight, row))
    assert extrapolated == heavy_row
    quotient, remainder = divide(extrapolated, h)
    assert quotient == t_form and remainder == [0]

    columns = []
    for weight, row in zip(weights, rows):
        _, row_remainder = divide(row, h)
        columns.append(scale(weight, row_remainder))
    assert [
        sum(column[index] for column in columns) % P
        for index in range(2)
    ] == [0, 0]

    mutated = [row[:] for row in rows]
    mutated[0][0] = (mutated[0][0] + 1) % P
    bad = [0]
    for weight, row in zip(weights, mutated):
        bad = add(bad, scale(weight, row))
    assert divide(bad, h)[1] != [0]
    print("RATE_HALF_HEAVY_ROW_BARYCENTRIC_REMAINDER_GATE_PASS rows=5 rem=0")


if __name__ == "__main__":
    main()
