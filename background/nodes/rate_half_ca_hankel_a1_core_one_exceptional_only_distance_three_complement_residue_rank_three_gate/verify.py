#!/usr/bin/env python3
"""Exact checks for the distance-three complement-residue rank-three gate."""

from __future__ import annotations


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
    for shift in range(len(quotient) - 1, -1, -1):
        coefficient = work[shift + len(denominator) - 1] % P
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
    matrix = [row[:] for row in rows]
    pivot = 0
    for column in range(len(matrix[0])):
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


def check_pair_lagrange_ratios(e: int) -> int:
    roots_a = list(range(1, 2 * e + 1))
    roots_b = list(range(2 * e + 1, 2 * e + 4))
    a_poly = locator(roots_a)
    b_poly = locator(roots_b)
    d_polys = [locator(roots_a[2 * i : 2 * i + 2]) for i in range(e)]
    lambdas = [31 + i for i in range(e)]
    excluded = set(roots_a + roots_b)
    points = [point for point in range(P) if point not in excluded][: 6 * e + 3]

    inverse_rows: list[list[int]] = []
    direct_rows: list[list[int]] = []
    for point in points:
        a_value = evaluate(a_poly, point)
        b_value = evaluate(b_poly, point)
        inverse_row: list[int] = []
        direct_row: list[int] = []
        for d_i, lam in zip(d_polys, lambdas, strict=True):
            d_value = evaluate(d_i, point)
            q_zero = a_value
            q_internal = lam * b_value * a_value * pow(d_value, P - 2, P) % P
            ratio = q_zero * pow(q_internal, P - 2, P) % P
            expected = d_value * pow(lam * b_value % P, P - 2, P) % P
            require(ratio == expected, "pair-Lagrange inverse ratio mismatch")
            inverse_row.append(ratio)
            direct_row.append(d_value)
        inverse_rows.append(inverse_row)
        direct_rows.append(direct_row)

    require(rank(inverse_rows) == 3, "inverse-locator rank is not three")
    require(rank(direct_rows) == 3, "quadratic pair-locator rank is not three")
    return rank(inverse_rows)


def check_balanced_negative_control() -> tuple[int, int]:
    e = 4
    roots = list(range(1, 3 * e + 1))
    p_z = locator(roots)
    blocks: list[tuple[int, ...]] = []
    for base in ({0, 1, 2, 3}, {0, 1, 3, 6}):
        for shift in range(3 * e):
            blocks.append(tuple(sorted({(index + shift) % (3 * e) for index in base})))
    blocks.extend(((0, 3, 6, 9), (1, 4, 7, 10), (2, 5, 8, 11)))

    require(len(blocks) == len(set(blocks)) == 6 * e + 3, "control blocks repeat")
    degrees = [sum(index in block for block in blocks) for index in range(3 * e)]
    require(degrees == [2 * e + 1] * (3 * e), "control is not biregular")

    internal = (20, 21, 22, 23)
    rows: list[list[int]] = []
    complements: list[list[int]] = []
    for block in blocks:
        g_x = locator([roots[index] for index in block])
        h_x = divide_exact(p_z, g_x)
        complements.append(h_x)
        rows.append([evaluate(h_x, xi) for xi in internal])
    complement_rank = rank(complements)
    control_rank = rank(rows)
    require(complement_rank == 9 > e + 4, "control did not violate coefficient span")
    require(control_rank == 4, "balanced negative control did not violate rank three")
    return complement_rank, control_rank


def main() -> None:
    pair_ranks = {e: check_pair_lagrange_ratios(e) for e in (3, 4, 5)}
    complement_rank, control_rank = check_balanced_negative_control()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_"
        "DISTANCE_THREE_COMPLEMENT_RESIDUE_RANK_THREE_GATE_PASS "
        f"pair_ranks={pair_ranks} balanced_span={complement_rank} "
        f"balanced_control_rank={control_rank}"
    )


if __name__ == "__main__":
    main()
