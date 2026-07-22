#!/usr/bin/env python3
"""Exact finite-field checks for the quadratic locator-rank gate."""

from __future__ import annotations

from itertools import combinations_with_replacement


P = 1009


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] % P == 0:
        poly.pop()
    return [value % P for value in poly]


def mul(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % P
    return trim(out)


def locator(roots: list[int]) -> list[int]:
    out = [1]
    for root in roots:
        out = mul(out, [(-root) % P, 1])
    return out


def divide_exact(numerator: list[int], denominator: list[int]) -> list[int]:
    work = numerator[:]
    quotient = [0] * (len(numerator) - len(denominator) + 1)
    inverse_lead = pow(denominator[-1], P - 2, P)
    for shift in range(len(quotient) - 1, -1, -1):
        coefficient = work[shift + len(denominator) - 1] * inverse_lead % P
        quotient[shift] = coefficient
        for index, value in enumerate(denominator):
            work[shift + index] = (work[shift + index] - coefficient * value) % P
    require(not any(work[: len(denominator) - 1]), "nonexact polynomial division")
    return trim(quotient)


def evaluate(poly: list[int], point: int) -> int:
    out = 0
    for coefficient in reversed(poly):
        out = (out * point + coefficient) % P
    return out


def rank(rows: list[list[int]]) -> int:
    width = max(len(row) for row in rows)
    matrix = [row + [0] * (width - len(row)) for row in rows]
    pivot = 0
    for column in range(width):
        choice = next(
            (row for row in range(pivot, len(matrix)) if matrix[row][column] % P),
            None,
        )
        if choice is None:
            continue
        matrix[pivot], matrix[choice] = matrix[choice], matrix[pivot]
        scale = pow(matrix[pivot][column], P - 2, P)
        matrix[pivot] = [scale * value % P for value in matrix[pivot]]
        for row in range(len(matrix)):
            if row == pivot:
                continue
            factor = matrix[row][column] % P
            if factor:
                matrix[row] = [
                    (left - factor * right) % P
                    for left, right in zip(matrix[row], matrix[pivot], strict=True)
                ]
        pivot += 1
        if pivot == len(matrix):
            break
    return pivot


def x_times(poly: list[int]) -> list[int]:
    return [0, *poly]


def quadratic_rows(vectors: list[list[int]]) -> list[list[int]]:
    return [
        [vector[i] * vector[j] % P for i, j in combinations_with_replacement(range(len(vector)), 2)]
        for vector in vectors
    ]


def basis(e: int, b_degree: int = 3) -> tuple[list[list[int]], set[int]]:
    roots_a = list(range(1, 2 * e + 1))
    roots_b = list(range(2 * e + 1, 2 * e + b_degree + 1))
    a_poly = locator(roots_a)
    b_poly = locator(roots_b)
    out = [a_poly]
    for index in range(e):
        d_i = locator(roots_a[2 * index : 2 * index + 2])
        out.append(mul(b_poly, divide_exact(a_poly, d_i)))
    return out, set(roots_a + roots_b)


def check_cubic_packet(e: int) -> int:
    u_basis, excluded = basis(e)
    require(rank(u_basis) == e + 1, "pair-Lagrange basis lost rank")

    products = [
        mul(u_basis[i], u_basis[j])
        for i, j in combinations_with_replacement(range(e + 1), 2)
    ]
    spanning = [mul(u_basis[0], u_basis[0])]
    for index in range(1, e + 1):
        cross = mul(u_basis[0], u_basis[index])
        spanning.extend((cross, x_times(cross), mul(u_basis[index], u_basis[index])))

    expected = 3 * e + 1
    require(rank(spanning) == expected, "printed quadratic span is dependent")
    require(rank([*spanning, *products]) == expected, "quadratic product escaped span")

    points = [point for point in range(P) if point not in excluded][: 6 * e + 3]
    coefficient_rows: list[list[int]] = []
    for point in points:
        values = [evaluate(poly, point) for poly in u_basis]
        scale = pow(values[-1], P - 2, P)
        coefficient_rows.append([value * scale % P for value in values])
    q_rank = rank(quadratic_rows(coefficient_rows))
    require(q_rank == expected, "toy quadratic evaluation did not attain the bound")
    require(len(points) - q_rank == 3 * e + 2, "row-nullity arithmetic mismatch")
    return q_rank


def main() -> None:
    ranks = {e: check_cubic_packet(e) for e in (3, 4, 5)}

    quartic_basis, _ = basis(4, b_degree=4)
    quartic_products = [
        mul(quartic_basis[i], quartic_basis[j])
        for i, j in combinations_with_replacement(range(5), 2)
    ]
    require(rank(quartic_products) > 13, "degree-four mutation did not break the cubic gate")

    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_"
        "DISTANCE_THREE_QUADRATIC_LOCATOR_RANK_GATE_PASS "
        f"ranks={ranks} mutation=degree_four"
    )


if __name__ == "__main__":
    main()
