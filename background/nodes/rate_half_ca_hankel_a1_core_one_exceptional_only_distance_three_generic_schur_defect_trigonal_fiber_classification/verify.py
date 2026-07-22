#!/usr/bin/env python3
"""Exact checks for the generic Schur-defect trigonal classification."""

from __future__ import annotations

from itertools import combinations
from random import Random


P = 101
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


def need(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] % P == 0:
        poly.pop()
    return [value % P for value in poly]


def add(left: list[int], right: list[int]) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index in range(len(out)):
        out[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % P
    return trim(out)


def scale(poly: list[int], scalar: int) -> list[int]:
    return trim([scalar * value % P for value in poly])


def multiply(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a_value in enumerate(left):
        for j, b_value in enumerate(right):
            out[i + j] = (out[i + j] + a_value * b_value) % P
    return trim(out)


def locator(roots: tuple[int, ...] | list[int]) -> list[int]:
    out = [1]
    for root in roots:
        out = multiply(out, [(-root) % P, 1])
    return out


def evaluate(poly: list[int], value: int) -> int:
    out = 0
    for coefficient in reversed(poly):
        out = (out * value + coefficient) % P
    return out


def inverse(value: int) -> int:
    need(value % P != 0, "attempted to invert zero")
    return pow(value, P - 2, P)


def divmod_poly(dividend: list[int], divisor: list[int]) -> tuple[list[int], list[int]]:
    remainder = dividend[:]
    quotient = [0] * max(1, len(dividend) - len(divisor) + 1)
    if len(dividend) >= len(divisor):
        for shift in range(len(dividend) - len(divisor), -1, -1):
            coefficient = remainder[shift + len(divisor) - 1] * inverse(divisor[-1]) % P
            quotient[shift] = coefficient
            for index, value in enumerate(divisor):
                remainder[shift + index] = (
                    remainder[shift + index] - coefficient * value
                ) % P
    return trim(quotient), trim(remainder[: max(1, len(divisor) - 1)])


def divide_exact(dividend: list[int], divisor: list[int]) -> list[int]:
    quotient, remainder = divmod_poly(dividend, divisor)
    need(remainder == [0], "nonzero exact-division remainder")
    return quotient


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
        work[pivot_row] = [factor * value % P for value in work[pivot_row]]
        for index in range(len(work)):
            if index == pivot_row or work[index][column] == 0:
                continue
            factor = work[index][column]
            work[index] = [
                (value - factor * pivot_value) % P
                for value, pivot_value in zip(work[index], work[pivot_row], strict=True)
            ]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_row


def dimensions(pairs: tuple[tuple[int, int], ...]) -> tuple[int, int, int, int]:
    e_value = len(pairs)
    roots = tuple(root for pair in pairs for root in pair)
    a_poly = locator(roots)
    b_poly = locator(B_ROOTS)
    d_polys = [locator(pair) for pair in pairs]
    u_polys = [a_poly] + [
        multiply(b_poly, divide_exact(a_poly, d_poly)) for d_poly in d_polys
    ]

    ambient = [multiply(a_poly, a_poly)]
    for u_poly in u_polys[1:]:
        a_u = multiply(a_poly, u_poly)
        ambient.extend((a_u, [0] + a_u, multiply(u_poly, u_poly)))
    products = [
        multiply(u_polys[i], u_polys[j])
        for i in range(e_value + 1)
        for j in range(i, e_value + 1)
    ]

    recovery_rows: list[list[int]] = []
    for index, d_poly in enumerate(d_polys):
        _, remainder = divmod_poly(b_poly, d_poly)
        remainder += [0] * (2 - len(remainder))
        n_value, m_value = remainder
        p_value = d_poly[0]
        s_value = -d_poly[1] % P
        constant_row = [1, 0, -p_value] + [0] * e_value
        linear_row = [0, 1, s_value] + [0] * e_value
        constant_row[3 + index] = -n_value % P
        linear_row[3 + index] = -m_value % P
        recovery_rows.extend((constant_row, linear_row))

    recovery_nullity = (e_value + 3) - rank(recovery_rows)
    return rank(d_polys), rank(ambient), rank(products), recovery_nullity


def main() -> None:
    b_poly = locator(B_ROOTS)
    r_poly = [62, 58, 1]
    prefix_records = {}
    for e_value in range(3, len(FIBER_PAIRS) + 1):
        pairs = FIBER_PAIRS[:e_value]
        record = dimensions(pairs)
        need(record == (3, 3 * e_value + 1, 3 * e_value, 1), f"bad prefix {e_value}: {record}")
        prefix_records[e_value] = record

        fiber_values = []
        for pair in pairs:
            d_poly = locator(pair)
            left = pair[0]
            y_value = evaluate(r_poly, left) * inverse(evaluate(b_poly, left)) % P
            fiber_values.append(y_value)
            difference = add(r_poly, scale(b_poly, -y_value))
            divide_exact(difference, d_poly)
        need(len(set(fiber_values)) == e_value, "recovered fiber levels collide")

    control_pairs = FIBER_PAIRS[:-1] + ((2, 4),)
    control = dimensions(control_pairs)
    need(control == (3, 37, 37, 0), f"bad saturation control: {control}")

    # The rank-three precondition is real: a common antipodal involution is
    # rank two and is intentionally outside the concurrency theorem.
    antipodal_pairs = ((1, 100), (2, 99), (3, 98), (4, 97))
    antipodal = dimensions(antipodal_pairs)
    need(antipodal[0] == 2, "rank-two scope control was not detected")

    rng = Random(20260722)
    available = [value for value in range(1, P) if value not in B_ROOTS]
    generic_trials = 0
    for e_value in range(3, 7):
        for _ in range(8):
            roots = rng.sample(available, 2 * e_value)
            pairs = tuple(
                (roots[2 * index], roots[2 * index + 1])
                for index in range(e_value)
            )
            record = dimensions(pairs)
            if record[0] != 3:
                continue
            pair_rank, ambient_rank, square_rank, recovery_nullity = record
            need(pair_rank == 3, "random scope dispatch failed")
            need(ambient_rank == 3 * e_value + 1, "random ambient rank failed")
            need(
                ambient_rank - square_rank == recovery_nullity,
                f"random defect identity failed at e={e_value}: {record}",
            )
            need(recovery_nullity <= 1, "random generic defect exceeded one")
            generic_trials += 1
    need(generic_trials >= 24, "too few deterministic generic trials")

    print(
        "RATE_HALF_DISTANCE_THREE_GENERIC_SCHUR_DEFECT_TRIGONAL_CLASSIFICATION_PASS "
        f"prefixes={len(prefix_records)} e12={prefix_records[12]} "
        f"control={control} rank2_scope={antipodal[0]} generic_trials={generic_trials}"
    )


if __name__ == "__main__":
    main()
