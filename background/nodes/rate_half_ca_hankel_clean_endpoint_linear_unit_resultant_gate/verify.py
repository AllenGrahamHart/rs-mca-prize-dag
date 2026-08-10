#!/usr/bin/env python3
"""Verify the unit-resultant product with exact Sylvester determinants."""


PRIME = 1_000_003


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] % PRIME == 0:
        poly.pop()
    return [value % PRIME for value in poly]


def determinant(matrix: list[list[int]]) -> int:
    rows = [[value % PRIME for value in row] for row in matrix]
    value = 1
    for column in range(len(rows)):
        pivot = next(
            (row for row in range(column, len(rows)) if rows[row][column]),
            None,
        )
        if pivot is None:
            return 0
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            value = -value
        entry = rows[column][column]
        value = value * entry % PRIME
        inverse = pow(entry, PRIME - 2, PRIME)
        for row in range(column + 1, len(rows)):
            factor = rows[row][column] * inverse % PRIME
            for index in range(column, len(rows)):
                rows[row][index] = (
                    rows[row][index] - factor * rows[column][index]
                ) % PRIME
    return value % PRIME


def resultant(first: list[int], second: list[int]) -> int:
    """Return Res(first, second); coefficients are in ascending order."""
    first = trim(first[:])
    second = trim(second[:])
    m = len(first) - 1
    n = len(second) - 1
    if n == 0:
        return pow(second[0], m, PRIME)
    if m == 0:
        return pow(first[0], n, PRIME)

    first_desc = list(reversed(first))
    second_desc = list(reversed(second))
    size = m + n
    matrix = []
    for shift in range(n):
        matrix.append([0] * shift + first_desc + [0] * (n - 1 - shift))
    for shift in range(m):
        matrix.append([0] * shift + second_desc + [0] * (m - 1 - shift))
    assert all(len(row) == size for row in matrix)
    return determinant(matrix)


def main() -> None:
    checked = 0
    for m in range(2, 9):
        for h in (7, 31, 101):
            for constant in (0, 2, 13):
                # Q=t^m-h and
                # (t+c) sum_j (-c)^j t^(m-1-j)=t^m-(-c)^m.
                q_poly = [-h] + [0] * (m - 1) + [1]
                b_poly = [constant, 1]
                w_poly = [pow(-constant, m - 1 - degree, PRIME) for degree in range(m)]
                x_gap = (h - pow(-constant, m, PRIME)) % PRIME
                assert x_gap

                res_b = resultant(q_poly, b_poly)
                res_w = resultant(q_poly, w_poly)
                assert res_b * res_w % PRIME == pow(x_gap, m, PRIME)

                mutated = w_poly[:]
                mutated[0] = (mutated[0] + 1) % PRIME
                assert (
                    res_b * resultant(q_poly, mutated) % PRIME
                    != pow(x_gap, m, PRIME)
                )
                checked += 1

        for b_degree in range(1, m):
            for w_degree in range(m - b_degree, 4 * m + 2):
                k_degree = w_degree + b_degree - m
                assert k_degree >= 0
                assert k_degree <= 4 * m

    print(
        "RATE_HALF_CA_HANKEL_CLEAN_ENDPOINT_LINEAR_UNIT_RESULTANT_GATE_PASS "
        f"sylvester_instances={checked} mutations={checked}/{checked}"
    )


if __name__ == "__main__":
    main()
