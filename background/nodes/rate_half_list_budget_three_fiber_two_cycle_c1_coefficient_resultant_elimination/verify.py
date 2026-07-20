#!/usr/bin/env python3
"""Exact checks for the c=1 coefficient-resultant elimination."""

from __future__ import annotations

import importlib.util
from itertools import combinations
from pathlib import Path
from random import Random


HERE = Path(__file__).resolve().parent
DEPENDENCY = (
    HERE.parent
    / "rate_half_list_budget_three_fiber_two_cycle_mismatch_trace_resolvent_elimination"
    / "verify.py"
)
SPEC = importlib.util.spec_from_file_location("mismatch_trace_algebra", DEPENDENCY)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load mismatch trace algebra")
algebra = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(algebra)

PRIME = algebra.PRIME


def poly_add(left: list[int], right: list[int]) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index in range(len(out)):
        out[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % PRIME
    return algebra.trim(out)


def poly_scale(poly: list[int], scalar: int) -> list[int]:
    return algebra.trim([(scalar * value) % PRIME for value in poly])


def interpolate(points: list[tuple[int, int]]) -> list[int]:
    out = [0]
    for index, (x_value, y_value) in enumerate(points):
        basis = [1]
        denominator = 1
        for other, (x_other, _) in enumerate(points):
            if other == index:
                continue
            basis = algebra.poly_mul(basis, [-x_other % PRIME, 1])
            denominator = denominator * (x_value - x_other) % PRIME
        out = poly_add(
            out,
            poly_scale(basis, y_value * pow(denominator, -1, PRIME) % PRIME),
        )
    return algebra.trim(out)


def determinant(matrix: list[list[int]]) -> int:
    work = [[value % PRIME for value in row] for row in matrix]
    result = 1
    for column in range(len(work)):
        pivot = next(
            (row for row in range(column, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            result = -result
        pivot_value = work[column][column]
        result = result * pivot_value % PRIME
        inverse = pow(pivot_value, -1, PRIME)
        for row in range(column + 1, len(work)):
            scale = work[row][column] * inverse % PRIME
            if not scale:
                continue
            for entry in range(column, len(work)):
                work[row][entry] = (
                    work[row][entry] - scale * work[column][entry]
                ) % PRIME
    return result % PRIME


def resultant(left: list[int], right: list[int]) -> int:
    left, right = algebra.trim(left[:]), algebra.trim(right[:])
    if left == [0] or right == [0]:
        return 0
    left_degree = len(left) - 1
    right_degree = len(right) - 1
    size = left_degree + right_degree
    if size == 0:
        return 1
    matrix = [[0] * size for _ in range(size)]
    left_descending = list(reversed(left))
    right_descending = list(reversed(right))
    for row in range(right_degree):
        matrix[row][row : row + left_degree + 1] = left_descending
    for offset in range(left_degree):
        row = right_degree + offset
        matrix[row][offset : offset + right_degree + 1] = right_descending
    return determinant(matrix)


def norm_from_sum_product(
    repeated: int,
    total: int,
    product: int,
    invariant_i: int,
    invariant_j: int,
    *,
    omit_product_in_norm: bool = False,
) -> int:
    x_value = (repeated * repeated + product + 3 * repeated * total) % PRIME
    y_value = (repeated * repeated + product - 9 * repeated * total) % PRIME
    e_zero = repeated * (y_value - 16 * product) % PRIME
    f_zero = (16 * repeated * repeated - y_value) % PRIME
    j_even = 4 * (e_zero * e_zero + product * f_zero * f_zero) % PRIME
    j_odd = 8 * e_zero * f_zero % PRIME
    i_even = (
        x_value**3 + 192 * repeated * repeated * x_value * product
    ) % PRIME
    i_odd = (
        -24 * repeated * x_value * x_value
        - 512 * repeated**3 * product
    ) % PRIME
    k_zero = (invariant_i**3 * j_even - invariant_j**2 * i_even) % PRIME
    k_one = (invariant_i**3 * j_odd - invariant_j**2 * i_odd) % PRIME
    norm_factor = 1 if omit_product_in_norm else product
    return (k_zero * k_zero - norm_factor * k_one * k_one) % PRIME


def homogenized_norm(
    repeated: int,
    unused: int,
    elementary: tuple[int, int, int, int],
    invariant_i: int,
    invariant_j: int,
    *,
    wrong_sum_sign: bool = False,
    omit_product_in_norm: bool = False,
) -> int:
    e_one, _, _, e_four = elementary
    denominator = repeated * unused % PRIME
    if denominator == 0:
        raise ValueError("interpolation points must be nonzero")
    total = (
        e_one - repeated + unused
        if wrong_sum_sign
        else e_one - repeated - unused
    ) % PRIME
    product = e_four * pow(denominator, -1, PRIME) % PRIME
    norm = norm_from_sum_product(
        repeated,
        total,
        product,
        invariant_i,
        invariant_j,
        omit_product_in_norm=omit_product_in_norm,
    )
    return pow(denominator, 6, PRIME) * norm % PRIME


def divided_quartic(
    repeated: int, elementary: tuple[int, int, int, int]
) -> list[int]:
    e_one, e_two, e_three, _ = elementary
    return [
        repeated**3 - e_one * repeated**2 + e_two * repeated - e_three,
        repeated**2 - e_one * repeated + e_two,
        repeated - e_one,
        1,
    ]


def homogenized_polynomial(
    repeated: int,
    elementary: tuple[int, int, int, int],
    invariant_i: int,
    invariant_j: int,
) -> list[int]:
    points = [
        (
            unused,
            homogenized_norm(
                repeated,
                unused,
                elementary,
                invariant_i,
                invariant_j,
            ),
        )
        for unused in range(1, 20)
    ]
    return interpolate(points)


def inner_resultant(
    repeated: int,
    elementary: tuple[int, int, int, int],
    invariant_i: int,
    invariant_j: int,
) -> int:
    return resultant(
        divided_quartic(repeated, elementary),
        homogenized_polynomial(
            repeated, elementary, invariant_i, invariant_j
        ),
    )


def ordered_packet(
    roots: tuple[int, int, int, int],
    invariant_i: int,
    invariant_j: int,
    *,
    wrong_sum_sign: bool = False,
    omit_product_in_norm: bool = False,
    increasing_only: bool = False,
) -> list[int]:
    elementary = algebra.elementary(roots)
    out = []
    for repeated in roots:
        for unused in roots:
            if repeated == unused:
                continue
            if increasing_only and repeated > unused:
                continue
            out.append(
                homogenized_norm(
                    repeated,
                    unused,
                    elementary,
                    invariant_i,
                    invariant_j,
                    wrong_sum_sign=wrong_sum_sign,
                    omit_product_in_norm=omit_product_in_norm,
                )
            )
    return out


def product(values: list[int]) -> int:
    out = 1
    for value in values:
        out = out * value % PRIME
    return out


def nested_resultant_on_split_quartic(
    roots: tuple[int, int, int, int],
    invariant_i: int,
    invariant_j: int,
) -> int:
    elementary = algebra.elementary(roots)
    return product(
        [
            inner_resultant(repeated, elementary, invariant_i, invariant_j)
            for repeated in roots
        ]
    )


def outer_invariants(source: tuple[int, int, int, int]) -> tuple[int, int]:
    return algebra.invariants_from_roots(algebra.centered(source))


def main() -> None:
    rng = Random(20260720)
    resultant_checks = 0
    interpolation_checks = 0

    for _ in range(6):
        lifts = rng.sample(range(1, 80), 4)
        roots = tuple(value * value % PRIME for value in lifts)
        if len(set(roots)) != 4:
            continue
        outer = algebra.centered(tuple(rng.sample(range(100, 300), 4)))
        invariant_i, invariant_j = algebra.invariants_from_roots(outer)
        elementary = algebra.elementary(roots)

        for repeated in roots:
            polynomial = homogenized_polynomial(
                repeated, elementary, invariant_i, invariant_j
            )
            assert len(polynomial) <= 19
            for unused in (23, 31, 47):
                assert algebra.eval_poly(polynomial, unused) == homogenized_norm(
                    repeated,
                    unused,
                    elementary,
                    invariant_i,
                    invariant_j,
                )
                interpolation_checks += 1

            expected = product(
                [
                    homogenized_norm(
                        repeated,
                        unused,
                        elementary,
                        invariant_i,
                        invariant_j,
                    )
                    for unused in roots
                    if unused != repeated
                ]
            )
            assert (
                inner_resultant(
                    repeated, elementary, invariant_i, invariant_j
                )
                == expected
            )
            resultant_checks += 1

        packet = ordered_packet(roots, invariant_i, invariant_j)
        e_four = elementary[3]
        direct_norm_product = product(
            [
                algebra.c1_components(
                    repeated,
                    *[
                        root
                        for root in roots
                        if root not in (repeated, unused)
                    ],
                    invariant_i,
                    invariant_j,
                )[2]
                for repeated in roots
                for unused in roots
                if unused != repeated
            ]
        )
        expected_nested = pow(e_four, 36, PRIME) * direct_norm_product % PRIME
        assert product(packet) == expected_nested
        assert (
            nested_resultant_on_split_quartic(
                roots, invariant_i, invariant_j
            )
            == expected_nested
        )

    omega = (1, 4, 9, 16)
    positive_i, positive_j = outer_invariants((1, -1 % PRIME, 2, 3))
    reverse_i, reverse_j = outer_invariants((4, -4 % PRIME, 2, 3))
    negative_i, negative_j = outer_invariants((3, 5, 7, 29))

    assert product(ordered_packet(omega, positive_i, positive_j)) == 0
    assert (
        nested_resultant_on_split_quartic(omega, positive_i, positive_j) == 0
    )
    assert product(ordered_packet(omega, reverse_i, reverse_j)) == 0
    assert product(ordered_packet(omega, negative_i, negative_j)) != 0
    assert (
        nested_resultant_on_split_quartic(omega, negative_i, negative_j) != 0
    )

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C1_COEFFICIENT_RESULTANT_PASS "
        f"resultants={resultant_checks} "
        f"interpolation_checks={interpolation_checks} "
        "positive=2 negative=1"
    )


if __name__ == "__main__":
    main()

