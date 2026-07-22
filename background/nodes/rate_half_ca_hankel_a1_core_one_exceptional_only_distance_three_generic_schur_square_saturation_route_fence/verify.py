#!/usr/bin/env python3
"""Exact certificate for the generic Schur-square saturation route fence."""

from __future__ import annotations

from itertools import combinations


PRIME = 101
B_ROOTS = (81, 18, 8)
FIBER_PAIRS = (
    (75, 41),
    (3, 49),
    (79, 76),
    (1, 36),
    (5, 58),
    (9, 34),
    (10, 50),
    (13, 39),
    (14, 62),
    (17, 40),
    (19, 61),
    (22, 23),
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] % PRIME == 0:
        poly.pop()
    return [value % PRIME for value in poly]


def add(left: list[int], right: list[int]) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index in range(len(out)):
        out[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % PRIME
    return trim(out)


def scale(poly: list[int], scalar: int) -> list[int]:
    return trim([(scalar * value) % PRIME for value in poly])


def multiply(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a_value in enumerate(left):
        for j, b_value in enumerate(right):
            out[i + j] = (out[i + j] + a_value * b_value) % PRIME
    return trim(out)


def locator(roots: tuple[int, ...] | list[int]) -> list[int]:
    out = [1]
    for root in roots:
        out = multiply(out, [(-root) % PRIME, 1])
    return out


def evaluate(poly: list[int], value: int) -> int:
    out = 0
    for coefficient in reversed(poly):
        out = (out * value + coefficient) % PRIME
    return out


def inverse(value: int) -> int:
    require(value % PRIME != 0, "attempted to invert zero")
    return pow(value, PRIME - 2, PRIME)


def divide_exact(dividend: list[int], divisor: list[int]) -> list[int]:
    remainder = dividend[:]
    require(len(remainder) >= len(divisor), "negative quotient degree")
    quotient = [0] * (len(remainder) - len(divisor) + 1)
    leading_inverse = inverse(divisor[-1])
    for shift in range(len(quotient) - 1, -1, -1):
        coefficient = remainder[shift + len(divisor) - 1] * leading_inverse % PRIME
        quotient[shift] = coefficient
        for index, value in enumerate(divisor):
            remainder[shift + index] = (
                remainder[shift + index] - coefficient * value
            ) % PRIME
    require(not any(remainder[: len(divisor) - 1]), "nonzero division remainder")
    return trim(quotient)


def rank(rows: list[list[int]]) -> int:
    width = max(len(row) for row in rows)
    work = [row + [0] * (width - len(row)) for row in rows]
    pivot_row = 0
    for column in range(width):
        pivot = next(
            (index for index in range(pivot_row, len(work)) if work[index][column]),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        factor = inverse(work[pivot_row][column])
        work[pivot_row] = [factor * value % PRIME for value in work[pivot_row]]
        for index in range(len(work)):
            if index == pivot_row or work[index][column] == 0:
                continue
            factor = work[index][column]
            work[index] = [
                (value - factor * pivot_value) % PRIME
                for value, pivot_value in zip(work[index], work[pivot_row], strict=True)
            ]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_row


def product_rank(pairs: tuple[tuple[int, int], ...]) -> tuple[int, int, int, int]:
    roots = tuple(root for pair in pairs for root in pair)
    a_poly = locator(roots)
    b_poly = locator(B_ROOTS)
    d_polys = [locator(pair) for pair in pairs]
    u_polys = [a_poly] + [
        multiply(b_poly, divide_exact(a_poly, d_poly)) for d_poly in d_polys
    ]
    products = [
        multiply(u_polys[i], u_polys[j])
        for i, j in combinations(range(len(u_polys)), 2)
    ] + [multiply(poly, poly) for poly in u_polys]
    ambient = [multiply(a_poly, a_poly)]
    for u_poly in u_polys[1:]:
        a_u = multiply(a_poly, u_poly)
        ambient.extend((a_u, [0] + a_u, multiply(u_poly, u_poly)))
    return rank(d_polys), rank(u_polys), rank(ambient), rank(products)


def main() -> None:
    all_roots = [root for pair in FIBER_PAIRS for root in pair] + list(B_ROOTS)
    require(len(set(all_roots)) == len(all_roots), "fixture roots are not disjoint")

    b_poly = locator(B_ROOTS)
    r_poly = [62, 58, 1]
    b_0, b_1, b_2, _ = b_poly
    r_0, r_1, r_2 = r_poly
    conic_constant = (-b_0 * r_1 + b_1 * r_0) % PRIME
    conic_s = (-b_0 * r_2 + b_2 * r_0) % PRIME
    conic_p = (-b_1 * r_2 + b_2 * r_1 - r_0) % PRIME
    conic_matrix_twice = [
        [2 * r_0 % PRIME, r_1, conic_s],
        [r_1, 2 * r_2 % PRIME, conic_p],
        [conic_s, conic_p, 2 * conic_constant % PRIME],
    ]
    require(rank(conic_matrix_twice) == 3, "fiber conic is degenerate")
    d_polys = [locator(pair) for pair in FIBER_PAIRS]
    fiber_values: list[int] = []
    linear_factors: list[list[int]] = []
    for pair, d_poly in zip(FIBER_PAIRS, d_polys, strict=True):
        left, right = pair
        c_value = evaluate(b_poly, left) * inverse(evaluate(r_poly, left)) % PRIME
        require(c_value != 0, "zero fiber value")
        require(
            evaluate(b_poly, right) * inverse(evaluate(r_poly, right)) % PRIME
            == c_value,
            "pair is not in one B/R fiber",
        )
        fiber_values.append(c_value)
        fiber_poly = add(b_poly, scale(r_poly, -c_value))
        linear = divide_exact(fiber_poly, d_poly)
        require(len(linear) == 2 and linear[-1] == 1, "fiber cofactor is not monic linear")
        linear_factors.append(linear)

        pair_sum = (left + right) % PRIME
        pair_product = left * right % PRIME
        conic_value = (
            r_0 * pair_sum * pair_sum
            + r_1 * pair_sum * pair_product
            + r_2 * pair_product * pair_product
            + conic_s * pair_sum
            + conic_p * pair_product
            + conic_constant
        ) % PRIME
        require(
            conic_value == 0,
            "pair coefficient point left the conic",
        )

    require(len(set(fiber_values)) == len(fiber_values), "fiber values are not distinct")
    e_value = len(FIBER_PAIRS)
    pair_rank, v_rank, ambient_rank, square_rank = product_rank(FIBER_PAIRS)
    require(pair_rank == 3, "pair locators are not on the generic rank-three branch")
    require(v_rank == e_value + 1, "coefficient space has wrong dimension")
    require(ambient_rank == 3 * e_value + 1, "ambient product generators are dependent")
    require(square_rank == 3 * e_value, "fixture does not have the claimed defect")

    for i, j in combinations(range(e_value), 2):
        c_i, c_j = fiber_values[i], fiber_values[j]
        denominator_inverse = inverse(c_i - c_j)
        u_poly = scale(linear_factors[j], c_i * denominator_inverse)
        v_poly = scale(linear_factors[i], -c_j * denominator_inverse)
        reconstructed = add(multiply(u_poly, d_polys[j]), multiply(v_poly, d_polys[i]))
        require(reconstructed == b_poly, "two-fiber Bezout identity failed")
        functional_value = (
            u_poly[-1] * inverse(c_i) + v_poly[-1] * inverse(c_j)
        ) % PRIME
        require(functional_value == 0, "annihilating functional failed")

    control_pairs = FIBER_PAIRS[:-1] + ((2, 4),)
    control = product_rank(control_pairs)
    require(control == (3, 13, 37, 37), "generic negative control did not restore saturation")

    mutated_r = [63, 58, 1]
    require(
        any(
            evaluate(b_poly, left) * inverse(evaluate(mutated_r, left)) % PRIME
            != evaluate(b_poly, right) * inverse(evaluate(mutated_r, right)) % PRIME
            for left, right in FIBER_PAIRS
        ),
        "R mutation was not detected",
    )

    print(
        "RATE_HALF_DISTANCE_THREE_GENERIC_SCHUR_SQUARE_SATURATION_ROUTE_FENCE_PASS "
        f"e={e_value} pair_rank={pair_rank} ambient_rank={ambient_rank} "
        f"square_rank={square_rank} control_rank={control[-1]}"
    )


if __name__ == "__main__":
    main()
