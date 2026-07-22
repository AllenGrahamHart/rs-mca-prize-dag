#!/usr/bin/env python3
"""Exact controls for the quartic internal-slice lambda-cube matrix."""

from __future__ import annotations

import runpy
from pathlib import Path


SOURCE = (
    Path(__file__).resolve().parents[1]
    / "rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_boundary_torus_kernel_reduction"
    / "verify.py"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def add(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index in range(len(out)):
        out[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % prime
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def mul(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % prime
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def interpolate(points: list[int], values: list[int], prime: int) -> list[int]:
    out = [0]
    for index, point in enumerate(points):
        basis = [1]
        denominator = 1
        for other_index, other in enumerate(points):
            if other_index == index:
                continue
            basis = mul(basis, [(-other) % prime, 1], prime)
            denominator = denominator * (point - other) % prime
        scaled = [
            coefficient * values[index] * pow(denominator, -1, prime) % prime
            for coefficient in basis
        ]
        out = add(out, scaled, prime)
    return out


def build_control(e: int, prime: int) -> tuple[int, int, list[int]]:
    source = runpy.run_path(str(SOURCE))
    locator = source["locator"]
    evaluate = source["evaluate"]
    derivative = source["derivative"]
    primitive_root = source["primitive_root"]
    matrix_rank = source["matrix_rank"]

    if e == 3:
        return 0, 0, []

    domain_order = 8 * e + 8
    require((prime - 1) % domain_order == 0, "bad field order")
    generator = pow(
        primitive_root(prime), (prime - 1) // domain_order, prime
    )
    domain: list[int] = []
    value = 1
    for _ in range(domain_order):
        domain.append(value)
        value = value * generator % prime
    require(value == 1 and len(set(domain)) == domain_order, "bad subgroup")

    s, x_0 = domain[:2]
    pairs = [tuple(domain[2 + 2 * k : 4 + 2 * k]) for k in range(e)]
    triple = tuple(domain[2 + 2 * e : 5 + 2 * e])
    active = tuple(domain[5 + 2 * e :])
    b_poly = locator(triple, prime)
    c_poly = locator(active, prime)
    d_polys = [locator(pair, prime) for pair in pairs]
    internal = list(range(2, e + 2))
    i_poly = locator(tuple(internal), prime)
    i_prime = derivative(i_poly, prime)

    r_values: dict[tuple[int, int], int] = {}
    for k, pair in enumerate(pairs):
        for row in pair:
            a_over_d = 1
            for other, d_poly in enumerate(d_polys):
                if other != k:
                    a_over_d = a_over_d * evaluate(d_poly, row, prime) % prime
            r_values[k, row] = (
                evaluate(b_poly, row, prime)
                * pow(
                    internal[k] * evaluate(i_prime, internal[k], prime),
                    -1,
                    prime,
                )
                * a_over_d
            ) % prime

    component_polys: list[list[list[int]]] = []
    for l in range(e):
        points = [
            row
            for k, pair in enumerate(pairs)
            if k != l
            for row in pair
        ]
        row_components: list[list[int]] = []
        for k in range(e):
            if k == l:
                row_components.append([0])
                continue
            values: list[int] = []
            for pair_index, pair in enumerate(pairs):
                if pair_index == l:
                    continue
                for row in pair:
                    value = 0
                    if pair_index == k:
                        value = (
                            pow(r_values[k, row], 3, prime)
                            * pow(evaluate(d_polys[l], row, prime), 2, prime)
                            * pow(
                                evaluate(c_poly, row, prime)
                                * (internal[l] - internal[k]) ** 2,
                                -1,
                                prime,
                            )
                        ) % prime
                    values.append(value)
            row_components.append(interpolate(points, values, prime))
        component_polys.append(row_components)

    matrix: list[list[int]] = []
    for l in range(e):
        for degree in range(5, 2 * e - 2):
            matrix.append(
                [
                    poly[degree] if degree < len(poly) else 0
                    for poly in component_polys[l]
                ]
            )

    rank = matrix_rank(matrix, prime)
    deletion_ranks = [
        matrix_rank(
            [row[:column] + row[column + 1 :] for row in matrix], prime
        )
        for column in range(e)
    ]
    require(all(value == rank - 1 for value in deletion_ranks), "control lost coloops")

    lambdas = [(11 + 2 * index) % prime or 1 for index in range(e)]
    degrees: list[int] = []
    for l in range(e):
        combined = [0]
        for k, poly in enumerate(component_polys[l]):
            combined = add(
                combined,
                [coefficient * pow(lambdas[k], 3, prime) % prime for coefficient in poly],
                prime,
            )
        degrees.append(len(combined) - 1)

    # Recheck C^{-1} through the sparse subgroup derivative at every exceptional root.
    a_poly = locator(tuple(row for pair in pairs for row in pair), prime)
    a_prime = derivative(a_poly, prime)
    for pair in pairs:
        for row in pair:
            inverse_c = (
                row
                * (row - s)
                * (row - x_0)
                * evaluate(a_prime, row, prime)
                * evaluate(b_poly, row, prime)
                * pow(domain_order, -1, prime)
            ) % prime
            require(
                inverse_c * evaluate(c_poly, row, prime) % prime == 1,
                "subgroup derivative inverse mismatch",
            )

    return len(matrix), rank, degrees


def main() -> None:
    expected = {
        (3, 97): (0, 0, []),
        (4, 241): (4, 4, [5, 5, 5, 5]),
        (5, 97): (15, 5, [7, 7, 7, 7, 7]),
        (7, 193): (49, 7, [11, 11, 11, 11, 11, 11, 11]),
    }
    observed = {key: build_control(*key) for key in expected}
    require(observed == expected, "unexpected lambda-cube matrix controls")
    print(
        "RATE_HALF_DISTANCE_THREE_QUARTIC_LAMBDA_CUBE_KERNEL_PASS "
        f"controls={observed} e3_no_rows=True e4_plus_full_rank=True"
    )


if __name__ == "__main__":
    main()
